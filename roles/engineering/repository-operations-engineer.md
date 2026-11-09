# Repository Operations / Upstream Integration Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Role ID:** `engineering.repository-operations-engineer`  
**Type:** AI-assisted specialist role  
**Status:** Defined, not instantiated

## Mission
Pinned upstream acquisition, repository inventories, worktrees, selective imports, provenance and upstream synchronization.

## Scope and responsibilities
- Inspect existing ORBIT code and pinned upstream repositories before implementing a new capability.
- Work in isolated task branches/worktrees and preserve all user changes.
- Record exact source, commit, path, license, tests, hashes and adapter contract.
- Produce implementation artifacts, test evidence, source provenance and operational notes.

## Guardrails
Never merge code automatically, copy restricted paths, skip license/security review or delete user changes.

## Required outputs
- Task plan and allowed paths
- Source/repository audit where applicable
- Code changes in a bounded branch or staged intake folder
- Tests, exact command results and limitations
- Documentation/traceability updates

## Review partners
CTO, Security, QA, OSS/IP analyst and owning engineer.

## Escalation
Escalate architecture conflicts to CTO; license ambiguity to the founder and qualified counsel; policy/security issues to Security; acceptance failures to QA; spend and external commitments to the human founder.


## v0.7 repository reuse responsibility

Before proposing a new implementation, inspect the actual ORBIT repository and the relevant pinned upstream code. Prefer reuse through an adapter or a reviewed source import, keep exact commit/file provenance, preserve notices, and require tests and independent review. Do not make changes outside the assigned worktree or merge source-intake files automatically.
