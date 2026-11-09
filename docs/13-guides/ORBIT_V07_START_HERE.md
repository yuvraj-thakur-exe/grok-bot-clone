# ORBIT v0.7 — start and operate

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## What is in this package

This is the CTO/engineering specification, upstream analysis, 35-repository pin catalogue, storage and repository operation tooling, role charters, IDE-agent rules and quality/compliance plan. It does not contain the application runtime or full upstream source trees.

## Read first

1. `RUN_FIRST_IN_IDE_AGENT.md` — read-only audit of the actual ORBIT app.
2. `AGENTS.md` and `CODING_AGENT_MASTER_PROMPT.md` — coding and team invariants.
3. `docs/02-research/REPOSITORY_OPERATIONS_ANALYSIS.md` — repository analysis.
4. `docs/02-research/V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md` — source paths to inspect and adapt.
5. `docs/13-guides/REPO_OPERATIONS_COMMAND_REFERENCE.md` — commands.
6. `docs/10-infrastructure/500GB_STORAGE_ARCHITECTURE.md` and `500GB_DRIVE_SETUP_WINDOWS.md` — storage.
7. `docs/08-development/V07_CTO_REPOSITORY_EXECUTION_BOARD.md` — roles, priorities and gates.
8. `docs/05-ai-system/V07_HUMAN_LIFE_AND_WORK_AUTOMATION.md` — product capabilities and safety boundaries.

## Windows first setup

```powershell
Get-Volume -DriveLetter E | Format-List DriveLetter,FileSystem,Size,SizeRemaining,HealthStatus
.\scripts\init_orbit_storage.ps1 -Path 'E:\ORBIT-Storage'
$env:ORBIT_HOME='E:\ORBIT-Storage'
py -3 scripts/orbit_repo_ops.py list
```

Change `E:` to the verified drive letter. The initializer creates folders and a JSON manifest only. It does not format or encrypt the volume.

## Acquire a minimal upstream set

Open Git Bash in the pack folder:

```bash
export ORBIT_HOME='/e/ORBIT-Storage'
bash scripts/clone_upstreams.sh --product-base --openhands-sdk
```

Then inspect:

```bash
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py audit "$ORBIT_HOME/01-upstream-checkouts/openmausbot"
python scripts/orbit_repo_ops.py verify
```

## Use an upstream module

1. Find the relevant path in the file-level adoption map.
2. Inspect license, NOTICE, nested licenses, code, imports, dependencies, security and adjacent tests.
3. Run upstream tests in a disposable sandbox after inspection.
4. Stage the exact path using `scripts/import_upstream_path.py` and the required human review acknowledgements.
5. Adapt into the actual ORBIT repository with an upstream source record, preserved notices and ORBIT conformance tests.
6. Submit a PR; independent QA/security and founder gate before merge/release.

## First engineering milestone

Audit the actual ORBIT app, preserve current code and uncommitted work, then ship one vertical slice: workspace → task → agent runtime → safe read-only tool → evidence/artifact → reconnect → cancel/resume. Do not start by cloning 35 huge projects or wiring every connector. No source merge is claimed by this blueprint.
