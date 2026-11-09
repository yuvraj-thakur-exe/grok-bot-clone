# ORBIT v1.0 repository operations and source-code reuse manual

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Purpose

This is the operator manual for turning open-source repositories into selected, tested ORBIT improvements. The desired workflow is **inspect → reuse → adapt → verify → maintain**, not wholesale rewrite. A repository being open source does not mean every file, model, sample, nested dependency, generated asset or subdirectory has the same license.

## 1. Define the ORBIT storage root

Choose the verified physical drive root. Windows example (replace `E:` only after checking the disk serial/model/size in Disk Management or `Get-Disk`):

```powershell
Get-Disk | Format-Table Number,FriendlyName,SerialNumber,OperationalStatus,PartitionStyle,Size
Get-Volume | Format-Table DriveLetter,FileSystemLabel,FileSystem,Size,SizeRemaining
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
py -3 scripts/orbit_storage.py init $env:ORBIT_HOME
py -3 scripts/orbit_storage.py status $env:ORBIT_HOME
```

PowerShell helper (Git for Windows Bash required for source cloning):

```powershell
./scripts/clone_upstreams.ps1 -Selectors @('--product-base','--openhands-sdk','--playwright','--opensandbox')
```

Linux/WSL:

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
export ORBIT_HOME=/mnt/orbit-storage
python3 scripts/orbit_storage.py init "$ORBIT_HOME"
python3 scripts/orbit_storage.py status "$ORBIT_HOME"
```

The initializer only creates directories and a manifest. It does not format, partition, encrypt, mount, or enforce quotas. Do not point it at an unverified drive. The 500 GB plan reserves 60 GB and uses soft target allocations.

## 2. Choose repositories by task, not by star count

```bash
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py list --recommended-only
python scripts/orbit_repo_ops.py show openmausbot
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify
```

To review the six v1.0 additions:

```bash
bash scripts/clone_upstreams.sh --all-v10-new
```

Do not clone all 50 repositories at once. Start with the smallest set for one user-visible feature. Do not install dependencies or execute upstream setup scripts during initial intake.

## 3. Inspect source before copying

```bash
python scripts/repo_audit.py "$ORBIT_UPSTREAM_DIR/openmausbot" --output-dir "$ORBIT_HOME/00-control/audits/openmausbot"
```

Read root and nested `LICENSE`, `NOTICE`, `COPYING`, package manifests, lockfiles, security docs, threat models, CODEOWNERS, build/test configuration and provenance. Locate the implementation and its nearest tests. Use GitHub search or ripgrep to find callers and imports. Record the dependency closure. The static audit is a heuristic triage tool, not malware scanning or license approval.

## 4. Choose the reuse method

| Method | When to use | Typical result |
|---|---|---|
| Dependency | Mature library with stable public API | Add pinned package and adapter |
| Separate service | Runtime is coupled or has its own lifecycle | Run behind a narrow authenticated API |
| SDK/interface | Protocol or client is useful without taking the server | Integrate SDK with ORBIT policy checks |
| Selective source copy | Small, self-contained module is needed | Stage exact path, preserve notices and adapt |
| Maintained fork | Large cohesive component needs long-term changes | Keep upstream remote, patch branch and sync plan |
| Rewrite | No viable safe/license-compatible reuse exists | ADR showing why reuse failed |

Do not merge OpenClaw, Hermes and another agent framework as competing global orchestrators. ORBIT owns canonical user, workspace, task, authorization, approval, memory-consent and audit state.

## 5. Create a clean application worktree

The actual ORBIT application Git URL/path is a required input. First clone it yourself and run `RUN_FIRST_IN_IDE_AGENT.md` in read-only mode. Preserve uncommitted changes. Then:

```bash
python scripts/create_orbit_app_worktree.py \
  --repo "$ORBIT_HOME/02-workspaces/orbit-app-source" \
  --task integrate-agent-approval \
  --created-by "Human maintainer"
```

The helper creates an isolated `orbit/app/<task>` branch and metadata. It does not modify the original checkout or run project commands.

## 6. Stage exact source with provenance

Example OpenMausBot file (verify the path at the locked commit):

```bash
python scripts/import_upstream_path.py \
  --repo-id openmausbot \
  --checkout "$ORBIT_UPSTREAM_DIR/openmausbot" \
  --path shared/live-approval.ts \
  --approved-by "Human maintainer" \
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \
  --license-reviewed --security-reviewed --tests-reviewed
```

Save the returned `manifest_sha256`. Then apply the exact staged path into your app worktree:

```bash
python scripts/apply_staged_source.py \
  --repo-id openmausbot \
  --source-path shared/live-approval.ts \
  --target-root "$ORBIT_HOME/02-workspaces/orbit-app-worktrees/integrate-agent-approval" \
  --target-path apps/orbit-server/src/adapters/upstream/openmausbot/live-approval.ts \
  --applied-by "Human maintainer" \
  --change-id approval-adapter-001 \
  --intake-root "$ORBIT_HOME/10-source-intake" \
  --expected-manifest-sha256 "PASTE_MANIFEST_SHA256" \
  --license-reviewed --security-reviewed --tests-reviewed
```

The helper verifies the package lock, origin, pinned commit, manifest digest, per-file hashes and clean feature worktree. It refuses symlinks and overwrites, writes a source-provenance JSON record, and never git-adds, commits, merges, pushes or deploys. Human review is still required.

## 7. Modify, do not blindly transplant

1. Compare the candidate code with existing ORBIT modules. Prefer changing an existing adapter or service contract over copying duplicate implementations.
2. Identify imports, package versions, environment variables, database tables, worker assumptions, telemetry, subprocesses, filesystem paths, network endpoints and generated files.
3. Port only required code and tests. Do not copy `.git`, `node_modules`, `.venv`, caches, build output, binaries or secret files.
4. Preserve upstream copyright and license notices. Add modification statements where required. Include nested dependency licenses and update SBOM/THIRD_PARTY_NOTICES.
5. Replace upstream-global identity/task/permission assumptions with ORBIT contracts.
6. Add ORBIT adapter tests: inputs/outputs, authorization, workspace isolation, tenant boundaries, event provenance, timeout, retry, cancellation, idempotency and failure recovery.
7. Run upstream tests in an isolated checkout where needed, then ORBIT lint/typecheck/unit/integration/e2e/security/benchmark suites.
8. Have QA and Security review independently. Human maintainer reviews the diff and commits a PR.

## 8. Keep local modifications maintainable

For small imported modules, record upstream commit and file hashes in `docs/source-provenance/`. For larger components, prefer a maintained fork or vendor patch series with:

- upstream remote and exact base commit;
- patch list and rationale;
- license/NOTICE delta;
- ORBIT adapter interface and ownership;
- test commands and last passing revision;
- sync cadence and responsible owner;
- deprecation/replacement strategy.

Never replace local patches with an upstream reset. Update in a disposable upstream worktree, reapply patches, run tests, and promote by normal PR.

## 9. 500 GB operational profile

The budget is 440 GB allocated targets plus 60 GB free reserve: 100 GB upstream sources, 100 GB workspaces, 90 GB models, 35 GB user data/memory, 25 GB artifacts, 20 GB evaluations, 25 GB backups, 20 GB source intake, 10 GB quarantine, 10 GB control and 5 GB logs/cache. These are planning targets, not hard quotas. Keep user data encrypted and separate critical backup on another physical/approved remote location.

## 10. Current state and acceptance

This pack is a repository operation and engineering blueprint. It does not contain full upstream checkouts or ORBIT's application runtime. The real ORBIT application URL/path must be supplied before the team can audit and integrate actual app source. Never describe a copied file as a shipped feature until it is integrated, built, tested and released.
