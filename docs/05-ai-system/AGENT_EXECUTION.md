# Agent execution engine

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Bounded execution loop

1. Receive task plus immutable policy snapshot.
2. Resolve workspace/agent configuration and authorized context.
3. Build a plan with steps and required tools.
4. Validate plan against policy and resource budgets.
5. Request approval for consequential actions.
6. Execute one bounded model/tool step at a time through Tool Gateway.
7. Persist step input/output metadata and checkpoint.
8. Verify tool result and task objective.
9. Continue, ask user, or complete with evidence and artifacts.

## Hard limits

Every run has maximum steps, wall-clock time, model calls, token budget, tool concurrency, file size and browser navigation budget. Defaults are configurable and conservative. A model cannot raise its own budget or grant itself tools.

## Stop conditions

Stop on success, user cancellation, policy denial, expired approval, repeated identical failure, exhausted budget, unresolved ambiguity, human verification, or unsafe/untrusted instruction conflict. `needs_human` is a valid outcome, not a failure to hide.

## State and replay

Persist task ID, run attempt, agent/model/prompt versions, tool arguments hash, policy decision, step sequence, checkpoint, and artifact refs. Replay must not repeat external side effects without idempotency protection. Never store hidden model reasoning traces; store concise plans, decisions, citations, and operational evidence.

## Desktop observe-act-verify loop

Native desktop task handling must use fresh accessibility observation, completeness assessment, semantic unambiguous target selection, authorization/approval, one action, fresh observation and explicit verification. If snapshot is partial, ref stale/ambiguous, session changed or delivery unknown, stop/reobserve or hand off. Do not replay mutations because a network timeout occurred. Browser and native desktop loops are different worker adapters but share a durable task/event contract.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.


## v0.5 adapter and reuse requirements

Agent execution is an ORBIT task, even when a separate runtime executes it. Every runtime receives a task-scoped capability envelope and returns normalized progress, tool, usage, error and artifact events. Cancellation and deadlines must be propagated. A runtime cannot change ORBIT workspace permissions, task completion state, memory consent or external-action approval.

