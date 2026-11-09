# Technology Research and Recommendations

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Review date:** 08 November 2026. Re-check release/version compatibility before implementation.

## Frontend

Use Next.js App Router, React and TypeScript. Official App Router docs describe filesystem routing and React features such as Server Components and Suspense. Keep streaming chat/task panels interactive while using server rendering where useful. Do not put secrets or tool execution in client components.

## Backend and jobs

Use FastAPI + Pydantic for typed async APIs and Python AI ecosystem integration. FastAPI docs distinguish small post-response tasks from heavy jobs that should run in separate workers/queue infrastructure. ORBIT's long-running work must not depend on in-process request tasks.

## Durable workflows

Evaluate Temporal behind an internal workflow interface. Its docs describe durable workflow executions using recorded event history that can recover after infrastructure failures. This fits long-running research, browser sessions, approval waits and retryable steps. Keep nondeterministic model/API calls in workflow activities, with idempotency and reconciliation.

## Browser automation

Use Playwright. Browser contexts isolate storage state such as cookies and local storage. Use an isolated context per workspace/task policy. Context isolation alone is not host/network isolation; use separate worker process/container and egress controls too.

## Data and telemetry

PostgreSQL is authoritative persistence; pgvector can support ACL-filtered project retrieval. Redis is cache/rate limiting/ephemeral coordination, not sole task state. S3-compatible storage holds files/artifacts. OpenTelemetry provides vendor-neutral traces, metrics and logs; redact secrets and prompt content.

## MCP version warning

The 2026-07-28 MCP specification introduces a stateless core, request metadata, header-based routing, caching hints, authorization hardening and extensions. Official TypeScript SDK docs state v1 implements the 2025-11-25 specification and v2 supports 2026-07-28. Do not copy stale MCP examples or assume old package names; pin a supported protocol/SDK line and add compatibility tests.

## Sandboxing

Docker rootless mode runs daemon/containers as non-root using user namespaces. It is useful defense-in-depth, not proof that arbitrary hostile code is safely sandboxed. Before public multi-tenant execution, evaluate gVisor, Firecracker microVMs or Kata Containers, per-job credentials and restricted egress.

## Security frame

OWASP LLM application risks relevant to ORBIT include prompt injection, insecure output handling, sensitive data disclosure, insecure plugin design and excessive agency. Convert each into implemented controls and tests; prompt instructions alone are insufficient.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
