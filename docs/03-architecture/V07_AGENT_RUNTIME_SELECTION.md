# ORBIT agent runtime selection — v0.7

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Decision

ORBIT owns one durable control plane. Runtime libraries are workers behind typed adapters; they do not own tenant identity, global memory permissions, task event history, approval authority, usage budget or user account state.

## Current candidates

| Candidate | Intended role | Decision posture |
|---|---|---|
| OpenClaw | Personal gateway/channel runtime and extension ecosystem | External backend or selected SDK/extension; no second control plane |
| Hermes Agent | Optional personal/CLI agent runtime | External CLI/ACP adapter; compare tool and memory features |
| OpenMausBot | Desktop product shell and multi-agent UX | Preferred shell prototype candidate; only public OSS paths; exclude `enterprise/` |
| OpenHands Software Agent SDK | Coding worker | P1 disposable repo/task worker |
| Pydantic AI | Typed Python specialist worker | P1 worker candidate |
| OpenAI Agents Python | Handoff, guardrail, tracing and tool runtime | Benchmark against Pydantic AI; choose one primary Python worker framework |
| LangGraph | Durable/stateful agent graph framework | Compare for complex branching workflows; do not duplicate Temporal/task state |
| DSPy/GEPA | Offline prompt/skill optimization | Research pipeline only; holdout tests and human review |

## One selection per layer

- Global task orchestration: ORBIT task service, optionally Temporal as durable engine.
- Specialist agent worker framework: select one of Pydantic AI, OpenAI Agents SDK, Hermes, OpenHands depending task type.
- Coding worker: OpenHands SDK first POC; isolated workspace.
- Local inference server: Ollama for convenient local serving, llama.cpp as alternative low-level backend. Benchmark before choosing default.
- Tool transport: MCP SDK, with ORBIT policy on every call.
- Connected apps: Composio vs selected OpenClaw extensions vs direct connectors; one connection registry.
- Memory: one canonical ORBIT memory ACL/service; Mem0/Graphiti/Letta are optional storage/retrieval backends, not separate authorities.

## Selection score

Measure task quality, tool-call accuracy, cancellation, resume, latency, memory use, token/cost use, isolation, connector coverage, upgrade cadence, license compliance, local deployment and maintainability. Do not choose based on stars alone.
