# ORBIT open-source expansion radar — v0.6

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Capability | Primary candidates | What to test | Main risk |
|---|---|---|---|
| Product shell / multi-agent UX | OpenMausBot OSS | Build, UX, chat/team model, approval, routines, connector lifecycle | Enterprise subtree/brand carve-out; large surface; inherited secrets patterns |
| Gateway/channels | OpenClaw | Gateway protocol, plugin SDK, channels, extensions | In-process plugins are trusted code; large dependency tree |
| Python agent backend | Hermes Agent, Pydantic AI, OpenAI Agents Python | Tool calls, handoffs, guardrails, resume/cancel, provider portability | Overlapping orchestration and state models |
| Coding | OpenHands Software Agent SDK | Disposable repo workspaces, patch quality, test execution | Host/sandbox privilege separation |
| Sandbox | OpenSandbox | API, network egress, credentials, lifecycle, performance | Container isolation limitations; infra complexity |
| Browser | Stagehand, Browser Use | Reliability, semantics, screenshot/DOM, cost and site compatibility | Prompt injection, auth/session leakage, unsafe forms |
| Connected apps | Composio, OpenClaw extensions | OAuth scope, toolkit quality, revoke, event/webhook correctness | Large tool surface, cloud boundary and nested licenses |
| Skill catalog | VoltAgent index, OpenClaw skills, Agent Skills format | Search quality, canonical origin and manifest | A catalogue license does not apply to linked skills |
| Memory | Mem0, Letta Code, Graphiti | Recall quality, correction, temporal conflict, deletion and ACL | Sensitive data leakage and stale memories |
| Document ingestion | Docling, LlamaIndex | PDF/DOCX/XLSX/HTML parsing, table accuracy, source citations | Parser attacks, model/download footprint |
| Vector retrieval | Qdrant | Recall@k, tenant filter, delete propagation, backup | Derived indexes must not become source of truth |
| Local LLM inference | Ollama, llama.cpp | Tokens/s, first-token latency, context window, RAM/CPU, quantization | Model quality, weight license, hardware limits |
| Speech | faster-whisper | Word error rate, latency, language and diarization options | Audio privacy and consent |
| Workflow durability | Temporal, LangGraph | Retries, timers, cancellation, human interrupt, recovery | Avoid duplicate workflow owners |
| Optimization | DSPy, Hermes self-evolution | Held-out success, cost, prompt/skill regressions | Overfitting and uncontrolled mutation |
| Observability | OpenTelemetry JS | Traces, metrics, redaction, genAI semantic conventions | Sensitive prompts and tool arguments in telemetry |

## Selection criteria

Score each candidate from 0–5 for (1) capability fit, (2) API stability, (3) license/attribution clarity, (4) security controls, (5) maintainer activity, (6) test quality, (7) dependency footprint, (8) hardware fit, (9) integration cost and (10) operational ownership. Security, license or data-sovereignty blockers override a high average score.

## Explicit non-goals

- Do not add all frameworks into one runtime.
- Do not download all model weights into the 500 GB model cache.
- Do not install all community skills.
- Do not use enterprise/source-available features without a separate license.
- Do not adopt a cloud connector just because its catalogue is large.
- Do not copy code without pin, provenance, license and tests.
