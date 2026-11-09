# ORBIT v0.5 — CTO and team execution workstreams

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Leadership model

The founder is the human CEO and final decision owner. CTO coordinates the engineering programme; CPO owns product acceptance; COO maintains delivery flow; AI research, software, runtime, browser, desktop, sandbox, data, security, QA, SRE, design, writing, legal/IP and open-source roles provide specialist work. These are AI-assisted role charters, not actual employees or legal officers.

## Workstreams

| ID | Priority | Owner(s) | Deliverable | Gate |
|---|---|---|---|---|
| W0 Repository baseline | P0 | CTO + QA + Backend | Current repo audit, baseline metrics, feature map | Existing code preserved; reproducible baseline |
| W1 Product-shell decision | P0 | CTO + Product + Security + Legal/IP | Shell comparison and build/UX/security ADR | One shell selected; restricted paths excluded |
| W2 Control plane | P0 | Backend + Security | Workspace/task/event/approval/policy model | Canonical state and auth tests |
| W3 Runtime portability | P1 | Agent Runtime + AI Research | One default runtime adapter; optional OpenClaw/Hermes PoCs | Cancellation, usage, errors and artifact conformance |
| W4 Coding worker | P1 | Coding Worker + Sandbox + QA | OpenHands-backed disposable repository task | No workspace escape; tests and diff verified |
| W5 Browser | P1 | Browser Engineer + Security | Driver benchmark, one baseline adapter | Domain policy and egress tests |
| W6 Skills | P1 | Agent Runtime + Security + Open Source | Catalogue, intake, digest lock and sandbox | No unreviewed execution; no mass install |
| W7 Memory and RAG | P1 | Data/RAG + Privacy + QA | Mem0/Letta comparison, source-aware retrieval | Consent, scopes, provenance, delete verified |
| W8 Durable workflows | P1 | Backend + SRE | Temporal PoC; LangGraph tradeoff report | One retry and checkpoint authority |
| W9 Product team UI | P1 | Frontend + UX | Agents, projects, activity, approvals and artifacts | Complete journey user-tested |
| W10 Personal/work routines | P2 | Product + Integrations + QA | Study, research, calendar/inbox and business routines | User-visible scope, pause/revoke, approvals |
| W11 Desktop | P2 | Desktop + Security + QA | Pairing and read-only observation then narrow actions | Local stop, permission and lease tests |
| W12 Supply chain | P0/P1 | SRE + Security + Legal/IP | SBOM, license/vulnerability gates and provenance | No unresolved release-blocking issue |
| W13 Continuous improvement | P2 | AI Research + QA | Offline skill/prompt optimization | Holdout improvement; human-reviewed PR |

## Weekly cadence

- Architecture and source-reuse review: decisions, patches, upstream syncs and dependency overlap.
- Product review: user journeys, friction, accessibility, prioritization and competitor evidence.
- Security/license review: new dependencies, permissions, skill changes, secrets, CVEs, license exceptions.
- QA/evaluation review: tests, benchmarks, reliability, safety and cost.
- Operations review: queue age, latency, availability, recovery, cost and incident status.
- Founder review: budget, risk acceptance, hiring/legal/commercial questions and release decisions.

## Definition of a complete workstream

A source decision, code owner, testable deliverable, data-flow map, security/license review, operational owner, rollout/rollback, documented limitations and evidence. “Integrated” means built and tested against the target ORBIT repository, not merely cloned.
