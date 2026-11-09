# Screen specifications

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Screen | Required behavior | Critical states |
|---|---|---|
| Workspace home | recent tasks, create task, workspace status | empty, loading, permission denied |
| Chat/task | streaming messages, attachments, citations, plan, task timeline | queued, running, needs approval, failed, cancelled |
| Task detail | ordered steps, tool events, approvals, artifacts, retry/cancel | replay/reconnect, partial result |
| Agent editor | role/instructions, model policy, tool grants, test run | validation, unsaved, incompatible model |
| Research workspace | query plan, source list, evidence and report | source blocked, stale source, conflict |
| Files | upload, parse/index status, preview, collection search | quarantine, unsupported, parse failure |
| Skills | manifest, version, permissions, test results | untrusted import, failed validation |
| Routines | trigger, timezone, policy, next run, run history | paused, missed, repeated failure |
| Connectors | auth consent, declared scopes, health, revoke | expired token, partial scope |
| Settings/privacy | memory, retention, exports, provider and security preferences | export/delete in progress |

Do not ship buttons without real handlers. Every screen needs responsive layouts and keyboard-accessible primary actions. Detailed wireframes are implementation artifacts and must be created only after validating the existing app shell if one exists.

## ORBIT v0.2 alignment

The v0.2 experience adds explicit device pairing, visible desktop activity and immediate stop/pause. Show action delivery separately from UI verification; see `DESKTOP_ACTIVITY_PANEL.md`.
