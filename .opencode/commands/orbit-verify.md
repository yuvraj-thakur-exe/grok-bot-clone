---
description: Independently verify a task against its Done-when
agent: qa
subtask: true
---
Verify task $ARGUMENTS: read its row in TASKS.md, re-run every "Done when" command, test at least one failure path, then run `node scripts/check-docs.mjs`. Report PASS/FAIL per criterion with command + output. Do not fix.
