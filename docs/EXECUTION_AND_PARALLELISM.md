# ORBIT local execution and parallelism

## Task model

A task is a small, typed process request with:

- immutable task ID;
- executable plus argument array (`argv`), never one concatenated shell string;
- workspace-relative working directory;
- explicit dependency IDs;
- maximum runtime;
- allowed operating systems;
- risk mode (`inspect`, `workspace-write`, or `external`);
- explicit environment-variable passthrough allowlist.

The scheduler validates the entire DAG and rejects cycles before starting any process. Tasks with satisfied dependencies can run concurrently under a global semaphore, capped at eight workers. Default parallelism is three to avoid saturating a typical developer laptop. The example manifest runs host inspection, config parsing and tests independently, then runs a follow-up only after its two prerequisites pass. The user can set a lower or higher limit after measuring CPU/RAM impact.

## Failure and recovery behavior

- A failed or skipped dependency blocks its dependants.
- Every task has a timeout and bounded output capture.
- The runner attempts process-tree termination after timeout/output overflow.
- Results and redacted output are stored under `.orbit/runs/<run-id>/`.
- No external side-effect task is supported by this local toolkit.
- Workspace-write tasks require an explicit CLI switch.
- Idempotency, durable checkpoints, remote workers and cross-machine leases belong in the ORBIT control-plane workflow engine, not this local helper.

## Parallelism policy

Parallelize independent, bounded work only. Examples: separate static-analysis commands, independent documentation lint, independent test partitions, isolated repo metadata checks. Do not concurrently mutate the same Git worktree, shared database, browser profile, desktop session or deployment target.

Use one writer per mutable resource. All other workers receive read-only snapshots or independent worktrees. Merge only after tests and diff review.

## Production evolution

The production workflow interface must later add:

- durable task/event state in the authoritative database;
- lease ownership and heartbeat;
- idempotency keys and explicit delivery disposition;
- cancellation and restart recovery;
- worker heartbeats and capability reports;
- workspace/user policy checks;
- approval checkpoints and audit records;
- per-task CPU, memory, disk, network and cost budgets.

Redis may coordinate ephemeral work but is not the source of truth for durable tasks.
