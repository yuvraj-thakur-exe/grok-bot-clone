# Desktop driver error mapping

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Purpose

Normalize upstream driver errors for ORBIT without erasing detail needed for safe recovery. Store the upstream `error.code`, disposition and contract version in a structured field.

| Upstream condition (examples) | ORBIT normalized code | Retry guidance | Recovery |
|---|---|---|---|
| `STALE_REF` | `DESKTOP_STALE_REF` | Do not reuse old ref | Fresh complete observation and reselect target |
| `AMBIGUOUS_TARGET` | `DESKTOP_TARGET_AMBIGUOUS` | Unsafe | Stop; refine scope or ask user |
| `PERM_DENIED` / permission report denied | `DESKTOP_PERMISSION_REQUIRED` | Not by blind retry | User grants OS permission, then reprobe |
| `ACTION_NOT_SUPPORTED` | `DESKTOP_CAPABILITY_UNAVAILABLE` | Unsafe for same operation | Explain limitation; use another approved channel |
| `APP_NOT_FOUND` / `WINDOW_NOT_FOUND` | `DESKTOP_TARGET_NOT_FOUND` | Read-only lookup may be refreshed | Re-list apps/windows; do not pick another app implicitly |
| `TIMEOUT` | `DESKTOP_TIMEOUT` | Depends on disposition and operation | For mutation, treat unknown unless explicit non-delivery |
| `APP_UNRESPONSIVE` | `DESKTOP_APP_UNRESPONSIVE` | Never infer safe retry | Reobserve app; hand off if outcome uncertain |
| `INVALID_ARGS` / `POLICY_DENIED` | `DESKTOP_ACTION_DENIED` | No execution if explicit not-delivered | Correct schema/policy; do not mutate arguments after approval without reapproval |
| Malformed output / unsupported contract | `DESKTOP_DRIVER_PROTOCOL_INVALID` | Unsafe | Stop mutation; collect redacted diagnostics and check compatibility |
| Node unavailable / lease expired | `DEVICE_UNAVAILABLE` / `LEASE_EXPIRED` | No action accepted | Re-pair/reconnect/issue new lease; fresh snapshot required |

## Mapping contract

- Do not map solely by message strings; use upstream code and structured disposition.
- Preserve original code, details, suggestion, delivery and retry in a nested `driver_error` field with redaction.
- Never manufacture `retry=safe` if missing. Missing disposition on a mutating result becomes `delivery=unknown, retry=unsafe`.
- Preserve distinction between “no permission”, “unsupported” and “unknown”.
- Ensure error code mapping is versioned and tested against recorded JSON fixtures.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
