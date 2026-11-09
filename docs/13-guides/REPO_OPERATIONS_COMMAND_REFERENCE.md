# ORBIT repository operations — command reference v0.9

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Prerequisites

Git, Python 3.11/3.12 and PyYAML are needed for the helper scripts. Install language toolchains only for the upstream currently being audited. A verified mounted dedicated storage drive is recommended; Windows example: `E:\ORBIT-Storage`, Linux/WSL: `/mnt/orbit-storage`.

## Initialize and inspect storage

```powershell
Get-Disk | Format-Table Number,FriendlyName,Size
Get-Volume | Format-Table DriveLetter,FileSystem,Size,SizeRemaining,HealthStatus
.\scripts\init_orbit_storage.ps1 -Path 'E:\ORBIT-Storage'
$env:ORBIT_HOME='E:\ORBIT-Storage'
```

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,LABEL
python3 scripts/orbit_storage.py init /mnt/orbit-storage
export ORBIT_HOME=/mnt/orbit-storage
python3 scripts/orbit_storage.py status "$ORBIT_HOME"
```

The initializer creates directories/manifests. It does not format, partition, mount, encrypt or impose hard quotas.

## Catalogue, clone and verify

```bash
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py list --recommended-only
python scripts/orbit_repo_ops.py show openmausbot
python scripts/orbit_repo_ops.py verify
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
```

50 repositories are pinned. Do not clone all repositories by default. Examples of focused additions:

```bash
bash scripts/clone_upstreams.sh --vllm --sglang       # GPU server comparison only
bash scripts/clone_upstreams.sh --promptfoo --garak   # authorized evaluation/red-team
bash scripts/clone_upstreams.sh --haystack --duckdb   # RAG alternative + offline analytics
bash scripts/clone_upstreams.sh --graphrag --guardrails --milvus # graph RAG, validation, vector DB
```

## Audit and worktree

```bash
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openmausbot"
python scripts/create_upstream_worktree.py --repo-id openmausbot --task approval-adapter --created-by "Human reviewer"
```

The worktree helper refuses unpinned, wrong-origin or dirty source checkouts and writes metadata under `00-control/worktrees`. It does not merge or push.

## Stage one source path for review

```bash
python scripts/import_upstream_path.py \\
  --repo-id openmausbot \\
  --checkout "$ORBIT_HOME/01-upstream-checkouts/openmausbot" \\
  --path shared/approval-mode.ts \\
  --approved-by "Human reviewer" \\
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \\
  --license-reviewed --security-reviewed --tests-reviewed
```

Only use this after reviewing source and adjacent tests. The command stages files and hashes them; it never merges.

## Create an ORBIT application feature worktree

```bash
python scripts/create_orbit_app_worktree.py \
  --repo "$ORBIT_HOME/02-workspaces/orbit-app-source" \
  --task reuse-browser-adapter \
  --created-by "Human maintainer"
```

## Apply reviewed staged source

`import_upstream_path.py` prints `manifest_sha256` in its JSON result. Copy that digest to the apply command; the helper refuses a changed staging manifest. See `V09_REPO_CODE_REUSE_PLAYBOOK.md` for the full sequence.

```bash
python scripts/apply_staged_source.py --help
```

## Modify and test

1. Work in a separate worktree/branch; leave the pinned checkout detached and clean.
2. Preserve upstream URL, commit, selected paths and hashes.
3. Adapt through ORBIT's interface; avoid patching upstream internals when an adapter is sufficient.
4. Carry applicable notices and modification headers; update SBOM/component register.
5. Run upstream tests in an isolated environment, then ORBIT unit/contract/security/e2e tests.
6. Obtain independent QA/security review and a human approval before a production merge/release.

## Regression checks

```bash
python -m unittest discover -s tests/operations -v
python scripts/validate_package.py
bash -n scripts/clone_upstreams.sh
```


> Current v1.0 manual: `V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`. The command reference in this file is retained for compatibility; the V10 guide is authoritative.
