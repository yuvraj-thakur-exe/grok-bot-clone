# CTO repository execution board — ORBIT v0.7

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Current priority order

| Priority | Workstream | Responsible virtual role | Output | Blocker / acceptance |
|---|---|---|---|---|
| P0 | Audit actual ORBIT source repository | CTO + Repository Operations | Build baseline, stack map, dirty-file report, module map | Actual repository required; no overwrite |
| P0 | Initialize 500 GB target drive | Founder + SRE | Verified mount, storage manifest, free-space report | Human verifies correct physical drive |
| P0 | Product shell decision | CTO + Product + Frontend | Existing ORBIT vs OpenMausBot prototype comparison | One shell selected; enterprise excluded |
| P0 | Upstream clone and audit | Repository Operations | 35 pin inventory and reports for selected repos | Never clone all by default |
| P1 | Coding worker | Agent Runtime + Sandbox | OpenHands worker in disposable workspace | egress denied by default, cancel/resume test |
| P1 | Tool and app integration | Integration Engineer + Security | MCP adapter + one OAuth integration | read-only first, exact scopes |
| P1 | Browser worker | Browser Engineer | BrowserDriver conformance | browser session isolation and approvals |
| P1 | Local model adapter | Model Runtime | Ollama vs llama.cpp benchmark | hardware and model license evidence |
| P1 | Memory/document pipeline | Data/RAG + Product | scoped memory + Docling ingest | ACL, source citations and deletion propagate |
| P2 | Voice and personal workflows | Voice + Product | whisper worker, reminders and routines | explicit consent and retention settings |
| P2 | Skill evolution | AI Research + QA | offline GEPA evaluation and PR proposal | held-out tests, no autonomous production self-edit |

## Delegation format

Every task card has: workstream ID, objective, base repo/commit, allowed paths, disallowed paths, tool/capability grant, network policy, data sensitivity, budget, expected artifacts, tests, rollback, reviewer and acceptance evidence.

## Stop conditions

Stop on unknown license, missing NOTICE, unexpected enterprise path, secrets in imported files, unreviewed install hooks, no test baseline, unexplained source drift, unsafe network egress, failed ACL test, model download without consent, or inability to rollback.

## Human gates

The human founder approves drive initialization, spending, external account authorization, legal uncertainty, production rollout, external communications and releases. Security and QA may block acceptance. Virtual agents cannot self-approve exceptions.


## v0.8 repository operation handoff

The v0.8 current work is assigned in `V08_CTO_AND_TEAM_EXECUTION_PLAN.md`. The repository catalogue now contains 41 pinned sources and uses `create_upstream_worktree.py` for isolated changes. This v0.7 board remains a historical workstream record.
