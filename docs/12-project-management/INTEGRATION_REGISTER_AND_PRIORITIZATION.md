# Integration register and prioritisation

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Integration/reference | Owner role | Status | Priority | Next action | Exit gate |
|---|---|---|---|---|---|
| agent-browser | Browser automation lead | Researched, not integrated | P1 evaluation | Compare against Playwright on identical test tasks | Contract, auth, egress, download and security tests |
| json-render | Frontend/AI lead | Researched, not integrated | P2 | Prototype constrained catalog in isolated feature branch | Schema validation, no arbitrary code, action auth and accessibility tests |
| agent-skills | OSS/AI lead | Research-only; license unresolved | P2 | Review each skill file/license | Exact provenance and compatible license approved |
| skills CLI | OSS lead | Researched, not integrated | P2 | Assess CLI telemetry and lockfile behavior | Telemetry/privacy decision, checksum lock and install tests |
| portless | DevEx lead | Optional developer tool | P3 | Test multi-worktree local URLs with opt-in TLS | No LAN exposure; safe CA install/removal |
| OpenHands / ACP backends | Agent runtime lead | Researched, not integrated | P2 | Draft adapter and capability contract | Workspace isolation, auth, cancellation and event replay tests |
| OpenSandbox | Sandbox lead | Researched, not integrated | P1 evaluation | Compare Docker baseline and OpenSandbox API | Egress, secret handling, lifecycle and isolation tests |
| agent-desktop | Desktop automation lead | Documented in v0.2 | P2 | Continue behind Local Desktop Node | Pair/revoke, read-only OS tests, action authorization |

## Order of work

1. Stabilise ORBIT task/policy/audit contracts.
2. Harden and verify one sandbox runtime.
3. Use Playwright as browser baseline; benchmark agent-browser adapter.
4. Define `AgentBackend` and evaluate ACP/OpenHands integration.
5. Add portable skill registry with license/provenance gates.
6. Prototype schema-constrained dynamic UI.
7. Add Local Desktop Node after core task reliability.
8. Add optional local development URL proxy.

No integration becomes a hard dependency until a measurable acceptance case justifies it.

## v0.4 source-reuse and product-shell decision

The five newly supplied repositories are audited in `docs/02-research/REUSE_FIRST_REPOSITORY_AUDIT_V04.md`. The preferred product-shell candidate is the public OpenMausBot edition if the actual ORBIT repository does not already contain an equal or better shell. OpenClaw and Hermes stay behind optional `AgentRuntimeAdapter`/gateway boundaries. Hermes self-evolution is offline-only; VoltAgent skills are catalogue metadata only. Additional candidates are in `docs/02-research/OPEN_SOURCE_COMPONENT_RADAR_V04.md`.

Before any import, review the pinned commit, nested licenses, notices, dependency closure, code tests and security. `enterprise/` in OpenMausBot is excluded absent a separate license. Never recreate the feature until the upstream reuse report documents why adoption is not viable.

### v0.4 knowledge and workflow candidates

- LlamaIndex: candidate for document ingestion and source-aware RAG. Preserve document ACLs and source citations.
- Qdrant: optional vector index, never the canonical document or memory record.
- Temporal: candidate durable workflow engine.
- LangGraph: agent graph/checkpoint candidate.
- Mem0 is the first memory-adapter proof of concept; compare Letta rather than adding both by default.
- Stagehand is the first additional TypeScript browser driver to benchmark against Playwright and agent-browser.
- OpenHands Software Agent SDK is the first coding worker proof of concept.
