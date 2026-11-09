# Development workflow

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

1. Read `AGENTS.md`, product scope, relevant architecture docs and open ADRs.
2. Inspect repository status, branches, uncommitted work, package scripts and existing tests.
3. Reproduce the issue or write acceptance criteria before editing.
4. Create a small implementation plan and identify affected layers/contracts.
5. Implement the smallest vertical slice; preserve working behavior.
6. Add unit/integration tests and security/edge-case tests where applicable.
7. Run format, lint, type checks, migrations, tests and build relevant to the change.
8. Inspect `git diff`; remove secrets, debug code, unrelated changes and generated debris.
9. Update docs, API schema and changelog when needed.
10. Report changed files, commands/results, limitations and follow-up risks.

Do not claim tests passed if they were not run. If a dependency/service is unavailable, report exactly what could not be validated and keep mock tests clearly separated from live integration tests.

## Desktop integration workflow

Implement in this order: fake driver and contracts → process runner → local pairing/node shell → WSS/lease lifecycle → read-only capability/observation → activity UI → allowlisted semantic action → approvals → OS E2E. Do not start with physical pointer automation or broad MCP exposure. All changes update ADR-013, API/schema, security docs, tests and feature status.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
