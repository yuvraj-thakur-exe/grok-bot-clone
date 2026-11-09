# MCP and plugin ecosystem

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Goal

Allow users to attach external tools while preserving ORBIT's policy, tenant, audit and execution boundaries. MCP is an integration protocol, not a trusted execution environment. A connected server is an external principal with declared capabilities.

## Connector lifecycle

Discover server/manifest -> verify origin and version -> inspect tool/resource/prompt schemas -> classify risk and requested scopes -> administrator/user approval -> store credentials in the secret broker -> run compatibility and permission tests -> enable -> monitor -> revoke/update. Imported manifests remain disabled until reviewed.

## Protocol versioning

The public MCP specification released `2026-07-28` and changes protocol behavior (including stateless core, request metadata, header routing, authorization changes and extensions). The MCP TypeScript SDK v2 documentation identifies it as the stable line for the `2026-07-28` spec, while v1.x is a maintenance line for the older `2025-11-25` spec. ORBIT must pin a protocol/SDK version, implement an adapter, document supported protocol eras and add negotiation/compatibility tests. Do not paste stale v1 initialization examples into a modern v2 client without checking the selected transport and version.

## Plugin manifest

Required fields: plugin ID, publisher, version, description, entrypoint/transport, tool schemas, data access scopes, secret requirements, risk classes, network destinations, resource budgets, timeout, supported protocol version, license, update policy and provenance. Validate schema and package integrity. Maintain allowlist/denylist and kill switch.

## Isolation

Run local MCP servers in separate processes/containers with minimal filesystem and network access. Remote servers receive only the data in each authorized call. Tool responses are untrusted. Enforce output-size limits, timeout, cancellation and policy check per invocation. Do not let plugin metadata grant the plugin additional scopes.

## Marketplace safety

A public registry is P2+ and requires publisher verification, signed releases, dependency scanning, review/moderation, revocation, vulnerability reporting and transparent permissions. Do not auto-install plugins discovered by an agent.

## Desktop MCP boundary

`agent-desktop mcp` is optional for trusted local developer use. Its dynamic command catalog exposes upstream command surface, not ORBIT workspace authorization. Never pass its full tool list to production agents. Instead implement named ORBIT operations, fixed schemas, policy and approvals. Pin and test the MCP protocol version/SDK independently from the desktop driver's JSON output contract.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.


## v0.5 plugin trust tiers

MCP and plugin protocols standardize interfaces, not trust. An in-process plugin is trusted code. Untrusted extensions run out-of-process with restricted filesystem/network, bounded IPC, scoped credentials and explicit tool grants. A skill, server or connector cannot authorize itself by declaring read-only annotations.

