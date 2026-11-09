# Agent Desktop integration guide for implementers

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Adoption approach

Use upstream `agent-desktop` as an external pinned driver. Do not vendor source or fork OS-specific accessibility APIs for v1. The current repository metadata reviewed on 2026-11-08 lists npm package 1.2.0 / Cargo workspace 1.2.0 and JSON envelope 2.6; the implementation must verify current release artifacts and exact checksums again. These version numbers are different version namespaces.

## Step-by-step build plan

1. Define `DesktopDriver` protocol in a standalone internal package and provide `FakeDesktopDriver`.
2. Add schema types and test fixtures for device status, permission reports, complete/partial observations, refs, action receipt and errors.
3. Add the driver subprocess runner: fixed path, argv list, environment allowlist, no shell, process group, timeout, output cap and structured parse.
4. Pin release artifact per OS/architecture and validate checksum/signature; track upstream commit, package version and JSON contract.
5. Build Local Desktop Node with outbound authenticated WSS, device pairing, heartbeat, lease expiry and local pause.
6. Add local policy allowlist and serialization lock before any mutating tool is reachable.
7. Implement read-only observation commands, redaction and capability discovery.
8. Add one semantic action at a time on a disposable app; verify fresh state and preserve delivery semantics.
9. Add approvals and high-impact semantic intent classification.
10. Build real interactive test lanes for the target operating systems.

## Process invocation requirements

Use e.g. `asyncio.create_subprocess_exec(binary_path, "snapshot", "--app", app_name, "-i", "--compact", ...)`. Do not use `create_subprocess_shell`. Validate all values against schemas before constructing argv. Do not accept `--force`, arbitrary `--arg`, arbitrary output path or arbitrary executable path from an LLM tool call.

A process runner should return:
- exit code and bounded stdout/stderr;
- parse status and envelope version;
- command category (read-only/mutating/restricted);
- structured delivery disposition when present;
- timeout/cancel state;
- sanitized diagnostic metadata.

Do not infer safe retry from exit code alone. A timeout can occur after a mutation was delivered.

## Driver compatibility and upgrades

- Maintain a compatibility matrix of ORBIT adapter version × driver package version × JSON contract version × OS/architecture.
- Pin exact artifact and checksum in lockfile/manifest; do not download “latest” at runtime.
- Run contract fixture tests on every upgrade.
- Require staged rollout and a rollback binary for node upgrades.
- Upstream docs and command lists can change; the ORBIT allowlist should be explicit and reviewed, not generated from all upstream commands.
- Record `driver_version`, `contract_version`, OS build and capability report on each session.

## Optional MCP use

`agent-desktop mcp` serves upstream CLI commands over stdio. Use only as a developer convenience in a trusted local IDE environment. ORBIT's end-user tool gateway must use a curated set of named operations, because dynamic MCP tool discovery is not a permissions system. Never expose the complete upstream tool catalog directly to an untrusted model.

## FFI decision gate

Start with subprocess. Consider C FFI only if benchmarks show that process startup materially harms interaction latency or reliability, and after defining ABI lifecycle, memory ownership, threading, panic/unwind, crash isolation and per-platform build/release policy. In-process native access expands the control plane's crash/security blast radius.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
