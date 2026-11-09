# Prompt architecture and versioning

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Composition order

1. Immutable platform policy and safety constraints.
2. Workspace policy and permissions summary.
3. Agent role and versioned instructions.
4. Task objective and structured plan state.
5. Authorized memory and evidence with provenance labels.
6. Tool schemas and currently granted capabilities.
7. User request and relevant conversation context.

Tool permission enforcement is implemented in code, not prompt text. Prompts can explain policy but cannot grant permissions.

## Versioning

Prompts are named, versioned, reviewed and tested. Record prompt version with every task run. Store templates as source files; avoid editing production prompts through an untracked database field. Red-team prompt changes for injection, secret exfiltration and refusal behavior.

## Reasoning privacy

Persist concise plans, decisions, validation results and citations. Do not expose or require raw hidden chain-of-thought. Provide user-useful explanations and execution evidence instead.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
