# Functional Requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | Create/manage workspaces and membership | P0 |
| FR-002 | Create/list/rename/delete conversations | P0 |
| FR-003 | Persist and stream messages, reconnect safely | P0 |
| FR-004 | Configure providers securely | P0 |
| FR-005 | Router exposes model capabilities/cost/latency | P0 |
| FR-006 | Create durable task from prompt | P0 |
| FR-007 | Persist task/run/step/event state through restarts | P0 |
| FR-008 | Typed registered tools and schemas | P0 |
| FR-009 | Policy-check/audit every tool call | P0 |
| FR-010 | Claim-level research evidence/citations | P0 |
| FR-011 | Upload supported files and query them | P0 |
| FR-012 | Inspect/download authorized artifacts | P0 |
| FR-013 | Cancel active tasks | P0 |
| FR-014 | Isolated browser with visible progress | P1 |
| FR-015 | Sandboxed repository/Git workflow | P1 |
| FR-016 | Inspect/edit/export/delete memory | P1 |
| FR-017 | Versioned/tested skills | P1 |
| FR-018 | Schedule approved skills | P2 |
| FR-019 | Bounded specialist delegation | P2 |
| FR-020 | Versioned MCP/plugin connectors | P2 |
| FR-021 | Usage and budget view | P1 |
| FR-022 | Workspace policy controls | P1 |
| FR-023 | Workspace export/delete | P1 |
| FR-024 | Clear task states in UI | P0 |
| FR-025 | Human takeover for CAPTCHA/MFA | P1 |

## Desktop requirements (future capability)

- `DSK-FR-001`: user can pair, list and revoke Local Desktop Nodes.
- `DSK-FR-002`: device reports OS, architecture, driver/contract version and supported capabilities.
- `DSK-FR-003`: node requires active signed-in graphical session and local permission checks.
- `DSK-FR-004`: all tasks use expiring workspace/task/device/session-bound leases.
- `DSK-FR-005`: ORBIT offers bounded read-only observations with completeness and evidence status.
- `DSK-FR-006`: only allowlisted typed semantic actions are available.
- `DSK-FR-007`: consequential action approval binds exact target and argument hash.
- `DSK-FR-008`: action receipt exposes delivery/retry/verification scope; unknown delivery is not retried.
- `DSK-FR-009`: local pause/stop and device revocation block new actions.
- `DSK-FR-010`: screenshots and clipboard are off by default and separately permissioned.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.

## v0.3 additional requirements

- `ORG-001`: Internal AI roles must have explicit charters, scope, budget and review partner; no role may bind the company.
- `BRAND-001`: First-party product UI uses original ORBIT design assets and neutral feature labels.
- `BRAND-002`: Legal attribution, license and source provenance remain visible where required.
- `INT-001`: External agent backends must expose a declared capability profile and normalized events.
- `INT-002`: Sandbox provider must enforce deny-by-default network egress and task-scoped resources.
- `INT-003`: Skills must have immutable source, digest, declared tool permissions and license metadata.
- `UI-001`: Generated interfaces must conform to a versioned ORBIT component catalog.
- `UI-002`: Generated UI action events must be re-authorized server-side.
- `LIC-001`: Every release artifact must include a validated SBOM and third-party notices.
