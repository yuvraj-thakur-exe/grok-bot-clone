# Authentication and authorization

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Authentication

Use a maintained OIDC provider/library. For a self-hosted MVP, support a secure email/password or local auth mode only if password hashing, verification, reset, session rotation, and abuse controls are implemented. Prefer OIDC for production deployments. Browser sessions use secure, HTTP-only, SameSite cookies; state-changing requests receive CSRF protection. API tokens are scoped, hashed at rest, revocable, and shown only once.

## Authorization model

RBAC at workspace level plus capability grants at tool level:

- `owner`: workspace lifecycle, membership and billing configuration.
- `admin`: manage agents, connectors, routines and workspace policy.
- `member`: create tasks and use approved resources.
- `viewer`: read-only access.

Every tool invocation is checked against: authenticated actor, workspace membership, agent grant, tool risk class, resource scope, policy version, and approval status. Backend services must not infer trust from a frontend-hidden button.

## Service identities

Workers use short-lived workload identity or narrowly scoped service credentials. A browser worker gets access only to its assigned task session. It does not receive database superuser credentials or all connector secrets.

## Session and account safety

Rotate session identifiers after authentication and privilege changes. Enforce logout/revocation. Rate-limit login, password reset, token creation, and expensive tasks. Record security-relevant changes in audit events. Avoid account enumeration in public errors.

## Acceptance tests

- Workspace A cannot read/write Workspace B resources by guessing IDs.
- Viewer cannot create tasks or modify agents.
- Revoked connector tokens are unusable by queued tasks.
- An expired approval cannot authorize an action.
- A task launched by one member cannot elevate its own role.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
