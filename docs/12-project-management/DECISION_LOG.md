# Decision log

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Decision | Status | Rationale |
|---|---|---|---|
| D-001 | Modular monolith control plane first; isolated workers for risk boundaries | Proposed | reduces early operations burden while retaining execution isolation |
| D-002 | PostgreSQL is source of truth; Redis is cache | Proposed | durable ownership, relational integrity and recoverability |
| D-003 | Durable workflow engine for long-running tasks | Proposed | checkpoints, waits, retries and worker recovery |
| D-004 | Playwright BrowserContext per task/workspace boundary | Proposed | session isolation and repeatable browser automation |
| D-005 | Provider-neutral model adapters | Proposed | avoid lock-in and support local/hosted providers |
| D-006 | Single-agent reliability before multi-agent orchestration | Approved baseline | delegation magnifies execution and security failures |
| D-007 | Tor is deferred and isolated, not a normal proxy mode | Proposed | avoids credential/session leakage and misuse of anonymity network |

When a decision changes, add an ADR with context, alternatives, consequences, date, decision owner and migration plan. Do not silently edit history.

## 2026-11-08 — Native desktop reference

Reviewed `vercel-labs/agent-desktop`. Decision proposed: integrate as a native accessibility driver via Local Desktop Node, not as ORBIT's agent/browser/sandbox. Detailed ADR-013 and research note record rationale, security impact, alternatives and evidence.

## ORBIT v0.2 alignment

The v0.2 roadmap adds a gated desktop workstream after core auth, durable tasks and policy gateway. See `DESKTOP_INTEGRATION_PLAN.md`; desktop is not the first MVP path.
