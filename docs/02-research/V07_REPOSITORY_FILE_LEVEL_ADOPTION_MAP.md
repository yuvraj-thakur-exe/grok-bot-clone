# ORBIT v0.7 — repository file-level adoption map

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## How to read this map

- **Copy/adapt candidate:** source code may be staged after per-file license/notice/security review.
- **SDK/dependency candidate:** prefer the supported package boundary; avoid copying internal files.
- **External runtime:** run behind an ORBIT adapter and sandbox; do not merge another control plane.
- **Research only:** examine the approach, write an ADR and build a small evaluation, not production adoption.

## User-selected upstreams

### OpenMausBot — `milind-soni/OpenMausBot`

Pinned at `3f81576655ca45af91bfaaa63dc37251222828eb`; public OSS core Apache-2.0. `enterprise/` is excluded and separately licensed. Keep LICENSE, NOTICE, LICENSING.md and third-party attributions. Do not reuse name, mascot, logos or screenshots as ORBIT assets.

Review these narrow modules first:

| Path | What it contains / why useful | ORBIT treatment |
|---|---|---|
| `server/agent-tool-policy.ts` | Read-only tool-name allowlist and read-only annotations | Copy only if full module/test provenance is preserved; reimplement ORBIT's server-side authorization adapter around it |
| `server/agents-turn.ts` | Per-turn capability flags, handoff tokens, turn-kind classification | Adapt contract to ORBIT task IDs, turn leases, task origin and approval state |
| `server/app-events.ts` | Source filters, event previews, bounded batches, untrusted event block and provenance | Strong source-adaptation candidate; preserve bounds, idempotency and trust labels |
| `shared/approval-mode.ts`, `shared/live-approval.ts` | Approval-mode and live approval domain contracts | Adapt after review; approval must bind exact action/resource/account/data/expiry |
| `shared/routine-schedule.ts`, `shared/routine-run.ts` | Routine schedule and run-state contracts | Adapt with timezone/DST, deduplication, cancellation and retry-budget tests |
| `shared/skill-import.ts`, `shared/skill-md.ts`, `shared/written-skill.ts` | Skill parsing and import rules | Adapt to immutable ORBIT skill versions, provenance and capability grants |
| `shared/connector-scopes.ts`, `shared/connector-account-link.ts` | Connector scopes/account-link records | Adapt to minimum OAuth scopes, account/workspace isolation and revocation |
| `shared/team-setup.ts`, `shared/bot-profile.ts`, `shared/thread-model.ts` | Agent roster, profile and thread contracts | Map into canonical ORBIT tenant/workspace/project/agent/thread IDs |
| `server/` adjacent tests | Unit/integration regression protection | Carry tests where feasible and add ORBIT contract tests |

**Do not copy the whole application blindly.** The repo is a full product. Audit package scripts, third_party/, nested licenses, local credential flow, cloud/enterprise feature boundaries and build graph. The CLI onboarding path documents plaintext config credentials with restricted file permissions, while packaged desktop docs describe OS-backed encryption where supported. ORBIT must use its own approved secret vault, not inherit either path without review.

### OpenClaw — `openclaw/openclaw`

Pinned at `7283c5182497e1ac5f95668de9f39ad3a9df3b11`; MIT. The repo is a large TypeScript monorepo.

| Path | Why inspect | Reuse mode |
|---|---|---|
| `packages/agent-core/` | Agent primitives | Package/adapter comparison, not wholesale fork |
| `packages/gateway-protocol/`, `packages/gateway-client/` | Gateway wire contracts and clients | Prefer protocol/client reuse where compatible |
| `packages/plugin-sdk/` | Extension contracts | Integrate only behind ORBIT's trust boundary |
| `packages/acp-core/` | Agent Client Protocol support | Compare as adapter boundary |
| `packages/net-policy/` | Network policy helpers | Review and test; ORBIT still owns final egress policy |
| `extensions/browser/`, `extensions/duckduckgo/` | Browser and search providers | Optional adapters; separate domain allowlist and secret isolation |
| `extensions/deep-research/`, `extensions/document-extract/` | Research/document tooling | Compare to internal research pipeline |
| `extensions/github/`, `extensions/slack/`, `extensions/telegram/`, `extensions/whatsapp/` | Channel and app connectivity | Select individual connectors; don't enable all by default |
| `extensions/ollama/`, `extensions/llama-cpp/` | Local model providers | Compare with direct provider adapters |
| `extensions/diagnostics-otel/` | Telemetry integration | Reuse only with sensitive payload redaction |

In-process plugins are trusted code in the gateway process. Untrusted plugins must execute out-of-process with restricted RPC, filesystem and egress. Preserve `THIRD_PARTY_NOTICES.md` and nested license evidence.

### Hermes Agent — `NousResearch/hermes-agent`

Pinned at `27afd192c2215d1e7363c38a2db77d0ab3f9db49`; MIT. Python CLI/runtime, gateway, cron, eval and ACP adapter are separate areas.

Review `agent/`, `gateway/`, `cron/`, `evals/`, `acp_adapter/`, `hermes_cli/` and `hermes_platform/` as separate modules. Prefer external process/ACP/CLI integration. Do not couple ORBIT to unversioned private functions or duplicate global orchestration, memory authority, user identity or approvals.

### Hermes Agent Self-Evolution — `NousResearch/hermes-agent-self-evolution`

Pinned at `0a929e3aa20e15cf04dc7c28492a7d41a5139125`; MIT indicated in README and `pyproject.toml`, but root LICENSE was not present in the inspected snapshot. Get rights-holder/license confirmation before copying or redistributing code.

Review `evolution/skills/`, `evolution/core/`, `datasets/`, `reports/` and `tests/`. Use only in offline experiment mode: candidate skills/prompts/tool descriptions → synthetic/golden dataset → train/validation/holdout → GEPA/MIPRO candidate → regression/security/cost checks → human-approved PR. No production self-edit.

### VoltAgent Awesome OpenClaw Skills — `VoltAgent/awesome-openclaw-skills`

Pinned at `5492fcd98f7c52c69e1b2fa58790faf4fc90ce13`; MIT for catalogue repository. It is an index of community skill links, not a license grant or safety guarantee for the linked repositories. Import listing metadata only at first. Resolve canonical source, exact commit, per-file license, dependencies, install scripts, network permissions and prompt-injection behavior per skill.

## Additional OSS candidates added in v0.7

| Project / pinned source | Candidate paths / components | ORBIT use |
|---|---|---|
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | `pydantic_ai_slim/`, `pydantic_graph/`, `pydantic_evals/` | Typed Python worker tools/evals; MIT |
| [Ollama](https://github.com/ollama/ollama) | `api/`, `server/`, `llm/`, `model/` | Local model-serving adapter; MIT; weights have separate terms |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | `include/`, `src/`, `ggml/`, `common/`, `examples/` | GGUF inference backend; MIT; hardware/model terms separate |
| [Docling](https://github.com/docling-project/docling) | `docling/`, `packages/`, `tests/` | PDF/Office/document parsing worker; MIT |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | `faster_whisper/`, `tests/` | Local speech transcription worker; MIT; models separately reviewed |
| [Graphiti](https://github.com/getzep/graphiti) | `graphiti_core/`, `mcp_server/`, `server/` | Temporal knowledge graph adapter; Apache-2.0 |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | `src/`, `examples/`, `tests/` | Python MCP interoperability; MIT; protocol metadata is not authorization |
| [OpenAI Agents Python](https://github.com/openai/openai-agents-python) | `src/`, `examples/`, `tests/` | Specialist worker/handoff/guardrail comparison; MIT |
| [Composio](https://github.com/ComposioHQ/composio) | `python/`, `ts/`, `harness/`, `skills/` | Connected app toolkit/auth adapter; MIT repo metadata, inspect each toolkit and hosted service terms |

## Non-duplication rule

Choose one canonical implementation per responsibility:

- One ORBIT control plane and task store.
- One product shell.
- One memory authority and ACL system, with optional retrieval/graph backends.
- One browser baseline plus experimental alternatives behind one `BrowserDriver` interface.
- One primary workflow engine; candidate SDKs are not multiple global orchestration engines.
- One model catalog/provider registry; Ollama and llama.cpp are providers, not agent brains.
- One integration registry; OpenClaw extensions and Composio are alternative connector sources.

## File-level import procedure

See [REPOSITORY_CODE_REUSE_AND_IMPORT_SPEC](../04-system-design/REPOSITORY_CODE_REUSE_AND_IMPORT_SPEC.md) and [REPO_OPERATIONS_COMMAND_REFERENCE](../13-guides/REPO_OPERATIONS_COMMAND_REFERENCE.md). The importer copies a reviewed path into source intake, hashes each file and writes `IMPORT_MANIFEST.json`. It does not resolve dependencies, install packages, merge changes or imply license clearance.


## Additional v0.7 repositories — file-level inspection hints

| Project | Paths to inspect first | Use and boundaries |
|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | `packages/playwright-core/`, `packages/playwright/`, `tests/`, root `LICENSE` and `NOTICE` | Cross-browser automation baseline (Apache-2.0). Use supported APIs, keep ORBIT's browser policy/approvals authoritative. |
| [MarkItDown](https://github.com/microsoft/markitdown) | `packages/markitdown/` and its package tests | Lightweight document/Office conversion (MIT); compare fidelity to Docling on layout, tables and scans. |
| [Chroma](https://github.com/chroma-core/chroma) | `chromadb/`, `clients/`, `rust/`, `schemas/` | Alternative vector store (Apache-2.0); compare with Qdrant and choose one baseline. |
| [Text Embeddings Inference](https://github.com/huggingface/text-embeddings-inference) | `router/`, `core/`, `backends/`, `integration_tests/` | Optional embedding inference service (Apache-2.0); model weights/tokenizers carry separate terms. |
| [Transformers](https://github.com/huggingface/transformers) | `src/transformers/`, `examples/`, `tests/` | Model architecture and tokenizer integration (Apache-2.0); each downloaded model/weight license is separate. |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | `sherpa-onnx/` in source tree, `c-api-examples/`, `python/`, `tests/` where present | Offline ASR/TTS/VAD/diarization (Apache-2.0); compare with faster-whisper and review audio/model licensing. |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | `python/`, `dotnet/`, `java/`, connector/plugin docs | Multi-language SDK (MIT); evaluate as alternative worker/plugin SDK, not another global orchestrator. |
| [Home Assistant Core](https://github.com/home-assistant/core) | `homeassistant/components/`, `tests/components/`, `homeassistant/helpers/` | Home automation platform (Apache-2.0); initially integrate through user-authorized APIs, not embedded core fork. High-impact home actions need confirmation. |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | `python/`, `dotnet/`, `docs/`, `skills/` | Multi-language agent/workflow framework (MIT); compare with existing worker choices before adoption. |


## v0.8 additions — file-level inspection map

| Repository | Inspect these paths first | Reuse boundary |
|---|---|---|
| vLLM | `vllm/`, `vllm/entrypoints/`, `vllm/engine/`, `benchmarks/`, `tests/` | GPU inference server candidate; benchmark against SGLang and review kernels/model terms |
| SGLang | `python/`, `sgl-router/`, `sgl-model-gateway/`, `rust/`, `benchmark/`, `test/` | Alternative GPU serving stack; select one server baseline |
| Promptfoo | `src/`, `plugins/`, `test/`, `architecture/` | Evaluation and authorized red-team harness; protect traces and test datasets |
| Haystack | `haystack/`, `test/`, `examples/` | RAG pipeline alternative to LlamaIndex; compare golden corpus and ACL behavior |
| DuckDB | `src/`, `extension/`, `test/`, `benchmark/`, `third_party/` | Local analytics only, not transactional task/identity authority |
| garak | `garak/`, `signatures/`, `tools/`, `tests/` | LLM security probes against owned or explicitly authorized targets |

These six repositories are pinned in the v0.8 lock and remain inspection-only. Do not copy entire repositories as application modules.


## v0.9 additions — source-level paths

Three projects are added to the pinned catalogue. Use the exact pin in `config/upstreams/upstream-lock.yaml` and the licence/NOTICE at that revision.

### Microsoft GraphRAG — MIT, experimental graph RAG

- `packages/graphrag/graphrag/` — primary package implementation.
- `packages/graphrag-cache/`, `packages/graphrag-chunking/`, `packages/graphrag-common/`, `packages/graphrag-input/`, `packages/graphrag-llm/`, `packages/graphrag-storage/`, `packages/graphrag-vectors/` — separated packages to review for dependency closure.
- `tests/` — carry the relevant package tests.
- Use only for graph enrichment/retrieval after source ACL, provenance and deletion policy are enforced in ORBIT.

### Guardrails AI — Apache-2.0, structured output validation

- `guardrails/guard.py`, `guardrails/async_guard.py` — main execution interface.
- `guardrails/validators/`, `guardrails/schema/`, `guardrails/run/`, `guardrails/formatters/` — validator and schema pipeline modules.
- `tests/` — validate expected output and failure behavior.
- Review remote validator/Hub integrations; a validator result is not an authorization token.

### Milvus — Apache-2.0, distributed vector storage

- `internal/proxy/`, `internal/querynodev2/`, `internal/rootcoord/`, `internal/storage/` — server subsystems to inspect.
- `pkg/`, `client/` — API/client contracts.
- `tests/`, `go.mod` — tests and dependency closure.
- Do not import internal Milvus server code into ORBIT. Evaluate as an external vector service only if Qdrant/Chroma benchmarks show a scale need.

These paths are source navigation targets, not a promise that any directory is a stable public API. Confirm exact code, tests, package boundaries and nested licenses at the locked revision before applying.
