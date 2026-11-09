# Technical Feasibility

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Capability | Feasibility | Complexity | Principal dependency/risk | Phase |
|---|---|---:|---|---:|
| Provider-neutral chat | High | Medium | API differences, usage/cost | 1 |
| Streaming and cancel | High | Medium | Reconnect/order/cancellation semantics | 1 |
| Durable tasks | High | High | Workflow determinism and migration/recovery | 1–2 |
| Research/citations | High | Medium | Search quality, freshness, SSRF | 2 |
| Document extraction/RAG | High | Medium | Parser security, prompt injection, ACL | 2 |
| Playwright browser tasks | High | High | Website drift/session security/human checks | 3 |
| Git/code sandbox | High | Very high | Isolation and package/network risk | 3 |
| Memory | High | Medium | Privacy, staleness and conflicts | 4 |
| Skills/routines | High | High | Safe replay and permissions | 4–5 |
| Multi-agent | High | High | Cost, latency, shared-state attacks | 5 |
| MCP/connectors | High | Medium-high | Spec versions, OAuth and plugin trust | 5–6 |
| Local models | High | Medium | Hardware and capability differences | 1–6 |
| Voice/video | Provider-dependent | High | Model support and media cost | Later |
| Frontier model training | Not viable for initial team/budget | Extreme | Compute, data and research capacity | Not planned |

A realistic product is an agent orchestration/execution platform built on available models. Do not advertise ORBIT as a newly trained foundation model.

## Native desktop capability feasibility

| Capability | Feasibility | Complexity | Principal dependency/risk | Phase |
|---|---|---:|---|---:|
| Native app read-only observation | High with supported driver + interactive session | High | OS permissions, accessibility tree quality and active session | 4–5 |
| Semantic desktop actions | Medium-high for supported controls | Very high | Stale/ambiguous refs, UI side effects, per-platform gaps | 5 |
| Local Desktop Node | High | Very high | Packaging, device identity, pairing, leases, local security and updates | 5 |
| Cross-platform support | Feasible, not uniform | Very high | Dedicated interactive tests for AX/UIA/AT-SPI, X11/Wayland differences | 6 |
| Desktop screenshots/clipboard | Technically feasible, restricted | High | OS privacy permissions and sensitive user content | Later / opt-in |
| Native desktop FFI | Possible | Very high | ABI, memory/thread lifecycle, crash blast radius | Only if subprocess profiling warrants |

Do not equate the presence of an upstream command with ORBIT support. Product UI must show current node capabilities and permissions. Keep the initial desktop MVP read-only; semantic mutations are a separate gated milestone.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
