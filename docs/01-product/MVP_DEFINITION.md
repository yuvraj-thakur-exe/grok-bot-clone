# MVP Definition

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Outcome:** a user can create a workspace, have persisted streaming chat through a configured provider, start a bounded research/file task, inspect task status, citations and artifacts, and trust that tools/permissions/history are recorded.

## P0
Repo foundation and CI; auth/workspace isolation; Postgres migrations; object storage; one live provider and deterministic mock; provider/capability abstraction; streaming/cancel/error states; durable task/event lifecycle; tool registry and default-deny policy; audit/idempotency/budgets; read-only search/page extraction and source evidence; safe file upload/parse/Q&A; task timeline and artifacts; unit/integration/E2E tests.

## P1
Isolated Playwright browser worker; read-only browser tasks; approval-gated forms; disposable Git/code sandbox; memory CRUD/provenance; testable skills; manual scheduling.

## P2
Event routines, bounded multi-agent, MCP/OAuth connectors, plugin/skill registry, voice and multimodal.

Static mock UI, in-memory task state, invented citations or a prompt-only fake tool system are not MVP substitutes.

## v0.2 MVP scope decision: desktop is not core MVP

Native desktop control is **not** part of the first ORBIT MVP. First establish the authenticated task/chat foundation, provider adapter, durable execution, tool gateway, research/files and isolated browser/code workers. Then introduce a read-only Local Desktop Node prototype as a separate beta milestone. Semantic desktop mutation remains disabled until pairing, local policy, leases, approvals, delivery-aware recovery and interactive OS tests are complete. This ordering avoids turning an unfinished agent into a remote-control product.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.

## v0.3 scope clarification

The following remain post-MVP or optional: external ACP agent backends, generative UI runtime, skill marketplace/installer, OpenSandbox integration, Firecracker microVM pools, native desktop control, Portless-style developer routing and multi-agent company dashboard. The initial MVP must first prove a single agent can safely complete and recover a task with durable state, policy-controlled tools, cancellation, audit and tests.
