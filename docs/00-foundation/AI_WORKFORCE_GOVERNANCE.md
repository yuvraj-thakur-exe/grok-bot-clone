# AI workforce governance

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This specification governs ORBIT's use of specialist AI roles internally and as a customer-facing multi-agent feature.

## Agent identity record

Every role agent has: immutable `agent_id`; role and version; owner; model/provider policy; allowed tools; workspace scope; budget; max parallel child tasks; data classification; memory policy; skill set; approval requirements; evaluation profile; status; audit trail.

## Delegation envelope

Every delegated task must include:
- `task_id`, parent task and workspace/tenant IDs;
- objective, expected output schema and acceptance criteria;
- permitted data sources, tools and domains;
- read/write scope and action risk class;
- time, token, cost and concurrency budgets;
- deadline, cancellation token and retry policy;
- trusted context and explicitly untrusted source references;
- reviewer role and escalation conditions.

Child agents receive the minimum context needed. They do not inherit all parent permissions automatically. A child cannot delegate beyond its own authority.

## Role boundaries

- Research agents collect evidence; they cannot approve source credibility alone for high-impact claims.
- Coding agents can propose code changes inside scoped worktrees; merge/deploy requires policy and human review.
- Security agents can flag/block through deterministic release gates; an LLM assessment is not a substitute for scanners or expert review.
- Finance agents can calculate and recommend; they cannot initiate payments, purchases or financial orders.
- Legal research agents can inventory licenses and prepare questions; they cannot provide final legal clearance.
- Product agents can recommend priorities; the founder/product owner approves scope changes.

## Multi-agent orchestration policy

Use a coordinator + specialist DAG only when subtasks are separable and outputs can be independently validated. Prefer a single agent for small tasks. Avoid committee chatter and duplicate model calls.

Required controls: acyclic task graph; bounded fan-out; maximum depth; shared budget; deadline propagation; cancellation propagation; per-child context isolation; conflict resolution; provenance-preserving aggregation; reviewer independence; no self-approval; deduplication; durable event log.

## Evaluation

Track task success, evidence precision, acceptance criteria completion, rework rate, tool error rate, unsafe-action attempts, cost per successful task, time to verified completion, cancellation compliance and privacy incidents. Track results by role, model, skill version and runtime profile.
