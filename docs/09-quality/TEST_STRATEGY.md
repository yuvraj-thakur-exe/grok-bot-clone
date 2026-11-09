# Test strategy

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Test layers

- Unit: pure domain logic, policy evaluation, state transitions, parsers and routing.
- Integration: PostgreSQL, object store, queue/workflow engine, provider adapters and tool gateway.
- Contract: OpenAPI compatibility, worker message schemas, plugin/MCP manifests.
- E2E: login, task, stream reconnect, tool use, approval, artifacts, cancellation and recovery.
- Security: isolation, injection, SSRF, secret redaction and sandbox boundary.
- Performance: API, streaming, queue delay, browser concurrency, retrieval and cost/task.
- AI eval: versioned task dataset with evidence and safety checks.

## Test data

Use synthetic users/workspaces, fake credentials, deterministic mock providers and controlled web fixtures. No real user credentials or private documents in CI. Mark tests as mock, local integration, staging or production verification.

## Release gates

All critical unit/integration tests and security regression suite pass. Migration upgrade path is tested. No critical/high unresolved vulnerability without documented risk acceptance. E2E smoke tests pass in the target deployment profile. AI eval results are reviewed for safety and material regressions.

## Native desktop quality strategy

A native desktop capability is not covered by browser E2E or API unit tests. Use fake-driver contract tests for CI and dedicated interactive-session OS tests for real AX/UIA/AT-SPI. Test permission denial, session lock, app restart, partial accessibility trees, ambiguous targets, delivery uncertainty and pause/stop. Only declare a platform/capability verified after repeatable real-host evidence.

## ORBIT v0.2 alignment

The v0.2 quality plan adds real interactive OS tests separate from browser/API tests. Cover permission, incomplete trees, stale refs, ambiguous target, unknown delivery and local stop; see `DESKTOP_AUTOMATION_TEST_MATRIX.md`.


## v0.5 reuse conformance testing

For every adapter, test contract conformance against fixtures and a real pinned upstream build. Test cancellation, timeouts, partial failure, duplicate events, secret redaction, usage accounting, workspace isolation and artifact provenance. A repository clone or successful dependency installation is not integration evidence.

