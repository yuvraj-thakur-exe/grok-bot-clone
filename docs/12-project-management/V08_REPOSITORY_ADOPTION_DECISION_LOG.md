# ORBIT v0.8 — repository adoption decisions

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

| Decision | Current position | Revisit when |
|---|---|---|
| Reuse over rewrite | Mandatory engineering default | An ADR demonstrates no usable upstream or unacceptable fit/maintenance risk |
| Product shell | OpenMausBot public OSS is a prototype candidate; actual ORBIT shell first gets audited | Build, security, license and UX evaluation on real app repo |
| Global control plane | ORBIT owns user, workspace, task, policy, approval and audit truth | Never delegate this to an unreviewed upstream runtime |
| Agent runtime | Select one external runtime adapter after baseline vertical slice | Measured reliability and integration trade-offs |
| Coding worker | OpenHands SDK is first proof-of-concept candidate | Isolation, cancellation, tests and cost pass |
| Browser | Playwright baseline; Stagehand/Browser Use alternatives | A conformance benchmark proves a better fit |
| Sandbox | Docker baseline; OpenSandbox optional provider | Isolation/performance test and operational readiness |
| Memory | Compare Mem0 and Letta after ACLs exist | Measured quality, correction and deletion behaviour |
| RAG | Compare LlamaIndex and Haystack, select one | Golden-corpus benchmark |
| Vector DB | Compare Qdrant and Chroma, select one | Real workload benchmark |
| Local serving | Ollama/llama.cpp on laptop; vLLM/SGLang on compatible GPU hosts | Hardware-specific benchmark and model rights review |
| Evaluation | ORBIT tasks plus Promptfoo; security probes with garak | Before major prompt/model/agent release |
| Local analytics | DuckDB for eval and event analysis, not canonical task store | Data volume and query workloads justify it |
| Skills | Catalogue discovery only; individual skill source review | License, code and security review completed |
| Self-evolution | Offline proposal generation only | Evaluation and human PR gate in place |

## Reuse classes

- **A: package/service adoption candidate:** integrate through stable package/API/process boundary.
- **B: selective source adaptation candidate:** stage narrow code path, adjacent tests and notices.
- **C: research/benchmark only:** evaluate and document; no code copy.
- **D: blocked:** missing or incompatible licensing, security or technical evidence.

Every current repository remains inspection-only until a separate acceptance record upgrades its state. No blanket approval is implied by the pin catalogue.
