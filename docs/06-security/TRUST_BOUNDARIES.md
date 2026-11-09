# Trust boundaries and data classification

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Data classes

- Public: intentionally public docs and source code.
- Internal: product configuration, non-public plans, task metadata.
- Confidential: user uploads, conversation content, code repositories, memory.
- Secret: API keys, OAuth refresh tokens, cookies, encryption keys, signing keys.

## Boundary rules

Models may receive only context authorized for the task and provider. Hosted model providers are external processors; routing must honor workspace privacy settings. Browser workers receive one isolated session at a time. Code workers receive a task-specific workspace snapshot, not host filesystem access. Plugins receive only declared data and scopes. Logs exclude secret and confidential payloads by default.

## Untrusted inputs

Treat user prompts, web pages, emails, PDFs, repository files, tool outputs and MCP responses as untrusted data. They do not change system policy. The system must label provenance and prevent data from one tenant entering another tenant's context.

## Data-flow review

Any new connector, provider, storage bucket, telemetry exporter or worker network path requires a data-flow review and update to this document before production.

## v0.2 desktop boundary

The user-owned OS session is outside the cloud control plane trust boundary. The Local Desktop Node is a separately authenticated endpoint with a local policy gate. Cloud policy alone is insufficient; node policy alone is insufficient. Both must permit. Do not mount desktop sockets, clipboard, home directories or privileged devices into shared workers. All UI text is untrusted input crossing from an external application into the model context.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
