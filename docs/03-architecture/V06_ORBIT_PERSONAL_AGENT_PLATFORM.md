# ORBIT personal and work agent platform — v0.6

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Product definition

ORBIT is a user-controlled agent platform for personal life and professional work. The user sets goals and boundaries; ORBIT coordinates specialists, tools and devices to make progress, ask for judgment and return evidence-backed work.

## Canonical control plane

ORBIT owns user/workspace/context identity, task lifecycle, event ledger, permissions, approvals, budget, memory consent, secrets handles, connector account scopes, schedules, artifacts and provenance. Upstream agent runtimes are execution backends, not independent authorities.

## Capability surfaces

1. Conversation and multimodal input: text, voice, images, files, structured forms and progressive updates.
2. Project/workspace management: goals, plans, subtasks, deadlines, files, roles, task board, decisions and outcomes.
3. Specialist team: researcher, coder, analyst, writer, planner, QA, designer, data/RAG specialist and operations agent.
4. Browser and computer: isolated web sessions, search/read/compare, browser form preparation, screenshots, downloads, desktop node, remote sandbox and user takeover.
5. App connections: email, calendar, documents, spreadsheets, code hosting, project management, messaging and supported services through OAuth/MCP/connector adapters.
6. Creation: reports, presentations, spreadsheets, code patches, diagrams, images, audio/video assets and exports.
7. Personal life: reminders, study plans, travel planning, household workflows, subscriptions, appointments and shopping research. Consequential actions remain approval-gated.
8. Business and operations: CRM, sales pipeline, support, content pipeline, research, bookkeeping preparation and analytics; not autonomous financial/legal authority.
9. Long-running work: schedules, webhooks, triggers, deadlines, monitoring, retries, resumable work and notifications.
10. Memory and knowledge: user preferences, project facts, source-grounded documents, correction, deletion, retention and context separation.
11. Local and remote compute: local models, remote providers, coding sandboxes, browser workers and paired desktop nodes.
12. Skill and tool ecosystem: curated registry, signed/digested packages, capability manifests, user approvals and isolated execution.

## Task lifecycle

`intake → clarify only essential missing data → plan → risk classify → select workers → authorize tools → execute → observe → validate → ask human where needed → package artifact/evidence → notify → retain/delete by policy`.

Task state must be durable and idempotent. Worker output is data, not authorization. Web pages, files, app events, repositories, skills and model outputs are untrusted inputs.

## Competitor requirements

Public Grok Bot material emphasizes always-on bots, their own computers, tools/apps, end-to-end task completion and approvals. Meta's official Muse material emphasizes a dedicated secure VM, browser, app connections, long-running work, user approval and an audit trail. OpenAI's official dots material emphasizes always-on delegated projects, their own cloud computer, connected apps, ongoing progress and user-configured rules. ORBIT should match the underlying task quality and trust boundary rather than copy product branding.

Public references reviewed 2026-11-08:
- https://x.ai/news/introducing-grok-bot
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse
- https://chatgpt.com/features/dots/
- https://help.openai.com/en/articles/20001530-getting-started-with-your-dot

## Security invariants

- Separate per-user execution environments and per-context data scopes.
- Policy gateway authorizes every tool call regardless of model or framework claims.
- Least privilege, just-in-time scoped credentials, never model-visible secrets.
- Egress deny by default for code/sandbox workers; allowlisted web access by policy.
- Exact approval for external side effects and a complete audit receipt.
- User can pause, cancel, revoke connector, stop desktop node and delete memory.
- Memory retrieval includes provenance, confidence and scope filters.
- Background jobs expire and have retry, cost and duration caps.
