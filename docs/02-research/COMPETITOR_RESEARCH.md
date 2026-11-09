# Competitor Research — Grok Bot

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Reviewed:** 08 November 2026. **Method:** public official product/developer documentation. No authenticated account was used; no private endpoint or access control was bypassed. This is not complete UI reverse engineering.

## Publicly documented capabilities and implications

| Area | Public docs describe | ORBIT implication |
|---|---|---|
| Interaction | Chat, voice calls/notes | Chat-first, voice-extensible UI |
| Multiple bots | Bots can cooperate across apps, sites and tools | Real task delegation and shared task graph, not separate chat tabs |
| Computer | Persistent cloud computer with browser, filesystem and terminal | Persistent workspaces and execution workers are core product surfaces |
| Shared state | Bots on one account can share sessions, files and CLI credentials | ORBIT should default to stronger workspace/task isolation and explicitly scope sharing |
| Integrations | Connected apps and custom MCP/API tools | Provider-neutral connectors with manifests and scopes |
| Skills | Reusable workflow instructions capture inputs, steps, decisions, validation and safety | Versioned, tested skill schema |
| Routines | Schedule/event-trigger automation | Add only after reliable workflow execution |
| Approvals | Message, publish, purchase, delete, permissions, production and legal actions may require approval | Exact-action, expiring approval + audit |
| Secrets | Secure forms/vault are separate from ordinary chat | Secrets never enter model context or ordinary logs |
| Model tools | xAI developer docs list Web Search, X Search, Code Interpreter, Image Generation, Collections Search and custom functions | Provider-specific tool capabilities must be adapters, not universal assumptions |

## Design lessons

1. A persistent computer is a major product surface, not a helper function.
2. Shared browser credentials increase blast radius; ORBIT should not assume agent identity provides isolation.
3. A successful task should become a skill only after review and tests.
4. Approval must attach to the exact action/target/arguments, not blanket autonomy.
5. Users need an execution timeline with browser/terminal activity, progress, tool calls and artifacts.
6. Durable single-agent execution should precede multi-agent complexity.

## Unknown / not verified

- Private authenticated UI, subscription behavior and onboarding were not tested.
- Internal implementation, prompts, infrastructure and orchestration are not public evidence and are not inferred.
- No comparative task benchmark was run; ORBIT cannot claim superiority from this report.
- Public descriptions do not prove every capability is available to every account, plan or region.

## Conclusion

ORBIT should compete on trustworthy execution, open deployment, provider choice, explicit workspace boundaries, evidence, recovery and developer ergonomics. Do not copy branding, icons, layouts or proprietary assets. Source links: `RESEARCH_REFERENCES.md`.

## Additional execution-tool reference: Vercel Labs agent-desktop

This is not a direct end-user AI assistant competitor. It is an open-source native desktop driver and useful engineering reference for ORBIT's computer-use layer. Its design is deliberately narrow: accessibility-tree observation, snapshot-scoped refs, semantic interaction, structured JSON and platform-specific skills. ORBIT should adopt those engineering patterns and build its own orchestration, policy, local device connection and user experience. Do not claim feature parity with upstream until a real integration passes platform tests.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
