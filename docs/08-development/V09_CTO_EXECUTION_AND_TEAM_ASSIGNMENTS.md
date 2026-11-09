# ORBIT v0.9 CTO execution and team assignments

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Executive mandate

Build ORBIT by extending a real existing application and selectively adapting proven upstream modules. Preserve useful working code. Avoid wholesale rewrites, duplicate orchestrators, duplicate gateways, multiple vector databases, and multiple local inference servers without benchmark evidence.

## Responsibilities

| Role | Required output | Gate |
|---|---|---|
| Founder/CEO (human) | Goals, budgets, legal decisions, external commitments and release approval | Final human authority |
| CTO/Principal Architect | Existing-code audit, target architecture, one-owner-per-capability map, ADRs | No duplicate control plane |
| Repository Operations Engineer | Exact pins, clones, worktrees, audit reports, import manifests, upstream sync | Origin/commit/hash verified |
| OSS/IP Analyst | License files, NOTICE, nested dependency, trademark and model terms review | No unknown license in release |
| Security/Privacy Lead | Threat model, secrets, egress, sandbox, skill and personal/work data review | May block unsafe merge |
| Product Shell Engineer | Evaluate OpenMausBot OSS shell; produce build and adaptation report | `enterprise/` excluded |
| Agent Runtime Engineer | Compare OpenClaw and Hermes adapters, select one execution path for MVP | ORBIT retains task/policy state |
| Coding Worker Engineer | OpenHands SDK proof of concept with disposable workspaces | No host credentials by default |
| Browser/Computer Engineer | Playwright baseline, browser isolation, desktop node separation | Read-only first, approvals on writes |
| Memory/RAG Engineer | Mem0 vs Letta, LlamaIndex vs Haystack, Qdrant vs Chroma vs Milvus comparisons | Consent, provenance, ACL, deletion |
| Local Model Engineer | Ollama/llama.cpp baseline; vLLM vs SGLang only on suitable GPU infra | Reproducible hardware benchmark |
| Integrations Engineer | MCP, Composio and direct API connector catalogue | Minimum OAuth scopes |
| QA/Benchmark Engineer | Competitor job suite, unit/e2e, red-team and regression evidence | Independent evidence, not self-certification |
| SRE/Storage Engineer | 500 GB drive, quotas/alerts, backup and recovery plan | Never fill reserve or trust same-disk backup |
| UX/Product Designer | Approval cards, task timeline, agent roster, provenance and pause/cancel | User understands action consequence |

Virtual agents can research, generate code and propose changes. They are not legal employees, officers, security approvers or human reviewers. A bot cannot self-approve a source import, license, secret, payment or release.

## Phases and exit criteria

### Phase 0 — Discover and preserve

- Audit the actual ORBIT source repository read-only.
- Capture git status and current branch; make a verified backup before edits.
- Map current modules to the 44-source reuse catalogue.
- Mark existing features as keep, refactor, adapt, replace or retire with evidence.
- Exit: founder accepts audit and a small MVP vertical slice.

### Phase 1 — Repository operations

- Verify 500 GB disk identity and capacity.
- Initialize the ORBIT folder tree and manifest.
- Clone only chosen source pins.
- Produce static audit, license/NOTICE records and exact source map.
- Exit: origin, commit, storage and license metadata verified.

### Phase 2 — One task end to end

- Use one UI shell and one agent backend behind an adapter.
- Build ORBIT task/event, policy, approval, audit and artifact contracts.
- Run one delegated task with a pause/cancel/approval path.
- Exit: tests prove the complete task and recovery flow.

### Phase 3 — Tools and computer

- Integrate one browser automation baseline and one sandbox worker.
- Add one coding agent and connected-app proof of concept.
- Add a desktop local node only after pairing, leases and narrow permissions.
- Exit: authorization and evidence are enforced by ORBIT, not model prompts.

### Phase 4 — Memory and life workflows

- Add scoped memory, document search, routines, calendar/email/docs connector path.
- Add voice and local-model profile only after actual laptop benchmarks.
- Add personal/work isolation, export and delete propagation.
- Exit: user consent and retrieval provenance are tested.

### Phase 5 — Competitive readiness

- Run reproducible Grok Bot / Muse / dots task scenarios where public claims can be mapped to tasks.
- Score task success, quality, reliability, latency, cost, permissions and user correction.
- Publish honest limitations and benchmark environment.
- Exit: no superiority claim without independent measured results.

## Operating cadence

Every task includes owner, objective, acceptance tests, source files, branch, time/cost budget, risk and rollback. Daily work starts with a clean diff/status; each change goes through build/lint/tests and QA/Security review. Weekly CTO reviews upstream freshness, dependency risks, model spend, task quality, incidents and storage capacity.
