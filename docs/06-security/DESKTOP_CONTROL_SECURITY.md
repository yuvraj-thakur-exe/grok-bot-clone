# Desktop control security and privacy specification

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Threat model additions

Assets: device identity, desktop session, OS accessibility permissions, visible user content, clipboard, screenshots, open files, authenticated app sessions, task data, approvals and driver integrity.

Threat actors: prompt-injected web/UI content, malicious or compromised agent/model, compromised control plane, malicious plugin/MCP server, malicious repository, compromised Local Desktop Node/package, another local OS user, stolen device key and accidental user misclick.

## Required controls

### Device identity and pairing

- Use one-time, expiring, single-use pairing challenge shown by both control plane and local node.
- Bind public key to user + workspace; key private material stored in OS keychain/credential store where supported.
- Mutual authentication for node control channel; TLS certificate validation and replay-resistant request signing/nonces.
- Device revocation immediately rejects future tasks and invalidates leases.
- Do not expose an unauthenticated HTTP listener. Outbound-only WSS is the default network topology.
- Avoid storing long-lived provider credentials on the node.

### Local execution

- Fixed absolute executable path; pinned version + checksum/signature verification at install/update.
- Fixed CLI command allowlist; typed input schema; deny arbitrary args/subcommands.
- `execFile`/argument array only; never shell parsing.
- Timeout, output cap, process-tree cancellation, concurrency limit and private temp directory.
- Validate JSON envelope, version and required disposition fields; malformed responses become `unknown` and action stops.
- Local policy runs independently of control-plane policy; deny if either side denies or has unknown state.
- Never escalate privileges to make a feature work. Respect OS privacy permissions.

### User consent and approvals

- User explicitly enables desktop control and sees node identity, current task, target app and available capability set.
- Local node presents current activity and offers immediate pause/stop.
- Exact approval binds workspace, task, device/session, operation, target context, normalized args hash, policy version, approval actor and short expiry.
- Changing target, arguments, app/window scope or policy invalidates approval.
- Critical financial/legal/security operations are unavailable to generic desktop automation in the initial release.

### Data minimization

- Do not persist full accessibility snapshots by default.
- No screenshot, clipboard read, password field, browser cookies, keychain or arbitrary local file contents in ordinary logs.
- Redact common PII/secrets and sensitive controls before model exposure; redaction is defense in depth and may be imperfect.
- Use bounded in-memory buffers and explicit opt-in for debug artifacts.
- Define retention and deletion for evidence artifacts; default shortest practical retention.

### Isolation

- Desktop Node has no permission to control other OS users or secure desktop.
- Desktop driver process runs as the signed-in user, not root/admin.
- Only one mutating lease per physical desktop session; prevent concurrent agents from racing the same UI.
- The node process and desktop driver have no authority to access the code worker's host mounts or secret store.

## Abuse cases and expected result

| Abuse case | Control / expected result |
|---|---|
| Prompt injection in UI tells agent to exfiltrate | Treat UI text as untrusted; no policy or secret access |
| Fake/replayed pairing token | One-time expiry, nonce, device key proof; reject replay |
| Stolen device credential | Workspace binding, revocation, key rotation, short leases |
| Agent replays a click after timeout | Delivery semantics; no retry unless explicit safe |
| Two agents race same desktop | Per-session mutation lock and lease serialization |
| Target ambiguity or stale ref | Refusal + fresh snapshot; never coordinate guess fallback |
| Malformed driver JSON | Protocol error; no action and raise security telemetry |
| Malicious app text or giant tree | Node/text/depth/output limits and content untrusted |
| Screenshot/clipboard leaks | Capability off by default, approval, redaction, short retention |
| Node disconnects mid-action | Lease expires; action disposition unknown; manual verification before retry |
| Agent uses `click` to hit destructive control | Semantic target risk classification and exact approval |
| Dependency binary replaced | Signed/checksummed pinned release, provenance and update audit |

## Security acceptance gates

- No public inbound node port.
- No shell-string command execution.
- No arbitrary command schema accepted from model.
- Pairing and lease replay tests pass.
- Revocation propagates and invalidates sessions.
- Cross-workspace device/action access denied.
- All desktop mutations produce audit receipt with disposition.
- No automatic retry for unknown/uncertain/delivered-unverified action.
- Screenshot/clipboard access disabled by default.
- Secrets and private desktop content absent from test logs/telemetry.
- Local stop and disconnect lease expiry tested on real host OS.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
