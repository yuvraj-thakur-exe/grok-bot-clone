# ORBIT engineering documentation index — v1.0

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier release directories/documents are retained as historical decision records.

**Status:** Reuse-first engineering and repository-operations blueprint. No ORBIT runtime implementation is bundled.

| Area | Contents |
|---|---|
| `00-foundation/` | Charter, project scope, vision, operating model, organization, brand and workforce governance |
| `01-product/` | PRD, requirements, stories, use cases, features, acceptance, MVP and priorities |
| `02-research/` | Competitor surface, 50-source catalogue, exact module maps, feasibility, licensing observations and repo operations analysis |
| `03-architecture/` | HLD/LLD, policy/task plane, browser/desktop/sandbox, external runtime, personal-work OS and adapters |
| `04-system-design/` | API, database, auth, queues, storage, repo import, skills and backend contracts |
| `05-ai-system/` | Agent loop, orchestration, memory/RAG, model routing, research, connectors, routines and skills |
| `06-security/` | Threat model, approvals, privacy, license compliance, source trust, SBOM and supply-chain controls |
| `07-design/` | Design system, UX, accessibility, rebranding and screen specifications |
| `08-development/` | Standards, IDE workflows, CTO execution, team roles and repository operations |
| `09-quality/` | Test strategy, conformance, competitor parity, evaluation and performance gates |
| `10-infrastructure/` | 500 GB storage, deployment, sandbox, CI/CD and backup/recovery |
| `11-operations/` | Runbooks, observability, desktop operation, performance and recovery |
| `12-project-management/` | Roadmap, WBS, risks, decisions and integration priorities |
| `13-guides/` | Start here, copy/modify, CLI operation, deployment and handoff |
| `14-templates/` | ADR, feature, incident, research and upstream adoption templates |
| `roles/` | 30 virtual role charters and role registry |
| `scripts/` | Pinned clone, audit, intake, apply, storage, worktree and validation helpers |
| `tests/operations/` | Isolated regression tests for repository/storage tooling |
| `architecture/diagrams/` | System, task, trust, desktop, storage and source-import Mermaid diagrams |
| `docs/source-material/` | User-provided source material preserved byte-for-byte with provenance |

## Current v1.0 documents

- `13-guides/V10_START_HERE.md` — current entry point and first-run sequence.
- `13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md` — exact clone → inspect → worktree → stage → apply → adapt → test → sync workflow.
- `02-research/V10_OPEN_SOURCE_FILE_LEVEL_ADOPTION_MAP.md` — module-level reuse maps for 50 pinned repositories.
- `02-research/V10_OPEN_SOURCE_DECISIONS_AND_EXCLUSIONS.md` — six new candidates and reasons other projects were not promoted.
- `02-research/ORBIT_REPOSITORY_OPERATIONS_ANALYSIS_V10.md` — state model, tooling, storage, risks and limits.
- `03-architecture/V10_INTEGRATED_PERSONAL_WORK_OPERATING_SYSTEM.md` — study, research, coding, communication, home, business and creative workflows.
- `08-development/V10_CTO_IMPLEMENTATION_WARROOM.md` — team ownership, authority boundaries, workstreams and release gates.
- `09-quality/V10_COMPETITIVE_PARITY_BENCHMARKS.md` — reproducible Grok Bot/Muse/dots parity tests.
- `10-infrastructure/V10_500GB_STORAGE_OPERATIONS.md` — dedicated drive setup and operating policy.
- `14-templates/UPSTREAM_ADOPTION_RECORD_TEMPLATE.md` — reusable evidence record for every imported module.

## IDE entry points

- `AGENTS.md` is authoritative for coding agents.
- `RUN_FIRST_IN_IDE_AGENT.md` requires a read-only audit of the actual app before any rewrite.
- `CODING_AGENT_MASTER_PROMPT.md` provides CTO/developer team instructions.
- `CODEX.md`, `CLAUDE.md`, `GEMINI.md`, `ANTIGRAVITY.md`, `.cursor/rules/orbit.mdc`, `.agent/rules/orbit.md` and `.github/copilot-instructions.md` point back to the same policy.

## Architecture truths

- ORBIT owns canonical task state, user identity, authorization, approvals, memory consent and audit.
- Browser, native desktop, coding/shell and sandbox execution are separate security domains.
- Pinning a repository is not production approval. Every source file and transitive package is separately reviewed.
- Imported code is copied only into a clean feature worktree, with hashes/provenance and no automatic git commit/merge.
- Model weights, datasets and third-party assets have separate terms from their runtime engines.
- The 500 GB drive is not RAM/VRAM and is not a disaster-recovery backup.
- Competitor parity is only claimed through repeatable end-to-end benchmark evidence.
- Virtual role agents do not have employment, legal, spending or release authority.

## Historical versions

Earlier v0.2–v0.9 documents remain for traceability. Their repository counts and status apply only to their own release snapshots. The current lock at `config/upstreams/upstream-lock.yaml` is the authoritative 50-entry snapshot.
