# ORBIT v1.0 open-source source map and adoption decisions

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Selection policy

The 50-repository lock is a research and source-intake catalogue, not an installation list. Exact commits are pinned. Prefer one primary implementation per concern. Compare alternatives with ORBIT's real workloads before adopting them. All paths below are source areas to inspect at the pinned revision; inspect their package READMEs, build manifests, nearest tests and dependency closure before copying.

## Newly added v1.0 repositories

| Repository | Pin | License metadata | Source paths to inspect | Intended use | Caution |
|---|---|---|---|---|---|
| [Google ADK Python](https://github.com/google/adk-python) | `dd7161f7a2b88cd7ae482cc2acd8423675ac027c` | Apache-2.0 | `src/google/adk/`, `examples/`, `tests/`, `pyproject.toml` | Compare typed agent, tool, evaluation and deployment patterns | Candidate specialist-worker framework only; ORBIT stays task/policy authority |
| [OpenAI Codex](https://github.com/openai/codex) | `c9b4267c370a755da12ec1c8648c2451163212b7` | Apache-2.0 | `codex-rs/`, `codex-cli/`, `sdk/`, `third_party/`, `NOTICE` | Coding-agent worker, patch and worktree patterns | Review `NOTICE` and nested third-party components; run only in disposable workspace |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `62bab5b232c15b925d31e655ce844ab939c882b7` | Apache-2.0 | `packages/`, `evals/`, `integration-tests/`, `schemas/` | Optional coding/research CLI backend and extension patterns | Backend adapter only; do not duplicate ORBIT identity or permissions |
| [OpenSearch](https://github.com/opensearch-project/OpenSearch) | `0b131ddecfe5be4cef617acda803e8c824c8c875` | Apache-2.0 | `server/`, `plugins/`, `modules/`, `client/`, `qa/` | Hybrid lexical/vector search when simpler search is inadequate | Heavy service; no default deployment without relevance/load benchmark |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | `3ea751c087f32b16e039a2233dd6eefecef325d5` | MIT | inspect `sweagent/`, `config/`, `tests/`, `trajectories/` if present | Issue-to-patch coding worker and repair benchmark | The pinned snapshot is older than v1.0 additions; recheck maintenance and advisories before use |
| [FAISS](https://github.com/facebookresearch/faiss) | `29782a03747addd1122bf040b6c3488c8d669fe9` | MIT | `faiss/`, `faiss/python/`, `faiss/benches/`, `tests/` | Local ANN index library comparison | Compare with Qdrant/Chroma/Milvus; do not run four vector stores by default |

Repository-level license metadata is not file-level clearance. Review root/nested licenses, notices, dependencies, assets and model/data terms.

## Existing primary source maps

### Product, gateway and agent runtime

- **OpenMausBot**: `server/agent-tool-policy.ts`, `server/agents-turn.ts`, `server/app-events.ts`; `shared/approval-mode.ts`, `shared/live-approval.ts`, `shared/outside-write.ts`, `shared/routines.ts`, `shared/skill-import.ts`, `shared/connector-scopes.ts`, `shared/team-setup.ts`. Product-shell candidate; exclude `enterprise/` completely and preserve all Apache/NOTICE obligations. Do not reuse product name, mascot, logo or trade dress.
- **OpenClaw**: `packages/plugin-sdk/`, `packages/gateway-protocol/`, `packages/agent-core/`, `packages/net-policy/`; inspect `extensions/browser/`, `extensions/deep-research/`, `extensions/document-extract/`, `extensions/github/`. In-process native plugins are trusted code, not isolated plugins.
- **Hermes Agent**: `agent/`, `gateway/`, `cron/`, `evals/`, `acp_adapter/`, `hermes_state*`. Optional separate runtime; avoid a second ORBIT-wide scheduler/gateway.
- **Hermes Self-Evolution**: `evolution/skills/`, `evolution/core/`, `datasets/`, `tests/`. Offline skill/prompt optimization only; human review before promotion.
- **OpenHands SDK**: inspect `openhands/` SDK modules, examples and tests for coding worker contracts.
- **Microsoft Agent Framework / Pydantic AI / Google ADK / OpenAI Agents SDK**: compare typed tools, handoffs, evaluation and cancellation. Select one Python specialist worker framework if needed, not multiple global agents.

### Coding and local inference

- **OpenAI Codex**: inspect `codex-rs/`, `codex-cli/`, `sdk/` for CLI execution and patch/worktree lifecycle.
- **Gemini CLI**: inspect `packages/`, `evals/`, integration tests for command/tool extension patterns.
- **SWE-agent**: inspect agent action loop and task repair evals; run in a disposable sandbox.
- **Ollama / llama.cpp / vLLM / SGLang**: select an inference server by target hardware and concurrency. Models and quantizations have separate licenses and checksums.
- **Transformers / Text Embeddings Inference**: model/tokenizer and embedding-serving components; review each model's license separately.

### Browser, desktop, sandbox and integrations

- **Playwright** is the baseline browser engine. **Stagehand** and **Browser Use** are alternatives behind one `BrowserDriver` interface. Avoid simultaneous uncontrolled engines.
- **OpenSandbox** is a sandbox provider candidate after Docker isolation/egress baseline. **OpenHands SDK** runs only in disposable workspaces. Native desktop is a different trust boundary and needs a local paired node.
- **Composio** and MCP SDKs supply connector/protocol plumbing. ORBIT authorizes every tool invocation and uses least-privilege OAuth scopes.
- **OpenClaw extensions** can be useful feature references, but treat in-process extensions as trusted code; place untrusted code in a separate process/container.

### Memory, search, retrieval and documents

- **Mem0 / Letta Code / Graphiti**: compare memory extraction, user-editable memory, temporal facts and scopes. ORBIT owns consent, ACL, correction, retention and deletion.
- **LlamaIndex / Haystack / GraphRAG**: choose the ingestion/RAG pipeline by evaluation. GraphRAG is enrichment, not universal default.
- **Qdrant / Chroma / Milvus / FAISS**: select one backend for the deployment profile. FAISS is an index library; Qdrant/Chroma/Milvus are databases/services. Do not treat them as identical.
- **OpenSearch**: lexical and hybrid retrieval where Postgres full-text + chosen vector backend are not sufficient. Measure RAM/disk/ops before adding it.
- **Docling / MarkItDown**: ingest documents; outputs remain untrusted and source-labelled.
- **DuckDB**: local analytical files and evaluation queries, not primary transactional user state.

### Voice, safety and evaluation

- **faster-whisper / sherpa-onnx**: choose local/offline speech stack by device, model terms and latency.
- **Guardrails AI**: structured output validation; not a substitute for authorization.
- **Promptfoo / DSPy / garak**: evaluation, offline prompt/skill optimization and authorized security probes. Never run probes against systems without permission.
- **Temporal / LangGraph**: Temporal for durable long-running workflows; LangGraph for bounded agent graphs. Only one canonical business-task state machine.
- **OpenTelemetry**: common traces/metrics. Redact secrets and sensitive payloads before export.

## Adoption gate

Every imported feature must have an ADR, source pin, license evidence, file hashes, test evidence, dependency/license closure, threat review, rollback plan, owner and upstream sync plan. Use `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md` for the exact copy/modify sequence.
