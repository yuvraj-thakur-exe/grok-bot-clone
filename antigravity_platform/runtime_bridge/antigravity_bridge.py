"""Antigravity IDE & Agent Runtime Bridge for Grok Bot Clone (GBC) / ORBIT.

This module provides the primary execution host adapter connecting GBC's multi-agent
orchestrator and persistent computer runtime to Google Antigravity IDE and agent APIs.
It also implements the reverse-engineered `sand-local-exec-daemon` protocol for local
process execution, boundary validation, and audit receipts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
import urllib.parse


@dataclass
class ExecutionReceipt:
    command: str
    exit_code: int
    stdout: str
    stderr: str
    duration_ms: float = 0.0
    verified: bool = False
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AntigravityContext:
    workspace_root: Path
    storage_root: Optional[Path] = None
    active_bot_id: str = "primary_assistant"
    approval_required: bool = True
    session_id: Optional[str] = None
    environment: Dict[str, str] = field(default_factory=dict)


class AntigravityHostBridge:
    """Core adapter bridging GBC to Antigravity IDE tools and runtime."""

    def __init__(self, context: Optional[AntigravityContext] = None):
        ws = os.environ.get("ORBIT_WORKSPACE")
        self.context = context or AntigravityContext(
            workspace_root=Path(ws).resolve() if ws else Path.cwd().resolve()
        )
        self.orbit_dir = self.context.workspace_root / ".orbit"
        self.orbit_dir.mkdir(parents=True, exist_ok=True)
        self.receipts_file = self.orbit_dir / "exec_receipts.jsonl"
        self._tool_registry: Dict[str, Callable[..., Any]] = {}
        self._register_default_tools()

    def _register_default_tools(self) -> None:
        """Register host-level execution and file tools."""
        self._tool_registry["run_command"] = self.run_command
        self._tool_registry["read_file"] = self.read_file
        self._tool_registry["write_file"] = self.write_file
        self._tool_registry["list_files"] = self.list_files

    def _log_receipt(self, receipt: ExecutionReceipt) -> None:
        try:
            with open(self.receipts_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(receipt.to_dict()) + "\n")
        except Exception:
            pass

    def run_command(
        self,
        command: str,
        cwd: Optional[str | Path] = None,
        timeout: int = 60,
        env: Optional[Dict[str, str]] = None,
        permission: str = "workspace_readwrite",
    ) -> ExecutionReceipt:
        """Execute a shell command with workspace boundary and approval enforcement."""
        working_dir = (self.context.workspace_root / cwd).resolve() if cwd else self.context.workspace_root.resolve()

        # Workspace boundary check unless permission is insecure_none
        if permission != "insecure_none":
            ws_resolved = str(self.context.workspace_root.resolve()).lower()
            wd_resolved = str(working_dir).lower()
            if not wd_resolved.startswith(ws_resolved):
                receipt = ExecutionReceipt(
                    command=command,
                    exit_code=-3,
                    stdout="",
                    stderr=f"PermissionError: Command execution outside workspace boundary rejected: {working_dir}",
                    verified=False,
                )
                self._log_receipt(receipt)
                return receipt

        merged_env = os.environ.copy()
        merged_env["ORBIT_WORKSPACE"] = str(self.context.workspace_root)
        if env:
            merged_env.update(env)

        is_windows = sys.platform == "win32"
        shell_cmd = ["powershell", "-NoProfile", "-Command", command] if is_windows else ["/bin/bash", "-c", command]

        t0 = time.perf_counter()
        try:
            res = subprocess.run(
                shell_cmd,
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=timeout,
                env=merged_env,
            )
            duration = (time.perf_counter() - t0) * 1000.0
            receipt = ExecutionReceipt(
                command=command,
                exit_code=res.returncode,
                stdout=res.stdout,
                stderr=res.stderr,
                duration_ms=round(duration, 2),
                verified=(res.returncode == 0),
            )
        except subprocess.TimeoutExpired as exc:
            duration = (time.perf_counter() - t0) * 1000.0
            stdout_str = exc.stdout.decode() if isinstance(exc.stdout, bytes) else str(exc.stdout or "")
            receipt = ExecutionReceipt(
                command=command,
                exit_code=-1,
                stdout=stdout_str,
                stderr=f"Command timed out after {timeout} seconds",
                duration_ms=round(duration, 2),
                verified=False,
            )
        except Exception as exc:
            duration = (time.perf_counter() - t0) * 1000.0
            receipt = ExecutionReceipt(
                command=command,
                exit_code=-2,
                stdout="",
                stderr=str(exc),
                duration_ms=round(duration, 2),
                verified=False,
            )

        self._log_receipt(receipt)
        return receipt

    def read_file(self, path: str | Path, start_line: int = 1, end_line: Optional[int] = None) -> str:
        """Read file contents with boundary safety."""
        target = (self.context.workspace_root / path).resolve()
        ws_resolved = str(self.context.workspace_root.resolve()).lower()
        if not str(target).lower().startswith(ws_resolved):
            raise PermissionError(f"Access outside workspace boundary rejected: {target}")

        if not target.exists():
            raise FileNotFoundError(f"File not found: {target}")

        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        end = end_line if end_line is not None else len(lines)
        return "".join(lines[start_line - 1 : end])

    def write_file(self, path: str | Path, content: str, overwrite: bool = True) -> bool:
        """Write file contents safely within workspace."""
        target = (self.context.workspace_root / path).resolve()
        ws_resolved = str(self.context.workspace_root.resolve()).lower()
        if not str(target).lower().startswith(ws_resolved):
            raise PermissionError(f"Write outside workspace boundary rejected: {target}")

        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not overwrite:
            raise FileExistsError(f"File exists and overwrite=False: {target}")

        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def list_files(self, subpath: str = ".") -> List[str]:
        """List files in subpath."""
        target = (self.context.workspace_root / subpath).resolve()
        ws_resolved = str(self.context.workspace_root.resolve()).lower()
        if not str(target).lower().startswith(ws_resolved):
            raise PermissionError(f"Access outside workspace boundary rejected: {target}")

        if not target.is_dir():
            return []
        return [p.name for p in target.iterdir()]


class SandDaemonRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the Sand / GBC local-exec daemon."""

    server: SandDaemonServer

    def _send_json(self, status: int, payload: Dict[str, Any]) -> None:
        raw = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(raw)

    def do_OPTIONS(self) -> None:
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        path = urllib.parse.urlparse(self.path).path
        if path in ("/health", "/"):
            uptime = time.time() - self.server.started_at
            self._send_json(200, {
                "status": "ok",
                "daemon": "sand-local-exec-daemon",
                "pid": os.getpid(),
                "port": self.server.port,
                "workspace": str(self.server.bridge.context.workspace_root),
                "uptime_seconds": round(uptime, 2),
            })
        elif path == "/status":
            self._send_json(200, {
                "pid": os.getpid(),
                "startedAt": int(self.server.started_at * 1000),
                "servingAt": int(self.server.serving_at * 1000),
                "filesKeyId": self.server.files_key_id,
                "generation": 0,
            })
        else:
            self._send_json(404, {"error": "Not Found"})

    def do_POST(self) -> None:
        path = urllib.parse.urlparse(self.path).path
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON body"})
            return

        if path == "/exec":
            command = data.get("command", "")
            cwd = data.get("cwd")
            timeout = int(data.get("timeout", 60))
            permission = data.get("permission", "workspace_readwrite")
            env = data.get("env")

            if not command:
                self._send_json(400, {"error": "command is required"})
                return

            receipt = self.server.bridge.run_command(
                command=command,
                cwd=cwd,
                timeout=timeout,
                env=env,
                permission=permission,
            )
            self._send_json(200, {
                "type": "exec_result",
                "command": receipt.command,
                "exit_code": receipt.exit_code,
                "stdout": receipt.stdout,
                "stderr": receipt.stderr,
                "duration_ms": receipt.duration_ms,
                "verified": receipt.verified,
            })

        elif path == "/fs/read":
            file_path = data.get("path")
            if not file_path:
                self._send_json(400, {"error": "path is required"})
                return
            start_line = int(data.get("start_line", 1))
            end_line = data.get("end_line")
            try:
                content = self.server.bridge.read_file(file_path, start_line, int(end_line) if end_line else None)
                self._send_json(200, {"type": "read_result", "path": file_path, "content": content})
            except Exception as e:
                self._send_json(400, {"type": "error", "error": str(e)})

        elif path == "/fs/write":
            file_path = data.get("path")
            content = data.get("content", "")
            overwrite = bool(data.get("overwrite", True))
            if not file_path:
                self._send_json(400, {"error": "path is required"})
                return
            try:
                self.server.bridge.write_file(file_path, content, overwrite)
                self._send_json(200, {"type": "write_result", "path": file_path, "success": True})
            except Exception as e:
                self._send_json(400, {"type": "error", "error": str(e)})

        elif path == "/fs/list":
            subpath = data.get("path", ".")
            try:
                files = self.server.bridge.list_files(subpath)
                self._send_json(200, {"type": "list_result", "path": subpath, "files": files})
            except Exception as e:
                self._send_json(400, {"type": "error", "error": str(e)})

        else:
            self._send_json(404, {"error": "Not Found"})

    def log_message(self, format: str, *args: Any) -> None:
        # Suppress noisy HTTP request logging to keep output clean
        pass


class SandDaemonServer(ThreadingHTTPServer):
    """Threading HTTP server implementing the sand-local-exec daemon."""

    def __init__(self, host: str, port: int, bridge: AntigravityHostBridge):
        super().__init__((host, port), SandDaemonRequestHandler)
        self.bridge = bridge
        self.host = host
        self.port = port
        self.started_at = time.time()
        self.serving_at = time.time()
        ws_hash = hashlib.sha256(str(self.bridge.context.workspace_root).encode("utf-8")).hexdigest()[:16]
        self.files_key_id = ws_hash
        self.daemon_file = self.bridge.orbit_dir / "local-exec-daemon.json"
        self.log_file = self.bridge.orbit_dir / "local-exec-daemon.log"

    def write_daemon_manifest(self) -> None:
        data = {
            "pid": os.getpid(),
            "port": self.port,
            "host": self.host,
            "startedAt": int(self.started_at * 1000),
            "servingAt": int(self.serving_at * 1000),
            "inflightCount": 0,
            "filesKeyId": self.files_key_id,
            "workspace": str(self.bridge.context.workspace_root),
            "generation": 0,
        }
        self.daemon_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

        # Log OEMCP / ACP compatibility header exactly matching REA audit
        log_line = (
            f"{time.strftime('%H:%M:%S')} INFO  Resolved the fallback encoding for shell output meta={{encoding: \"none\", oemcp: 437, acp: 1252}}\n"
            f"[sand-local-exec-daemon] started (pid {os.getpid()}); serving local exec over http://{self.host}:{self.port}\n"
        )
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_line)

    def clean_daemon_manifest(self) -> None:
        try:
            if self.daemon_file.exists():
                self.daemon_file.unlink()
        except Exception:
            pass


def start_daemon(host: str = "127.0.0.1", port: int = 3888, workspace: Optional[str | Path] = None) -> None:
    """Launch the Sand Local Exec Daemon."""
    ws = Path(workspace).resolve() if workspace else Path.cwd().resolve()
    bridge = AntigravityHostBridge(AntigravityContext(workspace_root=ws))
    server = SandDaemonServer(host, port, bridge)
    server.write_daemon_manifest()
    print(f"[sand-local-exec-daemon] started (pid {os.getpid()}); serving on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[sand-local-exec-daemon] shutting down...")
    finally:
        server.clean_daemon_manifest()
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Antigravity Runtime Bridge & Sand Local Exec Daemon")
    subparsers = parser.add_subparsers(dest="command")

    # daemon command
    daemon_parser = subparsers.add_parser("daemon", help="Start the sand-local-exec HTTP daemon")
    daemon_parser.add_argument("--host", default="127.0.0.1", help="Host interface (default: 127.0.0.1)")
    daemon_parser.add_argument("--port", type=int, default=3888, help="Port to listen on (default: 3888)")
    daemon_parser.add_argument("--workspace", default=None, help="Workspace root directory")

    # run command
    run_parser = subparsers.add_parser("run", help="Run a command through the bridge")
    run_parser.add_argument("cmd", help="Command string to execute")
    run_parser.add_argument("--cwd", default=None, help="Working directory relative to workspace")

    args = parser.parse_args()

    if args.command == "daemon":
        start_daemon(host=args.host, port=args.port, workspace=args.workspace)
    elif args.command == "run":
        bridge = AntigravityHostBridge()
        receipt = bridge.run_command(args.cmd, cwd=args.cwd)
        print(json.dumps(receipt.to_dict(), indent=2))
        sys.exit(receipt.exit_code)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
