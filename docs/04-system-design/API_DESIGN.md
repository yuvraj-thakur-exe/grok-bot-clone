# API design

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Style:** REST for resource lifecycle and commands; SSE for streaming task events; WebSocket only where bidirectional low-latency interaction is justified (e.g. live computer session control). OpenAPI is the contract source. API versions are explicit (`/api/v1`).

## Resource groups

| Group | Routes (illustrative) | Notes |
|---|---|---|
| Auth | `/auth/*`, `/me` | OIDC/session lifecycle; never expose tokens in logs |
| Workspaces | `/workspaces`, `/workspaces/{id}` | membership and role checks |
| Agents | `/workspaces/{id}/agents` | versioned config and tool grants |
| Conversations | `/workspaces/{id}/conversations` | paginated message history |
| Tasks | `/workspaces/{id}/tasks`, `/tasks/{id}` | idempotent create, cancel, retry |
| Events | `/tasks/{id}/events` | SSE with cursor/sequence replay |
| Approvals | `/approvals/{id}`, `/approvals/{id}/decision` | exact action binding and expiry |
| Artifacts | `/artifacts/{id}`, `/artifacts/{id}/download` | short-lived signed links |
| Providers | `/provider-configs`, `/models` | secret refs never returned |
| Skills | `/skills`, `/skills/{id}/versions` | reviewed immutable versions |
| Routines | `/routines`, `/routines/{id}/runs` | schedule controls and history |
| Connectors | `/connectors`, `/connectors/{id}/authorize` | OAuth consent, scoped grants |
| Research | `/research/jobs`, `/research/jobs/{id}/report` | source manifest and citations |

## Contract requirements

- Request and response schemas are typed and validated with Pydantic.
- All mutations accept `Idempotency-Key` where retries could duplicate side effects.
- Every tenant-scoped request resolves workspace membership from authenticated identity, not a trusted body field.
- Errors use a stable envelope: `code`, `message`, `request_id`, optional field errors. Do not return stack traces.
- Paginate collections with opaque cursors; define max page size.
- SSE events include `id`, `event`, and typed JSON `data`; clients reconnect with `Last-Event-ID`.
- Use optimistic concurrency (`ETag`/version) for mutable agent, skill, and routine settings.
- OpenAPI schema changes require compatibility checks and generated-client tests.

## API versioning

Additive optional fields are normally non-breaking. Removing fields, changing semantics, or tightening validation requires deprecation and a version strategy. Internal worker messages are separately versioned from public REST contracts.

## v0.2 desktop control resources

Add device pairing/status/revocation, capability-report, lease lifecycle, observation, single-action, and task desktop-event resources. See `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md` and `API_CONTRACTS.yaml` for draft paths and schemas.

The Local Desktop Node uses authenticated outbound WSS, not a public inbound endpoint. Public REST endpoints create/revoke pairing and leases; internal broker messages are authenticated, lease-bound and replay-resistant. Tool requests use fixed enum operations and schemas, never arbitrary command strings. The API's approval resource binds an exact normalized action to policy version, device/session and expiry.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
