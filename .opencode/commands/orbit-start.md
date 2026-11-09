---
description: Phase 0 bootstrap check — repo state, doc integrity, research clone, next tasks
agent: cto
---
Bootstrap ORBIT. Output ≤10 lines.
1. `git status --short`. If this is not a git repo, tell the human to run `git init` (do not run it).
2. If `apps/` or `packages/` contain anything not described in docs/03-architecture/MODULE_STRUCTURE.md, run task T-006 (audit) before anything else; never delete.
3. Run `node scripts/check-docs.mjs` and report the result.
4. Run `bash scripts/bootstrap-research.sh opencode`.
5. Print the next 3 `todo` tasks from TASKS.md whose deps are done.
6. Ask at most one question, only if blocked.
