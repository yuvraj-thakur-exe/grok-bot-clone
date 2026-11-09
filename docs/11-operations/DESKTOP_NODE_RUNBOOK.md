# Desktop Node operations runbook

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Device offline

1. Check `last_seen_at`, node version and broker heartbeat.
2. Check whether the local app is paused or user has logged out/locked screen.
3. Confirm WSS/TLS and proxy connectivity; do not open inbound firewall ports.
4. Expire leases and resume tasks only after a fresh device health check.
5. Never mark interrupted action as failed/not-delivered without evidence.

## Permission denied

1. Report exact permission required and affected capability.
2. Direct user to the OS privacy settings or supported permission guide.
3. Do not request admin elevation or attempt permission bypass.
4. Re-run capability discovery after user grants permission; update capability report.

## Driver contract mismatch

1. Stop all mutations for that node version.
2. Record driver package version, JSON contract version, OS version and error code.
3. Check compatibility matrix and pinned artifact checksum.
4. Roll back or update through signed package path; run contract self-test.

## Unknown action delivery

1. Do not replay the original mutation.
2. Re-observe the target app/window using a fresh snapshot.
3. Verify intended postcondition and any side effect.
4. If unclear or consequential, stop and request user review.
5. Record the unknown disposition and recovery decision.

## User reports unexpected click or action

1. Pause node and revoke active lease if needed.
2. Preserve audit metadata, not raw desktop content by default.
3. Identify exact approved action hash and tool/driver version.
4. Check semantic intent classifier, target identity, approval context and delivery receipt.
5. Treat possible unauthorized action as security incident and follow `docs/06-security/INCIDENT_RESPONSE.md`.

## Data exposure

If screenshots, clipboard text, raw accessibility trees or credentials entered telemetry/storage unexpectedly: pause collection, restrict access, assess retention and recipients, purge according to incident/legal process, rotate affected credentials, and document the incident.

## ORBIT v0.2 alignment

The v0.2 operations plan adds node offline, permission, driver version, unknown delivery and desktop data exposure runbooks. Never replay an uncertain mutation; see `DESKTOP_NODE_RUNBOOK.md`.
