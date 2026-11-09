# ORBIT v0.8 — start here

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Deliverable scope

This package contains repository research, 41 pinned upstreams, copy/adapt workflows, a dedicated 500 GB storage plan, static repository audit/import/worktree utilities, team plans and IDE-agent rules. It does not bundle the 41 source repositories or modify the actual ORBIT application. No production feature integration is claimed.

## Read in this order

1. `RUN_FIRST_IN_IDE_AGENT.md` — read-only audit of the actual ORBIT repository.
2. `AGENTS.md` and `CODING_AGENT_MASTER_PROMPT.md` — mandatory development rules.
3. `docs/13-guides/V08_REPOSITORY_OPERATIONS_ANALYSIS_AND_SOURCE_MODIFICATION.md` — detailed repository operation and how-to guide.
4. `docs/02-research/REPOSITORY_OPERATIONS_ANALYSIS.md` and `docs/02-research/V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md` — original upstream source paths.
5. `docs/02-research/V08_OPEN_SOURCE_EXTENSION_REVIEW.md` — six additional repository analyses.
6. `docs/08-development/V08_CTO_AND_TEAM_EXECUTION_PLAN.md` — team execution and gates.
7. `docs/10-infrastructure/500GB_STORAGE_ARCHITECTURE.md` — drive layout and retention.
8. `docs/13-guides/REPO_OPERATIONS_COMMAND_REFERENCE.md` — utility commands.

## Initialize the 500 GB disk

Verify the physical disk and drive letter first. On Windows:

```powershell
Get-Disk | Format-Table Number,FriendlyName,Size,OperationalStatus
Get-Volume | Format-Table DriveLetter,FileSystem,Size,SizeRemaining,HealthStatus
.\scripts\init_orbit_storage.ps1 -Path 'E:\ORBIT-Storage'
$env:ORBIT_HOME='E:\ORBIT-Storage'
```

On Linux/WSL:

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,LABEL
python3 scripts/orbit_storage.py init /mnt/orbit-storage
export ORBIT_HOME=/mnt/orbit-storage
```

Never use the test-only skip-capacity flag on the real drive. These utilities do not format, partition or encrypt the volume.

## Minimal source acquisition

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify
```

## First real engineering task

1. Provide the actual ORBIT application repository URL to the IDE agent.
2. Run `RUN_FIRST_IN_IDE_AGENT.md` read-only.
3. Preserve the current branch, dirty files, user changes and working build.
4. Produce an existing-code module map and reuse decision.
5. Build one vertical slice before acquiring the full catalogue.

Do not clone all 41 repositories or download model weights before selecting a specific capability and checking space, hardware and licensing.
