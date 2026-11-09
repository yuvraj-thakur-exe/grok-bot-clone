# ORBIT v0.9 — start here

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## What changed

- 44 exact upstream source pins with a per-capability reuse map.
- Three additional projects: Microsoft GraphRAG, Guardrails AI and Milvus.
- A staged-source-to-application helper that verifies manifest hashes before copying into a clean feature worktree.
- A dedicated ORBIT application worktree helper.
- A 500 GB drive layout with 60 GB reserve and explicit storage lifecycle controls.
- 30 virtual team role charters and an updated CTO workstream.

## First actions

1. Extract the pack into the actual ORBIT application repository or a separate operations directory.
2. Provide the real ORBIT GitHub repository URL to your IDE agent.
3. Run `RUN_FIRST_IN_IDE_AGENT.md` in read-only mode before changes.
4. Verify your physical 500 GB drive using Windows `Get-Disk` / `Get-Volume` or Linux `lsblk`.
5. Set `ORBIT_HOME` only after verifying the correct volume.
6. Initialize storage using the instructions in `docs/10-infrastructure/500GB_STORAGE_ARCHITECTURE.md`.
7. Use `docs/13-guides/V09_REPO_CODE_REUSE_PLAYBOOK.md` for clone → inspect → worktree → stage → apply → adapt → test.

## The 500 GB rule

The storage script creates directories and a manifest only. It does not format, partition, encrypt, mount, or enforce quotas. The drive's space is not additional RAM or VRAM. Do not download all model weights just because they fit on disk.

## Recommended first source selection

Start with a single product shell and one worker path. Suggested initial inspection set:

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox --playwright
```

Do not clone all 44 upstreams before checking drive capacity and deciding which modules are required.

## Required deliverable from the first IDE audit

The IDE agent must return: current architecture map, build/test commands, all existing features worth preserving, exact modules that can be reused, conflicts/duplicates, dependency graph, security issues, license status, data flows, MVP integration sequence, and a list of source files it proposes to adapt. It must not rewrite the application before that audit is reviewed.
