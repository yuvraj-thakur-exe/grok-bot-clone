# Scalability and Failure Handling

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Scale web/API, workflow workers, browser/code workers and document workers independently. Keep per-workspace concurrency, token, cost, run-time, upload, search depth and delegation limits.

Invariants: accepted task has durable record; events have sequence; side effects have idempotency/reconciliation; retries bounded/jittered; approval waits survive restart; cancellation enforced at worker boundary; task replay disables external side effects.

| Failure | Behavior |
|---|---|
| Model timeout/429 | Bounded retry; compatible fallback only if policy permits; disclose switch |
| Worker crash | Workflow retries/reschedules from checkpoint |
| Browser crash | Reopen safe context or request user reauthentication |
| Redis outage | Cache degraded; durable tasks unaffected |
| PostgreSQL outage | Fail closed before writes/side effects |
| Object storage outage | Mark artifact pending; retry idempotently |
| Temporal outage | Do not start unsafe execution; preserve queued task state |
| OAuth revoked | Pause and request reconnection |
| Approval expires | Do not execute; request new approval |
| Ambiguous external side effect | Reconcile receipt/status before retry |

## Desktop node scaling and failures

A Local Desktop Node is a stateful endpoint with low concurrency, not a horizontally scalable stateless worker. Route leases to one device identity, apply a single mutation lock per physical session, heartbeat and expire lease state. Scale broker connections independently from task workers. On disconnect, mark in-flight action outcome unknown unless explicit driver evidence proves non-delivery. Do not resubmit the action. Node queues must be bounded; never queue stale ref mutations for later replay.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
