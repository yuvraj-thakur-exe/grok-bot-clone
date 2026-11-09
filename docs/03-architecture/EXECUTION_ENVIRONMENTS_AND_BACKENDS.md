# Execution environments and agent backends

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Supported deployment profiles

| Profile | Description | Use case | Security boundary |
|---|---|---|---|
| Local development | Control plane + workers on developer workstation | IDE iteration and testing | Local OS account; never run untrusted tasks without a sandbox |
| Local isolated | Control plane local; each task in disposable container | Single-user self-host | Container plus network policy and restricted mounts |
| Remote container | Worker containers on dedicated host/cluster | Private beta and team workloads | Per-task identity, namespace, egress and quotas |
| MicroVM | Firecracker-like VM per task | Stronger multi-tenant execution at scale | Hypervisor boundary plus host hardening |
| External agent backend | OpenHands/ACP-compatible or other agent runtime | BYO coding agent, specialised execution | Backend identity, isolated workspace and scoped credentials |
| User desktop | Local Desktop Node on interactive device | Native app control | Device pairing, OS permissions, local policy and lease |

## AgentBackend interface proposal

Methods: `discover_capabilities()`, `create_session()`, `resume_session()`, `send_input()`, `stream_events()`, `read_artifact()`, `cancel()`, `close_session()`, `health()`.

Every call requires an authenticated backend ID, workspace scope, task ID, deadline, cancellation signal and capability check. Use typed event envelopes with sequence numbers and replay cursor. Backend-specific metadata is namespaced and must not become a hidden cross-tenant channel.

## Adapter capability manifest

Declare supported operations, model requirements, tools, file semantics, runtime isolation, network policy, persistence, event streaming, checkpointing, cancellation guarantees, secret handling, supported platforms and version. Unknown capability = unavailable, not assumed.

## Backend switching

Switch only between explicit session boundaries. The adapter must define what is portable: user prompt, approved task plan, selected files, artifacts and summary. Never copy runtime tokens, raw credentials, browser cookies, local desktop state or hidden prompts into another backend. Require user consent when data residency or processor changes.
