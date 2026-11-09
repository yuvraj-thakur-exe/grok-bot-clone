# Secret management and privacy

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Secret lifecycle

Create -> store encrypted -> grant scoped short-lived access -> use in isolated broker/worker -> redact -> rotate -> revoke -> verify deletion. Secret values are never returned by read APIs. Workers receive only the credential needed for the current connector operation.

## Browser credentials

Persistent browser login is high-risk. Store state encrypted with workspace-bound keys, isolate by user/workspace and optionally by task, support session revocation, and offer a “clear browser data” control. Do not share cookies between unrelated agents or workspaces by default. Never ask users to paste passwords into ordinary chat; use secure credential forms or OAuth.

## Privacy controls

Provide data export, memory inspection, memory deletion, connector revocation, task history controls and configurable retention. Clearly disclose which external model provider receives content. Do not use customer content for training by default. Any future training/feedback use requires explicit policy and consent design.

## Logging

Log event IDs, actor, scope, action, status and timing. Redact authorization headers, cookies, API keys, document bodies and full prompts unless specifically required for opt-in debugging with safeguards. Define retention periods before production.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.


## v0.5 credential path review

All provider and connector credentials are write-only through ORBIT settings and referenced by opaque vault handles. Prefer OS-backed secret storage or envelope encryption with a managed key. Do not copy upstream local plaintext config behavior into ORBIT, even where owner-only file permissions are used. Never pass secrets through prompt text, CLI arguments, environment variables visible to unrelated processes, logs or tool output. Worker-specific secrets are delivered over a short-lived pipe or secret broker and revoked after task completion.

