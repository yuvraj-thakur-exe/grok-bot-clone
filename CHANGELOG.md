# ORBIT Engineering Pack Changelog

> **Document baseline:** ORBIT 1.1.0 / 1.0.0-draft (2026-11-08). Older versions are historical snapshots.

## 1.1.0 — 2026-11-08

- Added cross-platform Windows CMD (`orbit.bat`), PowerShell (`orbit.ps1`), and POSIX (`orbit.sh`) CLI launchers.
- Added standard-library `doctor`, `storage`, `context-pack`, and `run` commands (`src/orbit_cli`).
- Added bounded parallel task DAG execution (`orbit run`) with explicit workspace-write guards and resource ceilings.
- Added 500 GB storage initializer/status manager with reserve safeguards.
- Added deterministic context packer with SHA-256 manifest and token budget accounting.
- Added Windows, Ubuntu, and macOS CI matrix configs and comprehensive unit test suite (`tests/`).
- Fixed cross-platform JSON path handling in test suite.

## 1.0.0-draft — 2026-11-08

- Expanded the exact pinned source catalogue from 44 to 50: Google ADK, OpenAI Codex, Gemini CLI, OpenSearch, SWE-agent and FAISS.
- Added six-repository module maps and source reuse decisions/exclusions.
- Added current repository operations manual covering safe disk setup, selective clone, static audit, clean app worktrees, manifest-hash source staging, guarded copy into an ORBIT feature branch, adaptation, testing and upstream sync.
- Added a Windows PowerShell wrapper for the pinned Bash clone tool.
- Aligned every clone directory name to the canonical lock ID so `orbit_repo_ops.py verify` checks the correct paths.
- Added CTO implementation war room and 30 virtual role ownership, personal/work system architecture and measurable competitor-parity benchmark scenarios.
- Added a 500 GB operations manual with 440 GB target allocation and 60 GB reserve.
- Added source adoption record template, improved README/index and current IDE agent instructions.
- Preserved original user-supplied source files byte-for-byte.
- No ORBIT application runtime integration is claimed; actual application repository is still required.

## 0.9.0-draft — 2026-11-08

- Added GraphRAG, Guardrails AI and Milvus to the pinned source catalogue and file-level reuse map.
- Added manifest-bound source application and clean application worktree helpers.
- Added the 500 GB source/workspace/model/data allocation and repository operations regression tests.

## 0.8.0-draft — 2026-11-08

- Added vLLM, SGLang, Promptfoo, Haystack, DuckDB and garak.
- Added repository source analysis and operations workflow.

## 0.7.0-draft — 2026-11-08

- Added Playwright, MarkItDown, Chroma, Text Embeddings Inference, Transformers, sherpa-onnx, Semantic Kernel, Home Assistant and Microsoft Agent Framework.

## 0.6.0-draft — 2026-11-08

- Added repository operations, source-intake provenance, local inference, document parsing, speech and memory candidates.

## 0.2–0.5 historical

Earlier releases added the desktop node, initial system architecture, product governance, IDE agent pack, reuse-first policy and early source candidates. See the relevant archived docs for their historical scope.
