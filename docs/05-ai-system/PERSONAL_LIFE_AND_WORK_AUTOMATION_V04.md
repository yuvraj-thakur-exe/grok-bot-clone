# Personal life and work automation — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Objective

ORBIT should turn a user's intent into a clear plan, carry out the safe parts, obtain confirmation for sensitive actions, and return verifiable results. It is a workbench for daily life, not a covert surveillance tool or a bot that silently spends money and sends messages.

## Core user experience

- One main assistant conversation and a roster of named specialist agents.
- Each agent shows its role, model, connected apps, current task, working environment, memory scope and permissions.
- Tasks have a timeline: plan, delegated work, progress, approval requests, evidence, artifacts and final verification.
- Users can pause, stop, edit, reassign, revoke access or take over a computer/browser session.
- One task may produce a document, spreadsheet, presentation, code patch, issue/PR, calendar proposal or other artifact.
- Users can export a specialist team or workflow as a portable package without credentials, personal memory, transcript history or active permissions.

## Capability catalogue

| Domain | Example capabilities | Default mode |
|---|---|---|
| Personal knowledge | Search notes/files, summarize, connect project facts, recall approved preferences | Read-only |
| Research | Web search, compare sources, extract data, build evidence-backed reports | Read-only; disclose sources and uncertainty |
| Study and learning | Study calendar, quizzes, revision plans, flashcards, assignment support | User-directed; user owns submitted work |
| Software/projects | Repo audit, issue analysis, implementation, test execution, PR drafts, release notes | Isolated workspace; review before merge |
| Communication | Inbox triage, draft email/messages, meeting notes, follow-up drafts | Draft-only; sending asks approval |
| Scheduling | Calendar planning, reminders, routines, deadlines and recurring summaries | Read first; writes require approval |
| Documents and files | Create/edit docs, sheets, slides, PDFs, images and project folders | Workspace-scoped; destructive changes require approval |
| Travel and bookings | Search places/routes, prepare itineraries, fill forms and book where allowed | Purchase/booking confirmation before commitment |
| Shopping and household | Compare items, lists, orders, warranty and maintenance reminders | No payment or purchase without exact approval |
| Finance and business admin | Expense categorization, cash-flow organization, research and scenario modeling | Information/support only; no autonomous trading/payment/tax filing |
| Creative/media | Images, video concepts, voice, audio, slides, websites and prototypes | User-directed generation; publication requires approval |
| Device workflows | Browser, desktop, files and local app control | Per-device capability and visible session controls |
| Health/administration | Organize user-provided records, draft questions and appointment notes | No diagnosis, treatment or autonomous medical action |

## Proactive and always-on behavior

Every proactive feature is opt-in and separately scoped:

- scheduled routines run at explicit local times and display their timezone;
- event triggers list the source account, event types and actions they may start;
- quiet hours, pause, expiration, notification and data retention are configurable;
- every run has a durable task ID, visible history, budget and stop control;
- no hidden audio/video/location monitoring;
- no new connector permissions or new recipients can be added by an unattended run;
- a trigger cannot approve its own sensitive action.

## Approval matrix

| Action class | Default |
|---|---|
| Read approved files, notes, repository status or public web pages | Allowed within scope |
| Create draft files in assigned workspace | Allowed within quota |
| Modify existing files or commit code | Approval depends on workspace and risk profile; review diff first |
| Send email/chat, post publicly, submit forms | Exact human approval |
| Delete files/data, change account/security settings, rotate credentials | Exact human approval |
| Purchase, pay, transfer, subscribe, book non-refundable services | Exact human approval with merchant/amount/terms visible |
| Deploy to production, merge protected branch, change access policy | Exact human approval and independent QA/security gate |
| Medical, legal, investment, credit or high-impact decision | No autonomous execution or decision authority |

Approvals must include the exact target and normalized action parameters. A change to price, recipient, account, file scope, permissions or payload invalidates the approval.

## Memory and personalization

- Capture only through explicit user-facing memory policy or user action.
- Store source, time, confidence, scope, agent visibility, expiry and reason.
- Keep personal, academic, work, financial and project scopes separate.
- Agent-specific memory is private to its namespace unless the user grants shared access.
- The user can inspect, correct, export, delete and pause memory capture.
- Do not treat inferred attributes or model-generated summaries as verified facts.
- Never store passwords, MFA codes, full payment credentials or unnecessary sensitive records as memory.

## Multi-agent team examples

- Research team: web researcher → subject analyst → citation checker → report writer.
- Study team: planner → tutor → quiz generator → progress reviewer.
- Software team: repo auditor → architect → implementation worker → test/QA reviewer → release-notes writer.
- Business operations team: inbox triager → calendar planner → finance analyst → action-item tracker.
- Personal admin team: document organizer → scheduler → form-preparation assistant → human approval gate.

The coordinator owns the plan and task state; specialists work in bounded scopes; reviewer agents cannot approve their own changes.
