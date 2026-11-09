# Security requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

- Enforce authentication and workspace authorization server-side on every resource and tool call.
- Separate planning from tool execution. Models never receive raw infrastructure credentials.
- Store secrets in a secret manager or encrypted credential broker; never in prompts, source, database plaintext or logs.
- Encrypt transport and sensitive stored data; define key rotation and recovery.
- Validate and normalize every tool input; cap body, file, archive, URL, runtime and output sizes.
- Use CSRF protection, secure cookies, CSP, safe CORS, rate limits and abuse monitoring.
- Keep audit trail for privileged actions, approvals, connector changes and execution runs.
- Run dependency, container and secret scans in CI; produce an SBOM before public release.
- Back up and regularly restore database plus object storage.
- Have a security contact and incident response process before public launch.

Security baseline does not constitute a compliance certification. Do not claim SOC 2, ISO 27001, GDPR compliance or penetration-test completion without evidence and appropriate review.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
