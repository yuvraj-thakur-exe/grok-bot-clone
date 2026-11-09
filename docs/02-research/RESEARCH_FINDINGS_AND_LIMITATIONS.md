# Research findings and limitations

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Evidence basis:** user-provided ORBIT brief plus official public documentation reviewed on 2026-11-08. This is not an authenticated hands-on audit of every Grok UI flow.

## Source-derived requirements

The ORBIT source brief requires an open-source, provider-agnostic, self-hostable platform combining chat, agents, browser/computer execution, persistent workspaces, memory, skills, routines, multi-agent coordination, research, code execution, files, multimodal interfaces, MCP/plugins and security controls. It explicitly emphasizes public research first, phased execution, honest feature status, tests, approvals and no claims of unsupported capabilities.

## Public competitor evidence

Official Grok Bot docs describe persistent computer access including browser, filesystem and terminal; cooperation among Bots; user-defined skills and scheduled routines; and approval/security controls for consequential actions. These support using execution environment, teamwork, workflow reuse and approval UX as comparison dimensions. They do not establish private implementation details, source code, internal model architecture, exact benchmarks or unrestricted product capabilities.

## Important implementation findings

- A persistent computer is a major security boundary. Official computer documentation describes shared computer state among Bots within an account, so ORBIT should not reproduce shared browser state as a default isolation model.
- Reusable skills should be structured workflows with input, steps, validation and expected output; review and testing should precede scheduling.
- Consequential actions such as external messages, purchases, deletion, permission changes and production changes should have explicit approval.
- Durable workflows are more appropriate than in-process request background tasks for long-running work that must survive worker restarts.
- Browser contexts provide an isolation primitive for cookies and local storage; combine it with tenant-scoped session ownership and network controls.
- MCP is versioned and evolves; pin protocol/SDK versions and isolate compatibility in an adapter package.

## Unknown / not verified

Authenticated Grok UI states; account-tier-dependent capabilities; exact backend architecture; internal task orchestration; private system prompts; model weights; performance/cost benchmarks; hidden endpoints; and any workflow not publicly documented. No proprietary source, private API or access control has been bypassed.

## Product recommendation

ORBIT should differentiate on open provider choice, local-first execution, transparent task evidence, reliable recovery, user-owned memory, explicit tool policies, and a reusable skill ecosystem. Validate these with users; feature count alone is not advantage.

## v0.2 native desktop reference research

The review of `vercel-labs/agent-desktop` confirms a separate category of tool from the browser and code workers: a CLI/C library for native OS accessibility trees and semantic desktop operations. It does not embed a model, coordinate agents, or automate browser pages. The ORBIT integration proposal is therefore a Local Desktop Node connected to a Desktop Session Broker, with the upstream binary as a pinned driver. See `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` for file-level findings and limitations.

Upstream public repository metadata on 2026-11-08 declared npm/Cargo version 1.2.0 and the JSON output contract documented as 2.6. These are different version namespaces and must be checked again before implementation; GitHub `main` is mutable. The license declared by the upstream project is Apache-2.0. ORBIT must review dependency notices and distribution obligations.

The architecture uses native Accessibility (macOS AX), UI Automation (Windows UIA) and AT-SPI (Linux). OS APIs and application frameworks are not equivalent. Permission, active session and per-capability behavior must be discovered at runtime. A platform matrix is not a claim that every application exposes a complete tree.

The recommendation to run a Local Desktop Node in the user's interactive session, pair it through outbound authenticated WSS, use expiring leases, local policy and exact approvals is ORBIT engineering inference, not functionality supplied by upstream `agent-desktop`.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
