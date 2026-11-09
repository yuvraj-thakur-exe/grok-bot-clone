# Open-source component radar — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Snapshot date:** 08 November 2026. Licenses below are repository metadata observed during research, not a legal approval for every transitive dependency or asset.

## Recommended candidates

| Component | License observed | Best ORBIT use | Adoption posture | Do not do |
|---|---|---|---|---|
| [OpenHands Software Agent SDK](https://github.com/OpenHands/software-agent-sdk) | MIT | Coding/repository worker, ephemeral workspace execution, agent event API | P1 proof of concept | Do not let coding workers inherit broad personal account credentials |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Apache-2.0 | Container/microVM sandbox lifecycle and egress controls | P1 after Docker baseline | Do not expose the sandbox control plane to models |
| [Stagehand](https://github.com/browserbase/stagehand) | MIT | TypeScript browser `observe/act/extract` adapter | P1 browser benchmark | Do not enable simultaneous uncontrolled browser engines |
| [Browser Use](https://github.com/browser-use/browser-use) | MIT | Alternative autonomous browser driver in Python | P2 comparison | Do not use hosted cloud features without cost/data review |
| [Mem0](https://github.com/mem0ai/mem0) | Apache-2.0 | Long-term memory extraction and retrieval backend | P1 memory proof of concept | Do not treat extracted memories as verified truth or share memory across agents by default |
| [Letta](https://github.com/letta-ai/letta-code) | Apache-2.0 | Stateful-agent identity and continual-memory patterns | P2 alternative to Mem0, not an extra memory layer | Do not deploy both Mem0 and Letta as competing sources of truth |
| [LangGraph](https://github.com/langchain-ai/langgraph) | MIT | Explicit stateful workflow graphs, checkpoints and human-in-loop interrupts | P2 workflow PoC | Do not add a second orchestrator unless benchmarks justify it |
| [DSPy](https://github.com/stanfordnlp/dspy) | MIT | Offline prompt/skill/tool-description optimization and evaluation | P2 self-improvement PoC | Do not confuse prompt optimization with model-weight training |
| [Temporal](https://github.com/temporalio/temporal) | MIT | Durable long-running tasks, retries, timers and recovery | P1 workflow comparison | Do not stack Temporal and LangGraph as competing owners of retries/state |
| [OpenTelemetry JS](https://github.com/open-telemetry/opentelemetry-js) | Apache-2.0 | Traces, metrics and logs across task/model/tool/worker steps | P1 baseline | Do not export raw prompts, secrets or private browser/desktop content |
| [LlamaIndex](https://github.com/run-llama/llama_index) | MIT | Document ingestion, connectors, indexing and RAG pipelines | P2 knowledge-ingestion adapter | Do not lose document ACLs, provenance or citation links |
| [Qdrant](https://github.com/qdrant/qdrant) | Apache-2.0 | Vector index for semantic retrieval | P2 optional store after baseline | Do not treat vector index as the source-of-truth database |
| [OpenClaw](https://github.com/openclaw/openclaw) | MIT | Gateway, channels, model adapters and extension ecosystem | P1 optional runtime | Do not treat in-process plugins as sandboxed |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | MIT | Optional agent runtime and persistent-memory/skills comparison | P2 backend | Do not make it a second ORBIT control plane |

## Browser decision

Keep the ORBIT `BrowserDriver` contract and current Playwright baseline. Benchmark one additional TypeScript-native candidate first: Stagehand. Compare Browser Use only where Python-specific capabilities or task benchmarks justify another runtime. Keep existing `agent-browser` as a reference candidate. Use one selected browser engine per deployment profile, not all browser projects simultaneously.

Measure: task success, DOM/accessibility robustness, screenshot/vision use, file downloads, uploads, authentication state, CAPTCHA/MFA boundaries, egress control, latency, memory, cancellation and recovery. Human approval stays outside the browser runtime.

## Memory decision

ORBIT owns the authoritative memory record, consent, source provenance, confidence, scope, expiry and user correction/deletion. Benchmark Mem0 as an extraction/retrieval adapter. Compare Letta as a stateful-agent backend only if agent identity and continuity are a major requirement. Do not let a third-party memory layer silently become the user profile database.

Memory classes:

1. User-authorized profile facts and preferences.
2. Project/workspace facts with source links and last-verified time.
3. Episodic task summaries with retention policy.
4. Semantic knowledge chunks that retain source citations.
5. Sensitive or high-impact data, which is excluded by default unless a deliberate feature, consent and privacy review exist.

## Workflow decision

Temporal is the durable execution candidate for long-lived schedules, retries and recoverable task workflows. LangGraph is a graph/agent-control candidate for explicit stateful agent decisions. They solve overlapping but not identical problems. A workflow ADR must define exactly one owner for durable business state, one retry owner per side effect, and the checkpoint/replay semantics before adopting either.

## Additional implementation references

- OpenHands Software Agent SDK: https://github.com/OpenHands/software-agent-sdk
- Browser Use: https://github.com/browser-use/browser-use
- Stagehand: https://github.com/browserbase/stagehand
- Mem0: https://github.com/mem0ai/mem0
- Letta current code: https://github.com/letta-ai/letta-code
- LangGraph: https://github.com/langchain-ai/langgraph
- DSPy: https://github.com/stanfordnlp/dspy
- Temporal: https://github.com/temporalio/temporal
- OpenTelemetry JS: https://github.com/open-telemetry/opentelemetry-js
- LlamaIndex: https://github.com/run-llama/llama_index
- Qdrant: https://github.com/qdrant/qdrant
- Agent Skills specification: https://agentskills.io/specification
- Model Context Protocol: https://modelcontextprotocol.io/

MCP is a protocol integration target. Do not import an MCP SDK whose exact license metadata is `NOASSERTION` until the actual package license is confirmed.


## v0.5 source selection authority

This radar is discovery, not approval. The decision status, capability owner and integration choice are centralized in `docs/02-research/V05_SOURCE_DECISION_MATRIX.md` and the pinned `config/upstreams/upstream-lock.yaml`. Do not add every candidate as a runtime dependency.

