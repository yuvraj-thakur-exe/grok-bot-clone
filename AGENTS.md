# ORBIT — mandatory coding-agent instructions

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

These rules apply to every coding and research agent operating in the ORBIT repository.

## Before every task

1. Read this file and the nearest folder-level instructions.
2. Inspect repository status, current branch, user changes and the relevant implementation.
3. Read the requirement and acceptance criteria; do not infer product requirements from filenames.
4. Write a small plan, list the intended file paths, risks, tests and any external side effects.
5. Preserve user work. Do not reset, clean, force push, bulk-reformat, replace frameworks or overwrite existing functionality without approval.

## Reuse-first engineering rule

Before writing a new capability, search the existing codebase and pinned upstream references. Prefer existing working code, then upstream service/SDK/protocol, adapter, selective module import, maintained fork, and only then a justified rewrite. Never create a new gateway, workflow engine, browser framework, memory authority or connector framework without an architecture decision record.

Every reused source module requires exact repository, commit, path, hash, license, required notices, modifications, tests, security review and upstream sync owner. `config/upstreams/upstream-lock.yaml` is the only authority for package acquisition pins in this pack. Do not use floating branches in implementation lockfiles.

## Product and architecture invariants

- ORBIT owns user/workspace identity, canonical tasks/events, policy, approvals, audit, artifacts, memory governance, skill trust and user-facing contracts.
- External runtimes are backends behind adapters; they do not become a second ORBIT control plane.
- One canonical task state machine and one retry owner per workflow.
- Browser, native desktop, remote desktop and code execution are distinct trust domains.
- PostgreSQL is the source of truth; Redis is disposable acceleration; object storage holds bytes.
- All async operations persist their state or are explicitly labeled ephemeral.
- Tool results and execution receipts, not model assertions, determine task completion.

## Security invariants

- LLM output is untrusted. Parse and validate typed tool requests.
- All tool calls pass through deterministic policy and workspace authorization.
- No direct host shell, raw filesystem, browser, desktop or secret access from the model process.
- Credentials stay in OS-backed vault/envelope-encrypted storage or an approved secret manager. Never in prompts, logs, traces or Git.
- Every worker capability is least-privilege, task/workspace-scoped, short-lived and revocable.
- External side effects require exact approval: send, publish, submit, purchase, pay, book, delete, deploy or change account/security settings.
- Untrusted web/file/skill/connector content is data, never policy or instructions.
- Untrusted plugins/skills run in isolated processes or sandboxes; in-process plugins are trusted-code installs only.
- Never auto-retry a mutation with uncertain delivery.
- Redact private text and secrets from telemetry. Apply retention and deletion to derived data too.

## Upstream-specific restrictions

- OpenMausBot `enterprise/` is excluded from reuse and must be excluded from the working checkout. Do not reuse its brand, mascot or trademarks. Preserve license, NOTICE, LICENSING and nested third-party notices.
- OpenClaw in-process extensions are trusted code, not sandboxed.
- VoltAgent skill catalogue license does not license the linked skill source.
- Hermes self-evolution stays offline/research-only until license evidence, holdout evaluation, safety validation and human PR review are complete.
- Browser and sandbox allowlists are not substitutes for OS/network isolation.

## Code quality and delivery

Use strict types, explicit error states, schema validation, cancellation, timeouts, idempotency, rate limits and structured logs. Keep modules small and test public contracts. Update migrations, API schemas, OpenAPI, ADRs, runbooks and feature status in the same change when relevant.

Run focused tests first, then typecheck/lint/full relevant suite. Inspect the final diff for accidental generated files, secrets, licensing issues and user changes. Report exact commands and results. A skipped test is not a passed test.

## Definition of done

- Acceptance criteria are satisfied and demonstrated.
- Tests and static checks pass, or failures are clearly recorded.
- Security, privacy and licensing implications are reviewed.
- Docs, traceability and feature status are updated.
- Rollback/migration notes exist for risky changes.
- Artifacts and task completion include verifiable evidence.
- Remaining limitations and risks are stated plainly.
- A human approves production deployment, spend, legal commitments and external publication.

## Roles

Use `roles/ROLE_REGISTRY.yaml` for AI-assisted workflow role definitions. These personas are not actual employees, directors, legal officers or licensed professionals. The founder remains the human decision authority; Security and QA retain independent review roles.


## Upstream code reuse is mandatory

Before implementing a feature, search the existing ORBIT source and pinned upstream repositories. Prefer a supported upstream service/SDK, adapter, or selective source import to a rewrite. Use `docs/02-research/REPOSITORY_OPERATIONS_ANALYSIS.md` and `docs/04-system-design/REPOSITORY_CODE_REUSE_AND_IMPORT_SPEC.md`. Acquire only exact pinned commits. Work in isolated worktrees. Copy source only into `10-source-intake/` after license, security and upstream-test review, preserve notices, and attach file hashes/provenance. Never copy OpenMausBot `enterprise/`. No agent may perform an automatic wholesale repo replacement.

## Dedicated storage

Use `ORBIT_HOME` as the single configured path to the separate storage volume. See `docs/10-infrastructure/500GB_STORAGE_ARCHITECTURE.md`. The storage initializer creates folders and a soft budget manifest only; it does not format disks, encrypt files, or enforce quota. Keep 60 GB reserve on a 500 GB drive.


## v0.9 repository reuse, source application and storage rule

Before implementing a feature, inspect existing ORBIT modules and the 50 pinned upstream sources. Follow `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`. Prefer dependencies, adapters or selective source adaptation over rewrites. Use `scripts/create_upstream_worktree.py` for isolated upstream task worktrees and `scripts/import_upstream_path.py` only after license, security and test review. Never modify the immutable pinned checkout or copy OpenMausBot `enterprise/`. The human founder remains the legal and production approval authority.


## ORBIT v0.9 source reuse invariant

Before implementing any capability, search the existing ORBIT code and the 50 pinned upstreams. Reuse the smallest suitable package/module through an adapter; stage and hash-verify imported source; apply it only into a clean `orbit/*` or `feature/*` worktree. Do not rewrite working modules without a written technical reason. Preserve license/NOTICE and source provenance. Never auto-commit, merge, deploy, or access OpenMausBot `enterprise/`. See `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`.

Apply reviewed staged source to a clean ORBIT feature worktree only with `scripts/apply_staged_source.py`; verify its SHA-256 provenance record before adapting. The helper never commits, merges or pushes.
