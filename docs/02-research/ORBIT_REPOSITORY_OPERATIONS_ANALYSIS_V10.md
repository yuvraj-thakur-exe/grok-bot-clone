# ORBIT v1.0 repository operations analysis

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## System overview

There are three repositories in the workflow: (1) this blueprint/operations pack, (2) immutable upstream checkouts under `01-upstream-checkouts`, and (3) the actual ORBIT application checkout supplied by the founder. Their roles must not be mixed. The pack's scripts create source checkouts, worktrees, file-intake manifests, provenance and validation; they do not constitute the ORBIT product runtime.

## Repository state model

`catalogued → pinned → cloned → audited → selected → staged → reviewed → copied-to-feature-worktree → adapted → tested → PR-reviewed → merged → released`.

Each stage has a separate status. Cloned is not audited; staged is not integrated; copied is not built; tested locally is not release-approved.

## Operational commands

```bash
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py show openmausbot
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify
python scripts/repo_audit.py "$ORBIT_UPSTREAM_DIR/openmausbot" --output-dir "$ORBIT_HOME/00-control/audits/openmausbot"
python scripts/create_orbit_app_worktree.py --repo "$ORBIT_HOME/02-workspaces/orbit-app-source" --task approval-ui --created-by "Human maintainer"
```

The exact staging and application steps are in `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`.

## Storage allocation and policy

The dedicated disk is configured for 440 GB of folder targets and 60 GB of free reserve. The 50 repositories are not meant to be cloned in full simultaneously. Start with a product-shell candidate and one or two workers. Keep archives and unknown code in quarantine. Keep personal memory encrypted and ACL-scoped. Keep critical backups on another physical or approved remote target.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Rewriting mature code instead of adapting | Require source-map and ADR before new implementation |
| Duplicate global gateways/orchestrators | One canonical ORBIT task/policy control plane; backend adapter contract |
| Supply-chain or malicious skill | Quarantine, pin, inspect, isolate, SBOM and independent review |
| License/NOTICE loss | File-level provenance, root/nested license review and release gate |
| Importing whole monorepo | Copy minimal path + tests; use service/dependency for larger systems |
| Disk exhaustion | 60 GB reserve, status reporting and download/build stop thresholds |
| Lost changes during upstream update | Immutable pin plus patch/worktree and sync PR; never force reset |
| False product parity claim | Reproducible held-out end-to-end benchmark suite |

## What is not done

No actual ORBIT application repository was attached or identified in this task. This pack cannot determine which existing application files should be modified, and no ORBIT runtime changes are claimed. The next mandatory input is the real application repository URL or an archive containing its Git source and build instructions.
