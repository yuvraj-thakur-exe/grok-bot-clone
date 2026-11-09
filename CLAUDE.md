# Claude Code instructions

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Current baseline:** ORBIT v1.0.0-draft. Follow `AGENTS.md` as the canonical policy.

## Mandatory workflow

- Audit existing code and preserve current changes before edits.
- Reuse existing ORBIT implementation or exact pinned upstream code before writing replacements.
- Read `CODING_AGENT_MASTER_PROMPT.md`, `RUN_FIRST_IN_IDE_AGENT.md`, `docs/02-research/V05_SOURCE_DECISION_MATRIX.md` and `docs/04-system-design/V05_REUSE_AND_ADAPTATION_PLAYBOOK.md`.
- Keep ORBIT's task/workspace/policy/approval/memory authority canonical. Integrate OpenClaw, Hermes and other runtimes only behind adapters.
- Exclude OpenMausBot `enterprise/`; preserve all license, NOTICE and third-party attribution; do not reuse upstream marks or mascot.
- Do not install community skills or run upstream scripts automatically. Review source, license, permissions, digest and sandbox requirements first.
- Never claim a feature/test/integration is complete without execution evidence.

## Required result

Provide a concise plan, exact file-level diff, tests run and outcomes, license/security impact, docs updated, rollback notes and remaining limitations. The human founder approves spending, legal commitments, public releases and production deployments.


## v0.9 repository reuse, source application and storage rule

Before implementing a feature, inspect existing ORBIT modules and the 50 pinned upstream sources. Follow `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`. Prefer dependencies, adapters or selective source adaptation over rewrites. Use `scripts/create_upstream_worktree.py` for isolated upstream task worktrees and `scripts/import_upstream_path.py` only after license, security and test review. Never modify the immutable pinned checkout or copy OpenMausBot `enterprise/`. The human founder remains the legal and production approval authority.


## ORBIT v0.9 source reuse invariant

Before implementing any capability, search the existing ORBIT code and the 50 pinned upstreams. Reuse the smallest suitable package/module through an adapter; stage and hash-verify imported source; apply it only into a clean `orbit/*` or `feature/*` worktree. Do not rewrite working modules without a written technical reason. Preserve license/NOTICE and source provenance. Never auto-commit, merge, deploy, or access OpenMausBot `enterprise/`. See `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`.

Apply reviewed staged source to a clean ORBIT feature worktree only with `scripts/apply_staged_source.py`; verify its SHA-256 provenance record before adapting. The helper never commits, merges or pushes.
