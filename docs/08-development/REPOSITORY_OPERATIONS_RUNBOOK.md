# Repository operations runbook — v0.6

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Operation | Command / location | Expected evidence |
|---|---|---|
| Initialize drive | `py -3 scripts/orbit_storage.py init E:\ORBIT-Storage` | `.orbit-storage.json` and folder list |
| Check disk use | `py -3 scripts/orbit_storage.py status E:\ORBIT-Storage` | Per-directory byte totals and volume free space |
| Clone pinned sources | `bash scripts/clone_upstreams.sh --product-base --openclaw` | Git HEAD equals pinned SHA |
| Static repo inventory | `python scripts/repo_audit.py <checkout>` | Markdown and JSON audit report |
| Create isolated source task worktree | `python scripts/create_upstream_worktree.py --help` | New branch, workspace and metadata manifest |
| Stage selected code | `python scripts/import_upstream_path.py --help` | Source-intake copy and import manifest |
| Inspect branch changes | `git status --short`, `git diff --stat`, `git diff --check` | No accidental user/generated changes |
| Validate pack | `python scripts/validate_package.py` | JSON pass report |

## Incident handling

If an imported repository contains secrets, malicious scripts or restricted files, stop the task, preserve minimal evidence, move the checkout to quarantine, revoke any exposed tokens and notify Security. Do not run the suspicious content to test whether it is malicious.

## Cleanup

Delete only task worktrees or build/cache directories confirmed disposable and past retention. Never automatically delete user documents, memory stores or artifacts. Keep upstream pins and provenance manifests even when a local checkout is deleted.
