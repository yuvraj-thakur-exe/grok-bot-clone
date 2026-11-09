# Operations runbooks index

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Maintain an executable runbook for: API unavailable; database unavailable; workflow engine backlog; browser worker pool exhausted; provider outage/rate limit; object store failure; queue poison task; suspected credential compromise; cross-tenant access report; runaway routine; failed migration; restore/rollback; user data deletion failure.

Each runbook includes symptoms, dashboard/query, severity, immediate containment, diagnosis, safe recovery, escalation owner, communication guidance and verification commands. Record actual command output during incident drills; do not leave generic “restart service” as the only response.

## Desktop node runbooks

Use `DESKTOP_NODE_RUNBOOK.md` for offline nodes, permission denial, contract mismatch, unknown action delivery, unexpected UI action and desktop-content exposure. Never recover by blindly replaying a mutating command.

## ORBIT v0.2 alignment

The v0.2 operations plan adds node offline, permission, driver version, unknown delivery and desktop data exposure runbooks. Never replay an uncertain mutation; see `DESKTOP_NODE_RUNBOOK.md`.
