# Fallback, budgets and cost controls

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Define task budgets before launch: provider spend, token estimate, tool calls, browser time, code CPU/RAM, network transfer and wall-clock duration. Enforce budgets in deterministic services. The model cannot override them.

Fallback decision order: check provider health -> check capability equivalence -> check privacy and region constraints -> check budget -> retry transient failure with bounded policy -> select compatible alternative or pause. Never downgrade silently for research quality, code execution, vision or tool calling.

Track estimated and actual cost. Provider pricing is versioned configuration with effective dates. Alert at workspace thresholds and block new expensive work when hard budget is reached. Local inference may have zero API invoice but still consumes compute and power; report it separately.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
