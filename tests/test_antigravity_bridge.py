from __future__ import annotations

import json
import socket
import tempfile
import threading
import time
import unittest
import urllib.request
from pathlib import Path

from antigravity_platform.runtime_bridge.antigravity_bridge import (
    AntigravityContext,
    AntigravityHostBridge,
    SandDaemonServer,
)


def get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return int(s.getsockname()[1])


class AntigravityBridgeTests(unittest.TestCase):
    def test_run_command_and_logging(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            bridge = AntigravityHostBridge(AntigravityContext(workspace_root=ws))
            receipt = bridge.run_command("echo 'Bridge Test'")
            self.assertEqual(receipt.exit_code, 0)
            self.assertTrue(receipt.verified)
            self.assertIn("Bridge Test", receipt.stdout)
            self.assertGreater(receipt.duration_ms, 0)

            # Verify receipt file
            receipts_file = ws / ".orbit" / "exec_receipts.jsonl"
            self.assertTrue(receipts_file.exists())
            line = receipts_file.read_text(encoding="utf-8").strip()
            data = json.loads(line)
            self.assertEqual(data["command"], "echo 'Bridge Test'")
            self.assertEqual(data["exit_code"], 0)

    def test_workspace_boundary_protection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            bridge = AntigravityHostBridge(AntigravityContext(workspace_root=ws))

            # Attempt file read outside workspace
            with self.assertRaises(PermissionError):
                bridge.read_file("../../outside.txt")

            # Attempt file write outside workspace
            with self.assertRaises(PermissionError):
                bridge.write_file("../../outside.txt", "hacked")

            # Attempt command execution in an outside directory
            outside_dir = ws.parent.resolve()
            outside_receipt = bridge.run_command("echo test", cwd=outside_dir)
            self.assertEqual(outside_receipt.exit_code, -3)
            self.assertIn("PermissionError", outside_receipt.stderr)

    def test_file_read_write_operations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            bridge = AntigravityHostBridge(AntigravityContext(workspace_root=ws))

            rel_file = "subdir/test.txt"
            bridge.write_file(rel_file, "Line 1\nLine 2\nLine 3\n")

            content = bridge.read_file(rel_file)
            self.assertEqual(content, "Line 1\nLine 2\nLine 3\n")

            partial = bridge.read_file(rel_file, start_line=2, end_line=2)
            self.assertEqual(partial, "Line 2\n")

            files = bridge.list_files("subdir")
            self.assertEqual(files, ["test.txt"])

    def test_sand_daemon_server_lifecycle_and_endpoints(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            bridge = AntigravityHostBridge(AntigravityContext(workspace_root=ws))
            port = get_free_port()
            server = SandDaemonServer("127.0.0.1", port, bridge)
            server.write_daemon_manifest()

            # Verify daemon file was created
            daemon_file = ws / ".orbit" / "local-exec-daemon.json"
            self.assertTrue(daemon_file.exists())
            manifest = json.loads(daemon_file.read_text(encoding="utf-8"))
            self.assertEqual(manifest["port"], port)
            self.assertEqual(manifest["daemon"] if "daemon" in manifest else manifest.get("inflightCount"), 0)

            # Start server in background thread
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            time.sleep(0.1)

            base_url = f"http://127.0.0.1:{port}"

            try:
                # 1. GET /health
                req = urllib.request.Request(f"{base_url}/health")
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200)
                    body = json.loads(resp.read().decode("utf-8"))
                    self.assertEqual(body["status"], "ok")
                    self.assertEqual(body["daemon"], "sand-local-exec-daemon")

                # 2. GET /status
                req = urllib.request.Request(f"{base_url}/status")
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200)
                    body = json.loads(resp.read().decode("utf-8"))
                    self.assertIn("filesKeyId", body)

                # 3. POST /exec
                payload = json.dumps({"command": "echo 'Daemon Live'"}).encode("utf-8")
                req = urllib.request.Request(f"{base_url}/exec", data=payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200)
                    body = json.loads(resp.read().decode("utf-8"))
                    self.assertEqual(body["type"], "exec_result")
                    self.assertEqual(body["exit_code"], 0)
                    self.assertIn("Daemon Live", body["stdout"])

                # 4. POST /fs/write and POST /fs/read
                write_payload = json.dumps({"path": "daemon_test.txt", "content": "Daemon OK"}).encode("utf-8")
                req = urllib.request.Request(f"{base_url}/fs/write", data=write_payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200)
                    body = json.loads(resp.read().decode("utf-8"))
                    self.assertTrue(body["success"])

                read_payload = json.dumps({"path": "daemon_test.txt"}).encode("utf-8")
                req = urllib.request.Request(f"{base_url}/fs/read", data=read_payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req) as resp:
                    self.assertEqual(resp.status, 200)
                    body = json.loads(resp.read().decode("utf-8"))
                    self.assertEqual(body["content"], "Daemon OK")

            finally:
                server.shutdown()
                server.clean_daemon_manifest()
                server.server_close()
                self.assertFalse(daemon_file.exists())


if __name__ == "__main__":
    unittest.main()
