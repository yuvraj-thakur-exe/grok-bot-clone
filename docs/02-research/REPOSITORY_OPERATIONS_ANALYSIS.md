# ORBIT repository operations analysis — v0.9

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Executive decision

ORBIT should use upstream code as a maintained asset, not as inspiration to rewrite every capability. The working rule is **clone → pin → inspect → audit → run upstream tests → isolate → adapt → test ORBIT contract → attribute → sync**. Copying a repository is not the same as understanding its architecture; pasting a file without dependencies, license notices and tests is usually a bug-delivery mechanism.

The five user-supplied repositories have been inspected at pinned commits in `config/upstreams/upstream-lock.yaml`. Additional candidate repositories are listed in the same lock. The audit is based on public GitHub metadata, README, root entries, available license files/metadata and selected source paths. It is not a complete line-by-line code audit, build, penetration test or legal opinion.

## Operating map: the five requested repositories

### 1. OpenMausBot — product-shell and multi-agent UX reference

- Source: https://github.com/milind-soni/OpenMausBot
- Pinned revision: `3f81576655ca45af91bfaaa63dc37251222828eb`
- Repository metadata: Apache-2.0; upstream `LICENSING.md` says `enterprise/` is separately source-available and production use requires a separate license. Its product name and mascot are trademarks. See its `LICENSE`, `NOTICE`, `LICENSING.md`, `third_party/`, `CLA.md` and `enterprise/LICENSE` before any distribution.
- Primary language/toolchain observed: TypeScript, Electron, Vite, pnpm, Node >=24; package scripts include `build`, `typecheck`, `test`, `package:prepare`, desktop packaging and CUA/browser smoke tests.
- Product surfaces observed: `src/` UI, `server/` local harness/API, `shared/` contracts, `electron/` desktop lifecycle, `companion/` companion app, `connector/` connected apps, `relay/`, `skills/`, `evals/`, `third_party/`.

**High-value review paths (exact inspected paths):**

| Path | Reuse target | Required ORBIT adaptation |
|---|---|---|
| `server/agent-tool-policy.ts` | Explicit read-only tool allowlist and annotations | Use as a pattern only; server-side ORBIT policy must authorize every call |
| `server/agents-turn.ts` | Turn-scoped capability flags, handoff tokens and turn-kind restrictions | Map to ORBIT task/lease/approval identity; never trust tool-provided flags alone |
| `server/app-events.ts` | Bounded event batches, untrusted event data blocks, provenance labeling and source filtering | Preserve untrusted-data boundaries, size limits and event idempotency |
| `shared/approval-mode.ts`, `shared/live-approval.ts` | Approval data models and interaction patterns | Bind approvals to exact action, resource, account, data and expiry |
| `shared/routine-schedule.ts`, `shared/routine-run.ts` | Scheduling contracts and run state | Add DST/time-zone tests, duplicate suppression, cancellation and retry budgets |
| `shared/skill-import.ts`, `shared/skill-md.ts`, `shared/written-skill.ts` | Skill parsing/import conventions | Add immutable version/digest, independent source license and sandbox grants |
| `shared/connector-scopes.ts`, `shared/connector-account-link.ts` | Connector account and scope modeling | Minimize OAuth scopes; add per-workspace separation and revocation verification |
| `shared/team-setup.ts`, `shared/bot-profile.ts`, `shared/thread-model.ts` | Roster, profile, context/thread domain patterns | Map to canonical ORBIT agent/project/context IDs |
| `server/` tests near each module | Regression evidence | Run source tests before adaptation; carry relevant tests and add ORBIT contract tests |

**Recommended use:** benchmark this as the first product-shell starting point if the actual ORBIT repository has no functioning shell. If ORBIT already has working frontend/backend code, preserve it and reuse OpenMausBot modules selectively. Do not blindly copy `src/`/`server/` in one operation. The source-acquisition helper excludes `enterprise/` from the checkout. The developer must still ensure no import, generated artifact or dependency reintroduces excluded content. Do not inherit upstream plaintext CLI credential storage unchanged; ORBIT's own secret vault must use OS keychain/encryption and write-only API semantics.

**Build inspection commands (execute only after license/security review):**

```bash
node --version
pnpm --version
pnpm install --frozen-lockfile
pnpm typecheck
pnpm test
pnpm build
```

Use the exact package scripts from the pinned `package.json`; build commands are not claims that they were run for this pack. Avoid packaging commands until the full third-party/enterprise/brand audit is complete.

### 2. OpenClaw — gateway, channels, model providers and extension ecosystem

- Source: https://github.com/openclaw/openclaw
- Pinned revision: `7283c5182497e1ac5f95668de9f39ad3a9df3b11`
- Root license metadata and `LICENSE`: MIT; very large TypeScript monorepo. Inspect the root `THIRD_PARTY_NOTICES.md` and each package/extension dependency.
- Architecture surfaces observed: `packages/agent-core/`, `packages/gateway-client/`, `packages/gateway-protocol/`, `packages/plugin-sdk/`, `packages/acp-core/`, `packages/net-policy/`, `extensions/`, `skills/`, `src/`, `ui/`, `crates/`.
- Extension examples observed: `extensions/browser/`, `extensions/duckduckgo/`, `extensions/deep-research/`, `extensions/github/`, `extensions/document-extract/`, `extensions/diagnostics-otel/`, `extensions/memory-core/`, `extensions/memory-lancedb/`, `extensions/telegram/`, `extensions/whatsapp/`, `extensions/slack/`, `extensions/ollama/`, `extensions/llama-cpp/`.

**Recommended use:** use official package boundaries and protocols first. Treat OpenClaw as an optional gateway/channel backend, or selectively use a connector/extension after validating its dependencies. Do not create a second canonical user/task database. Native in-process plugins run with gateway process trust; an allowlist is not a sandbox. Use a separate process/container and narrow RPC for untrusted code.

**Build inspection commands:**

```bash
pnpm install --frozen-lockfile
pnpm build
pnpm ui:build
```

Read `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, package manifests and `THIRD_PARTY_NOTICES.md` first. The README's supported Node versions are time-sensitive; use the exact pinned package's `engines` field.

### 3. Hermes Agent — optional Python runtime

- Source: https://github.com/NousResearch/hermes-agent
- Pinned revision: `27afd192c2215d1e7363c38a2db77d0ab3f9db49`
- Root `LICENSE`: MIT; Python agent and gateway implementation.
- Inspected root surfaces: `agent/`, `gateway/`, `cron/`, `evals/`, `hermes_cli/`, `hermes_platform/`, `acp_adapter/`, `hermes_agent/`, `docker/`, `apps/`.
- The `agent/` package is extensive and includes provider adapters, state management, turn control, tools, memory and verification code. This degree of coupling is a reason to use it as a separate worker/backend before considering internal source imports.

**Recommended use:** build an `AgentBackend` adapter that starts Hermes as a separate worker or uses a supported protocol. Normalize task IDs, turn events, tool calls, cancellation, usage, files and errors at the ORBIT boundary. Do not import private helper modules across dozens of Python files unless a clear, stable seam and test suite exist. Do not allow Hermes to bypass ORBIT approval checks or directly own personal identity/task state.

**Install/test:** follow the pinned repository's current `README.md`, `AGENTS.md`, `pyproject.toml`, lock files, `evals/` and `SECURITY.md`. Start with a disposable virtual environment; do not install globally.

### 4. Hermes Agent Self-Evolution — offline improvement lab

- Source: https://github.com/NousResearch/hermes-agent-self-evolution
- Pinned revision: `0a929e3aa20e15cf04dc7c28492a7d41a5139125`
- License evidence at inspected revision: README and `pyproject.toml` declare MIT, but a root `LICENSE` file was not present. Confirm rights-holder license evidence before redistributing copied code.
- Inspected surfaces: `evolution/`, `datasets/`, `reports/`, `tests/`, `generate_report.py`, `PLAN.md`, `pyproject.toml`.
- The README describes DSPy + GEPA skill/prompt/tool-description optimization. The plan describes code evolution as a higher-risk later phase and places it behind tests and review.

**Recommended use:** offline-only optimization of skill text and tool descriptions against golden datasets and held-out tasks. Require baseline score, candidate score, regression tests, cost/latency results, prompt-injection tests, semantic-preservation checks and a human-reviewed pull request. Do not mutate production prompts, skills or code during live conversations. Do not use private user sessions for training/optimization unless consent and data governance explicitly allow it.

### 5. VoltAgent Awesome OpenClaw Skills — discovery catalogue

- Source: https://github.com/VoltAgent/awesome-openclaw-skills
- Pinned revision: `5492fcd98f7c52c69e1b2fa58790faf4fc90ce13`
- Repository license: MIT for the catalogue. It indexes many independently authored skills; it does not grant the catalogue's MIT license to each external skill.
- Inspected surfaces: `categories/`, `README.md`, `CONTRIBUTING.md`, `LICENSE`.

**Recommended use:** build a searchable discovery index, not an installer that runs every result. For each chosen skill fetch its canonical source, immutable commit/release, license, digest, manifest, scripts, dependencies and security review. Keep the skill quarantined until a user/operator approves the requested capabilities. Curated does not mean safe.

## Additional open-source candidates added in v0.7

Exact commit pins and root GitHub license metadata are in the upstream lock. These are evaluation candidates; nested dependencies, model weights, cloud features and data terms still require separate review.

| Repository | License metadata | Purpose in ORBIT | Recommended mode |
|---|---|---|---|
| Pydantic AI | MIT | Typed Python agent workers, tools and realtime interfaces | Compare for Python specialist workers; not a second global orchestrator |
| Ollama | MIT | Local model serving | Local model provider adapter; model weights have separate licenses |
| llama.cpp | MIT | Quantized GGUF inference | Local inference performance and quantization option |
| Docling | MIT | Document structure/layout extraction | Document ingestion adapter |
| faster-whisper | MIT | Speech-to-text | Optional local transcription worker |
| Graphiti | Apache-2.0 | Temporal knowledge graph memory | Experimental memory graph adapter after basic ACL/deletion works |
| MCP Python SDK | MIT | Python MCP clients/servers | Python tool interoperability; MCP annotations never authorize actions |
| OpenAI Agents Python | MIT | Handoffs, guardrails and tracing in Python | Compare as a specialist workflow SDK; preserve model/provider portability goals |
| Composio | MIT metadata | Connected app toolkits, auth and tool discovery | Connector/OAuth proof of concept; inspect feature and cloud boundaries |

## Operating ownership

| Work area | Accountable virtual role | Independent reviewer |
|---|---|---|
| Upstream selection and architecture | CTO / Principal Architect | Security + QA + Founder |
| Clone, pin, worktree, source diff | Repository Operations Engineer | Backend Engineer |
| License, NOTICE and provenance | OSS/IP Analyst | Founder + qualified counsel |
| Package/connector adaptation | Integration Engineer | Security + QA |
| Local models and inference | Model Runtime Engineer | AI Research + SRE |
| Memory/RAG | Data/RAG Engineer | Security + Product |
| Acceptance and benchmark | QA/Evaluation Engineer | Product + Security |

These are AI-assisted role charters, not actual hires or statutory officers. The human founder retains approval authority.

## Required output for every upstream audit

1. Repository URL, exact commit SHA, date and origin remote.
2. Root/nested license and attribution summary.
3. Directory and package map; language and build commands.
4. Candidate files/packages and dependency graph.
5. Threat model: privileges, network, credentials, telemetry, install scripts and persistence.
6. Tests available and exact upstream tests executed.
7. Reuse mode decision: service, SDK, package, selective import, fork or reject.
8. ORBIT adapter boundary and migration/data mapping.
9. File hashes, modifications, provenance, notices and SBOM delta.
10. Rollback and upstream synchronization plan.

## Important scope limitation

This analysis was performed against GitHub sources at the lock's recorded commits. It does not imply that any repository has been cloned to the user's 500 GB drive, installed, built, merged into ORBIT or verified at runtime. The local operational scripts are supplied so those steps can be performed in the actual ORBIT environment with evidence.


## v0.7 extension

The detailed per-repository file map is in [V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP](V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md). The command-level operating sequence, Windows/Linux drive setup, staging commands and verification steps are in [REPO_OPERATIONS_COMMAND_REFERENCE](../13-guides/REPO_OPERATIONS_COMMAND_REFERENCE.md). At v0.7, the lock tracked 35 repositories. v0.8 added six more, bringing that release to 41. v0.9 adds three more and the current lock contains 44. Do not copy all 44 into the application.


## v0.7 expanded catalogue and practical source reuse

At v0.7, the catalogue contained 35 exact commit pins. Nine candidates added browser automation (Playwright), document conversion (MarkItDown), alternative vector retrieval (Chroma), embedding serving (Text Embeddings Inference), model architecture/tokenizers (Transformers), offline voice (sherpa-onnx), multi-language agent SDKs (Semantic Kernel and Microsoft Agent Framework), and home automation (Home Assistant). See [file-level adoption map](V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md).

Do not adopt competing alternatives in parallel: compare Playwright/Stagehand/Browser Use, Docling/MarkItDown, Qdrant/Chroma, faster-whisper/sherpa-onnx, and Pydantic AI/OpenAI Agents/Semantic Kernel/Microsoft Agent Framework. Each comparison ends with one chosen baseline and an adapter for later replacement. Home Assistant is an external connector target first, not a product-shell fork.


## v0.8 additional repository analysis

Six more pinned repositories extend ORBIT's serving, evaluation, retrieval, analytics and LLM security coverage. The file-level map is in `V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md`; operational choices and limitations are documented in `V08_OPEN_SOURCE_EXTENSION_REVIEW.md`.

- vLLM and SGLang are GPU-serving alternatives, not two mandatory runtimes.
- Promptfoo and garak provide evaluation/red-team tooling, only against authorized targets.
- Haystack is a retrieval pipeline alternative to LlamaIndex.
- DuckDB is for local analytics, not transactional user/task state.

The v0.8 catalogue has 41 exact commit pins. All new projects are still inspection-only.


## v0.9 additional repository analysis — current catalogue 44

Three more repositories were pinned for inspection on 08 November 2026. They are candidate components, not runtime approvals.

### Microsoft GraphRAG

- URL: https://github.com/microsoft/graphrag
- Pin: `34b2b67ae4601ad0b47bcd179fbe3f2a23aa0857`
- Root metadata: MIT.
- Inspected structure: `packages/graphrag/`, `packages/graphrag-cache/`, `packages/graphrag-chunking/`, `packages/graphrag-common/`, `packages/graphrag-input/`, `packages/graphrag-llm/`, `packages/graphrag-storage/`, `packages/graphrag-vectors/`, `tests/`, `unified-search-app/`.
- Use: graph extraction and graph-enhanced RAG experiment after a baseline retrieval solution exists.
- Boundary: do not turn it into a second agent/task orchestrator. Preserve ORBIT ACL, document provenance, deletion and consent.

### Guardrails AI

- URL: https://github.com/guardrails-ai/guardrails
- Pin: `06d0ff2c5f9bcb493d976b76f885e37e41ce845d`
- Root metadata: Apache-2.0.
- Inspected structure: `guardrails/`, `guardrails/validators/`, `guardrails/schema/`, `guardrails/run/`, `tests/`, `pyproject.toml`.
- Use: typed/structured output validation adapter and guardrail pipeline experiment.
- Boundary: framework validators are not a complete security or authorization layer. Review remote validators, external integrations and false-positive/bypass rates. ORBIT approval and policy remain authoritative.

### Milvus

- URL: https://github.com/milvus-io/milvus
- Pin: `686b129ca584fe2e8ae88b06ead95ffa03bad56a`
- Root metadata: Apache-2.0.
- Inspected structure: `internal/`, `pkg/`, `client/`, `tests/`, `go.mod`; key internal areas include `internal/proxy/`, `internal/querynodev2/`, `internal/storage/`, `internal/rootcoord/`.
- Use: distributed vector search/storage alternative when ORBIT has measured scale requirements.
- Boundary: compare with Qdrant and Chroma, not as a default third backend. Keep PostgreSQL/ORBIT as source of truth for identity, tenant ACL and metadata.

### v0.9 practical source application change

The local workflow now has two distinct steps: (1) `import_upstream_path.py` stages a selected path and emits `manifest_sha256`; (2) `apply_staged_source.py` requires that exact digest and revalidates every file hash before copying to an explicit new path in a clean `orbit/*` or `feature/*` ORBIT app worktree. It refuses path overwrite, symlinks, dirty targets and altered manifests. It never `git add`, commits, merges or pushes. The exact workflow is in `../13-guides/V09_REPO_CODE_REUSE_PLAYBOOK.md`.

The v0.9 lock snapshot contained 44 exact upstream pins. The current v1.0 lock contains 50; this is a catalogue, not an instruction to clone all 50 or a claim that these projects have been built or integrated. See `V10_OPEN_SOURCE_FILE_LEVEL_ADOPTION_MAP.md`.
