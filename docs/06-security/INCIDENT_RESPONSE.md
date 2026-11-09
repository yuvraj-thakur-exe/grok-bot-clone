# Incident response plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Severity

- SEV-1: confirmed cross-tenant exposure, credential compromise, remote code execution, or widespread destructive action.
- SEV-2: material security issue affecting a bounded user/workspace or service outage.
- SEV-3: contained defect with limited impact and no evidence of data exposure.

## Response sequence

1. Detect and declare incident; assign incident lead.
2. Contain: revoke keys/tokens, pause affected workers/routines, disable connector/tool or isolate service.
3. Preserve evidence: audit events, task IDs, hashes, relevant logs; avoid collecting excess personal data.
4. Assess scope and affected tenants/data.
5. Eradicate root cause and rotate compromised credentials.
6. Recover from known-good state; verify integrity and permissions.
7. Notify affected parties and authorities as required by applicable law and counsel.
8. Publish internal postmortem with timeline, root cause, impact, actions and owners.

## Preparedness

Maintain on-call ownership, secret revocation runbooks, backup restore procedure, status communication template and contact list. Run tabletop exercises before production launch. Do not promise notification timelines until legal obligations and incident facts are known.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
