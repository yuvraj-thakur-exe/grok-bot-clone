# Definition of Done

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

A feature is Done only when:

- It satisfies linked requirement IDs and acceptance criteria.
- Its user-visible success, loading, empty, error and cancellation states work.
- Authorization and policy are enforced server-side.
- Inputs/outputs are validated and sensitive data is redacted.
- Unit and relevant integration/E2E tests pass.
- Failure, retry and recovery behavior is defined.
- Telemetry and audit events are added where needed.
- Documentation, config examples and API contracts are updated.
- No fake button, placeholder integration or misleading completion claim remains.
- A reviewer can reproduce the validation from documented commands.

## Desktop-specific Definition of Done

- Paired node and short-lived lease are workspace/task/session bound.
- Local stop/pause, revocation and disconnect behavior are tested.
- Driver release and contract version are pinned and verified.
- Every mutation is allowlisted, authorized, approval-gated as required and audited.
- Fresh snapshot and delivery disposition are respected; no blind retry.
- Raw desktop content is not logged and retained artifacts have expiry/deletion tests.
- Dedicated platform integration evidence exists for each advertised OS/action.

## ORBIT v0.2 alignment

The v0.2 quality plan adds real interactive OS tests separate from browser/API tests. Cover permission, incomplete trees, stale refs, ambiguous target, unknown delivery and local stop; see `DESKTOP_AUTOMATION_TEST_MATRIX.md`.
