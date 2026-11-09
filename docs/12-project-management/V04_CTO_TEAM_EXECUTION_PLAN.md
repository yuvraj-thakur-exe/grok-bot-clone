# ORBIT v0.4 CTO and virtual company execution plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Executive directive

The CTO team is instructed to turn ORBIT into a reuse-first multi-agent personal/work platform. The team must reuse stable upstream code wherever possible, not independently rewrite mature gateways, desktop shells, browser drivers, memory services, skill registries or coding agents.

This is an engineering organization workflow. Its AI role agents are not actual employees or legal officers. The human founder remains accountable for spend, legal commitments, external communication and production releases.

## Virtual team assignment

| Role | Responsibility for v0.4 | Deliverable |
|---|---|---|
| Founder / CEO (human) | Product position, budget, distribution/licensing, risk acceptance and release decision | Approved product scope and constraints |
| CTO / Principal Architect | Choose product foundation, enforce single source of truth, approve adapter seams and ADRs | Foundation decision and architecture map |
| CPO / Product Lead | Convert competitor feature surface into product requirements and journeys | Prioritized PRD, milestone acceptance |
| COO / Delivery Lead | Coordinate workstreams, blockers, weekly review and dependency order | Delivery dashboard and decision log |
| Chief AI Research Officer | Evaluate runtime/model/evaluation alternatives; benchmark skills and agent behavior | Research matrix and reproducible benchmark |
| Agent Runtime Engineer | Integrate OpenMausBot/OpenClaw/Hermes via adapters | Runtime conformance PoCs |
| Backend Engineer | Identity, workspace/task model, approvals, connector and API integration | First-party control-plane integration |
| Frontend Engineer + UX Designer | Reuse/adapt the selected product shell and brand it with ORBIT identity | Working ORBIT desktop/web workspace |
| Browser Automation Engineer | Stagehand/Playwright/agent-browser comparison | BrowserDriver with task tests |
| Desktop Computer-Use Engineer | Reuse safe computer modules; build paired local node and user takeover | Desktop observe/act PoC |
| Data/RAG Engineer | ORBIT memory model; Mem0 vs Letta evaluation | Memory/knowledge ACLs, provenance, deletion and retrieval benchmark |
| Sandbox Runtime Engineer | Docker baseline/OpenSandbox evaluation | Isolated code execution with egress limits |
| Security/Privacy Lead | Review licenses, runtime permissions, plugin trust, credential flow and privacy | Threat model, license gates and block list |
| Legal/IP Compliance Analyst | Check enterprise carve-outs, notices, trademark and OSS conditions | Per-upstream legal review record |
| QA / Agent Evaluation Engineer | Test parity, reliability, failure recovery and unsafe-action behavior | Regression suite + benchmark report |
| DevOps/SRE Engineer | Build reproducibility, SBOM, telemetry, packaging and recovery | CI gates, observability, restore plan |
| Open Source/Developer Relations | Maintain upstream remotes, patches, attribution and contribution process | Upstream sync and contribution policy |
| Technical Writer | User setup, capability disclosures and privacy documentation | Updated docs and onboarding |

## Workstreams and sequence

| ID | Priority | Owner | First deliverable | Exit gate |
|---|---|---|---|---|
| V4-A Existing ORBIT source audit | P0 | CTO + Backend + QA | Current repository map and code coverage matrix | No rewrite/replacement decision before baseline |
| V4-B OpenMausBot OSS base decision | P0 | CTO + Legal/IP + Security | Build and license audit; fork-vs-selective-reuse ADR | `enterprise/` excluded; `NOTICE` retained; secret storage plan approved |
| V4-C Upstream code import | P0 | Backend + Frontend | Pinned upstream workspace and minimal product-shell boot | Clean build/test and source provenance |
| V4-D Unified control plane | P0 | Backend + Security | Auth/workspace/task/approval/audit seams | Cross-workspace authorization and exact approvals tested |
| V4-E Runtime adapters | P1 | Agent Runtime Engineer | OpenClaw and Hermes external adapter PoC | Backend events, cancellation and usage tests |
| V4-F Skill ecosystem | P1 | AI Research + Security | Curated discovery and skill lock pipeline | Each skill has digest/license/permission review |
| V4-G Memory | P1 | Data/RAG + Privacy | Mem0 + LlamaIndex proof; compare Letta and Qdrant only if benchmarks justify | Consent, scopes, source, expiry, correction/deletion |
| V4-H Coding worker | P1 | Sandbox + Agent Runtime | OpenHands SDK coding task in disposable workspace | Cannot escape workspace; output diff/tests auditable |
| V4-I Browser and desktop | P1/P2 | Browser + Desktop | Stagehand comparison; local desktop safe path | Separate trust domains, approval and stop/takeover |
| V4-J Personal life/work journeys | P1 | CPO + UX + QA | 8 vertical workflows end-to-end | User sees progress, can intervene, result verifiable |
| V4-K Offline self-improvement | P2 | AI Research + QA | GEPA skill optimization experiment | Holdout test, safety pass, PR and rollback only |
| V4-L Production readiness | P0 at release | SRE + Security + QA | SBOM, security review, backup/restore and SLO report | Human approval only after independent signoff |

## Eight first workflows

1. Research a question, cite authoritative sources and create a report.
2. Organize notes/files into a project knowledge space with user-visible sources.
3. Create a study plan and run a quiz/revision session.
4. Audit a GitHub repository, propose a plan, modify code in a sandbox, run tests and produce a diff.
5. Triage inbox/calendar data and draft a response/schedule; ask before sending or booking.
6. Create/edit an office artifact (document, spreadsheet or presentation) and validate the file.
7. Delegate a bounded task to two or more specialist agents and return one verified deliverable.
8. Run a scheduled reminder or routine, record the run and allow pause/revoke.

## Weekly operating cadence

- Architecture review: decisions, source changes, adapter boundaries and technical debt.
- Product review: user journeys, priority, usability and differentiation.
- Security/license review: new dependencies, skills, plugins, vulnerabilities and permissions.
- QA/evaluation review: regression results, benchmark shifts, safety failures and reliability.
- Operations review: cost per completed task, latency, queue age, availability and incidents.
- Executive review: spend, risks, milestones and founder approvals.

## Stop conditions

Stop an integration if its license is unclear, it requires excessive permissions, it cannot be isolated, it breaks the canonical task model, it cannot be cancelled safely, it leaks data, it has no maintainable update path, or its operational burden exceeds the benefit. Produce a decision memo and switch to the next candidate; do not rewrite as a reflex.

## Superseded by the v0.5 coordinated baseline

Use `docs/13-guides/ORBIT_V05_START_HERE.md`, `docs/12-project-management/V05_IMPLEMENTATION_PLAN.md` and `docs/12-project-management/V05_REUSE_AND_BUILD_WORKSTREAMS.md` as the current implementation order. The v0.4 source analysis remains historical evidence; the actual ORBIT repository audit determines the final product-shell and runtime selection.
