# Technology stack decision matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Concern | Baseline choice | Alternatives / revisit trigger |
|---|---|---|
| Web | Next.js App Router + React + TypeScript | Vite SPA if repo or desktop runtime strongly favors it |
| UI components | Tailwind + accessible component primitives | existing design system if already adopted |
| API | FastAPI + Pydantic | retain existing backend if sound and typed |
| Database | PostgreSQL | managed Postgres; avoid multiple primary DBs in MVP |
| Vector retrieval | pgvector | dedicated vector DB only after measured need |
| Cache | Redis | built-in DB coordination only for very small scale |
| Workflow | Temporal candidate behind `WorkflowRuntime` | evaluate alternatives via recovery prototype |
| Browser | Playwright | use CDP only for justified integration needs |
| Code sandbox | disposable isolated worker; stronger runtime for public workloads | gVisor/Kata/Firecracker based on threat model |
| File storage | S3-compatible / MinIO local | cloud object storage with private access |
| Telemetry | OpenTelemetry | vendor backends via OTLP exporters |
| Local orchestration | Docker Compose | Kubernetes only when multi-host ops justify it |

## Selection rule

Do not replace an existing working component solely to match this table. Audit repository quality, maintenance, migration cost and security first. Every replacement requires an ADR and data migration/rollback plan. The table is a default recommendation, not a rigid mandate.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.

## v0.3 optional integration candidates

- Browser driver: Playwright baseline; evaluate agent-browser as an adapter.
- Generative UI: ORBIT-owned schema/catalog; evaluate json-render.
- Skill format: Agent Skills-compatible `SKILL.md`; evaluate skills CLI only after telemetry/license review.
- External agent: ORBIT `AgentBackend`; ACP adapter for compatible agents.
- Sandbox: Docker isolated profile first; OpenSandbox provider evaluation; microVM later.
- Local development: optional Portless-style named localhost routing, never production ingress.

These are candidates, not approved hard dependencies. Exact versions, license, SBOM and integration tests are release gates.
