# ORBIT reference adapter contracts

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Proposed internal contracts. Implementations are not included in this documentation package.

ORBIT owns the stable product contract. Third-party implementations sit behind adapters. The product must remain usable when any optional adapter is absent or replaced.

## Core interfaces

### `BrowserDriver`

Required operations: `create_session`, `navigate`, `observe`, `locate`, `act`, `wait`, `capture_optional`, `export_artifact`, `close_session`, `health`.

Required fields: workspace/task binding, browser profile ID, allowed domains, egress policy ID, timeout, output budget, download policy, confirmation policy, cancellation token and redaction mode.

Adapter invariants:
- isolated browser context per task unless user explicitly chooses a persistent profile;
- no use of an arbitrary personal Chrome profile in restricted mode;
- fresh semantic snapshot before action; refs are short-lived;
- `eval`, uploads, downloads, cross-origin navigation, external submissions and credential operations are individually policy gated;
- a page's content is untrusted and never becomes system/developer instruction;
- browser allowlists supplement, but never replace, sandbox/network egress controls;
- output caps, download quarantine, file scanning and complete cleanup.

### `DesktopDriver`

Implemented through the Local Desktop Node design from v0.2. Must remain separate from `BrowserDriver` and `CodeExecutionProvider`. Requires user-session device pairing, local policy, leases, OS capability discovery, snapshot completeness, opaque refs and strict delivery disposition.

### `SandboxProvider`

Required operations: `create`, `inspect`, `exec`, `read_file`, `write_file`, `snapshot` (optional), `pause` (optional), `resume` (optional), `terminate`, `health`, `list_artifacts`.

Every sandbox has immutable owner/task labels, resource quotas, TTL, image digest, mount plan, network policy, credential binding reference, audit correlation and deletion state. A sandbox must not receive a raw provider/master API key. Use an out-of-band credential broker and scoped egress injection when supported.

### `AgentBackend`

Required operations: `start`, `send_input`, `stream_events`, `cancel`, `inspect`, `collect_artifacts`, `close`. The backend may implement an external coding agent or a first-party ORBIT agent.

ORBIT retains task identity, workspace permissions, budgets, approval requirements, logs and final verification. ACP/MCP interoperability does not grant access rights. External agents receive a task-scoped, expiring workspace capability, not a global token.

### `SkillSource` / `SkillRuntime`

A source resolves immutable skill content and provenance. The runtime validates schema, license, checksum, tool declarations, scripts, network needs, agent compatibility and human review state before activation. Scripts execute in a sandbox; `SKILL.md` is instruction data, not trusted authority.

### `UISpecRenderer`

Consumes an ORBIT-owned declarative `UISpec` validated against a versioned catalog. It can display data, collect bounded user input and invoke named server-side actions. It cannot execute model-generated code, import arbitrary components, navigate with hidden privileges or authorize tools.

## Shared response envelope

All drivers return a common envelope:

```json
{
  "schema_version": "1.0",
  "ok": true,
  "operation_id": "opaque-id",
  "provider": { "id": "driver-name", "version": "pinned-version" },
  "data": {},
  "disposition": {
    "delivery": "not_applicable",
    "retry": "not_applicable",
    "verification": "not_attempted"
  },
  "timing_ms": 0,
  "warnings": [],
  "error": null
}
```

Errors include a stable ORBIT error code, retryability, recovery guidance, provider code and redacted details. Preserve upstream provider evidence inside a namespaced field; do not flatten away unsafe/unknown delivery semantics.

## Retry semantics

- Read-only requests may be retried within bounded budgets on transient transport errors.
- Mutations may be retried only when the provider explicitly establishes non-delivery or the operation is idempotent and idempotency key is honored.
- `unknown`, `delivery_uncertain` and `delivered_unverified` are not automatic retry permissions.
- A completed click, HTTP 200 or successful tool envelope is not proof that the intended business effect persisted. Verify the desired postcondition.

## Adapter conformance

Each adapter must pass common tests for workspace isolation, cross-tenant denial, cancellation, timeouts, malformed outputs, retries, output limits, policy denials, secret redaction, version drift, health checks and shutdown cleanup. Run provider-specific tests for browser/desktop/sandbox semantics. Publish conformance results against an exact adapter and provider version.


## v0.5 canonical integration rules

Every adapter receives ORBIT task/workspace identity, immutable policy snapshot, scoped credential handles, budget, deadline and cancellation token. It must return normalized lifecycle events, usage, errors and artifact references. Adapter capability claims are verified, not trusted from README or tool annotations. Only one default implementation is selected per capability; optional alternatives are disabled unless a measured ADR approves them.

