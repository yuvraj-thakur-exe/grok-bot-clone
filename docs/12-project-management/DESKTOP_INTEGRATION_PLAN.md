# Desktop integration work plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Epic DSK-EPIC-01: Reference and contracts

- DSK-001: Pin source research to a commit, package version and contract version.
- DSK-002: Approve license, dependency and supply-chain review.
- DSK-003: Define `DesktopDriver`, `FakeDesktopDriver` and normalized data contracts.
- DSK-004: Build fixtures for success, partial, stale, ambiguous, timeout and delivery uncertainty.

## Epic DSK-EPIC-02: Local Desktop Node

- DSK-010: Device pairing and OS-secure key storage.
- DSK-011: Outbound WSS and mutual authentication.
- DSK-012: Lease issue/renew/revoke/expiry.
- DSK-013: Local pause/stop and one mutation lock.
- DSK-014: Pinned subprocess runner and process cancellation.
- DSK-015: Capability/permission discovery and status UI.

## Epic DSK-EPIC-03: Read-only desktop observation

- DSK-020: `status`, `permissions`, `list-apps`, `list-windows`.
- DSK-021: `snapshot`, `find`, `get`, `is` with output caps and redaction.
- DSK-022: Evidence tri-state and partial observation policy.
- DSK-023: Desktop event timeline and user-visible activity panel.

## Epic DSK-EPIC-04: Safe semantic actions

- DSK-030: Strict allowlist and argument schemas.
- DSK-031: Action risk classifier and exact approvals.
- DSK-032: Click/set-value/check/uncheck/scroll one by one.
- DSK-033: Delivery disposition and post-action observation.
- DSK-034: No retries for unknown or uncertain delivery.

## Epic DSK-EPIC-05: Platform readiness

- DSK-040: macOS lab, TCC and screen capture tests.
- DSK-041: Windows UIA interactive session and integrity tests.
- DSK-042: Linux AT-SPI/X11/Wayland tests.
- DSK-043: Docs, installer, signed updates and rollback.

## Entry criteria

- Existing ORBIT repository audited.
- Core task/auth/policy model exists or is designed with migration path.
- Threat model and user consent UX approved.
- Fake driver contract tests pass before any native actions are enabled.

## Exit criteria

- Device can pair/revoke; leases expire correctly; node can pause/stop.
- Read-only observation is stable with explicit complete/partial state.
- Semantic actions have exactly-once-or-unknown handling, approvals and audit.
- Tests cover stale refs, ambiguity, disconnects, injection, data minimization and OS capability differences.
- Feature status is updated with evidence; no platform marked supported from a demo alone.

## ORBIT v0.2 alignment

The v0.2 roadmap adds a gated desktop workstream after core auth, durable tasks and policy gateway. See `DESKTOP_INTEGRATION_PLAN.md`; desktop is not the first MVP path.
