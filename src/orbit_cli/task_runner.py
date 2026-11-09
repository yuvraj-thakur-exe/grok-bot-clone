from __future__ import annotations

import asyncio
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .platforms import platform_id

TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
SENSITIVE_ENV_RE = re.compile(r"(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|PRIVATE)", re.IGNORECASE)
MAX_MANIFEST_BYTES = 2_000_000
MAX_TASKS = 100
MAX_OUTPUT_BYTES = 2_000_000
LOG_OUTPUT_BYTES = 256_000


@dataclass
class TaskResult:
    task_id: str
    status: str
    return_code: int | None
    duration_seconds: float
    command: str
    message: str = ""
    log_file: str | None = None


def _load_json(path: Path) -> dict[str, Any]:
    if path.stat().st_size > MAX_MANIFEST_BYTES:
        raise ValueError("Task manifest exceeds the 2 MB safety limit.")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read task manifest: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("Task manifest must be a JSON object.")
    return value


def validate_manifest(path: str | Path, workspace_root: str | Path) -> tuple[list[dict[str, Any]], Path]:
    manifest_path = Path(path).expanduser().resolve()
    root = Path(workspace_root).expanduser().resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Task manifest not found: {manifest_path}")
    data = _load_json(manifest_path)
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported task manifest schema_version; expected 1.")
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks or len(tasks) > MAX_TASKS:
        raise ValueError(f"Manifest must contain 1..{MAX_TASKS} tasks.")

    normalized: dict[str, dict[str, Any]] = {}
    allowed_keys = {"id", "argv", "cwd", "depends_on", "timeout_seconds", "platforms", "mode", "env_allowlist"}
    for raw in tasks:
        if not isinstance(raw, dict):
            raise ValueError("Each task must be a JSON object.")
        unknown = set(raw) - allowed_keys
        if unknown:
            raise ValueError(f"Task contains unsupported fields: {', '.join(sorted(unknown))}")
        task_id = raw.get("id")
        if not isinstance(task_id, str) or not TASK_ID_RE.fullmatch(task_id):
            raise ValueError(f"Invalid task id: {task_id!r}")
        if task_id in normalized:
            raise ValueError(f"Duplicate task id: {task_id}")
        argv = raw.get("argv")
        if not isinstance(argv, list) or not argv or any(not isinstance(x, str) or not x or "\x00" in x for x in argv):
            raise ValueError(f"Task {task_id}: argv must be a non-empty array of non-empty strings.")
        if len(argv) > 100 or sum(len(x) for x in argv) > 64_000:
            raise ValueError(f"Task {task_id}: argv exceeds safety limits.")
        if any(len(x) > 16_000 for x in argv):
            raise ValueError(f"Task {task_id}: an argument exceeds the 16 KB limit.")
        mode = raw.get("mode", "inspect")
        if mode not in {"inspect", "workspace-write", "external"}:
            raise ValueError(f"Task {task_id}: mode must be inspect, workspace-write, or external.")
        timeout = raw.get("timeout_seconds", 300)
        if not isinstance(timeout, int) or isinstance(timeout, bool) or not 1 <= timeout <= 3600:
            raise ValueError(f"Task {task_id}: timeout_seconds must be between 1 and 3600.")
        deps = raw.get("depends_on", [])
        if not isinstance(deps, list) or any(not isinstance(x, str) for x in deps):
            raise ValueError(f"Task {task_id}: depends_on must be an array of task IDs.")
        platforms = raw.get("platforms", ["windows", "linux", "macos"])
        if not isinstance(platforms, list) or not platforms or any(x not in {"windows", "linux", "macos"} for x in platforms):
            raise ValueError(f"Task {task_id}: platforms contains an unsupported platform.")
        env_allowlist = raw.get("env_allowlist", [])
        if not isinstance(env_allowlist, list) or any(not isinstance(x, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", x) for x in env_allowlist):
            raise ValueError(f"Task {task_id}: env_allowlist must be an array of environment variable names.")
        dangerous = [name for name in env_allowlist if SENSITIVE_ENV_RE.search(name)]
        if dangerous:
            raise ValueError(f"Task {task_id}: sensitive environment variables cannot be passed through: {', '.join(dangerous)}")
        cwd_raw = raw.get("cwd", ".")
        if not isinstance(cwd_raw, str):
            raise ValueError(f"Task {task_id}: cwd must be a relative path string.")
        cwd = (root / cwd_raw).resolve()
        try:
            cwd.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Task {task_id}: cwd must remain inside the workspace root.") from exc
        if not cwd.is_dir():
            raise ValueError(f"Task {task_id}: working directory does not exist: {cwd}")
        normalized[task_id] = {
            "id": task_id,
            "argv": argv,
            "cwd": str(cwd),
            "depends_on": deps,
            "timeout_seconds": timeout,
            "platforms": platforms,
            "mode": mode,
            "env_allowlist": env_allowlist,
        }

    for task in normalized.values():
        missing = sorted(set(task["depends_on"]) - set(normalized))
        if missing:
            raise ValueError(f"Task {task['id']}: unknown dependencies: {', '.join(missing)}")
        if task["id"] in task["depends_on"]:
            raise ValueError(f"Task {task['id']}: task cannot depend on itself.")

    # A DFS detects cycles before any process starts.
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visiting:
            raise ValueError(f"Dependency cycle detected at task: {task_id}")
        if task_id in visited:
            return
        visiting.add(task_id)
        for dep in normalized[task_id]["depends_on"]:
            visit(dep)
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in normalized:
        visit(task_id)
    return list(normalized.values()), root


def _resolve_executable(token: str) -> str:
    aliases = {
        "@python": sys.executable,
        "@git": shutil.which("git") or "git",
        "@node": shutil.which("node") or "node",
        "@uv": shutil.which("uv") or "uv",
    }
    return aliases.get(token, token)


def _minimal_environment(allowlist: list[str]) -> dict[str, str]:
    base_names = {
        "PATH", "HOME", "USERPROFILE", "HOMEDRIVE", "HOMEPATH", "SYSTEMROOT", "WINDIR",
        "COMSPEC", "PATHEXT", "TEMP", "TMP", "TMPDIR", "APPDATA", "LOCALAPPDATA", "PYTHONPATH",
        "PROGRAMFILES", "PROGRAMFILES(X86)", "LANG", "LC_ALL", "TERM",
    }
    names = base_names | set(allowlist)
    return {key: value for key, value in os.environ.items() if key.upper() in names}


async def _terminate_tree(proc: asyncio.subprocess.Process) -> None:
    if proc.returncode is not None:
        return
    if os.name == "nt":
        try:
            killer = await asyncio.create_subprocess_exec(
                "taskkill.exe", "/PID", str(proc.pid), "/T", "/F",
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            )
            await asyncio.wait_for(killer.wait(), timeout=8)
        except (OSError, asyncio.TimeoutError):
            proc.kill()
    else:
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except (ProcessLookupError, PermissionError):
            proc.terminate()
        try:
            await asyncio.wait_for(proc.wait(), timeout=3)
        except asyncio.TimeoutError:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                proc.kill()


async def _capture_output(proc: asyncio.subprocess.Process) -> tuple[bytes, bool]:
    output = bytearray()
    overflow = False
    assert proc.stdout is not None
    while True:
        chunk = await proc.stdout.read(8192)
        if not chunk:
            break
        if len(output) + len(chunk) > MAX_OUTPUT_BYTES:
            remaining = max(0, MAX_OUTPUT_BYTES - len(output))
            output.extend(chunk[:remaining])
            overflow = True
            await _terminate_tree(proc)
            break
        output.extend(chunk)
    return bytes(output), overflow


def _redact_output(text: str) -> str:
    patterns = [
        (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[A-Za-z0-9._~+/-]+=*"), r"\1[REDACTED]"),
        (re.compile(r"(?i)((?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|client_secret)\s*[=:]\s*['\"]?)[A-Za-z0-9._~+/-]{8,}"), r"\1[REDACTED]"),
    ]
    for pattern, replacement in patterns:
        text = pattern.sub(replacement, text)
    return text


async def _run_one(
    task: dict[str, Any],
    root: Path,
    semaphore: asyncio.Semaphore,
    run_dir: Path,
    allow_workspace_write: bool,
) -> TaskResult:
    task_id = task["id"]
    argv = list(task["argv"])
    argv[0] = _resolve_executable(argv[0])
    display_command = shlex.join(argv)
    if task["mode"] == "external":
        return TaskResult(task_id, "blocked", None, 0.0, display_command, "External side effects are not supported by this developer toolkit.")
    if task["mode"] == "workspace-write" and not allow_workspace_write:
        return TaskResult(task_id, "approval-required", None, 0.0, display_command, "Re-run with --allow-workspace-write after reviewing the manifest.")
    if platform_id() not in task["platforms"]:
        return TaskResult(task_id, "skipped", None, 0.0, display_command, f"Not configured for {platform_id()}.")

    env = _minimal_environment(task["env_allowlist"])
    # Keep this source checkout importable without inheriting an arbitrary caller PYTHONPATH.
    source_dir = root / "src"
    if source_dir.is_dir():
        env["PYTHONPATH"] = str(source_dir)
    started = time.monotonic()
    async with semaphore:
        kwargs: dict[str, Any] = {}
        if os.name == "nt":
            kwargs["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        else:
            kwargs["start_new_session"] = True
        try:
            proc = await asyncio.create_subprocess_exec(
                *argv,
                cwd=task["cwd"],
                env=env,
                stdin=asyncio.subprocess.DEVNULL,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
                **kwargs,
            )
        except FileNotFoundError:
            return TaskResult(task_id, "failed", 127, time.monotonic() - started, display_command, f"Executable not found: {argv[0]}")
        except OSError as exc:
            return TaskResult(task_id, "failed", 126, time.monotonic() - started, display_command, f"Could not start process: {exc}")

        capture_task = asyncio.create_task(_capture_output(proc))
        timed_out = False
        try:
            await asyncio.wait_for(proc.wait(), timeout=task["timeout_seconds"])
        except asyncio.TimeoutError:
            timed_out = True
            await _terminate_tree(proc)
            try:
                await asyncio.wait_for(proc.wait(), timeout=3)
            except asyncio.TimeoutError:
                proc.kill()
        output, overflow = await capture_task

    elapsed = time.monotonic() - started
    decoded = _redact_output(output.decode("utf-8", errors="replace"))
    log_file = run_dir / f"{task_id}.log"
    log_file.write_text(decoded[-LOG_OUTPUT_BYTES:], encoding="utf-8")
    if timed_out:
        status, message = "timed-out", f"Exceeded {task['timeout_seconds']} seconds; process tree termination was requested."
    elif overflow:
        status, message = "output-limit", f"Stopped after exceeding the {MAX_OUTPUT_BYTES} byte output limit."
    elif proc.returncode == 0:
        status, message = "passed", "Completed successfully."
    else:
        status, message = "failed", f"Process exited with code {proc.returncode}."
    return TaskResult(task_id, status, proc.returncode, elapsed, display_command, message, str(log_file))


async def execute_manifest(
    manifest_path: str | Path,
    workspace_root: str | Path,
    max_parallel: int = 3,
    allow_workspace_write: bool = False,
) -> dict[str, Any]:
    if not 1 <= max_parallel <= 8:
        raise ValueError("max_parallel must be between 1 and 8.")
    tasks, root = validate_manifest(manifest_path, workspace_root)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_dir = root / ".orbit" / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    semaphore = asyncio.Semaphore(max_parallel)
    task_map = {task["id"]: task for task in tasks}
    futures: dict[str, asyncio.Task[TaskResult]] = {}

    async def run_task(task_id: str) -> TaskResult:
        if task_id in futures:
            return await futures[task_id]
        async def body() -> TaskResult:
            task = task_map[task_id]
            deps = await asyncio.gather(*(run_task(dep) for dep in task["depends_on"]))
            failed_deps = [item.task_id for item in deps if item.status != "passed"]
            if failed_deps:
                return TaskResult(task_id, "skipped", None, 0.0, shlex.join(task["argv"]), f"Dependency did not pass: {', '.join(failed_deps)}")
            return await _run_one(task, root, semaphore, run_dir, allow_workspace_write)
        future = asyncio.create_task(body())
        futures[task_id] = future
        return await future

    results = await asyncio.gather(*(run_task(task["id"]) for task in tasks))
    result_data = {
        "schema_version": 1,
        "run_id": run_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "workspace_root": str(root),
        "manifest": str(Path(manifest_path).resolve()),
        "max_parallel": max_parallel,
        "results": [asdict(item) for item in results],
    }
    (run_dir / "run-summary.json").write_text(json.dumps(result_data, indent=2) + "\n", encoding="utf-8")
    return result_data
