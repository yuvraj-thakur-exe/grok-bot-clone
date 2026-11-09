# Human approval policy

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Approval-required action classes

By default, require explicit user approval before: sending external messages; publishing; purchases or financial actions; deleting/overwriting important data; changing account permissions; deploying production; accepting terms/legal representations; changing security controls; or accessing a newly connected sensitive resource.

## Approval object

An approval record contains actor, workspace, task, tool/action, target, canonical argument hash, policy version, risk summary, requested scope, expiry, and decision. The approval UI shows the exact action, destination/target, data to be sent or changed, and expected side effect.

## Binding and invalidation

Approval is valid only for the exact canonical action hash and target. Any payload, recipient, amount, URL, permission or policy change invalidates approval. Expired, revoked, replayed or cross-workspace approvals are rejected.

## No blanket approval by default

Do not present an “approve every action” default. Narrow reusable grants require explicit scope, expiry, revocation and audit. CAPTCHA, MFA and human-verification flows must pause for the user; do not bypass them.

## Desktop action approvals

Approval is semantic, not merely command-based. A click can be a high-impact action when the target is “Send”, “Delete”, “Purchase”, “Publish”, “Deploy”, permission grant or account/security setting. Exact approval binds workspace, task, node, desktop session, app/window context, operation, target evidence, normalized arguments hash, policy version, actor and expiry. Any changed binding invalidates approval. Critical financial/legal/security operations are blocked from generic desktop tool use unless a separate explicit product flow is approved.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
