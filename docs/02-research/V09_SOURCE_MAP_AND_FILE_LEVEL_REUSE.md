# ORBIT v0.9 source map and file-level reuse plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Why this map exists

The source catalogue contains 44 pinned repositories. It is a research index, not a command to clone everything. ORBIT should select the smallest proven module that solves the current task, preserve its source lineage and modify it in an isolated worktree. Never create a wholesale second copy of an upstream runtime when an adapter or library is enough.

## New v0.9 additions

| Repository | Pin | Observed license | Useful source areas | ORBIT use | Boundary |
|---|---|---|---|---|---|
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | `34b2b67ae4601ad0b47bcd179fbe3f2a23aa0857` | MIT | `packages/`, `tests/`, `unified-search-app/` | Experimental graph extraction and graph-enhanced retrieval | Compare against existing LlamaIndex/Haystack baseline; not a global orchestrator |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | `06d0ff2c5f9bcb493d976b76f885e37e41ce845d` | Apache-2.0 | `guardrails/`, `tests/`, `pyproject.toml` | Structured output validation and bounded output checks | A validator does not replace authorization, security policy or human approval |
| [Milvus](https://github.com/milvus-io/milvus) | `686b129ca584fe2e8ae88b06ead95ffa03bad56a` | Apache-2.0 | `internal/`, `pkg/`, `client/`, `tests/`, `go.mod` | Distributed vector-store alternative for scale | Compare with Qdrant/Chroma; keep ACL and metadata authority in ORBIT/PostgreSQL |

The observed licenses above are repository metadata at the pinned snapshot. Confirm each exact file's license, nested dependencies, NOTICE and third-party assets before copying. This table is not a legal opinion.

## High-value source map for the supplied projects

### OpenClaw

- `packages/plugin-sdk/` and `packages/gateway-protocol/`: inspect contracts before adapters.
- `packages/agent-core/`: evaluate reusable turn/agent abstractions, with ORBIT task state outside.
- `extensions/browser/`, `extensions/deep-research/`, `extensions/document-extract/`, `extensions/github/`, `extensions/duckduckgo/`, `extensions/telegram/`, `extensions/whatsapp/`: feature reference and possible isolated extension reuse.
- `packages/net-policy/`: study policy patterns. Native in-process plugin code remains trusted code, not a sandbox.

### OpenMausBot

- `server/agent-tool-policy.ts`, `server/agents-turn.ts`, `server/app-events.ts`: policy-aware agent turn context and untrusted event handling.
- `shared/approval-mode.ts`, `shared/live-approval.ts`, `shared/outside-write.ts`: approval concepts and state contracts.
- `shared/routine-schedule.ts`, `shared/routine-run.ts`, `shared/routines.ts`: routines and run-state patterns.
- `shared/skill-import.ts`, `shared/skill-md.ts`, `shared/written-skill.ts`: import/validation concepts for skills.
- `shared/connector-scopes.ts`, `shared/connector-account-link.ts`: OAuth scope and account-link concepts.
- `shared/team-setup.ts`, `shared/bot-profile.ts`, `shared/thread-model.ts`: agent roster and conversation data contracts.
- Never stage or checkout `enterprise/`. Preserve Apache-2.0 LICENSE, NOTICE and attribution obligations; do not reuse trademarks or mascot.

### Hermes Agent and Self-Evolution

- Inspect `agent/`, `gateway/`, `cron/`, `evals/`, `acp_adapter/` and `hermes_state*` modules in the runtime.
- Self-evolution: inspect `evolution/skills/`, `evolution/core/`, `datasets/` and `tests/` as offline optimization research.
- Keep only one ORBIT task/state authority. All evolved prompts/skills must pass holdout evaluation and human review; never live self-edit production source.

### Runtime, browser, memory and coding

- OpenHands SDK: inspect `openhands/` SDK modules and sandboxed execution contracts; adapt a coding-worker boundary.
- OpenSandbox: inspect `packages/`, SDK and runtime API; require egress/credential isolation.
- Playwright: use as browser automation baseline. Stagehand/Browser Use remain comparative alternatives.
- Mem0/Letta/Graphiti: compare extraction, memory lifecycle and temporal links; ORBIT owns consent, ACL, retention and deletion.
- Temporal/LangGraph: Temporal is for durable workflow execution; LangGraph is an agent graph library. Do not create competing task authorities.

### Retrieval, documents, models and voice

- Docling/MarkItDown: document parsing/conversion adapters; outputs remain untrusted, source-labelled inputs.
- LlamaIndex/Haystack/GraphRAG: compare ingestion and retrieval quality; choose one primary path plus optional graph enrichment.
- Qdrant/Chroma/Milvus: choose one vector backend based on local/scale requirements; don't run all by default.
- Ollama/llama.cpp/vLLM/SGLang: use one local or GPU inference backend per deployment profile; select through measured benchmarks.
- faster-whisper/sherpa-onnx: choose speech path based on device, offline, latency and model-license needs.

## Import path checklist

1. Locate exact file and nearest tests in the pinned commit.
2. Identify all imports, dependency versions, generated assets and nested license notices.
3. Inspect the target ORBIT module before copying. Prefer reusing an existing ORBIT abstraction.
4. Create a clean feature worktree from the actual ORBIT app repository.
5. Stage one exact upstream path with `import_upstream_path.py`.
6. Copy staged files into the feature worktree with `apply_staged_source.py`.
7. Update imports/configuration and replace upstream-only assumptions with ORBIT adapters.
8. Preserve notices, record source hashes and add ORBIT contract tests.
9. Run tests and security checks. QA/Security independently review.
10. Human maintainer commits and opens PR; no helper commits or merges automatically.

See `docs/13-guides/V09_REPO_CODE_REUSE_PLAYBOOK.md` for exact commands.
