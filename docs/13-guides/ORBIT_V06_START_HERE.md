# ORBIT v0.7 — start here

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Read in this order

1. `README.md` — product thesis and source boundaries.
2. `AGENTS.md` — mandatory engineering rules, including reuse-first.
3. `RUN_FIRST_IN_IDE_AGENT.md` — audit the actual ORBIT application repository.
4. `docs/02-research/REPOSITORY_OPERATIONS_ANALYSIS.md` — what to reuse from each upstream repository.
5. `docs/04-system-design/REPOSITORY_CODE_REUSE_AND_IMPORT_SPEC.md` — how to copy, adapt, test and maintain source.
6. `docs/10-infrastructure/500GB_STORAGE_ARCHITECTURE.md` — dedicated drive layout.
7. `docs/12-project-management/V06_CTO_AND_TEAM_EXECUTION_PLAN.md` — team execution and release gates.
8. `docs/09-quality/V06_COMPETITOR_PARITY_AND_BENCHMARKS.md` — quality bar.
9. `config/upstreams/upstream-lock.yaml` — 35 immutable commit pins.

## Initialize the dedicated drive

Windows PowerShell:

```powershell
py -3 scripts/orbit_storage.py init E:\ORBIT-Storage
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
py -3 scripts/orbit_storage.py status $env:ORBIT_HOME
```

Linux:

```bash
python3 scripts/orbit_storage.py init /mnt/orbit-storage
export ORBIT_HOME=/mnt/orbit-storage
python3 scripts/orbit_storage.py status "$ORBIT_HOME"
```

The initializer creates folders, a manifest and soft budget targets. It does not format a disk, encrypt it, move files or create hard quotas. 60 GB is reserved from the nominal 500 GB target.

## Acquire a small, useful source set

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox
```

After the first audit:

```bash
bash scripts/clone_upstreams.sh --openclaw --hermes --skills-index --stagehand
```

The helper fetches pinned commits only. It does not install dependencies or merge code. OpenMausBot `enterprise/` is excluded from its sparse checkout.

## Audit and stage code

```bash
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openmausbot"
python scripts/import_upstream_path.py --help
```

Copy one exact, reviewed source file/directory to `10-source-intake/`, preserve the generated import manifest and inspect its transitive dependencies. Then adapt it in the real ORBIT repository through a focused PR.

## First implementation milestone

Audit existing ORBIT source; preserve what works. Then implement one full vertical slice: workspace → task → selected backend → read-only tool → evidence/artifact → reconnect/resume → cancellation. Only after that introduce exact-approval connector writes, durable routines and desktop control.

## Current implementation truth

No actual ORBIT application repo was supplied in this task. No upstream application has been merged or built against ORBIT. This release adds pinned sources, operational scripts, analysis and instructions; it does not claim runtime integration.
