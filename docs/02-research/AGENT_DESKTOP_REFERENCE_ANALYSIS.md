# Agent Desktop reference analysis

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Reviewed:** 2026-11-08  
**Repository:** https://github.com/vercel-labs/agent-desktop  
**Scope:** public GitHub source, README, agent instructions, concepts, JSON contract, skills and architecture files. No private maintainer information or private user desktop was accessed.

## Executive finding

`agent-desktop` is a native desktop computer-use **driver**, packaged as a CLI and C library. It reads the OS accessibility tree and performs supported actions against elements identified in a snapshot. It deliberately has no LLM, planner or workflow engine. The calling agent owns observation, action selection and verification. It is not a web browser automation engine; its README explicitly directs browser-page automation to a separate browser tool such as agent-browser.

ORBIT should wrap it behind `DesktopDriver` and run it only from a paired Local Desktop Node in the user's signed-in interactive graphical session. This complements, rather than replaces, Playwright and the sandboxed code worker.

## Verified source-level findings

| Finding | Evidence in upstream | ORBIT implication |
|---|---|---|
| CLI + C library; no embedded model | README, FAQ, AGENTS | Treat as a low-level execution adapter, not agent brain |
| Native accessibility tree as primary observation | README, platform skills | Prefer semantic role/name/state over screenshot coordinates |
| Three platform adapters | `crates/macos`, `crates/windows`, `crates/linux`; platform skills | Build normalized interface; discover capabilities at runtime |
| Shared platform-neutral core | `crates/core/src/adapter/mod.rs` | Keep OS-specific implementation behind adapter boundary |
| Common dispatch + command preflight | `src/dispatch/mod.rs`, `src/command_policy/mod.rs` | One gateway and policy path; no bypass route |
| Snapshot-scoped refs | README, `CONCEPTS.md`, core skill | Refs are ephemeral; never persist as stable entity IDs |
| Ambiguity refuses rather than guesses | Core skill and platform guides | Identity ambiguity must fail closed |
| Partial observation is explicit | `CONCEPTS.md`, JSON output 2.2+ | `complete=false` is not proof of absence |
| Delivery/retry is explicit | `docs/json-output.md` | Retry only when disposition explicitly says safe |
| MCP tools are generated from CLI command tree | `src/mcp/mod.rs`, `src/mcp/catalog.rs` | MCP exposure is a transport/catalog mechanism, not authorization |
| Platform limitations differ | macOS/Windows/Linux skills | Capability/permission negotiation is mandatory |
| Skills are embedded usage instructions | README and `skills/` | ORBIT needs versioned and platform-specific desktop skill docs |
| Current repo metadata at review | `npm/package.json`, `Cargo.toml`, `docs/json-output.md` | Upstream declares npm/Cargo package 1.2.0; JSON envelope separately reports 2.6; track separately |
| Declared license | npm metadata and README | Apache-2.0; preserve notices and perform compatibility review |

## Technical architecture observed

- Core defines a `PlatformAdapter` composed from observation, action, input and system operations.
- Platform crates implement their OS APIs; core must not depend on platform crates.
- The CLI parses commands, performs preflight validation, dispatches to a shared command path and emits structured JSON.
- MCP stdio serves commands as tools. The upstream instructions tell callers to read the desktop and platform skills first.
- The product has both semantic accessibility operations and physical/headed fallbacks. The latter require tighter policy and user visibility.

## Useful design patterns for ORBIT

### 1. Evidence is not boolean

The upstream concepts distinguish `Known`, `Absent` and `Unknown`. ORBIT should retain the same tri-state model for desktop properties and broader research evidence. A read failure must not be flattened into “absent”; unknown evidence cannot satisfy conditions requiring a positive or negative fact.

### 2. Snapshot reference identity

An accessible element reference is valid only within the observation/session identity context that produced it. UI mutation can make it stale. ORBIT must reacquire a snapshot after meaningful state changes, reject stale or ambiguous refs, and avoid persisting refs in durable memory. Stable application/window identity may be retained with lifecycle proof, but refs must not be treated as durable handles.

### 3. Explicit delivery semantics

Upstream JSON has structured errors and delivery dispositions. Preserve the distinctions: `not_delivered`, `delivery_uncertain`, `delivered_unverified`, `delivered_verified` and `unknown`. `retry=safe` is the sole automatic retry signal for mutating operations. A command returning `ok=true` is not equivalent to application-level or server-side persistence. This matters for a UI click that may have submitted a form.

### 4. One command surface, one policy path

Every CLI command travels through the same preflight/dispatch path, and batch reuses that route instead of creating a second dispatcher. ORBIT should likewise ensure UI actions, agent tool calls, API calls and MCP connectors cannot bypass the same policy/approval service.

### 5. Runtime capability discovery

The existence of a CLI command does not mean it works on every OS or application. Probe capabilities and permissions at runtime, then give the agent only the actions available for the current device/session. Avoid hand-maintained claims that every app supports every action.

### 6. Skill documentation is operational data

Upstream has a core skill plus platform-specific skills that describe the observe/act/verify loop and platform gotchas. ORBIT should deliver versioned desktop skills to agents, with version compatibility and clear boundaries, not hide important constraints in a generic system prompt.

## Integration decision

**Decision:** Adopt a pinned, externally managed upstream `agent-desktop` CLI as the first driver implementation, behind ORBIT's internal adapter interface. Do not vendor or fork its source for v1. Evaluate the C FFI only if subprocess overhead is measured as a meaningful bottleneck and memory/lifecycle/security requirements justify in-process native integration.

**Do not** expose the full upstream CLI/MCP command catalog to the LLM. ORBIT owns a curated tool allowlist, local policy and workspace authorization. Upstream tool listing does not grant user consent.

## Platform limitations to carry into product UX

- macOS needs Accessibility permission; Screen Recording is separate for screenshot capability.
- Windows UI Automation must run in the user's interactive session; Session 0, secure desktop, locked desktop and other-user sessions are not a supported control target.
- Linux requires an active graphical session and AT-SPI bus; upstream documents Ubuntu 24.04+ baseline and differences between X11 and Wayland. Some pointer/screenshot/window operations are unavailable or gated on specific display sessions.
- Some apps expose incomplete or unreliable accessibility metadata. ORBIT must communicate unsupported capability and offer safe manual handoff rather than guessing.

## Not established by the research

- This repository review does not prove its current release artifact is compatible with ORBIT's chosen deployment OS/runtime. Verify exact checksum, signature, release, package metadata and security advisories at implementation time.
- GitHub default branch `main` is mutable. Record exact commit SHA and release versions used by each ORBIT build.
- Public docs are not a promise that every app/platform combination has equal support.
- No screenshot-based competitor benchmark was performed; no performance or success-rate claims are inferred.
- This research did not install the driver or execute native computer actions on a user's machine.

## Sources

- https://github.com/vercel-labs/agent-desktop/blob/main/README.md
- https://github.com/vercel-labs/agent-desktop/blob/main/AGENTS.md
- https://github.com/vercel-labs/agent-desktop/blob/main/CONCEPTS.md
- https://github.com/vercel-labs/agent-desktop/blob/main/docs/json-output.md
- https://github.com/vercel-labs/agent-desktop/blob/main/skills/agent-desktop/SKILL.md
- https://github.com/vercel-labs/agent-desktop/blob/main/skills/agent-desktop-macos/SKILL.md
- https://github.com/vercel-labs/agent-desktop/blob/main/skills/agent-desktop-windows/SKILL.md
- https://github.com/vercel-labs/agent-desktop/blob/main/skills/agent-desktop-linux/SKILL.md
- https://github.com/vercel-labs/agent-desktop/blob/main/src/dispatch/mod.rs
- https://github.com/vercel-labs/agent-desktop/blob/main/src/command_policy/mod.rs
- https://github.com/vercel-labs/agent-desktop/blob/main/crates/core/src/adapter/mod.rs
- https://github.com/vercel-labs/agent-desktop/blob/main/src/mcp/mod.rs
- https://github.com/vercel-labs/agent-desktop/blob/main/npm/package.json
- https://github.com/vercel-labs/agent-desktop/blob/main/Cargo.toml

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
