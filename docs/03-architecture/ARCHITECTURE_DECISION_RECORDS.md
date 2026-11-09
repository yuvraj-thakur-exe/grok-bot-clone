# Architecture Decision Records

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## ADR-001 Modular monolith + worker separation — Proposed
Start with a modular monolith API and separate execution workers. Rejected full microservices on day one due to operational cost. Revisit when scaling/ownership/security requires it.

## ADR-002 Next.js App Router + TypeScript — Proposed
Use for web workspace. Keep backend contracts explicit; do not let UI become domain source of truth.

## ADR-003 FastAPI + Pydantic — Proposed
Typed async API and Python AI ecosystem. Long jobs belong in workflow workers, not request handlers.

## ADR-004 PostgreSQL is source of truth — Proposed
Own users, workspaces, conversations, tasks, approvals, audit, evidence and metadata. pgvector optional. Redis is not authoritative.

## ADR-005 Temporal behind `WorkflowRuntime` — Proposed; prototype before lock-in
Use for durable long tasks, retries, timers and human wait states. Workflow code deterministic; model/network/tool work in activities. Risk: added infrastructure and developer learning curve.

## ADR-006 Provider adapters/capability registry — Proposed
Normalize streaming, tool calling, structured output and modality capability. No vendor SDK calls scattered through business services.

## ADR-007 Playwright isolated browser worker — Proposed
Context isolation for browser storage, plus worker/process/network isolation. BrowserContext is not an OS sandbox.

## ADR-008 Disposable code worker — Proposed
Rootless containers for local development; evaluate gVisor/Firecracker/Kata for public hostile workloads. No host mounts/socket/secrets.

## ADR-009 Exact-action approvals — Proposed
Approval binds actor, tool/version, target, canonical arguments hash, policy version and expiry. Single-use and rechecked immediately before action.

## ADR-010 S3-compatible artifact store — Proposed
Private objects; DB stores metadata/ACL. Require scanning, signed links and deletion orchestration.

## ADR-011 MCP versions are explicit — Proposed
Pin protocol/SDK and test compatibility. Current 2026-07-28 protocol has major changes; SDK v1 is maintenance line for 2025-11-25, SDK v2 supports 2026-07-28.

## ADR-012 Tor is not MVP — Proposed
Separate, disabled-by-default, credential-isolated worker only after a lawful use case and threat model; never for access-control evasion.

## ADR template fields
Context, drivers, alternatives, decision, consequences, security/privacy impact, migration, rollback and revisit trigger.

## ADR-013 Native desktop driver via Local Desktop Node — Proposed

**Context:** ORBIT requires native computer use, but a cloud worker cannot access the user's logged-in desktop. The upstream `vercel-labs/agent-desktop` project supplies an OS accessibility driver, not an agent, browser or sandbox.

**Decision:** Integrate the upstream driver behind an ORBIT `DesktopDriver` interface, invoked from an optional paired Local Desktop Node. Keep browser automation in Playwright and shell/code in isolated code workers. Use an external pinned CLI first; consider C FFI only after measured need.

**Consequences:** Adds local packaging, pairing, key lifecycle, outbound WSS, lease management, OS permission UX, capability matrix, local stop control, compatibility testing and privacy requirements. It reduces the temptation to place privileged host control inside shared cloud containers.

**Alternatives rejected:** expose the whole upstream MCP command list directly (tool discovery is not authorization); run the node as a system/root service (unnecessary privilege); expose the user's desktop through Docker mounts; reimplement OS-specific accessibility APIs in ORBIT v1; use screenshots/coordinates as the default interaction primitive.

**Security/privacy impact:** high sensitivity; requires explicit consent, exact approvals, least-privilege local process, local policy, no shell strings, ref expiry, delivery dispositions, redaction and audit. Revisit after cross-platform prototype and threat review.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.

## ADR-014 External agent backend abstraction — Proposed

**Context:** Users may bring coding agents or run agents in local, remote, container or cloud environments.  
**Decision:** Define ORBIT-owned `AgentBackend` and normalised event contracts. ACP is an adapter where supported, not the source of ORBIT identity/policy.  
**Consequences:** Backend capability manifests, task-scoped credentials, event replay and workspace transfer controls are required.  
**Rejected:** coupling the product to one external agent interface or allowing backend tool calls to bypass ORBIT authorization.

## ADR-015 Sandbox provider abstraction — Proposed

**Context:** Untrusted repository code and agent tools require stronger boundaries than a browser context or process wrapper.  
**Decision:** Define `SandboxProvider`; use a secure disposable container baseline first. Evaluate OpenSandbox adapter and microVM options after isolation tests.  
**Consequences:** runtime policy, image digests, egress, quotas, secret broker, artifact scanning and lifecycle tests become mandatory.  
**Rejected:** privileged containers, host Docker socket, broad host mounts or direct secret injection into guest environment.

## ADR-016 Constrained generative UI — Proposed

**Context:** Agent output may benefit from task-specific cards, forms, charts and control panels.  
**Decision:** Use ORBIT-owned component/action catalogs with schema validation. Evaluate json-render patterns/package behind a safe renderer.  
**Consequences:** catalog versioning, incremental stream validation, action authorization, accessibility and depth/size limits required.  
**Rejected:** arbitrary model-authored HTML/JS, `eval` or direct UI-to-tool calls.

## ADR-017 Portable skills with compliance gate — Proposed

**Context:** Reusable agent instructions should work across IDE harnesses and be reproducible.  
**Decision:** Support Agent Skills-compatible directories and ORBIT lock metadata, immutable source hashes, license state and permission manifests.  
**Consequences:** skill review/install lifecycle, script sandboxing, compatibility testing and update/revocation support required.  
**Rejected:** unverified global install from arbitrary repositories or executing skill scripts on the host.

## ADR-018 Original ORBIT identity and required attribution — Proposed

**Context:** ORBIT should have original product branding while adopting third-party components.  
**Decision:** Use ORBIT-owned product identity and remove third-party branding from ORBIT-owned UI where not required. Preserve all legally required notices, attribution, trademarks and provenance.  
**Consequences:** brand asset provenance, trademark clearance and third-party notices audit are release gates.  
**Rejected:** deleting upstream copyright/license files or presenting third-party software as original ORBIT-owned code.
