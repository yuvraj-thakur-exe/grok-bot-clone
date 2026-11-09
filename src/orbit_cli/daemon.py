"""Daemon lifecycle manager for ORBIT / Sand Local Exec Daemon."""
from __future__ import annotations

import json
import os
import signal
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, Optional


def get_daemon_manifest_path(workspace: Path) -> Path:
    return workspace / ".orbit" / "local-exec-daemon.json"


def is_pid_running(pid: int) -> bool:
    """Check if process with given PID is running."""
    if pid <= 0:
        return False
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if handle:
            kernel32.CloseHandle(handle)
            return True
        return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except (OSError, ProcessLookupError):
            return False


def get_daemon_status(workspace: Optional[str | Path] = None) -> Dict[str, Any]:
    ws = Path(workspace).resolve() if workspace else Path.cwd().resolve()
    manifest_path = get_daemon_manifest_path(ws)
    if not manifest_path.exists():
        return {"status": "stopped", "running": False, "workspace": str(ws)}

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        pid = data.get("pid", 0)
        port = data.get("port", 3888)
        running = is_pid_running(pid)

        if not running:
            return {"status": "stale", "running": False, "pid": pid, "workspace": str(ws)}

        # Probe health endpoint
        health_ok = False
        try:
            req = urllib.request.Request(f"http://127.0.0.1:{port}/health", headers={"User-Agent": "ORBIT-CLI"})
            with urllib.request.urlopen(req, timeout=1.0) as resp:
                health_ok = (resp.status == 200)
        except Exception:
            health_ok = False

        return {
            "status": "running" if health_ok else "unresponsive",
            "running": running,
            "pid": pid,
            "port": port,
            "filesKeyId": data.get("filesKeyId"),
            "startedAt": data.get("startedAt"),
            "workspace": str(ws),
        }
    except Exception as exc:
        return {"status": "error", "error": str(exc), "workspace": str(ws)}


def stop_daemon(workspace: Optional[str | Path] = None) -> Dict[str, Any]:
    ws = Path(workspace).resolve() if workspace else Path.cwd().resolve()
    manifest_path = get_daemon_manifest_path(ws)
    if not manifest_path.exists():
        return {"status": "not_running", "workspace": str(ws)}

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        pid = data.get("pid", 0)

        if is_pid_running(pid):
            if sys.platform == "win32":
                import subprocess
                subprocess.run(["taskkill", "/PID", str(pid), "/F"], capture_output=True, text=True)
            else:
                os.kill(pid, signal.SIGTERM)

        # Remove manifest
        try:
            manifest_path.unlink(missing_ok=True)
        except Exception:
            pass

        return {"status": "stopped", "pid": pid, "workspace": str(ws)}
    except Exception as exc:
        return {"status": "error", "error": str(exc), "workspace": str(ws)}
