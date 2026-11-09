# Integration architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

All external systems connect through an integration gateway. Product modules depend on internal interfaces and normalized schemas, not directly on vendor SDKs.

## Integration classes

- Model providers: inference, streaming, capability metadata, usage and health.
- Search providers: query, result normalization, source metadata and quotas.
- GitHub: repository selection, metadata, contents, branches and PR workflows.
- MCP: remote/local tool discovery and invocation under scoped permission manifests.
- OpenAPI/custom tools: generated contracts reviewed before registration.
- Storage: S3-compatible artifacts and upload/download operations.

## Common lifecycle

Discover -> user consent -> validate scopes/manifest -> store credential in secret broker -> connectivity test -> use from isolated worker -> audit -> rotate/revoke -> delete connector data. A failed or expired credential disables dependent operations and causes tasks to pause safely.

## Network controls

Use an outbound egress proxy or controlled network layer for browser/fetch/connector workers. Allowlist destination hosts by integration/task policy where practical. Revalidate redirects and resolved addresses. Do not let arbitrary MCP servers inherit broad network or filesystem privileges.

## Versioning

Pin vendor API and MCP protocol versions. Normalize provider errors/events internally. Store connector manifest version and granted permission version on invocations to support audit and reproducibility.

## v0.2 desktop integration

The upstream `agent-desktop` MCP stdio server may be used by developers locally, but production agent tools are exposed through ORBIT's curated policy gateway. ORBIT's broker connects to paired nodes over outbound authenticated WSS. Do not expose the full upstream dynamic command list, and do not treat MCP discovery as authorization. Version the driver and JSON output contract independently.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.

## v0.3 integration boundaries

Additional adapters are described in `REFERENCE_ECOSYSTEM_ANALYSIS.md`: `BrowserDriver`, `AgentBackend`, `SandboxProvider`, `SkillRegistry`, `UISpecEngine` and `LocalDevelopmentRouter`. Keep each optional and replaceable. ORBIT's identity, workflow state, policy, approval, audit and artifact ownership remain central.
