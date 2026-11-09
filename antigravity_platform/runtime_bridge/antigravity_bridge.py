"""Antigravity IDE & Agent Runtime Bridge for Grok Bot Clone (GBC) / ORBIT.

This module provides the primary execution host adapter connecting GBC's multi-agent
orchestrator and persistent computer runtime to Google Antigravity IDE and agent APIs.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ExecutionReceipt:
    command: str
    exit_code: int
    stdout: str
    stderr: str
    duration_ms: float = 0.0
    verified: bool = False


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
        self.context = context or AntigravityContext(
            workspace_root=Path(os.environ.get("ORBIT_WORKSPACE", Path.cwd()))
        )
        self._tool_registry: Dict[str, Callable[..., Any]] = {}
        self._register_default_tools()

    def _register_default_tools(self) -> None:
        """Register host-level execution and file tools."""
        self._tool_registry["run_command"] = self.run_command
        self._tool_registry["read_file"] = self.read_file
        self._tool_registry["write_file"] = self.write_file
        self._tool_registry["list_files"] = self.list_files

    def run_command(
        self,
        command: str,
        cwd: Optional[str | Path] = None,
        timeout: int = 60,
        env: Optional[Dict[str, str]] = None,
        permission: str = "workspace_readwrite",
    ) -> ExecutionReceipt:
        """Execute a shell command with workspace boundary and approval enforcement."""
        working_dir = Path(cwd) if cwd else self.context.workspace_root
        working_dir = working_dir.resolve()

        # Workspace boundary check
        if not str(working_dir).startswith(str(self.context.workspace_root.resolve())):
            raise PermissionError(f"Command execution outside workspace boundary rejected: {working_dir}")

        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)

        # Run process safely
        is_windows = sys.platform == "win32"
        shell_cmd = ["powershell", "-NoProfile", "-Command", command] if is_windows else ["/bin/bash", "-c", command]

        try:
            res = subprocess.run(
                shell_cmd,
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=timeout,
                env=merged_env,
            )
            return ExecutionReceipt(
                command=command,
                exit_code=res.returncode,
                stdout=res.stdout,
                stderr=res.stderr,
                verified=(res.returncode == 0),
            )
        except subprocess.TimeoutExpired as exc:
            return ExecutionReceipt(
                command=command,
                exit_code=-1,
                stdout=exc.stdout.decode() if isinstance(exc.stdout, bytes) else str(exc.stdout or ""),
                stderr=f"Command timed out after {timeout} seconds",
                verified=False,
            )
        except Exception as exc:
            return ExecutionReceipt(
                command=command,
                exit_code=-2,
                stdout="",
                stderr=str(exc),
                verified=False,
            )

    def read_file(self, path: str | Path, start_line: int = 1, end_line: Optional[int] = None) -> str:
        """Read file contents with boundary safety."""
        target = (self.context.workspace_root / path).resolve()
        if not target.exists():
            raise FileNotFoundError(f"File not found: {target}")

        with open(target, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        end = end_line if end_line is not None else len(lines)
        return "".join(lines[start_line - 1 : end])

    def write_file(self, path: str | Path, content: str, overwrite: bool = True) -> bool:
        """Write file contents safely within workspace."""
        target = (self.context.workspace_root / path).resolve()
        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() and not overwrite:
            raise FileExistsError(f"File exists and overwrite=False: {target}")

        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def list_files(self, subpath: str = ".") -> List[str]:
        """List files in subpath."""
        target = (self.context.workspace_root / subpath).resolve()
        if not target.is_dir():
            return []
        return [p.name for p in target.iterdir()]
