# Windows setup — dedicated 500 GB ORBIT drive

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Before starting

1. Connect/mount the dedicated drive.
2. Open PowerShell and inspect `Get-Disk`, `Get-Partition`, and `Get-Volume`.
3. Confirm the correct drive letter by its label, filesystem and size. Do not rely only on `E:`.
4. Back up anything important already on that drive.
5. Keep BitLocker or another approved full-disk encryption method enabled where available; the ORBIT storage helper itself does not encrypt.

## Initialize

```powershell
Get-Volume -DriveLetter E | Format-List DriveLetter,FileSystem,Size,SizeRemaining,HealthStatus
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\init_orbit_storage.ps1 -Path 'E:\ORBIT-Storage'
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
```

Set the environment variable persistently only after checking the location:

```powershell
[Environment]::SetEnvironmentVariable('ORBIT_HOME','E:\ORBIT-Storage','User')
```

Restart terminals/IDE after changing the persistent value.

## Clone repositories selectively

Use Git Bash or WSL for the Bash acquisition helper:

```bash
export ORBIT_HOME='/mnt/e/ORBIT-Storage'  # WSL mapping; verify with findmnt first
bash scripts/clone_upstreams.sh --product-base --openhands-sdk
```

Or set the actual Windows path as `ORBIT_HOME` in Git Bash's path format. Do not run clones to an unverified default directory.

## Inspect and report

```powershell
py -3 scripts/orbit_repo_ops.py list
py -3 scripts/orbit_repo_ops.py verify
py -3 scripts/repo_audit.py 'E:\ORBIT-Storage\01-upstream-checkouts\openmausbot'
```

## Windows operational limits

- Python script `chmod` bits are not a substitute for Windows ACLs.
- Symlink handling, case sensitivity and long paths can vary by filesystem and Git config.
- Do not store user credentials in repo checkouts, `.env` files in source intake or model prompts.
- Cloud sync should not be enabled for raw private memory, auth state, browser profiles, or credentials without an explicit data-processing review.


## v0.9 application source and feature worktrees

Keep your actual ORBIT application source checkout under `02-workspaces/orbit-app-source` and keep the source checkout clean. Use `scripts/create_orbit_app_worktree.py` to create a feature branch under `02-workspaces/orbit-app-worktrees`. Only copy reviewed source into a feature worktree using `scripts/apply_staged_source.py`; do not write imported source into the pinned upstream checkout or the app's primary checkout.
