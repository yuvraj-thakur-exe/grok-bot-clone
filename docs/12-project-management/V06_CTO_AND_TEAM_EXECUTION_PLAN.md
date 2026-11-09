# ORBIT v0.7 — CTO and virtual engineering team execution plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Executive mission

Turn ORBIT into a local-first, privacy-conscious personal and work agent platform that can take a goal, plan it, allocate specialist agents, use approved apps and computers, continue work in the background, return a verifiable artifact, and ask the human for judgment before consequential actions.

The team must leverage existing open-source code and mature interfaces. It must not waste months recreating browser drivers, connectors, inference runtimes, schedulers, memory engines or agent harnesses without proving that reuse is unsuitable.

## CTO architecture decisions

1. Preserve and audit the actual ORBIT repository before changing its technology stack.
2. Product shell: compare existing ORBIT UI to OpenMausBot OSS. Select one shell only; no competing desktop apps.
3. Control plane: ORBIT owns user/workspace/context/task/event IDs, authorization, approval state, audit, memory consent, billing/budgets and artifact provenance.
4. Agent backends: OpenClaw and Hermes are optional adapters; specialist workers can use OpenHands, Pydantic AI or OpenAI Agents SDK after benchmark. Do not run multiple global orchestrators.
5. Connectors: compare Composio, OpenClaw extensions and direct OAuth connectors. Keep a single ORBIT connection registry and policy layer.
6. Browser/computer: Playwright plus one benchmark-selected browser driver; desktop node and sandbox remain separate trust domains.
7. Memory: start with consented scoped memory and ordinary DB search; evaluate Mem0/Letta/Graphiti selectively, never stack three memory authorities.
8. Local models: benchmark Ollama and llama.cpp. Treat model weights, RAM/VRAM needs and licenses separately from runtime software.
9. Knowledge: evaluate Docling/LlamaIndex/Qdrant/Graphiti only for concrete ingestion/search gaps; PostgreSQL remains canonical metadata store.
10. Improvement: evaluate DSPy/GEPA on offline datasets, with holdout gates and human-reviewed PRs.

## Workstreams and owners

| Workstream | Lead role | Deliverable | Gate |
|---|---|---|---|
| A. Actual repository audit | CTO + Repository Operations | Repo baseline, modules, commands, risks | No user changes lost; build status known |
| B. Product-shell selection | Product + Frontend + CTO | Build comparison and one shell decision | Functional prototype, license/brand review |
| C. Upstream operations | Repository Operations | 35 pinned source records, audit reports, intake process | Exact SHAs and license evidence |
| D. Core control plane | Backend | Identity/task/events/policy/approval/audit contracts | Unit and API conformance tests |
| E. Agent runtime adapters | Agent Runtime + AI Research | One external backend and one specialist backend | Cancel/resume/usage/artifact test |
| F. Connectors | Integration Engineer | Two low-risk connectors, OAuth scopes, revocation | Read-only first; write approval test |
| G. Browser/sandbox | Browser + Sandbox Engineer | Browser and code-worker proof of concept | Network isolation, path allowlists, lifecycle cleanup |
| H. Memory and documents | Data/RAG | Scoped memory, document ingestion, retrieval citations | ACL, delete propagation and source evidence |
| I. Local inference and voice | Model Runtime | Ollama/llama.cpp/faster-whisper benchmark | Latency, RAM, CPU/GPU and model-license report |
| J. Skill system | AI Research + Security | Skill format, review workflow, permission model | Quarantine and sandbox enforcement |
| K. Observability | SRE | Trace IDs, usage, cost, latency, errors and redaction | No secret leakage; SLO dashboard |
| L. Competitive acceptance | QA + Product | Frozen Grok/Muse/dots task benchmark | Completion quality + safety + cost report |
| M. Storage/backup | SRE + Security | 500 GB layout, encrypted data, restore drill | 60 GB reserve; tested restore |
| N. Release/compliance | OSS/IP + QA + Founder | SBOM, notices, security/license evidence | Human release approval |

## First 30-day execution sequence

### Days 1–3: establish reality

- Clone or inspect the real ORBIT repository in read-only mode.
- Record tech stack, architecture, data stores, scripts, build/test results, working features and uncommitted changes.
- Initialize the 500 GB storage root and validate free space.
- Acquire only OpenMausBot, OpenClaw and OpenHands SDK sources; audit exact pins.
- Decide whether current ORBIT shell is retained, selectively adapted or replaced by OpenMausBot OSS base.

### Days 4–7: working vertical slice

- Create workspace/context/task IDs and immutable task events.
- Build one chat/workboard surface.
- Connect one agent backend behind an adapter.
- Run one read-only tool call and produce an evidence-bearing artifact.
- Demonstrate cancellation, reconnect and resume.

### Week 2: connected work

- Add OAuth-backed GitHub and one document/storage connector.
- Add browser worker and sandbox provider.
- Add exact approval cards for external writes.
- Create first benchmark set and trace redaction.

### Week 3: personal continuity

- Implement scoped user memory, preferences and per-project context.
- Add one routine/schedule with pause, retry limits, deduplication and notifications.
- Add document ingestion (Docling or LlamaIndex) with citations and deletion propagation.
- Add local model provider benchmark (Ollama vs llama.cpp) with small models only.

### Week 4: hardening and evaluation

- Run security tests, prompt-injection tests, connector revocation tests and sandbox escape probes appropriate to the prototype.
- Run parity tasks for project work, email/calendar, web research, coding and document creation.
- Review license, notices, SBOM, vulnerabilities, model terms and telemetry.
- Fix top failures, document limits and obtain human acceptance before exposing to real accounts.

The schedule is a sequencing proposal, not a guarantee of completion time. The scope must shrink if gates fail.

## Agent delegation rules

- CEO/Founder: strategy and binding decisions. Human only.
- CTO: architecture, task decomposition, dependency decisions and technical gate; cannot approve its own risky production action.
- Repository Ops Engineer: clone/pin/audit/worktree/import and provenance only.
- Backend/Frontend/AI roles: implement bounded tasks in separate worktrees.
- Security: independent policy, secrets, egress, isolation and threat review; may block.
- QA: independent test evidence; may block acceptance.
- OSS/IP analyst: license, notice and trademark report; qualified counsel handles legal advice.
- SRE: deployment, backup, rollback, performance and operations.
- Founder approves spend, external communication, production deployment, purchase/payment, legal commitment and public release.

## Required daily task packet

Every agent task includes objective, user/workspace scope, upstream repo/commit if applicable, allowed paths, prohibited paths, available tools, network policy, credential handles, cost/time budget, risk/approval class, test requirements, expected artifact and rollback plan.

## Success metrics

- reuse ratio: percentage of capabilities delivered by proven upstream code/SDK without duplicative rewrite (tracked with provenance, not gamed)
- integration lead time and patch carry count
- task completion accuracy and evidence completeness
- approval correctness and unauthorized side-effect rate (target zero)
- resume/cancel correctness for long-running tasks
- cross-context memory leakage (target zero)
- skill/plugin compromise detection rate
- p50/p95 latency, model/tool cost per successful task
- disk free headroom, backup RPO/RTO and restore success
- user trust, correction rate and task satisfaction

## Exit criteria

The first usable ORBIT alpha is not a set of demos. It must complete a multi-step user task, keep working after client disconnect, let the user change direction, ask before sensitive actions, recover after worker failure, cite its sources, export a usable artifact, and show a trustworthy audit trail. Security and QA sign off independently; founder approves release.
