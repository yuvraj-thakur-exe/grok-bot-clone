# Multi-agent coordination

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Build order

Do not start with a swarm. First prove a single agent can complete tasks with durable checkpoints, safe tools, clear evidence and measurable success. Then add a coordinator and a small set of specialist roles.

## Topology

A coordinator owns the parent task and delegates bounded child tasks to specialist agents. Child tasks have explicit objective, input artifacts, permitted tools, budget, deadline, and output schema. Shared context is passed by reference with ACL checks, not by giving every agent unrestricted workspace history.

## Collaboration rules

- Parallelize only independent work.
- Use dependency edges for tasks requiring prior outputs.
- Require evidence and structured output from research agents.
- Verification agent checks claims and artifacts, not just prose quality.
- Coordinator resolves conflicts and reports uncertainty.
- Child failure retries only within a bounded budget; escalate after retry budget.
- Cancellation and approvals propagate to children.

## Anti-patterns

Unbounded agent spawning, circular delegation, multiple agents modifying the same files without ownership, hidden inter-agent prompt injection, duplicated tool calls, and treating consensus as proof. Track cost and success at child and parent levels.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.


## v0.5 specialist team boundary

Each specialist has a role, model/runtime preference, memory namespace, skills, tools, budgets and parallelism limit. Delegation messages are typed, task-scoped and auditable. Agents cannot escalate their own tool grants, approve another agent's risky action, or silently share personal/work context. The coordinator verifies each subtask's evidence before synthesis.

