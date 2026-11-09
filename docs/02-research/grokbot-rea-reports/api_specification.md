# GROKBOT-RE: Protocol & API Specification

## 1. Local IPC Protocol (Electron Main <-> Renderer)
Communication uses Electron's `contextBridge` and `MessagePort`:
- `sand:boot-snapshot-sync`: Synchronous handshake returning environment, theme, and boot state.
- `sand:coordinator-port-request`: Requests a direct MessageChannel port to the background agent coordinator.
- `sand:coordinator-port`: Delivers MessagePort for high-throughput streaming and agent events.
- `sand:encode-png`: Offloads image conversions to a dedicated web worker / native module.

## 2. Local Execution Daemon Gateway Protocol
- Transport: Local Unix Domain Socket / Windows Named Pipe or Localhost TCP Gateway
- Message Schema:
```json
{
  "type": "exec",
  "command": "powershell -NoProfile -Command ...",
  "cwd": "D:\\workspace",
  "environment": { "PATH": "..." },
  "permission": "workspace_readwrite",
  "generation": 0
}
```
- Stream Events:
  - `stdout`: Raw bytes / text output chunks
  - `stderr`: Error output chunks
  - `exit`: Process exit code

## 3. Cloud / LLM Backend Protocol
- Primary Endpoints:
  - Chat Completion: `POST /api/chat/stream` (SSE / ConnectRPC streaming)
  - Auth Exchange: `POST /connectors-oauth-exchange-code/`
  - Telemetry: `POST /tev1/v1`
