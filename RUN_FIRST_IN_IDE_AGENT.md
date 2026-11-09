# RUN FIRST — ORBIT v0.7 repository audit and source selection

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Mode:** read-only. Do not edit, format, install, delete, migrate or execute untrusted project scripts during the baseline audit.

## 1. Protect the repository

- Record `pwd`, current branch, commit, remotes, status and untracked files.
- Do not reset, clean, stash, checkout another branch, overwrite files or discard user changes.
- Inspect repository instructions (`AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, Cursor rules, package-level agents files).
- Never print `.env`, secret stores, tokens, SSH keys, cookies or private config contents. Record only whether files exist and their permissions.

## 2. Inventory and baseline

Collect:
- language, framework, package manager, workspaces and runtime versions;
- product apps, backend services, workers, storage, queues and deployment topology;
- directory tree excluding generated files, dependencies and secrets;
- package manifests/lockfiles and dependency licenses;
- auth, workspace model, database schema, API surface and event model;
- current screens, features, integrations, agent runtime and execution boundaries;
- existing tests, CI workflows, build, lint, typecheck and test baseline;
- open security issues, TODOs, feature flags and deployment secrets handling.

Run only safe commands known to be non-destructive and already available. Ask before installing dependencies, changing lockfiles, running database migrations, connecting paid services, modifying a live environment or initiating a remote side effect.

## 3. Produce audit evidence

Create these files only after the founder/maintainer authorizes write mode, or return them in the audit report first:

- `docs/audit/CURRENT_REPOSITORY_AUDIT.md`
- `docs/audit/FEATURE_AND_ROUTE_INVENTORY.md`
- `docs/audit/DEPENDENCY_AND_LICENSE_INVENTORY.md`
- `docs/audit/BASELINE_TEST_REPORT.md`
- `docs/audit/UPSTREAM_GAP_ANALYSIS.md`

The report must distinguish implemented, partial, stubbed, planned and absent features. Include command, exit code, duration and output summary for each check. Do not label a test passed if it was not run.

## 4. Compare upstreams before choosing a foundation

Read `config/upstreams/upstream-lock.yaml` and `docs/02-research/V05_SOURCE_DECISION_MATRIX.md`. The upstream clone helper is for source inspection, not automatic merging.

Priority audit targets:
- OpenMausBot OSS shell: inspect product UI, local server, agent process lifecycle, permissions/approval, app connectors, channel/task model, computer/browser implementation, secret storage, build, tests and enterprise exclusion.
- OpenClaw: identify gateway protocol, extension SDKs, channel model, provider adapters, memory and skill integration. Treat in-process plugins as trusted code.
- Hermes Agent: identify optional runtime/CLI/ACP boundaries; avoid a duplicate control plane.
- OpenHands SDK: coding worker, workspace model, credential isolation and test evidence.
- OpenSandbox: sandbox lifecycle, egress policy, credentials and local/cluster deployment.
- Browser candidates: compare Playwright, agent-browser, Stagehand and Browser Use against one BrowserDriver contract.
- Memory candidates: compare Mem0 and Letta; preserve ORBIT's consent and deletion authority.
- Workflow candidates: compare Temporal and LangGraph without duplicating durable task ownership.
- Skill sources: inspect each canonical skill, its license, scripts, network access and declared permissions.

OpenMausBot `enterprise/` must not be checked out or copied into ORBIT without separate written rights. Do not reuse product name, mascot, logo or trade dress. Preserve Apache/MIT/other licenses and all nested third-party notices. Review each package, not merely the repository root license.

## 5. Required architecture decision record

Recommend exactly one initial choice for each of these: product shell, control-plane stack, agent runtime, browser driver, coding worker, sandbox provider, memory layer, durable workflow engine, vector store, skill format/registry and telemetry. Alternatives may remain optional, but there must be one default and clear fallback per capability.

For each choice compare existing ORBIT implementation, upstream maturity, license, maintenance activity, integration cost, security boundary, performance, developer experience, lock-in, operations burden and rollback path.

## 6. Stop conditions

Stop and report rather than implementing if: source repository is not the expected one; working-tree changes would be overwritten; no reproducible baseline exists; license or enterprise restrictions are unresolved; a secret is exposed; a candidate cannot be safely isolated; multiple components claim ownership of the same state; or the implementation would trigger a paid/external side effect without approval.

## 7. Audit report format

1. Executive summary and repository identity.
2. Existing functionality worth preserving.
3. Architecture and data flow.
4. Build/test baseline and failures.
5. Dependency, license and security inventory.
6. Feature-by-feature parity with ORBIT v0.7 requirements.
7. Upstream component decision matrix.
8. Highest-risk gaps and blockers.
9. Proposed first three vertical slices, changed paths and acceptance tests.
10. Founder approvals required.

## 8. First implementation after approval

Do not begin with all integrations. Implement the smallest vertical slice that proves the actual product: login/workspace → create task → select one agent/runtime → stream progress/events → invoke one safe read-only tool → persist result and evidence → reconnect → cancel. Then add a write action with exact approval and idempotency. Only then scale to specialist teams and more integrations.


## v0.7 repository and storage requirements

- Do not rewrite or replace existing ORBIT capabilities before locating them and comparing the 50 pinned upstreams.
- Produce a repository audit with `python scripts/repo_audit.py <actual-orbit-repo>`.
- Initialize the separate 500 GB drive with `python scripts/orbit_storage.py init <absolute-path>`; keep 60 GB reserve.
- Clone only sources required for the first milestone using `scripts/clone_upstreams.sh`; avoid cloning all large monorepos without a plan.
- Use `scripts/import_upstream_path.py` to stage reviewed source, not to merge it.
- The first source decision must compare actual ORBIT functionality against OpenMausBot public OSS and select one product shell. Never use `enterprise/`.
- Record every copied/modified upstream path with exact commit, file hash, license, notice and tests.


## v0.7 task packet requirement

Before writing code, identify the existing ORBIT module and the upstream module that already solves the problem. The agent must produce a reuse decision (dependency, adapter, selective import, fork or justified rewrite), exact file paths, dependencies, applicable tests, license/NOTICE evidence and rollback plan. Use `scripts/import_upstream_path.py` to stage reviewed source. Never replace an existing implementation without a passing baseline comparison and human approval.


## v0.9 repository reuse, source application and storage rule

Before implementing a feature, inspect existing ORBIT modules and the 50 pinned upstream sources. Follow `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`. Prefer dependencies, adapters or selective source adaptation over rewrites. Use `scripts/create_upstream_worktree.py` for isolated upstream task worktrees and `scripts/import_upstream_path.py` only after license, security and test review. Never modify the immutable pinned checkout or copy OpenMausBot `enterprise/`. The human founder remains the legal and production approval authority.


## ORBIT v0.9 source reuse invariant

Before implementing any capability, search the existing ORBIT code and the 50 pinned upstreams. Reuse the smallest suitable package/module through an adapter; stage and hash-verify imported source; apply it only into a clean `orbit/*` or `feature/*` worktree. Do not rewrite working modules without a written technical reason. Preserve license/NOTICE and source provenance. Never auto-commit, merge, deploy, or access OpenMausBot `enterprise/`. See `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`.

Apply reviewed staged source to a clean ORBIT feature worktree only with `scripts/apply_staged_source.py`; verify its SHA-256 provenance record before adapting. The helper never commits, merges or pushes.
