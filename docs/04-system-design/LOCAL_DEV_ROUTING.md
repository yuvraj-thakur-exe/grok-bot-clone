# Local development routing

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Purpose

Provide stable, named local URLs for frontend, API, docs, mock providers and callback services across multiple worktrees. This is developer tooling, not part of production ingress.

## Requirements

- Localhost-only bind by default; reject wildcard/LAN bind unless explicitly configured.
- Stable service label tied to repository/worktree identity.
- Conflict detection and process ownership; do not kill another process without explicit approval.
- TLS CA installation is opt-in, explained and reversible. Never silently modify system trust stores.
- OAuth redirect allowlists must use the actual local callback host and environment-specific client registrations.
- Avoid exposing local admin/debug endpoints to LAN or the public Internet.

## Portless evaluation

`vercel-labs/portless` can be evaluated as a developer convenience because it routes stable `.localhost` names to dynamic dev server ports. It must remain optional, pinned and replaceable. Its local CA/trust behavior is a privileged operation that requires explicit developer consent. Do not use it as ORBIT's production proxy or tenant isolation mechanism.
