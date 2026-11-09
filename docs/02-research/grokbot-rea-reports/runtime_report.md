# GROKBOT-RE: Research Report 02 — Desktop Runtime & Local Execution Engine

## 1. Process Topology & Supervision
Observable runtime state shows a resilient process supervision architecture:
- **Supervisor (`local-exec-supervisor.json`)**:
  - Tracks supervisor PID (observed: `352`) and timestamp.
  - Monitors child daemons, ensuring crash recovery and state resurrection.
- **Daemon (`local-exec-daemon.json` & `.log`)**:
  - Process ID: observed `6196`.
  - Discovered files key ID: `d83f273a0b950677`.
  - Logs indicate active terminal fallback encodings (`OEMCP: 437`, `ACP: 1252`) ensuring Windows console compatibility without garbled text outputs.
  - Communication happens over a local gateway endpoint.

## 2. Sandbox Boundaries & Permissions
Extracted daemon string tables reveal explicit permission modes:
- `workspace_readwrite`: Commands and file modifications strictly bounded within the active workspace root.
- `workspace_readonly`: Read-only file inspection; process execution rejected.
- `insecure_none`: Full system execution without directory bounds.
- `local-computer-use-gate.json`: Explicit toggle `{"isOn": false}` controlling automated mouse/keyboard emulation on the local host.

## 3. IPC & Gateway Protocols
- Handshake via `sand:boot-snapshot-sync` transfers initial environment state.
- Renderer requests MessagePort bridge via `sand:coordinator-port-request`.
- Bidirectional event streaming manages process standard streams (`stdin`, `stdout`, `stderr`, `exit`).

