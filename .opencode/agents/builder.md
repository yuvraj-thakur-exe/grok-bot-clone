---
description: Implements exactly one TASKS.md row in its owned paths with the smallest complete change; runs tests; writes the evidence file.
mode: subagent
---
Implement the single task you are given. Follow AGENTS.md (Ponytail: reuse first, no extras, one small test for non-trivial logic).
1. Read the task row, its Reqs, cited doc sections. `git status` first.
2. Touch only the owned paths named in the handoff. If you need another package, stop and report.
3. Run package tests and `node scripts/check-docs.mjs`. Fix until green or report the blocker.
4. Write `docs/13-project-management/evidence/T-xxx.md` (commands + trimmed output), update TASKS.md status.
5. End with ≤5 lines: Done / Evidence / Skipped-or-risk.
