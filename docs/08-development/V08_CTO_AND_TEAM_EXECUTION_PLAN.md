# ORBIT v0.8 — CTO and engineering execution plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Executive mandate

Build ORBIT as a secure personal/work agent platform by selecting and adapting mature upstream capabilities. Preserve existing ORBIT code. Never start a rewrite until repository audit proves that the current code and candidate upstream implementations are unsuitable.

## Phase A — control the source supply (first gate)

**Owner:** CTO + Repository Operations Engineer + Open Source/IP Analyst + SRE.

- Confirm the actual ORBIT application Git URL and primary branch.
- Create a clean baseline report: commit, dirty files, stack, build, tests, dependencies, secrets scan, SBOM and module map.
- Verify the dedicated 500 GB disk and initialize the planned directory structure only after the human verifies the physical volume.
- Clone only product-shell, coding-worker and browser/sandbox candidates initially.
- Verify all checkouts against 41 exact pinned commits.
- Produce per-repository audits and a source reuse decision matrix.

**Exit:** no source merges yet; baseline is reproducible and all user changes protected.

## Phase B — one vertical slice

**Owner:** CTO + Backend + Agent Runtime + Frontend + QA + Security.

Implement one real task lifecycle: workspace → task creation → runtime adapter → safe read-only tool → evidence/artifact → reconnect → cancel/resume. Keep identity, task state, authorization, approvals and audit events in ORBIT's control plane. The first agent runtime may be OpenClaw or Hermes behind an adapter; do not embed both as parallel control planes.

**Exit:** E2E task test passes, permissions are server-checked, event logs are redacted, cancellation and recovery work.

## Phase C — coding, browser and computer

**Owner:** Coding Worker Engineer (Repository Operations/Agent Runtime) + Browser Engineer + Sandbox Engineer + Desktop Engineer.

- Evaluate OpenHands SDK for one-repository coding tasks with per-task workspaces and minimal credentials.
- Use Playwright as the browser automation baseline. Compare Stagehand/Browser Use only through the same contract.
- Establish Docker sandbox baseline; evaluate OpenSandbox for isolation and lifecycle.
- Add local desktop node with read-only observation before any write/action permissions.

**Exit:** sandbox escape, egress and cancellation tests; browser evidence and fresh snapshots; desktop pairing, expiry and local stop tests.

## Phase D — memory, knowledge and connected applications

**Owner:** Data/RAG Engineer + Integration Engineer + Security + Product.

- Start with scoped SQL/document memory and explicit provenance.
- Compare Mem0 vs Letta; compare Graphiti only after memory ACLs and deletion work.
- Compare Docling vs MarkItDown; compare LlamaIndex vs Haystack on an approved golden corpus.
- Compare Qdrant vs Chroma and pick one store.
- Start with one read-only OAuth/MCP connector. Expand scopes after explicit user authorization.

**Exit:** source citations, personal/work isolation, delete propagation, OAuth revocation and minimum-scope conformance.

## Phase E — model/voice and always-on work

**Owner:** Model Runtime + Voice Engineer + SRE + Product.

- Benchmark Ollama and llama.cpp locally on real hardware.
- Benchmark vLLM vs SGLang only on a supported GPU server; disk capacity is not compute capacity.
- Add faster-whisper or sherpa-onnx as one voice pipeline after latency/privacy tests.
- Add Temporal for durable long-running work when retry, timers, recovery and event state justify it.
- Add user-controlled routines, heartbeat/trigger rules, pause, cancel, budget caps and audit.

**Exit:** measured model performance, spend ceilings, durable restart/recovery, offline/remote boundaries, user consent.

## Phase F — evaluation, security and release

**Owner:** QA + Security/Privacy + Open Source/IP Analyst + CTO + Human Founder.

- Create benchmark suite against public competitor task claims: persistent tasks, agent teams, computer use, connected apps, routine management, coding, research, memory correction/deletion and user approvals.
- Use Promptfoo and garak only against owned or authorized targets.
- Run dependency CVE/license scans, SBOM, secret scanning, threat model, recovery test, access-control tests and red-team suite.
- Require a human-approved release checklist.

**Exit:** measured results; unresolved severe risks block ship; rollback and restore evidence available.

## Team task contract

Every work item must contain: task ID, human owner, virtual agent role, source repo ID and pinned commit, permitted paths, forbidden paths, capability grants, data sensitivity, network egress, budget/cost limit, required tests, expected evidence, rollback, reviewer and definition of done. Multi-agent work must not share a mutable checkout. Use isolated worktrees and have one integrator reconcile changes.

## Explicit ownership map

- Founder/CEO (human): drive selection, spending, OAuth accounts, legal risk acceptance, external communication, production release.
- CTO: system boundaries, capability ownership, upstream selection, design review and merge criteria.
- Repository Operations: clones, pins, audit reports, worktrees, staging manifests and upstream sync.
- Product/UX: user outcome, contexts, routines, permission/approval design.
- Backend/Frontend: ORBIT application implementation and adapters.
- Agent Runtime/AI Research: runtime, orchestration and offline optimization.
- Browser/Desktop/Sandbox: separate execution planes and safety contracts.
- Data/RAG/Model/Voice: scoped memory, ingestion, local/remote model and multimodal.
- Integration: connector auth, least-privilege scopes and event provenance.
- Security/Privacy: can block unsafe code, data flow or release.
- QA/Benchmark: independent tests and evidence, cannot self-approve developer changes.
- SRE: storage health, builds, deployments, monitoring, backup/restore.
- Legal/IP analyst: advisory license/notice/trademark reviews; founder obtains qualified legal advice when needed.

Virtual agents are workflow assistants, not legal employees, directors or accountable human approvers.
