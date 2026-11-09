# ORBIT v1.0 start here

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Current release

This pack contains the coordinated reuse-first architecture, 50 pinned upstream repositories, source-file adoption maps, copy/modify operations, 500 GB storage plan, CTO workstreams, 30 virtual role charters, tests and IDE-agent instructions. It does not contain full upstream checkouts or the ORBIT runtime.

## First 60 minutes on the actual machine

1. Extract this pack into a control repository separate from the actual ORBIT app.
2. Verify the 500 GB physical drive with `Get-Disk`/`Get-Volume` or `lsblk`.
3. Set `ORBIT_HOME` to the verified volume and run the storage init/status commands. No formatting or encryption is performed by the helper.
4. Clone the real ORBIT app repository into `02-workspaces/orbit-app-source` and preserve its existing branch/history.
5. Run `RUN_FIRST_IN_IDE_AGENT.md` in read-only mode. Collect architecture map, existing features, build/tests, dependency graph, data-flow and security/license review.
6. Create one clean feature worktree and select a single vertical feature.
7. Clone only the required upstreams, inspect source/tests/licenses and stage the smallest source paths.

## Best first integration slice

Recommended proof of concept: product-shell decision + one approval flow + one specialist coding/browser worker. Keep the original ORBIT app functioning. Do not integrate four runtime frameworks simultaneously.

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify
```

If the product-shell decision is already made, select OpenClaw or Hermes as a separate gateway/runtime only after the control-plane boundary is documented. The `--all-v10-new` selector exists for research collection, not initial setup.

## Where to continue

- Repository usage/copy/adapt: `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`
- Source analysis: `docs/02-research/V10_OPEN_SOURCE_FILE_LEVEL_ADOPTION_MAP.md`
- Operations review: `docs/02-research/ORBIT_REPOSITORY_OPERATIONS_ANALYSIS_V10.md`
- Storage: `docs/10-infrastructure/V10_500GB_STORAGE_OPERATIONS.md`
- CTO team: `docs/08-development/V10_CTO_IMPLEMENTATION_WARROOM.md`
- Personal/work architecture: `docs/03-architecture/V10_INTEGRATED_PERSONAL_WORK_OPERATING_SYSTEM.md`
- Competitor evaluations: `docs/09-quality/V10_COMPETITIVE_PARITY_BENCHMARKS.md`
- New OSS choices/exclusions: `docs/02-research/V10_OPEN_SOURCE_DECISIONS_AND_EXCLUSIONS.md`
- Master handoff: `CODING_AGENT_MASTER_PROMPT.md`

## Completion truth

The next release can only claim application integration after the real app repository is audited, code is adapted, builds/tests pass and a human approves the PR. This pack provides the operation; it is not that integration itself.
