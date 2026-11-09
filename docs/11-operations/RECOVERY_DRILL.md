# Recovery drill record

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Not yet executed. This is a required operational exercise, not a claimed test result.

## Scenarios

1. Terminate an agent worker after checkpoint persistence.
2. Terminate browser worker while a page is loading.
3. Terminate immediately after a mock external side effect but before response is recorded.
4. Make PostgreSQL unavailable and restore from backup.
5. Make object storage unavailable during artifact write.

## Evidence to record

Date, environment, release SHA, scenario, injected failure, task IDs, expected outcome, actual outcome, duplicate side effects, measured recovery time, data loss window, owner and follow-up issues. Mark a scenario passed only with recorded evidence.

## ORBIT v0.2 alignment

The v0.2 operations plan adds node offline, permission, driver version, unknown delivery and desktop data exposure runbooks. Never replay an uncertain mutation; see `DESKTOP_NODE_RUNBOOK.md`.
