# Acceptance Criteria

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Chat:** message accepted once; stream chunks ordered and final result persisted; refresh restores messages; cancel stops supported generation; provider failure is explicit.

**Tools:** all invocations through gateway; invalid schema rejected; policy denial causes no execution; high-risk call requires unexpired exact-payload approval; audit identifies actor/workspace/tool/decision/result with redaction.

**Research:** each cited claim maps to stored evidence; source URL/metadata/fetch time persist; unsupported/conflicting claims are labeled or omitted.

**Browser:** context isolation per policy; no API secrets/host files exposed; visible action/status; pause for CAPTCHA/MFA/human checks.

**Code:** disposable sandbox only; no Docker socket/host home mount; attach diff and test output; push/PR is separate permissioned action.

## Native desktop acceptance (future milestone, not first MVP)

- Device pairing is explicit, expiring, single-use and revocable; local node uses outbound authenticated WSS and exposes no inbound listener.
- Local node only runs in the signed-in graphical session and presents active task + immediate pause/stop control.
- Cloud and local policy both authorize every action; lease is workspace/task/device/session-bound and expires.
- Driver version, JSON contract, OS capabilities and permissions are visible and verified at runtime.
- Read-only observations are bounded and redacted; incomplete snapshots cannot prove absence.
- Mutations use allowlisted typed operations, fresh snapshot refs, semantic risk classification, exact approvals where needed, a single action and fresh post-observation.
- Stale/ambiguous target or unknown delivery never triggers a blind retry.
- Cross-platform tests pass on dedicated interactive sessions before a platform is labelled supported.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.
