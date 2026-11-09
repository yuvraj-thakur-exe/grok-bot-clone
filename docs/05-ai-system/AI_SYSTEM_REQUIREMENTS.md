# AI system requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Core design

The model is a probabilistic planner and language interface, not the authority for permissions or truth. Deterministic services own identity, policy, task transitions, approvals, storage ACLs, quota enforcement, and audit records.

## Required capabilities

- Provider-neutral chat completion and streaming.
- Tool/function calling with schema validation.
- Capability discovery for text, vision, audio, structured outputs and context size.
- Context construction with explicit provenance and token budgets.
- Bounded agent loop with step/time/cost limits.
- Provider fallback only when task semantics and capability are preserved.
- Evidence-grounded research and file responses.
- Evaluation harness and prompt/model version tracking.

## Non-goals for MVP

Training a frontier foundation model, claiming AGI, unconstrained self-modification, or silently learning from private user data. ORBIT initially composes existing hosted/local models and builds differentiated execution infrastructure.

## Quality gates

Any change to prompts, tools, models, retrieval or routing runs a versioned evaluation suite. Report quality, latency, cost, safety and failure rates separately. A benchmark improvement cannot justify a security regression.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
