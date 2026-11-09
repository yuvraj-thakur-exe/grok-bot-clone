---
description: Expand an epic task into 3–8 verifiable subtasks (GSD plan step)
agent: cto
---
Expand epic $ARGUMENTS from TASKS.md. Read only its Reqs and cited docs. Produce subtasks with ids `T-xxxa…`, deps, Reqs (existing ids only), and a verifiable "Done when" each. Insert them under the epic in TASKS.md, keep the epic row as `blocked` until subtasks are done, then run `node scripts/check-docs.mjs`. Show the diff summary only.
