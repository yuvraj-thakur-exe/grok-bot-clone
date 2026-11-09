# Feature Prioritization

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Priority | Feature | Reason |
|---|---|---|
| P0 | Workspace/auth | Safe persistence boundary |
| P0 | Streaming chat/provider adapter | Core UX and model flexibility |
| P0 | Durable task lifecycle | Foundation for agent execution |
| P0 | Tool registry/policy/approval | Safety boundary |
| P0 | Research citations and file upload | Useful first task capabilities |
| P1 | Browser worker | Computer-use differentiator, high security cost |
| P1 | Git/code sandbox | Developer workflow |
| P1 | Memory/skills | Continuity and workflow reuse |
| P2 | Routines and multi-agent | Depend on proven single-agent runtime |
| P2 | MCP/connectors | Depend on mature permission and auth layer |
| P3 | Marketplace and voice/video | Provider-dependent and costly |

## v0.2 prioritization update

| Priority | Capability | Rationale / dependency |
|---|---|---|
| P0 | Core auth/workspaces, chat, durable tasks, model adapter, policy/audit | Required foundation |
| P1 | Research/files, Playwright browser worker, code/Git sandbox | High utility without local desktop installation |
| P2 | Local Desktop Node read-only prototype | New capability, after gateway and task reliability |
| P2 | Semantic desktop actions + approval | Requires device pairing, lease security and platform tests |
| P3 | Memory/skills/routines/multi-agent | Only after single-agent and tool reliability |
| P3 | MCP marketplace, voice/media and broader connectors | Ecosystem and provider-dependent |

Native desktop control is a high-risk execution capability, not a cosmetic UI feature. Do not move it earlier because it looks impressive in a demo.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.

## v0.3 integration prioritization

P0: task/event contract, policy gateway, audit, dependency inventory and license/SBOM release gate.  
P1: isolated sandbox baseline, browser driver conformance, skill registry and OpenTelemetry instrumentation.  
P2: ACP/external agent backends, constrained generative UI and Local Desktop Node.  
P3: optional local dev hostname proxy, Firecracker/high-density execution and wider skill marketplace.  

Do not prioritise an integration based on repository popularity alone. Require measurable user outcome, security review, licensing evidence and a conformance test suite.
