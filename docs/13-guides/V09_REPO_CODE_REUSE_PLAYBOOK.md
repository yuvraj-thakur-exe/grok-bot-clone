# ORBIT v0.9 repository code reuse playbook

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

This runbook explains how to copy a small upstream source unit into an ORBIT feature worktree, adapt it and keep provenance. It is intentionally explicit: there is no “AI just copies the whole repo into the app” shortcut, because that is how duplicated runtimes, license problems and brittle dependency trees happen.

## A. Set the storage root

Windows example:

```powershell
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
$env:ORBIT_UPSTREAM_DIR = "$env:ORBIT_HOME\01-upstream-checkouts"
py -3 scripts/orbit_storage.py status $env:ORBIT_HOME
```

Linux/WSL example:

```bash
export ORBIT_HOME=/mnt/orbit-storage
export ORBIT_UPSTREAM_DIR="$ORBIT_HOME/01-upstream-checkouts"
python3 scripts/orbit_storage.py status "$ORBIT_HOME"
```

Check the actual drive's free capacity before downloading. Do not use `--skip-capacity-check` on a real drive. A marketed 500 GB disk commonly reports less usable binary capacity; the 60 GB reserve is intentional.

## B. Clone only the needed upstreams

```bash
python scripts/orbit_repo_ops.py list
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify
```

For the new v0.9 choices:

```bash
bash scripts/clone_upstreams.sh --graphrag --guardrails --milvus
```

Do not clone all 44 by default. Don't install dependencies while doing acquisition.

## C. Inspect exact source before selecting it

```bash
python scripts/orbit_repo_ops.py show openmausbot
python scripts/repo_audit.py "$ORBIT_UPSTREAM_DIR/openmausbot" --output-dir "$ORBIT_HOME/00-control/audits"
```

Read `LICENSE`, `NOTICE`, `LICENSING.md`, package manifests, lockfiles, security policy, threat model, credential paths, tests and nested licenses. Search for the target feature and read the adjacent unit/integration tests. The audit is static and heuristic; it is not malware scanning or legal approval.

## D. Create the ORBIT application feature worktree

First clone your actual ORBIT application repository to `$ORBIT_HOME/02-workspaces/orbit-app-source` and complete the read-only audit. Keep the original checkout clean. From the ORBIT repo:

```bash
git status --short
# must be empty before branching
python scripts/create_orbit_app_worktree.py \
  --repo "$ORBIT_HOME/02-workspaces/orbit-app-source" \
  --task integrate-approval-ui \
  --created-by "Human maintainer"
```

The worktree is created under `$ORBIT_HOME/02-workspaces/orbit-app-worktrees`. Work in that feature worktree only.

## E. Create an upstream analysis worktree (optional)

Use the upstream worktree only when you need to experiment with an upstream patch or reproduce its tests:

```bash
python scripts/create_upstream_worktree.py \
  --repo-id openmausbot \
  --task approval-contract-study \
  --created-by "Human maintainer"
```

Never edit the pinned immutable checkout.

## F. Stage one reviewed upstream path

Example: stage OpenMausBot's public OSS approval contract file. The specific file is illustrative; check it still exists at the locked commit first.

```bash
python scripts/import_upstream_path.py \
  --repo-id openmausbot \
  --checkout "$ORBIT_UPSTREAM_DIR/openmausbot" \
  --path shared/live-approval.ts \
  --approved-by "Human maintainer" \
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \
  --license-reviewed --security-reviewed --tests-reviewed
```

The tool verifies exact origin and commit, excludes `enterprise/`, rejects symlinks/path traversal/secrets/generated folders, and writes SHA-256 provenance to `10-source-intake`. Its JSON output prints `manifest_sha256`. Copy that digest; this is a staged copy only.

## G. Apply the staged code into the ORBIT feature worktree

```bash
python scripts/apply_staged_source.py \
  --repo-id openmausbot \
  --source-path shared/live-approval.ts \
  --target-root "$ORBIT_HOME/02-workspaces/orbit-app-worktrees/integrate-approval-ui" \
  --target-path apps/orbit-server/src/adapters/upstream/openmausbot/live-approval.ts \
  --applied-by "Human maintainer" \
  --change-id approval-adapter-001 \
  --intake-root "$ORBIT_HOME/10-source-intake" \
  --expected-manifest-sha256 "PASTE_MANIFEST_SHA256_FROM_STAGE_OUTPUT" \
  --license-reviewed --security-reviewed --tests-reviewed
```

The helper checks the caller-supplied staging-manifest SHA-256 (paste the value from the stage command), matches the manifest against the current pinned source lock, checks every copied-file SHA-256, validates the original origin/commit, requires a clean feature branch, refuses existing target files and symlinks, and writes `docs/source-provenance/<repo-id>-<change-id>.json`. It copies files into the feature worktree only; it does not run formatting, rewrite imports, `git add`, commit, merge or push.

For a directory import, keep the destination path dedicated to that imported directory. Inspect the manifest's listed file paths and hashes before applying.

## H. Adapt, test and submit

1. Read the copied source and replace upstream-global assumptions with ORBIT interfaces.
2. Resolve dependencies intentionally; don't copy an entire `node_modules`, virtualenv, `dist`, generated build output or vendor folder.
3. Preserve copyright/license/NOTICE files and add modification notices as required.
4. Add adapter tests for input/output contract, authorization, tenant boundary, cancellation, timeout, retries and audit evidence.
5. Add an end-to-end test proving the user task, approval and final artifact are correct.
6. Run project lint/typecheck/unit/integration/e2e and security scans.
7. Review `git diff`, source provenance, SBOM and license report.
8. QA and Security provide independent review. Human maintainer commits and opens a normal PR.

## I. Sync upstream changes

Keep local modifications as a patch series in a branch. To update, fetch the new upstream revision separately, compare old/new commit, review release notes and license/NOTICE changes, rebase patches in a disposable worktree, rerun tests and update the pin through PR. Never force-reset a working feature branch to the newest upstream.

## Important rules

- Do not copy the whole OpenClaw/Hermes/OpenMausBot repository into ORBIT.
- Never access or stage OpenMausBot `enterprise/`.
- The skill catalogue's MIT license does not cover linked skills. Each skill is reviewed at its canonical source.
- Model weights and datasets have separate license/usage terms from inference engines.
- Plugin metadata or MCP annotations do not grant authorization.
- A reviewer flag is an attestation, not legal advice or automated certification.
- No script in this pack merges or deploys code.
