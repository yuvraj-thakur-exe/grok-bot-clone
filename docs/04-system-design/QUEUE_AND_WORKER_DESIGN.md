# Durable task and worker design

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Decision

Use a durable workflow engine (Temporal is the preferred candidate) for long-running tasks, waits, retries, approvals, and recovery. Do not use FastAPI in-process background tasks as the task system. A lightweight queue may still handle disposable low-value jobs, but task truth remains in durable workflow state and PostgreSQL records.

## Worker types

- `agent-worker`: orchestrates bounded model/tool loops.
- `browser-worker`: owns isolated Playwright contexts and browser sessions.
- `code-worker`: runs commands in disposable sandbox instances.
- `document-worker`: parses and indexes uploaded files.
- `scheduler-worker`: converts due routine triggers into idempotent tasks.
- `integration-worker`: calls third-party connectors with scoped credentials.

## Task lifecycle

`queued -> planning -> awaiting_approval -> running -> verifying -> succeeded`

Terminal/exceptional states: `failed`, `cancelled`, `expired`, `needs_human`, `blocked`. A state transition function validates allowed edges. A workflow may revisit `awaiting_approval` after a changed plan, but previous approval is invalidated.

## Reliability

- Persist checkpoints before and after external side effects.
- Use idempotency keys for external writes where supported.
- Use an outbox pattern for database-to-queue handoff.
- Exponential backoff with jitter for retryable failures; no blind retry for non-idempotent actions.
- Define retry budgets and wall-clock/resource budgets per task class.
- Cancellation is cooperative and propagated to child workflows and workers.
- Store event sequence IDs so clients can resume SSE without missing events.
- Poison jobs move to a dead-letter state with diagnostics and an operator action path.

## Concurrency

Bound model calls, per-user tasks, browser slots, file parsing, and tool execution separately. Apply tenant quotas and global backpressure. A queue backlog must not cause API process memory to grow without bound.

## Recovery drill

Kill a worker during a read-only browser step, during a file write, and immediately after an external side effect. Verify checkpoint recovery and duplicate suppression. Document the actual observed result in `docs/12-operations/RECOVERY_DRILL.md`.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
