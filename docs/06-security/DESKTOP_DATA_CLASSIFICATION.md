# Desktop data classification and redaction

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Data | Default classification | Model exposure | Persistence | Controls |
|---|---|---|---|---|
| Device ID, platform, online state | Operational metadata | Yes, only as needed | Yes | Workspace access checks |
| App/window title | Potentially sensitive | Redacted/limited context | Metadata only by default | Scope filter, length cap |
| Accessibility role/state | Low-to-moderate sensitivity | Yes if task relevant | No raw persistence by default | Bounded nodes and provenance |
| Accessible text/value | Sensitive user content | Only relevant selected nodes | Off by default | PII/secret redaction, short retention |
| Password/secure field | Secret | Never | Never | Drop entirely; do not query value |
| Screenshot | Highly sensitive | Disabled by default | Disabled by default | Separate permission + reason + redaction + expiry |
| Clipboard | Highly sensitive | Disabled by default | Never by default | Separate explicit permission, immediate deletion |
| Driver stderr/trace | May contain app details | No | Redacted bounded diagnostics | Redact before telemetry |
| Approval record | Security-sensitive metadata | No | Yes, minimal audit | Access controls, immutable audit |

Redaction is not perfect. The primary protection is minimize collection, scope observation and keep sensitive capabilities off. Do not promise that an algorithm can detect every secret in screen text.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
