# Data retention and deletion policy (draft)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This document defines the deletion mechanism; exact retention durations require owner/legal decisions before production.

## Data inventory

Identity/profile; workspace and membership; conversations/messages; task execution events; files and derived text; embeddings; browser state; code artifacts; memories; connector credentials; usage events; security/audit events; backups and telemetry.

## Retention principles

- Collect only data needed for product functionality, security, billing or user-requested persistence.
- Set purpose-specific retention rather than one indefinite global retention.
- Default to private workspace data.
- Provide export and delete controls for user content and memory.
- Keep secrets only while required for authorized connector use; support revoke and rotation.
- Minimize telemetry payloads and exclude secrets/content by default.

## Deletion workflow

Authenticate requester -> determine ownership and legal holds -> create durable deletion job -> revoke active sessions/connectors/routines -> delete primary DB rows and objects -> delete chunks/vectors/caches/derived artifacts -> propagate to workers and queued jobs -> apply backup expiration policy -> verify expected counts/checksums -> notify completion. Track failures and retry safely; do not claim complete while derived copies remain in active systems.

## Open policy decisions

Retention period for messages, tasks, artifacts, browser sessions, logs, backups and audit records; handling of legal holds; regional deletion requirements; user export format; organization-admin retention override; model provider retention disclosures. Obtain legal/privacy review before production.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
