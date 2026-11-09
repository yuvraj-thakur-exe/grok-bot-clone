# Desktop control API and data contract

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## API principles

The desktop API is a remote control plane for a device the user owns. It is not a generic arbitrary-command proxy. All routes require authentication, workspace authorization, device ownership and audit context.

## Proposed endpoints

| Method | Route | Purpose |
|---|---|---|
| POST | `/workspaces/{workspace_id}/desktop-devices/pairing-sessions` | Create short-lived pairing challenge |
| POST | `/desktop-pairing/{pairing_id}/complete` | Complete device pairing from the local node |
| GET | `/workspaces/{workspace_id}/desktop-devices` | List paired devices and capabilities |
| GET | `/desktop-devices/{device_id}` | Device status, key fingerprint, last seen, platform |
| DELETE | `/desktop-devices/{device_id}` | Revoke device; invalidate leases |
| POST | `/desktop-devices/{device_id}/capability-reports` | Submit bounded capability/permission report |
| POST | `/tasks/{task_id}/desktop-leases` | Request scoped execution lease |
| POST | `/desktop-leases/{lease_id}/renew` | Renew valid lease |
| DELETE | `/desktop-leases/{lease_id}` | Release/stop lease |
| POST | `/desktop-leases/{lease_id}/observations` | Request a fresh native snapshot |
| POST | `/desktop-leases/{lease_id}/actions` | Request one allowlisted desktop action |
| GET | `/tasks/{task_id}/desktop-events` | Subscribe to device/action timeline (SSE) |

Pairing must be rate limited, short-lived, single-use and protected against CSRF/replay. Complete pairing only after local confirmation and identity proof.

## Desktop action request

```json
{
  "action_id": "uuid",
  "snapshot_id": "s_opaque",
  "target_ref": "@opaque_snapshot:e7",
  "operation": "click",
  "arguments": {},
  "intent": "open_navigation_item",
  "expected_postcondition": {
    "kind": "surface_present",
    "surface": "dialog"
  },
  "idempotency_key": "uuid-or-random-opaque"
}
```

Reject unknown fields. `operation` is a fixed enum, not a raw command string. `intent` is derived or checked by server policy; model-supplied intent is advisory only. Server recomputes risk using target text/role/context and registered operation metadata. The client cannot self-declare an action harmless.

## Action receipt

```json
{
  "action_id": "uuid",
  "status": "completed",
  "operation": "click",
  "delivery": "delivered_unverified",
  "retry": "unsafe",
  "verification": {
    "status": "not_yet_verified",
    "scope": null
  },
  "driver": {
    "name": "agent-desktop",
    "package_version": "1.2.0",
    "contract_version": "2.6"
  },
  "observed_at": "2026-11-08T00:00:00Z",
  "redacted_evidence_ref": null
}
```

The example versions reflect upstream repository metadata observed on review date, not a permanently pinned ORBIT dependency. The implementation must record the exact release and commit actually installed.

## Delivery enum

- `not_delivered`: evidence says the operation did not reach the application.
- `delivery_uncertain`: it may have reached the application; outcome cannot be established.
- `delivered_unverified`: dispatched; the relevant postcondition was not verified.
- `delivered_verified`: the named UI-level postcondition was read back successfully.
- `unknown`: insufficient evidence to classify.

Only a driver response that explicitly establishes safe retry may enable automatic retry. Missing or malformed disposition is treated as `unknown` and unsafe. `delivered_verified` does not prove remote server persistence or business completion; verification scope must say exactly what was observed.

## Error envelope

Errors expose stable machine-readable `code`, `message`, `retry`, `delivery`, optional `details`, a bounded `suggestion` and a correlation ID. Do not branch policy on prose. Do not return stack traces, secrets, raw clipboard data or unredacted UI snapshots to clients by default.

Recommended codes: `DEVICE_UNAVAILABLE`, `DEVICE_REVOKED`, `LEASE_EXPIRED`, `SESSION_NOT_INTERACTIVE`, `DESKTOP_PERMISSION_REQUIRED`, `CAPABILITY_UNAVAILABLE`, `STALE_REF`, `TARGET_AMBIGUOUS`, `OBSERVATION_INCOMPLETE`, `ACTION_NOT_ALLOWED`, `APPROVAL_REQUIRED`, `APPROVAL_EXPIRED`, `ACTION_DELIVERY_UNKNOWN`, `DRIVER_VERSION_UNSUPPORTED`, `DRIVER_PROTOCOL_INVALID`, `DESKTOP_RATE_LIMITED`.

## Data model additions

| Entity | Important fields | Retention/notes |
|---|---|---|
| `desktop_devices` | id, user_id, workspace_id, public_key_fingerprint, platform, platform_version, status, created_at, last_seen_at, revoked_at | Device registry, minimal metadata |
| `desktop_sessions` | id, device_id, session_generation, interactive_state, capability_report_id, started_at, ended_at | Avoid storing OS session secrets |
| `desktop_capability_reports` | id, device_id, driver_version, contract_version, platform, capabilities JSONB, permission_state JSONB, reported_at | Latest report pointer; store history with bounded retention |
| `desktop_leases` | id, task_id, workspace_id, device_id, session_id, capability_scope JSONB, policy_version, expires_at, revoked_at | Short-lived; enforce single mutating lease per session |
| `desktop_action_records` | id, task_id, lease_id, action_id, operation, target_context_hash, args_hash, approval_id, delivery, retry, verification_scope, created_at | Do not store raw refs as durable IDs |
| `desktop_observation_artifacts` | id, task_id, lease_id, snapshot_id, completeness, redacted_payload_uri, payload_hash, expires_at | Off by default; redacted and short retention |

All tables require workspace ownership checks, foreign keys, indexes, deletion/retention strategy and audit events. Use application-level RLS or equivalent defense-in-depth; never trust a client-supplied workspace ID without verifying membership.

## Event types

`desktop.device.paired`, `.online`, `.offline`, `.revoked`, `desktop.session.started`, `.paused`, `.stopped`, `desktop.lease.issued`, `.renewed`, `.expired`, `desktop.observation.completed`, `.partial`, `desktop.action.requested`, `.approval_required`, `.approved`, `.denied`, `.completed`, `.delivery_unknown`, `desktop.verification.completed`, `.failed`.

Events are append-only audit facts. Client reconnect uses `Last-Event-ID` or cursor and must not replay actions.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
