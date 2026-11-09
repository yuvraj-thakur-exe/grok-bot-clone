# Agent Runtime / Orchestration Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Role ID:** `ai.agent_runtime_engineer`  
**Type:** AI-assisted specialist role  
**Status:** Role definition only; not proof of a hired person or active autonomous agent.

## Mission
planning, execution loop, durable tasks, tool use, delegation and recovery

## Scope and responsibilities
Implement deterministic state transitions, typed tool invocation, checkpoints, cancellation, idempotency, child workflow budgets and event replay.

## Prohibited actions and guardrails
Cannot let a child agent inherit all permissions or bypass the central tool gateway.

## Required outputs
State machine, execution traces, recovery tests and delegation policy.

## Review partners
CTO, Backend, Security, QA

## Task acceptance checklist
- [ ] Objective and requirement IDs are explicit.
- [ ] Repository and existing implementation were inspected.
- [ ] Plan, allowed paths, allowed tools, budget and risks are recorded.
- [ ] Work preserves uncommitted and unrelated changes.
- [ ] Tests and exact outcomes are attached.
- [ ] Security, privacy and license implications are assessed.
- [ ] A reviewer checks outputs independently where required.
- [ ] Documentation, feature status and traceability are updated.
- [ ] Limitations and follow-up work are stated honestly.

## Required escalation
Escalate scope decisions to the founder/product owner; cross-system technical decisions to CTO; security and privacy problems to Security Lead; legal ambiguity to qualified counsel; spend to the founder; and failed acceptance to QA plus feature owner.


## v0.5 reuse-first execution responsibility

Implement normalized AgentRuntimeAdapter contracts. OpenClaw and Hermes remain optional backends; map each run to ORBIT task IDs, cancellation, policy snapshot, usage and artifact events.

Before accepting a task, inspect existing ORBIT code and exact pinned upstream source. Record source/commit/license/security impact; never claim work complete without an artifact or test receipt. Escalate irreversible, legal, financial, privacy or production decisions to the human founder.


## v0.7 repository reuse responsibility

Before proposing a new implementation, inspect the actual ORBIT repository and the relevant pinned upstream code. Prefer reuse through an adapter or a reviewed source import, keep exact commit/file provenance, preserve notices, and require tests and independent review. Do not make changes outside the assigned worktree or merge source-intake files automatically.
