# Start here: using an IDE coding agent on ORBIT

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This pack is a design and execution specification, not a source-code implementation. Start by opening the actual ORBIT repository in your IDE and giving the agent the root `AGENTS.md` plus `CODING_AGENT_MASTER_PROMPT.md`.

## Exact first assignment

“Perform Phase 0 repository audit only. Do not modify or delete files. Inspect the repository, report the existing app/stack/tests/working features/risks, identify conflicts with the ORBIT docs, run existing safe checks, and create `docs/repository-audit/BASELINE.md` plus a list of proposed ADRs. Preserve all uncommitted work.”

Review that audit before letting the agent implement the vertical slice. Next, instruct it to implement one end-to-end flow: authenticated workspace -> create task -> model stream -> persist messages/task -> render progress -> cancel/reconnect. Do not ask it to build every feature in one enormous prompt.

## Tool permissions

Begin with read-only repository and browser research permissions. Allow file writes only inside the repo. Do not provide production secrets, personal browser profiles, unrestricted shell, or access to unrelated directories. Enable sandbox tests and require approval for destructive commands, dependency installation with scripts, outbound messaging, publishing, deployment, and credential changes.

## Required completion report

Agent reports changed files, architecture decisions, commands run, test results, untested areas, security implications, and next task. “Done” without evidence is not accepted.

## ORBIT v0.2 alignment

The v0.2 guide set adds a Local Desktop Node setup target. Treat it as planned until code, installers and OS tests exist; see `DESKTOP_NODE_QUICKSTART.md` and `FEATURE_STATUS.md`.
