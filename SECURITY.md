# Security policy

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

ORBIT is a planned AI agent workspace. Its security design treats models, public skills, upstream dependencies, web pages, attachments, connector events and tool outputs as untrusted unless independently validated.

## Reporting vulnerabilities

Do not publish exploit details or credentials in public issues. Use the private vulnerability reporting mechanism of the repository hosting service or the project's designated private contact when one is configured. Include affected version/commit, reproduction steps, impact and a proposed mitigation. Do not include user data or secrets.

## Security boundaries

- Models propose actions; deterministic policy authorizes tools.
- Browser, native desktop, remote desktop and code sandbox are separate trust domains.
- Untrusted skills/plugins must not execute in the main application process.
- External side effects require exact approval and audit.
- Secrets must be stored in an approved vault and redacted from prompts, logs and telemetry.
- Upstream dependencies must be pinned, scanned, license-reviewed and represented in an SBOM.
- OpenMausBot `enterprise/` is excluded from ORBIT source acquisition and reuse unless separately licensed in writing.

## Response expectations

Triage severity and affected assets, disable/rollback vulnerable components, rotate exposed credentials, preserve minimal investigation evidence, update dependencies and tests, and communicate user impact according to the incident policy. Do not claim production readiness before security review and recovery validation.
