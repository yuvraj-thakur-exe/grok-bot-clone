---
description: Take the next ready task from TASKS.md and run the work loop
agent: cto
---
Run the AGENTS.md work loop for the first `todo` row in TASKS.md whose Deps are all `done` (or the task id given: $ARGUMENTS).
Delegate implementation to `builder` (one package at a time), verification to `qa` for P0, review to `security` when SEC-xxx is in Reqs. Do not start a task from a later phase than ROADMAP.md allows. Finish with ≤5 lines: Done / Evidence path / Risk / Next task id.
