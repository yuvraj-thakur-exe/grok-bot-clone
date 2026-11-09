# ORBIT 500 GB dedicated storage architecture — v0.9

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Objective

Use the dedicated 500 GB drive as ORBIT's source, workspace, model, memory, artifact and evaluation data root. Keep the OS, application runtime and temporary system files on their normal locations unless there is a measured reason to move them. Use a single configurable `ORBIT_HOME` path rather than hardcoding a drive letter throughout code.

## Proposed layout and budget

| Folder | Target | Contents | Rules |
|---|---:|---|---|
| `00-control/` | 10 GB | manifests, docs, operation scripts, runbooks | Version-controlled source remains in the actual Git repo too |
| `01-upstream-checkouts/` | 100 GB | pinned upstream repositories, mirrors, worktrees | Sparse/partial clone where supported; no bulk vendor copies |
| `02-workspaces/` | 100 GB | ORBIT source, per-task worktrees, build output, sandbox workspaces | Disposable workspace per task; cleanup with retention |
| `03-models/` | 90 GB | approved model weights, tokenizers, local inference cache | Verify checksums/license; use quantized models when appropriate |
| `04-data-memory/` | 35 GB | user-consented documents, memory records, indexes, metadata | Encrypt; isolate personal/workspaces; deletion must propagate |
| `05-artifacts/` | 25 GB | reports, docs, spreadsheets, images, audio and exports | User-visible export and retention policy |
| `06-evaluations/` | 20 GB | golden tasks, benchmark sets, traces, regression reports | Avoid private data unless consented and minimized |
| `07-logs-cache/` | 5 GB | redacted logs and rebuildable cache | Rotate; never store raw secrets |
| `08-backups/` | 25 GB | encrypted local snapshots and restore test material | A backup on the same physical disk is not disaster recovery |
| `09-quarantine/` | 10 GB | untrusted repo archives, skills and imported files | No execution; scan before promotion |
| `10-source-intake/` | 20 GB | explicit selected upstream imports pending review | Keep provenance manifest; no auto merge |
| **Unallocated reserve** | **60 GB** | filesystem growth and emergency working space | Keep free; do not fill the drive to 100% |
| **Total** | **500 GB** | | |

These are target budgets, not hard quotas. `scripts/orbit_storage.py` creates directories and a manifest but does not partition, format, encrypt or impose filesystem quotas.

## Example root paths

- Windows: `E:\ORBIT-Storage`
- Linux: `/mnt/orbit-storage`
- macOS: `/Volumes/ORBIT-Storage`

Set `ORBIT_HOME` once in the terminal/profile or ORBIT config. Avoid drive-letter literals in source code. If storage is removable, detect mount availability before starting tasks and fail closed rather than silently writing sensitive data to another disk.

## Storage lifecycle

1. Upstream mirror: immutable source commit, license, provenance and minimal checkout.
2. Worktree: disposable task-specific branch; no shared mutable source across agents.
3. Source intake: quarantined copy with source hashes and import-review record.
4. Application workspace: ORBIT-owned code with tests, change history and migration.
5. Model cache: immutable model artifact plus source/license/checksum manifest.
6. Memory: scoped records with owner, consent, source, created/expiry time, correction and delete state.
7. Artifact: task ID, input references, generation provenance and export/retention settings.
8. Backup: encrypted snapshot, separate restore key and restore test log.

## Model storage and laptop constraints

500 GB is disk space, not system RAM or GPU VRAM. A model can fit on disk but fail or run slowly in memory. On a 16 GB laptop, begin with small quantized models or remote inference, monitor RAM/CPU and avoid loading several models simultaneously. Use Ollama or llama.cpp only as candidate runtimes; benchmark a few specific model sizes on the real laptop before choosing a default. Every model's weight license, usage restrictions and provenance are reviewed independently from the inference engine's software license.

## User-data safety

- Encrypt sensitive data at rest using an OS-backed or well-reviewed encryption layer.
- Separate personal, work, project, family and shared-agent contexts with enforced ACLs.
- Do not store credentials in model context, plain Markdown memory files or task logs.
- Apply retention, user export and deletion. Remove derived embeddings/indexes when source data is deleted.
- Local-only mode must be distinguishable from remote model/tool use; show the egress boundary.
- A single disk is a storage convenience, not a backup strategy. Keep critical backups encrypted on a separate physical device or approved cloud target.

## Operations and monitoring

Track total free bytes, per-folder bytes, model cache age, upstream worktree count, temporary sandbox count, artifact retention, backup freshness and integrity. Alert at 80% used, 90% used and 95% used; block large model downloads or build jobs before disk exhaustion. Never automatically delete user documents to free space. Clean only explicitly disposable caches/workspaces after ownership and retention checks.

## Initialization

```powershell
py -3 scripts/orbit_storage.py init E:\ORBIT-Storage
py -3 scripts/orbit_storage.py status E:\ORBIT-Storage
```

```bash
python3 scripts/orbit_storage.py init /mnt/orbit-storage
python3 scripts/orbit_storage.py status /mnt/orbit-storage
```


## v0.8 repository operations

The dedicated drive now budgets 100 GB to upstream checkouts and 20 GB to reviewed source intake, while retaining 60 GB unallocated reserve. See `docs/13-guides/V08_REPOSITORY_OPERATIONS_ANALYSIS_AND_SOURCE_MODIFICATION.md` for exact clone, audit, worktree, source-import and upstream-sync steps. The 41-source catalogue is not a requirement to clone every repository.


## v0.9 storage operating controls

- Upstream repositories are partial/shallow pinned checkouts where supported. Keep only the sources required by an approved workstream; the 100 GB target is not a mandate to clone 44 full repositories.
- `10-source-intake/` holds copied source under a per-repository manifest. The application-copy helper verifies the reviewed manifest SHA-256 and per-file hashes before copying to a clean feature worktree.
- `02-workspaces/` separates the immutable ORBIT application source checkout, feature worktrees, upstream patch worktrees and disposable task workspaces.
- `00-control/` contains audit, provenance, storage, worktree and capacity manifests.
- Keep the 60 GB reserve and set a stop condition before large model downloads, container images or full builds.
- Test backups by restoring to a separate physical device; a same-drive backup does not protect against drive failure.
