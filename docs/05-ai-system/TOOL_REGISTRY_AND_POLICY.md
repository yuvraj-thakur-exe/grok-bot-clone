# Tool registry and policy gateway

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Tool manifest

Every tool declares name/version, description, JSON input/output schemas, capability tags, required scopes, risk class, network scope, timeout, resource budget, idempotency support, audit fields, and owner. Tools are registered centrally; arbitrary model-generated function names are rejected.

## Risk classes

- `read`: bounded, read-only data access.
- `write_reversible`: a change with a supported undo path.
- `write_consequential`: external message, publish, purchase, delete, permission, deploy or account mutation.
- `privileged`: credentials, host, infrastructure, tenant admin, or security-sensitive operations.

## Gateway checks

Validate schema -> identify actor/workspace -> verify membership and agent grant -> classify resource and action -> enforce domain/network/size limits -> check approval -> execute through isolated worker -> normalize result -> redact -> audit.

## Tool response

Return structured status, safe summary, output refs, timestamps, and error classification. Do not expose environment variables, browser cookies, raw tokens or full secret-bearing request headers. Tool output is untrusted content and must be labelled as such to the model.

## Dangerous defaults to prohibit

No arbitrary host shell, Docker socket access, unrestricted network egress, unrestricted file path, cross-workspace resource identifiers, raw SQL tool, or “approve all future actions” default.

## Native desktop tool family

Register desktop operations as a separate capability namespace. The model receives only operations enabled by workspace policy, device capability, lease and local allowlist. The tool registry must not proxy arbitrary upstream CLI commands or auto-import MCP schemas as permission grants. Model input carries typed operation + snapshot ref; server rechecks semantic action risk against observed target. Preserve upstream JSON delivery disposition. Unknown/missing dispositions fail closed. Refer to `DESKTOP_COMMAND_ALLOWLIST.yaml`.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
