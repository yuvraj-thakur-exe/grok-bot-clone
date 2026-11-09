# Competitive product surface — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Research snapshot:** 08 November 2026. This document summarizes public product documentation, not independent verification of vendor internals or performance.

## What the category leaders publicly promise

| Product | Publicly described capabilities | Architectural observation | ORBIT parity requirement |
|---|---|---|---|
| [Grok Bot](https://x.ai/bot) | Multiple specialist Bots, persistent cloud computer, app/website use, parallel work, workflow routines, approvals, desktop/mobile access and continued background work | Official FAQ says a user's Bots share one persistent computer, files, browser sessions and logins; one Bot is not a security boundary from another Bot on the same account | ORBIT needs a multi-agent roster, long-running jobs, computer/browser workers, connected apps and routines. Prefer stronger isolation by project/agent and credential scopes rather than silently sharing every login and file |
| [Meta Muse](https://ai.meta.com/muse/) | Persistent secure VM with browser, app connectors, multi-step web tasks, appointments/forms/customer service, reminders, goals, background monitoring, document/image creation and permission controls | Its public positioning focuses on an always-available personal agent that can act through a dedicated computer and connected services while asking before certain sensitive actions | ORBIT needs a reliable computer environment, safe browser and connectors, permission presets, proactive tasks, memory and reviewable approvals |
| [OpenAI dots](https://openai.com/index/introducing-dots/) | Always-on agents with a cloud computer, feedback-based learning, plugin access to more than 4,000 apps, and access through ChatGPT, Slack and Teams; official onboarding describes ongoing project work, user context, review, feedback and pause controls | The product emphasizes persistent delegated work across tools and projects, with the user able to redirect and pause work | ORBIT needs always-on task continuity, broad connector coverage, user-controlled memory/feedback, persistent computer/browser workers and clear pause/review UX |

## Product capability matrix

The rows below are the minimum product systems ORBIT must deliver to compete. A capability is **not** considered shipped because an upstream repository contains code for it; it must work end-to-end in the ORBIT application and pass the evaluation suite.

| Capability | Why it is table stakes | Required ORBIT implementation | Release evidence |
|---|---|---|---|
| Specialist agent roster | Users need parallel, purpose-specific workers | Agent profiles, model choice, scoped instructions, memory, workspace, permissions and handoff | Multi-agent end-to-end benchmark |
| Persistent execution environment | Agents need to continue when the client closes | Recoverable cloud/local worker sessions, durable task state, reconnect and cancellation | Restart and recovery tests |
| Browser and computer use | Many tasks require real interfaces | Isolated browser workers plus paired native desktop node, visible session, takeover and stop | Cross-site task suite and action audit |
| Connected applications | Work is spread across email, files, calendars, chat and project tools | OAuth connectors, least-privilege scopes, revocation and webhook triggers | Connector scope and side-effect tests |
| Always-on routines | Value comes from recurring and event-driven work | Explicit opt-in schedules, timezone, event subscriptions, retries, notifications, pause/expiry | Duplicate-trigger and missed-run tests |
| Long-term memory | Agents need continuity and preferences | User inspect/edit/delete, source provenance, confidence, expiry and strict scopes | Memory accuracy and leakage tests |
| Skills ecosystem | Users need specialist workflows without waiting for core releases | Portable skills, catalogue discovery, per-skill license review, static scan, sandbox and pinning | Malicious-skill and supply-chain tests |
| Review and approvals | Agents can affect money, accounts and reputation | Exact action preview, target/amount/recipient/payload hash, expiry and one-time grant | Zero unauthorized high-impact side effects |
| Model and runtime choice | Model quality, cost and availability vary | BYO-provider, local model and runtime adapters, measured routing and spend controls | Model/provider conformance suite |
| Voice and mobile | Users need access away from the desktop | Voice input/output, mobile controls, notifications and handoff to persistent tasks | Device and latency tests |

## ORBIT's defensible differentiation

1. **Open and portable by design:** users can run local-first, self-hosted or managed workers; change models and agent runtimes without losing their task history or workspace.
2. **Stronger context isolation:** separate personal, academic, client and project scopes; separate agent credentials and workspaces when a task requires isolation. Do not inherit the shared-computer pattern as a security model.
3. **Verified completion over impressive demos:** every task has criteria, execution evidence, artifacts, side-effect status and recovery history.
4. **Safe personal automation:** reminders and monitoring are opt-in; account writes, messages, payments, purchases, bookings, publication and deletion remain user-approved.
5. **Portable teams and skills:** export role/configuration packages without secrets, transcripts, memory or active privileges; import requires trust review.
6. **A broad life/work system:** combine study, software, research, files, scheduling, communications, travel, home administration, creative production and business operations inside one consistent policy model.

## Competitive gaps to close, in order

- **P0:** working product shell, one persistent task plane, visible task history, stop/pause, model switching and artifact output.
- **P1:** multi-agent delegation, secure per-task computer/browser, app connectors, approvals, recurring routines and memory controls.
- **P2:** cross-device companion, voice, portable teams, curated skills, offline prompt/skill optimization and specialist life/work workflows.
- **P3:** richer collaboration, enterprise administration, multi-user tenancy and advanced local/microVM execution after security and cost validation.

## What not to claim

- Do not claim parity with another product based on a design document or a successful one-off demo.
- Do not claim “4,000 integrations” unless ORBIT actually has a maintained connector inventory and tested workflows at that scale.
- Do not claim full autonomy, AGI or guaranteed task completion.
- Do not claim stronger security without published threat models, isolation tests, permission tests and incident procedures.
- Do not copy the competitors' product names, mascot, UI assets or trade dress.

## Primary references

- xAI, Grok Bot product page: https://x.ai/bot
- xAI, Grok Bot FAQ: https://docs.x.ai/grok-bot/faq
- xAI, Use the computer and apps: https://docs.x.ai/grok-bot/computer-and-apps
- Meta, Muse: https://ai.meta.com/muse/
- Meta, Introducing Muse (08 September 2026): https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- OpenAI, Introducing dots (29 September 2026): https://openai.com/index/introducing-dots/
- OpenAI Help Center, Getting started with your dot: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot


## v0.5 evaluation update

Use the feature surface here as a research baseline, not as a verified internal capability claim. Compare ORBIT only through reproducible end-to-end tasks that measure task completion, long-running continuity, computer isolation, app connectivity, approvals, user control, privacy, cost and failure recovery. The acceptance protocol is `docs/09-quality/V05_BENCHMARKS_AND_ACCEPTANCE.md`.

