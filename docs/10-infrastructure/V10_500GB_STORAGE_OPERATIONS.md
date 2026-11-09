# ORBIT v1.0 dedicated 500 GB drive operations

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Storage budget

| Folder | Target GB | Why |
|---|---:|---|
| `00-control` | 10 | repository index, audit reports, manifests, runbooks and hashes |
| `01-upstream-checkouts` | 100 | selective shallow/pinned clones and disposable upstream worktrees |
| `02-workspaces` | 100 | actual ORBIT source clone, feature worktrees, coding jobs and builds |
| `03-models` | 90 | selected model weights, quantizations and inference cache |
| `04-data-memory` | 35 | user-approved files, memory records and indexes |
| `05-artifacts` | 25 | user-facing docs, exports, code and media |
| `06-evaluations` | 20 | golden tasks, traces and benchmark sets |
| `07-logs-cache` | 5 | redacted rotating logs and rebuildable cache |
| `08-backups` | 25 | encrypted local snapshots and restore test material |
| `09-quarantine` | 10 | untrusted archives/skills, never execute here |
| `10-source-intake` | 20 | explicitly staged files awaiting review |
| Free reserve | 60 | filesystem growth, temporary builds and emergency operations |
| **Total** | **500** | **440 GB soft targets + 60 GB reserve** |

## Physical disk safety

Windows first inspect:

```powershell
Get-Disk | Format-Table Number,FriendlyName,SerialNumber,OperationalStatus,PartitionStyle,Size
Get-Volume | Format-Table DriveLetter,FileSystemLabel,FileSystem,Size,SizeRemaining
```

Only after verifying the correct 500 GB disk and its drive letter:

```powershell
$env:ORBIT_HOME = 'E:\ORBIT-Storage' # replace E: only after verification
py -3 scripts/orbit_storage.py init $env:ORBIT_HOME
py -3 scripts/orbit_storage.py status $env:ORBIT_HOME
```

Use `scripts/init_orbit_storage.ps1` if you want the PowerShell-specific size check. These operations create folders and a manifest only. They do **not** format, partition, mount, encrypt or impose hard quotas. The physical disk is not mounted or initialized by this documentation pack.

Linux/WSL:

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
export ORBIT_HOME=/mnt/orbit-storage
python3 scripts/orbit_storage.py init "$ORBIT_HOME"
python3 scripts/orbit_storage.py status "$ORBIT_HOME"
```

## Efficient use of 500 GB

- Do not clone all 50 repos. Keep a pinned bare mirror only when repeated fetching is needed; use shallow/partial clones for feature work.
- Start with OpenMausBot product-shell, OpenClaw gateway, OpenHands coding worker, Playwright browser and OpenSandbox runtime only after the audit.
- Never put source-intake directly on an executable path. Promote only selected files to a feature worktree.
- Set a 60 GB free-space stop condition. At 80% disk use alert, at 90% block model downloads/builds, and at 95% stop nonessential writes.
- Model weights, quantization, tokenizer, model cards, checksum and license are tracked individually. Do not bulk download models.
- 500 GB storage does not add RAM or VRAM. Run only models fitting the actual RAM/VRAM/CPU and benchmark first.
- Same-disk backup does not protect from physical disk failure. Keep critical backups elsewhere.

## Storage status and maintenance

```bash
python scripts/orbit_storage.py status "$ORBIT_HOME"
python scripts/orbit_repo_ops.py list --recommended-only
python scripts/orbit_repo_ops.py verify
```

Schedule a weekly report for folder usage, stale worktrees, model cache, source-intake, artifacts, quarantine and backup freshness. Never auto-delete user documents or memories to free space. Worktree cleanup must verify owner/task status and obtain approval.
