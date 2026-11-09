# Agent backend contracts

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Normalised event envelope

```json
{
  "schema_version": "1.0",
  "event_id": "evt_...",
  "task_id": "task_...",
  "backend_id": "backend_...",
  "sequence": 12,
  "occurred_at": "2026-11-08T00:00:00Z",
  "type": "progress|message|tool_request|artifact|approval_required|completed|failed|cancelled",
  "payload": {},
  "provenance": {"backend_version": "...", "agent_profile": "..."}
}
```

## Contract invariants

- Event sequence is monotonic per task; duplicate event IDs are idempotent.
- Reconnect supports replay from last acknowledged sequence or returns an explicit replay-unavailable state.
- Tool requests are proposals until ORBIT policy authorizes them.
- Artifacts are uploaded through a scoped artifact API and scanned before download/share.
- `completed` is not user-visible success until ORBIT's acceptance verifier passes.
- Backend failure and task cancellation are distinct terminal states.
- Event payload size is bounded; sensitive output is redacted before durable persistence.

## API families

`/api/v1/agent-backends`, `/api/v1/agent-backends/{id}/capabilities`, `/api/v1/tasks/{task_id}/backends`, `/api/v1/tasks/{task_id}/events`, `/api/v1/tasks/{task_id}/cancel`, `/api/v1/artifacts`.

All endpoints require tenant scope, capability check and audit. Expose a backend only after its adapter passes contract tests.
