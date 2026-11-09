# Repository code reuse and import specification — v0.7

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Purpose

This document makes the desired workflow explicit: clone upstream code, reuse the existing implementation, make focused changes, test it, and maintain provenance rather than regenerate an equivalent implementation from scratch.

## Reuse decision ladder

1. Configure/use upstream as an external service or process.
2. Integrate its official SDK or public protocol.
3. Wrap its package behind an ORBIT adapter.
4. Import a small cohesive module with its tests and dependency closure.
5. Maintain a fork/worktree when strategic modifications are required.
6. Rewrite only with a documented technical, licensing, security or compatibility reason.

The default is not rewrite. The default is not wholesale fork either. Select the smallest reuse surface that solves the requirement.

## Standard repository lifecycle

### A. Acquire a pinned source

Use `config/upstreams/upstream-lock.yaml`. Clone with `scripts/clone_upstreams.sh` or the documented PowerShell command. Verify `git rev-parse HEAD` equals the recorded commit. Do not track an unreviewed floating branch in the application build.

### B. Inspect before installing

Read root and nested `LICENSE`, `NOTICE`, `LICENSING.md`, `SECURITY.md`, contribution guidelines, code owners, package manifests, lockfiles, install scripts, telemetry and build scripts. Enumerate root folders and source/test relationships. Check repository status. Do not run lifecycle scripts, postinstall hooks or unknown binaries during static inspection.

### C. Establish a disposable worktree

Create one worktree per task/agent, based on the exact pin. One developer/agent must not share a mutable working directory with another. Record the upstream base SHA in the task.

### D. Map the candidate module

Record the files imported by the candidate, public APIs, transitive dependencies, config/env needs, network domains, credential flow, filesystem writes, process execution, plugin loading and runtime lifecycle. If module boundaries are unclear, use package-level integration instead of copying private internals.

### E. Run upstream tests

Run the upstream maintainer-recommended focused test(s) first and record exact command/output. Then run lint, typecheck and broader tests as appropriate. Preserve relevant upstream tests with copied code. Do not claim tests passed if dependencies were not installed or the command was not run.

### F. Stage imports outside the application

Use `scripts/import_upstream_path.py` to copy an explicitly selected file/directory to the 10-source-intake staging folder after marking license, security and test review. The script refuses `.git`, common build/dependency directories, secret files and `enterprise/`. It records source URL, commit, source path, destination and SHA-256. Staging is not permission to merge into the application.

### G. Adapt in ORBIT

Prefer an adapter with narrow interfaces. Add ORBIT-specific policy, workspace scope, observability, timeout, cancellation, budget, retry and error mapping. Keep original filenames and notices where practical. Imported upstream files must carry modification notices where the upstream license requires them.

### H. Verify and promote

Run upstream tests, ORBIT unit/integration/conformance tests, security scans, license checks and a rollback test. Review code diff and provenance manifest. Require human approval before application merge or release.

## Source import record fields

- upstream ID, canonical URL, owner and project
- immutable commit SHA and tag/release (if any)
- root and nested license expression and evidence URL
- selected source paths and SHA-256 before import
- imported paths and SHA-256 after import
- changes made and rationale
- transitive dependencies and their licenses
- test commands/results and security findings
- reviewer names/roles and approval date
- upstream sync strategy and next review date

## Copy-and-modify example

```bash
# 1. Set the dedicated disk location.
export ORBIT_HOME="/mnt/e/ORBIT-Storage"  # adapt to your machine

# 2. Acquire exact source pins. This performs clone/fetch only.
bash scripts/clone_upstreams.sh --product-base --openclaw --hermes --skills-index

# 3. Inspect a pinned checkout and produce an audit report.
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openmausbot"

# 4. Stage one reviewed source path (example only; first inspect all imports/tests).
python scripts/import_upstream_path.py \
  --repo-id openmausbot \
  --checkout "$ORBIT_HOME/01-upstream-checkouts/openmausbot" \
  --path shared/approval-mode.ts \
  --approved-by "human-founder" \
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \
  --license-reviewed --security-reviewed --tests-reviewed

# 5. Review the staged copy and manifest before moving anything into the real ORBIT repo.
```

PowerShell equivalent for disk setup and audit:

```powershell
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
py -3 scripts/orbit_storage.py init $env:ORBIT_HOME
py -3 scripts/repo_audit.py "$env:ORBIT_HOME\01-upstream-checkouts\openmausbot"
```

The import script's CLI and allowed options are discoverable with `--help`.

## What agents must never do

- replace an existing ORBIT implementation before comparison
- copy a directory without its dependency closure and applicable tests
- import OpenMausBot `enterprise/` or bypass its entitlement boundary
- delete upstream LICENSE/NOTICE/copyright/attribution/modification notices
- copy third-party logos, mascot, screenshots, brand or trade dress into ORBIT branding
- assume a catalogue repository licenses the external skills it links to
- run unknown postinstall/install scripts on the developer host
- put API keys, cookies or private user data into prompts, logs, git history or test fixtures
- merge source-intake files automatically after copying
- claim source integration from a clone, a diagram or a generated plan

## Upstream sync strategy

For a selective import, store the original base commit and local patch series. For a maintained fork, keep the upstream remote and ORBIT remote. Sync monthly or on security advisories, whichever occurs first. Review diffs, license changes, SBOM delta, deprecations and tests. Do not update every upstream at once; use risk-based batches.
