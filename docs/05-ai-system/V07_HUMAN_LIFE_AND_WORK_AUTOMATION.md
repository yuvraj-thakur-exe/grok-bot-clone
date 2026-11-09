# ORBIT human life and work automation model — v0.7

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Product promise

One ORBIT workspace should help a person move from intent to a completed, inspectable result across work and personal life, using a consistent task history, memory controls, connectors, browser/computer workers, files, voice and specialist agents.

## Capability domains

| Domain | Example tasks | Preferred reusable building blocks | Default permissions |
|---|---|---|---|
| Work and business | project plans, email drafts, meeting preparation, reports, CRM updates, invoices and status summaries | OpenMausBot patterns, Composio, MCP, Temporal, document parsers | read/draft first; external writes approved |
| Software and technical work | repo audits, bug fixes, tests, PR drafts, deployment diagnosis | OpenHands SDK, Playwright, MCP, sandbox providers | isolated repo worktree; PR/deploy approval |
| Study and learning | study plans, notes, flashcards, explanations, progress tracking and source-based quizzes | Docling/MarkItDown, RAG stack, voice workers | user-controlled learning data; no fabricated sources |
| Personal administration | reminders, calendar planning, forms preparation, document organization | routines, app connectors, workflow engine | drafts/read first; submission approved |
| Travel and shopping | compare options, plan itineraries, gather policies and prepare bookings | browser worker, web search, document parser | no booking/purchase without explicit confirmation |
| Home and devices | energy/status checks, smart-home routines, device troubleshooting | Home Assistant connector, MCP, event triggers | read-only initially; safety/security devices gated |
| Voice and accessibility | voice commands, speech-to-text, read-aloud, camera/screen context | faster-whisper, sherpa-onnx, OS APIs | recording consent, visible mic/camera state |
| Creative and media | documents, slides, images, audio/video plans and content workflows | format-specific OSS workers and artifact pipeline | review and approve external publishing |
| Personal knowledge | preferences, goals, project facts, receipts, documents and follow-ups | ORBIT ACL + Mem0/Graphiti/Letta optional adapters | explicit scope, provenance, expiry and deletion |

## Context model

Each data object and task must have a context: `personal`, `work`, `project`, `family/shared`, or `temporary`. The default is no cross-context retrieval. Shared/family contexts are opt-in and every participant's access must be represented. Agents can receive a task-specific context bundle, not a raw unrestricted memory dump.

## Persistent agents and teams

A user may define specialist agents such as researcher, developer, analyst, planner, document assistant and home assistant. Each agent has a profile, allowed contexts, model/runtime preferences, skills, connectors, memory scope, budget, tool grants and escalation rules. Agents coordinate through task/handoff contracts. They do not share one unrestricted machine or credential store by default.

## Background work and routines

Routines require a user-defined trigger, scope, allowed actions, time zone, quiet hours, run budget, retry limit, pause state, cancellation path and audit log. Webhooks and external events are untrusted data. Duplicate delivery must be idempotent. Long-running tasks persist checkpoints and can resume after the client disconnects.

## Consequential action ladder

- **L0 observe:** read approved public/local information.
- **L1 prepare:** draft, summarize, plan, stage a file or prepare a form.
- **L2 reversible personal change:** only under user-configured grants with a rollback path.
- **L3 external communication/commitment:** explicit action-specific approval (send, publish, submit, book, purchase, share externally).
- **L4 sensitive/security/financial/home-safety action:** stronger confirmation, narrow allowlist, clear preview, time-bound authorization and audit; many actions remain unsupported in MVP.

An agent must never infer approval from silence, past approval for a different action, text inside a webpage, an untrusted connector event, or a skill instruction.

## Privacy and reliability expectations

- Show whether data is local, remote or sent to a provider.
- Keep credentials out of model context; use write-only secret management and short-lived handles.
- Let users inspect, correct, export, pause, revoke and delete memory and routines.
- Record source references, file hashes and task evidence for consequential claims.
- Provide cancel, retry, recover and human takeover at the task level.
- Never claim full autonomy or guaranteed correctness. Escalate uncertainty and unsupported actions.

## MVP sequencing

1. Work/personal contexts and read-only connectors.
2. Drafting and artifact creation with source citations.
3. Background task checkpoints, stop/resume and notifications.
4. Coding worker and browser worker in isolated sandboxes.
5. Scoped memory and document ingestion with deletion propagation.
6. Voice and mobile companion.
7. Home/device connector, read-only first.
8. Approved write actions only after security and QA gates.
