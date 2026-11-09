# Founder / CEO (Human)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Role ID:** `executive.founder_ceo_human`  
**Type:** Human accountable owner  
**Status:** Role definition only; not proof of a hired person or active autonomous agent.

## Mission
company strategy, final accountability, budgets, hiring, external commitments, legal and release approvals

## Scope and responsibilities
Approve strategy, budget, staffing, public commitments, legal acceptance and production releases. Resolve risk acceptance.

## Prohibited actions and guardrails
No AI tool may sign, pay, hire, publish, contract or deploy in the founder’s name. All approvals are explicit and logged.

## Required outputs
Strategy memo, milestone priorities, signed human decisions, release approval or rejection.

## Review partners
CTO, Product, COO, Security, Finance, Legal advisor

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

Retain human authority for spend, legal acceptance, hiring, public claims, product licensing, trademark, production release and risk exceptions. Review evidence before accepting milestones.

Before accepting a task, inspect existing ORBIT code and exact pinned upstream source. Record source/commit/license/security impact; never claim work complete without an artifact or test receipt. Escalate irreversible, legal, financial, privacy or production decisions to the human founder.


## v0.7 repository reuse responsibility

Before proposing a new implementation, inspect the actual ORBIT repository and the relevant pinned upstream code. Prefer reuse through an adapter or a reviewed source import, keep exact commit/file provenance, preserve notices, and require tests and independent review. Do not make changes outside the assigned worktree or merge source-intake files automatically.
