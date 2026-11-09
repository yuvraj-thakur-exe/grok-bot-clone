# ORBIT delivery roadmap — v0.5

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Dates are not committed until the actual application repository, team capacity, budget and deployment constraints are audited. The order below is dependency-based; the roadmap is not a claim of current implementation.

| Stage | Outcome | Exit gate |
|---|---|---|
| 0. Audit and decide | Actual repo audit, existing-code map, upstream component decision and architecture ADRs | Reproducible baseline; source and license decisions accepted |
| 1. Workspace vertical slice | Auth, project, agent profile, chat, task, event stream, artifact and reconnect | One end-to-end task can be created, observed and cancelled |
| 2. Execution kernel | Typed tools, policy, approval, idempotency, audit, quotas and checkpoint | Security tests for authorization and external actions pass |
| 3. Coding/browser/sandbox | Coding SDK, one browser driver, isolated workspace execution | Containment, egress, cancel, cleanup and evidence pass |
| 4. Research/files/memory | Search, document ingestion, scoped memory, RAG and deletion | Provenance, ACL and delete propagation pass |
| 5. Skills/connectors | Skill intake, lock, review, OAuth connectors and routines | Immutable provenance, permission and revoke pass |
| 6. Specialist team | Bounded delegation, agent roles, team workspace and synthesis | Parallel task isolation and quality tests pass |
| 7. Personal/work surface | Study, communication drafts, planning, documents, calendar/inbox and other workflows | User-tested flows with clear approval boundaries |
| 8. Computer use | Remote sandbox desktop and Local Desktop Node, read-only first | Pairing, permissions, leases, pause/stop and recovery pass |
| 9. Production readiness | SBOM, vulnerability/license scan, backup/restore, SLO and red-team | Independent approvals and founder release decision |

## Workstream controls

- Preserve existing working ORBIT code.
- Select only one default implementation per capability area.
- Browser, native desktop, sandbox desktop and code execution are separate trust domains.
- Avoid multiple gateways, schedulers, workflow engines, memory authorities or browser frameworks without an explicit ADR.
- All third-party source is pinned and reviewed; no mass skill installation.
- `portless` or similar tooling is local developer experience only, not production ingress.
- Do not claim Firecracker or any upstream performance figures without ORBIT benchmarks.

## Founder decisions

The human founder controls product scope, budget, first-party license, trademark/domain, commercial distribution, legal commitments, public communications, risk exceptions and production release. AI roles prepare evidence and proposals only.
