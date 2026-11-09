# Model routing and provider adapters

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Adapter contract

Each adapter exposes: `list_models`, `get_capabilities`, `complete`, `stream`, `count_tokens` (or estimate), `health`, and normalized errors. Capability metadata includes modality, tool calling, JSON/structured output, context limit, streaming, and known constraints. Never claim a capability solely because a model name looks capable; validate configuration and run smoke tests.

## Routing inputs

Task category, required modalities, tool-call needs, latency budget, quality tier, privacy policy, provider health, context size, user preference, and workspace budget. The router returns chosen provider/model plus a reason code and fallback plan. User-visible task details show which model was selected where relevant.

## Modes

- Fast: low-latency model for simple Q&A and classification.
- Balanced: default quality/cost balance.
- Deep: stronger reasoning/research/coding model, subject to spend cap.
- Local/private: models executing within the configured private environment.

## Fallback

Fallback is allowed only if required capabilities remain supported and the user’s privacy constraints are preserved. Never send private/local-only content to a hosted provider as a fallback. Do not switch from tool-capable model to a text-only model and pretend the task continued. Record fallback and degraded capability.

## Cost governance

Estimate before execution, cap per task/workspace, enforce maximum output, stop runaway loops, and meter actual token usage. Provider pricing is external and changes: keep rates in configurable metadata with an `effective_at` date, not hardcoded in application logic.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
