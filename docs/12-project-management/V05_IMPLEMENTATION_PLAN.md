# ORBIT v0.5 — implementation plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Strategic order

The implementation order is determined by dependencies and risk, not by the number of visible features. The first milestone is a reliable task engine; the agent team and life/work surface depend on it.

| Phase | Work | Primary owners | Exit gate |
|---|---|---|---|
| 0. Audit | Actual ORBIT repo audit, baseline, component map, upstream comparison | CTO, Backend, QA, Security | Audited source and reproducible build/test report |
| 1. Product foundation | Keep/adapt one shell; auth/workspace/project/agent; task/event state; model adapter | CTO, Frontend, Backend | One end-to-end task with persistence, stream, reconnect and cancel |
| 2. Execution kernel | Tool registry, deterministic policy, approvals, audit, idempotency, budgets | Backend, Security, QA | Policy and external side-effect tests pass |
| 3. Coding and browser | OpenHands PoC; one BrowserDriver; Docker sandbox baseline | Coding Worker, Browser, Sandbox | Workspace isolation, egress, cancel and diff/test receipts |
| 4. Knowledge and memory | Ingestion, provenance, scoped memory, retrieval and deletion | Data/RAG, Privacy, QA | No tenant/context leakage; provenance and delete tests pass |
| 5. Skills and connectors | Skill manifest, review/install pipeline, connector OAuth/scopes, routines | Agent Runtime, Security, Product | Immutable lock, permission review, revoke and schedule tests |
| 6. Specialist team | Delegation DAG, specialist roster, team rooms, handoff and synthesis | AI Research, Agent Runtime, Product | Bounded parallel tasks and failure isolation |
| 7. Life/work workflows | Study, research, file, calendar/inbox, business, travel and creative flows | Product, UX, Integrations, QA | Representative end-to-end journeys with approvals and evidence |
| 8. Computer use | Remote sandbox computer and Local Desktop Node read-only first | Desktop, Security, QA | Pair/lease/permission/revoke/stop and semantic action gates |
| 9. Production hardening | Security red-team, load/perf, SBOM, backup/restore, support and docs | SRE, Security, QA | Independent approvals and founder release decision |

## Priority decisions

- Keep current ORBIT implementation wherever it already provides an equivalent safe capability.
- Select one product shell only after audit; OpenMausBot public OSS is a candidate, not an automatic fork.
- Keep OpenClaw and Hermes optional; do not combine their gateways.
- Choose one BrowserDriver baseline and one MemoryProvider default.
- Use one durable workflow authority. Temporal is the primary PoC; LangGraph remains a bounded graph alternative.
- Begin with PostgreSQL/pgvector; only add Qdrant if benchmarks justify it.
- Keep routines paused until the user enables them.
- Keep native desktop out of first MVP; browser and code tasks must be reliable first.

## Workstream owners

See `V05_REUSE_AND_BUILD_WORKSTREAMS.md`, `roles/ROLE_REGISTRY.yaml` and individual role charters. Role names represent virtual workflow agents, not actual employees.

## Decision and change control

Every foundation choice uses an ADR with alternatives, evidence, cost, security, license, reversibility and owner. Any scope increase must identify its effect on schedule, risk, cost and operational complexity. No hidden scope expansion through dependencies.
