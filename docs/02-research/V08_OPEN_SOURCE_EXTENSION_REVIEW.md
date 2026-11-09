# ORBIT v0.8 — expanded open-source extension review

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Newly added pinned repositories

| Repository | Pin / root license | Inspect first | ORBIT opportunity | Decision boundary |
|---|---|---|---|---|
| [vLLM](https://github.com/vllm-project/vllm) | `d76fe936a1c4bb40abaf1b06aba37d849e95bdb2` / Apache-2.0 | `vllm/`, `vllm/entrypoints/`, `vllm/engine/`, `benchmarks/`, `tests/` | High-throughput GPU inference service | Optional GPU server. Benchmark against SGLang; do not assume it is a laptop/local default. Model weights are separately licensed. |
| [SGLang](https://github.com/sgl-project/sglang) | `cbbc6b67f48008a8b739f4667d7b14abb89088cf` / Apache-2.0 | `python/`, `sgl-router/`, `sgl-model-gateway/`, `rust/`, `benchmark/`, `test/` | Alternative GPU and multimodal inference serving | Benchmark against vLLM; pick one baseline per deployment. Check kernels, images and model license terms. |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | `2a6fdf9b2e1600ffa2a204e70e9fea7cb0c14cff` / MIT | `src/`, `plugins/`, `test/`, `architecture/`, root `LICENSE` | Prompt, model, agent, RAG evaluation and authorized red-team runs | Run against ORBIT-owned or expressly authorized endpoints only; protect eval datasets and traces. |
| [Haystack](https://github.com/deepset-ai/haystack) | `0ad74747ffd7d9f9b092db97ba2e222080992c2e` / Apache-2.0 | `haystack/`, `test/`, `examples/`, `pyproject.toml` | Modular retrieval/RAG pipeline alternative | Compare with LlamaIndex; choose one canonical ingestion/retrieval pipeline. ORBIT owns ACL, provenance and deletion. |
| [DuckDB](https://github.com/duckdb/duckdb) | `d4eea3f208d42ca4ee522aca23f5ea76f902b0ca` / MIT | `src/`, `extension/`, `test/`, `benchmark/`, `third_party/` | Local analytical queries over evaluations, events and benchmark exports | Not a transactional system of record. Review extensions, binary distribution and concurrent access. |
| [garak](https://github.com/NVIDIA/garak) | `892779207cbc38f65a738ef9cbdfbc1e83aa0b55` / Apache-2.0 | `garak/`, `signatures/`, `tools/`, `tests/` | LLM security probes for prompt injection, leakage, jailbreak and robustness | Pre-release testing of owned/authorized models only. Use non-production credentials and isolated test data. |

## Why these additions matter

1. Model-serving selection was thin. vLLM and SGLang add GPU server alternatives while Ollama and llama.cpp remain candidate local runtimes. Do not create four production serving layers. Select based on the actual compute environment.
2. Evaluation and security tests needed a practical command-line harness. Promptfoo covers evaluation/comparison and red-team workflows; garak brings dedicated model vulnerability probes. Both feed ORBIT's QA/security pipeline, not its runtime authority.
3. Retrieval needed a fair alternative comparison. Haystack is a second candidate alongside LlamaIndex. Run the same golden datasets, ACL tests, citations and deletion tests; select one pipeline.
4. DuckDB adds efficient local analysis for evaluation results and redacted operational metrics. It must not replace PostgreSQL or the canonical task store.

## Excluded or held back during this expansion

- Langfuse: repository metadata returned `NOASSERTION` in the current GitHub API snapshot, and its official licensing documentation says files outside `/ee` are MIT while `/ee` contains separately licensed features. Treat as a conditional integration candidate only after folder-level boundary review, not as a simple all-MIT clone.
- Microsoft AutoGen: repository metadata reported CC-BY-4.0. This is not adopted as a software-code dependency in this pack; require legal review before any use of its code.
- Ragas: repository license metadata was not resolved in the inspected snapshot; do not add to the reuse-approved inventory until rights and root license are confirmed.
- whisper.cpp: repository license metadata was not resolved in the inspected snapshot; compare sherpa-onnx and faster-whisper first.

## One owner per concern

| Concern | Baseline selection policy | Alternatives not to deploy together by default |
|---|---|---|
| GPU serving | Compare vLLM vs SGLang on supported GPU hardware | vLLM + SGLang as parallel production gateways |
| RAG pipeline | Compare Haystack vs LlamaIndex | Two independent ingestion/ACL systems |
| Vector database | Compare Qdrant vs Chroma with one representative dataset | Qdrant + Chroma both holding canonical memory |
| Local inference | Compare Ollama vs llama.cpp on actual laptop hardware | Multiple model servers downloading the same models |
| Evaluation | ORBIT golden tasks plus Promptfoo and garak test harnesses | Treating scanner scores as proof of safety |
| Local analytics | DuckDB for offline analytical datasets | DuckDB as transactional authority |

## Adoption gate

Each new source remains `pinned_for_inspection_only`. Required before runtime use: exact source and package license review, third-party dependency inventory, install-hook review, SBOM, security test, bounded adapter, conformance tests, measured task results, performance/cost results, rollback, and human release approval.
