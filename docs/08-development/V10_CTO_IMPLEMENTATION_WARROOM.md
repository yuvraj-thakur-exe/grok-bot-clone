# ORBIT v1.0 CTO implementation war room

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Executive goal

Deliver ORBIT by preserving the real application's working features and adapting mature open-source building blocks. Do not start by generating a new monolith. The first output is a source inventory and a safe, buildable vertical slice. The founder is the human decision-maker; named CTO/engineering agents are virtual role workflows, not real employees, directors, legal officers or autonomous spending authorities.

## Decision rights

- Human founder: budget, external account connections, privacy policy, licensing decisions, purchase, public communications, production credentials and release approval.
- CTO agent: architecture, sequencing, interface choices, technical acceptance and change proposals. Cannot approve its own high-impact change.
- Repository operations engineer: pins, sparse/shallow clones, worktrees, audits, staging and provenance.
- Product shell engineer: one shell evaluation and adaptation report. Must preserve useful upstream behavior and isolate unsupported enterprise code.
- Agent/runtime engineers: one selected control path and replaceable specialist backends.
- Security/privacy lead: independent veto on unsafe integration, credentials, egress, untrusted code or personal-data boundaries.
- QA/evaluation lead: reproducible evidence and regression gates; cannot accept tests written only by the implementation agent.
- OSS/IP analyst: root and nested licenses, patent/NOTICE obligations, trademarks and model/data terms; this is analysis, not legal representation.

## Workstreams and ordered outputs

| Priority | Workstream | Lead virtual role | Concrete output | Exit gate |
|---|---|---|---|---|
| P0 | Existing ORBIT repository audit | Repository Operations + CTO | Existing tree map, build commands, feature inventory, dependency graph, source/target maps, tests, dirty-state report | Human reviews read-only audit before edits |
| P0 | Product shell decision | Product Shell Engineer | OpenMausBot OSS build/architecture report vs current ORBIT app | `enterprise/` excluded; legal and security review; no branding reuse |
| P0 | Canonical task and policy contracts | CTO + Backend | Task/event/approval/identity API and DB mapping | No duplicate gateways or task authorities |
| P0 | Reuse pipeline | Repository Operations Engineer | Pinned mirrors, audit reports, app worktrees, stage/apply provenance | Hash, origin, commit, license and clean-worktree verified |
| P1 | One agent runtime | Agent Runtime Engineer | OpenClaw or Hermes adapter and provider matrix | Single task authority, pause/cancel/recovery pass |
| P1 | Coding worker | Coding Agent Engineer | OpenHands/Codex/SWE-agent candidate benchmark | Disposable workspace, no host credentials, tested patches |
| P1 | Browser and computer | Browser/Computer Engineer | Playwright baseline; desktop node separate | Read-only, stop/takeover, domain egress and approval tests |
| P1 | Sandbox | Sandbox Engineer | Docker baseline, OpenSandbox optional | Network and credential tests; resource limits; teardown |
| P1 | Apps and channels | Integration Engineer | MCP/Composio/direct connectors with scope catalogue | OAuth scope review, revocation and write approval |
| P1 | Memory and retrieval | Memory/RAG Engineer | One simple memory/RAG baseline then benchmark alternatives | User consent, provenance, ACL and deletion pass |
| P2 | Routines and continuity | Workflow Engineer | Durable timer/event-triggered work and recovery | No duplicate execution; user pause/cancel; retries/idempotency |
| P2 | Voice and mobile | Voice/Mobile Engineer | Local/remote voice path and companion controls | Consent, latency and device-security tests |
| P2 | Human-life workflows | Product + specialist agents | Study/research, documents, calendar, communication, home and business workflow packs | Real task completion evidence, not feature claims |
| P3 | Local inference | Model Runtime Engineer | Ollama/llama.cpp benchmark on actual machine | Memory/latency/cost measured; model terms reviewed |
| P3 | Scaling | SRE + Performance Engineer | vLLM/SGLang/OpenSearch/Milvus scale benchmark | Scale is justified by workload and budget |

## Mandatory execution loop

1. Start with `RUN_FIRST_IN_IDE_AGENT.md` and obtain a read-only audit of the actual ORBIT application repository.
2. Create an issue and acceptance criteria for one vertical feature.
3. Search current ORBIT source for the existing implementation and extension points.
4. Query the 50-repository lock; choose one source candidate and one alternative for comparison.
5. Clone only selected repositories at their exact pins.
6. Read license/NOTICE, packages, security docs, import graph and nearest tests.
7. Write an ADR explaining dependency vs service vs SDK vs source-copy vs fork vs rewrite.
8. Create a clean ORBIT feature worktree; stage exact files and manifest hashes.
9. Adapt the smallest code unit; add ORBIT contracts and tests.
10. QA and Security independently test. Human maintainer approves the commit and PR.
11. Record measured outcomes, limitations and upstream sync date.

## Virtual organization and 30 roles

Use `roles/ROLE_REGISTRY.yaml` and individual role charters. Required cross-functional groupings:

- Executive and product: founder/CEO, CTO/architect, CPO, COO.
- AI and agents: AI research, ML, agent runtime, data/RAG, model runtime, voice/multimodal.
- Engineering: backend, frontend, repository operations, integrations, browser, desktop, sandbox, mobile, home/device.
- Trust and quality: security/privacy, QA/evaluation, DevOps/SRE, benchmark/performance, data governance.
- Design and business: UX, technical writing, open-source/community, legal/IP advisory, finance, customer research.

AI agents can prepare code and evidence. They cannot self-approve security, license, money, external side effects, production deployment or release.

## Weekly operating cadence

- Daily: blockers, CI failures, stale imports and active high-impact task review.
- Twice weekly: integration architecture, source-code adoption and dependency/license review.
- Weekly: demo one end-to-end human task; inspect completion, quality, time, cost, recovery and side effects.
- Every release candidate: SBOM, notices, license review, security report, restore test, migration plan and human acceptance.

## Definition of success

ORBIT earns a competitor claim only when reproducible evaluations show reliable multi-agent handoff, persistent task continuity, useful computer/browser action, connector breadth, transparent approvals, user-controllable memory, recovery after restart, and stronger context boundaries on selected workloads. No design document or repository star count proves parity.
