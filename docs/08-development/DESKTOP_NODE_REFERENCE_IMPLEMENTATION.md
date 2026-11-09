# Local Desktop Node reference implementation notes

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This is an implementation guide, not production-ready code. Use it to shape module boundaries and tests; adapt it to the actual ORBIT runtime and threat model.

## Suggested modules

```text
apps/desktop-node/
  src/
    bootstrap/             # config, version, self-check
    identity/              # pairing, OS key storage, rotation
    transport/             # outbound WSS, heartbeat, lease messages
    session/               # interactive user session detection
    policy/                # local allowlist, risk floor, pause state
    driver/                # fixed executable runner, JSON contract parser
    redaction/             # sensitive labels, field and output filtering
    lifecycle/             # cancellation, process tree, shutdown
    ui/                    # tray/status/stop and pairing UX
    telemetry/             # redacted local events
  tests/
    unit/
    contract-fixtures/
    integration/
```

## Subprocess safety skeleton (Python)

```python
from __future__ import annotations
import asyncio
import json
from pathlib import Path
from typing import Any

MAX_OUTPUT = 1_048_576
ALLOWED = {"status", "permissions", "list-apps", "list-windows", "snapshot", "find", "get", "is"}

class DriverProtocolError(RuntimeError):
    pass

async def run_driver(binary: Path, command: str, argv: list[str], timeout_s: float = 10.0) -> dict[str, Any]:
    if command not in ALLOWED:
        raise PermissionError("desktop command is not enabled")
    if not binary.is_absolute() or not binary.is_file():
        raise FileNotFoundError("pinned desktop driver executable is unavailable")
    # argv must already be constructed from strict typed schemas; never accept raw command strings.
    proc = await asyncio.create_subprocess_exec(
        str(binary), command, *argv,
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        start_new_session=True,
    )
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout_s)
    except asyncio.TimeoutError:
        proc.kill()  # Production implementation must kill the whole process group/tree.
        await proc.wait()
        raise TimeoutError("desktop driver timed out; mutation delivery may be unknown")
    if len(stdout) > MAX_OUTPUT or len(stderr) > MAX_OUTPUT:
        raise DriverProtocolError("desktop driver output exceeded configured limit")
    try:
        payload = json.loads(stdout)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DriverProtocolError("desktop driver returned invalid JSON") from exc
    if not isinstance(payload, dict) or "ok" not in payload or "command" not in payload:
        raise DriverProtocolError("desktop driver envelope is incomplete")
    if payload.get("ok") is False:
        # Production adapter must preserve upstream error.code and disposition.
        raise DriverProtocolError("desktop operation failed; inspect structured error safely")
    return payload
```

Important production hardening omitted from this illustrative skeleton: process-group kill implementation, output streaming cap (not after full `communicate()`), argument validation per command, environment allowlist, driver checksum, rate limiting, structured stderr redaction, cancellation propagation and delivery-disposition validation. Do not paste this sample into production unchanged.

## Rust/Node implementation options

- Rust local node: native packaging and process supervision, strong type safety, shared runtime if the desktop node itself needs a cross-platform native UI.
- Python node: faster integration with FastAPI ecosystem, but must still be packaged, hardened and supervised; use `create_subprocess_exec` only.
- Node/TypeScript node: useful if ORBIT desktop shell already uses Electron/Tauri; use `spawn` with argv and no shell.

Choose based on existing repository/runtime audit, developer capability and packaging constraints. The upstream driver is Rust; that does not force the whole ORBIT backend to be Rust.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
