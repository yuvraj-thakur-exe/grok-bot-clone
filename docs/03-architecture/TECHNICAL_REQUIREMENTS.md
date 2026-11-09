# Technical Requirements Document (TRD)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Proposed baseline. All exact dependency versions and hosting limits must be confirmed during repository audit.

## Runtime requirements

- Web UI: modern evergreen Chromium/Firefox/WebKit; responsive desktop-first workspace and mobile-compatible review surfaces.
- Backend: supported Python runtime pinned by lockfile; async HTTP and worker processes.
- Frontend: supported Node.js LTS pinned by project tooling; strict TypeScript.
- Persistence: supported PostgreSQL with pgvector extension when retrieval is enabled.
- Workflow: durable execution runtime with persistence and worker recovery.
- Object storage: S3-compatible API with private bucket policy.
- Browser: Playwright-managed browser runtime in isolated worker images.

## Integration requirements

Provider adapters must support streaming, tool calls and structured response modes where available. Search adapters return normalized sources with URL/title/snippet/provider/timestamp. GitHub integration uses least-privilege GitHub App or fine-grained token permissions; clone URLs alone do not authorize repository writes. MCP and OpenAPI connectors are versioned and policy-wrapped.

## Operational requirements

Separate web/API/worker deployment, health/readiness endpoints, structured and redacted telemetry, migrations, object lifecycle policy, backups, graceful shutdown, CI security scans, and resource quotas for browser/code jobs.

## Compatibility policy

Pin all dependencies and containers. Record supported OS, browser versions, database versions, provider API versions, MCP protocol versions and migration notes. Upgrade quarterly or on security need, with contract tests and rollback plan. Avoid floating `latest` images in production.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
