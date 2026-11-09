# ORBIT v0.7 — upstream source decision matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Snapshot:** 08 November 2026. Commit pins and preliminary repository license metadata are in `config/upstreams/upstream-lock.yaml`. This is an engineering shortlisting document, not legal clearance.

## Selection principle

Keep one default owner per capability. Prefer a stable upstream service, SDK or adapter; selective code import comes only after exact source and license review. The first implementation choice may change after the real ORBIT repository audit.

| Capability | Primary candidate | Alternatives | v0.6 decision | Main boundary |
|---|---|---|---|---|
| Desktop/web product shell | Existing ORBIT shell; otherwise OpenMausBot public OSS | First-party UI rebuild only if necessary | Audit first; prototype one shell | Exclude `enterprise/`; no upstream brand/mascot; rework secrets |
| Personal gateway/channel runtime | OpenClaw adapter | Hermes Agent adapter | Optional external runtime; one default only | ORBIT retains canonical identity, task and authorization |
| Specialist agent runtime | Existing ORBIT agent loop or Hermes adapter | OpenHands for coding jobs | No second control plane | Normalize events, cancellation, usage and artifacts |
| Coding worker | OpenHands Software Agent SDK | Dedicated runtime CLI in sandbox | P1 PoC | Disposable repo workspace, no inherited personal credentials |
| Browser | Playwright baseline | Stagehand, agent-browser, Browser Use | Benchmark and select one | ORBIT owns domain policy, egress and approvals |
| Sandbox | Docker baseline | OpenSandbox | P1 provider comparison | Deny-by-default egress; scoped credentials; cleanup |
| Memory | ORBIT MemoryProvider contract | Mem0, Letta | Compare; choose one adapter | ORBIT consent, ACL, provenance, expiry, delete |
| Workflow | Temporal | LangGraph | Temporal durability PoC; LangGraph only for graph orchestration if justified | One durable task and retry authority |
| Document/RAG | LlamaIndex adapter | First-party parsers | P1 ingestion PoC | ACL and source citation propagation |
| Vector store | Postgres/pgvector baseline | Qdrant | Optional after retrieval benchmark | Derived index only, tenant filters and delete propagation |
| Skills | Agent Skills-compatible folders | OpenClaw skills ecosystem, VoltAgent index | Format compatibility; curated source review | Catalog license does not grant skill-source rights |
| Prompt/skill optimization | DSPy/GEPA patterns | Hermes self-evolution | Offline-only | Holdout tests, approval, PR and rollback |
| Telemetry | OpenTelemetry | Vendor-specific exporters | Adopt API standards after package review | Redact content and secrets; retention/access controls |

## Upstream-specific evidence and limitations

- **OpenClaw:** MIT repository metadata. Its Gateway, channels, tools, nodes, provider extensions and skill ecosystem are useful reference points. In-process native plugins are trusted code, not isolation. Use an external runtime adapter or trusted reviewed packages.
- **VoltAgent awesome-openclaw-skills:** MIT applies to catalogue repository content. Each canonical skill source has an independent license, threat profile and permission scope. The README reports a curated index of thousands of skills; do not treat a count as quality proof.
- **Hermes Agent:** MIT repository metadata. Evaluate its runtime and messaging/CLI interfaces as an optional backend. Avoid duplicated task, channel, memory or scheduler ownership.
- **Hermes self-evolution:** README and `pyproject.toml` state MIT, but root LICENSE was absent in the inspected snapshot. Do not redistribute until license text/rights-holder evidence is confirmed. Darwinian Evolver is identified as AGPL-3 in the upstream plan and remains external-CLI-only pending separate review.
- **OpenMausBot:** Apache-2.0 public OSS edition, with `enterprise/` under a separate source-available license. Exclude that folder. Preserve `LICENSE`, `NOTICE`, `LICENSING.md`, third-party files and attribution. No trademark rights are granted. CLI setup docs describe plaintext configuration keys with owner-only permissions on Unix; packaged desktop path documents OS-backed encryption where supported. ORBIT must unify on an approved secret vault.
- **OpenHands Software Agent SDK:** MIT metadata; candidate for coding-worker isolation and reusable agent abstractions. Test container/workspace boundary and credential handling independently.
- **OpenSandbox:** Apache-2.0 metadata; sandbox API/runtime candidate. Firecracker/microVM support depends on host capabilities. Do not claim performance until ORBIT benchmarks it.
- **Stagehand / Browser Use:** MIT metadata. Keep browser control and egress in ORBIT regardless of driver.
- **Mem0 / Letta Code:** Apache-2.0 metadata. Compare actual self-host/cloud data flow and memory semantics; ORBIT remains memory governance authority.
- **LangGraph / DSPy / Temporal:** MIT metadata at repository level in the pinned snapshot. Inspect package and server terms separately. Use only one durable workflow owner.
- **OpenTelemetry JS:** Apache-2.0 metadata. Package-level and transitive dependency checks still required.
- **LlamaIndex / Qdrant:** MIT / Apache-2.0 metadata respectively. Review Python package set, optional integrations, server distribution and deployment data paths.

## Adoption gates

No upstream is “approved” until: exact revision pinned; LICENSE/NOTICE/nested notices and transitive packages checked; code scanned; telemetry/install scripts inspected; data flow reviewed; security boundary tested; conformance tests pass; update owner and rollback defined; and the component register updated. Product shell selection requires a build, accessibility, platform, secret, upgrade and user-experience review against the current ORBIT repo.


## v0.6 additional evaluated candidates

The current 26-repository pinned list adds Pydantic AI, Ollama, llama.cpp, Docling, faster-whisper, Graphiti, the MCP Python SDK, OpenAI Agents Python and Composio. Their responsibilities and caveats are described in `V06_OPEN_SOURCE_EXPANSION_RADAR.md` and `REPOSITORY_OPERATIONS_ANALYSIS.md`. They remain inspection-only until benchmark and security review.
