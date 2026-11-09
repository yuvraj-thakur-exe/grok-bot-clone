# High-Level Design

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Component | Owns | Must not own |
|---|---|---|
| Web app | UI state, rendering and task event subscription | Tool execution, provider secrets, durable business truth |
| API/control plane | Auth, workspace policy, CRUD, task/approval commands | Long-running browser/code execution |
| Model router | Provider selection, capability negotiation, usage normalization | Permissions and external side effects |
| Agent orchestrator | Plan, step state, verification/delegation | Direct filesystem or network access |
| Tool Gateway | Schema, permission, risk, approval, idempotency, audit | Model planning |
| Workflow runtime | Durable orchestration, timers, retries, wait/resume | Hidden business authorization |
| Browser worker | Playwright in isolated context | Cross-workspace credentials, host filesystem |
| Code worker | Clone/edit/test/diff in sandbox | Production credentials, Docker socket, host home |
| Data layer | Durable records/artifact metadata | Authorization based only on opaque IDs |

API instances are stateless; workers scale independently. Worker restart must not silently lose tasks. Redis loss cannot destroy accepted tasks. Fail closed if PostgreSQL/audit state is unavailable before a side effect.

## v0.2 local desktop path

The HLD now includes an optional Desktop Session Broker and user-owned Local Desktop Node over outbound authenticated WSS. The node has local policy, pause/stop and a pinned `agent-desktop` driver. It does not share the code worker's privileges. The cloud HLD should not show a generic container directly controlling a host desktop.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
