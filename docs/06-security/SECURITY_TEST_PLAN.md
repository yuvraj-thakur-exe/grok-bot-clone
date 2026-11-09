# Security test plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Run these checks in local CI and staging using synthetic accounts/data:

- Auth bypass, session fixation, CSRF, broken access control and workspace IDOR.
- RBAC and tool-grant regression.
- Approval argument tampering, replay and expiry.
- Prompt injection from web, PDF, repo and MCP tool output.
- Secret leakage in API responses, telemetry, crash dumps and prompts.
- SSRF and redirect/DNS rebinding through browser and URL fetcher.
- Malicious archive, polyglot, large file, parser exploit and path traversal.
- Sandbox network, filesystem and resource isolation.
- Dependency/container image scanning and secret scanning.
- Rate-limit, denial-of-wallet and unbounded agent-loop tests.
- Backup restore, deletion propagation and audit integrity.

Track each finding with severity, exploitability, affected version, remediation owner, due date and retest evidence. External penetration test is a pre-production requirement for public multi-tenant deployment; it is not implied by automated tests.

## Desktop security tests

Add pairing replay, device revocation, WSS identity, lease expiry, local pause, session lock, stale/ambiguous ref, partial observation, unknown-delivery retry refusal, semantic high-risk click, prompt injection from UI, command injection, output cap, screenshot/clipboard denial and cross-workspace device access tests. See `DESKTOP_AUTOMATION_TEST_MATRIX.md`.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
