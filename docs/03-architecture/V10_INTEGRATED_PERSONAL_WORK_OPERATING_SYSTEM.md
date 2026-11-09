# ORBIT v1.0 integrated personal and work operating system

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Product objective

ORBIT is one user-controlled workspace for delegated AI work across personal, academic, creative and professional contexts. It is not a single chatbot, a loose pile of bots or an unbounded host-control agent. It combines a persistent task plane, specialist agents, connected apps, computers, approved memory, routines and user-facing artifacts.

## ORBIT-owned control plane

ORBIT owns canonical accounts, workspace/context ACL, task/event state, policies, approvals, budget limits, memory consent, skill provenance, connector scopes, audit evidence, notifications, artifacts and UI. It selects among replaceable open-source runtimes, inference providers, browser drivers and memory/retrieval components.

## Capability groups

| Human goal | Agent capabilities | External systems | Safety controls |
|---|---|---|---|
| Study and learning | tutor, timetable, notes, practice, progress analysis | LMS, calendars, documents | student controls, assessment integrity, no unapproved submissions |
| Research and knowledge | web search, source comparison, papers, citations, knowledge graphs | browser, search, repositories, document store | source evidence, provenance, uncertainty, copyright limits |
| Software and technical work | plan, repo audit, code edits, tests, build, issue triage, PR proposal | GitHub, IDE, shell, browser, sandbox | isolated worktree, branch policy, review, no production secrets by default |
| Communication and admin | draft email/chat, inbox triage, meeting prep, forms | email, calendar, contacts, office suite | send only after approval; verify recipient and attachments |
| Documents and creativity | reports, PDFs, slides, spreadsheets, images, video planning | local files and creation tools | file permissions, export preview, licensing, no silent overwrite |
| Business and operations | CRM, sales pipeline, inventory, customer support, operations reports | CRM, ticketing, finance, commerce | least privilege, financial action approval, audit record |
| Travel and daily life | itinerary research, bookings research, checklists and reminders | browser, maps, travel and booking services | verify dates/prices, explicit booking/payment consent |
| Home and devices | device status, energy routines, scene suggestions | Home Assistant and compatible APIs | default read-only; confirm physical actuation and safety-critical actions |
| Voice and mobile | dictation, speech output, mobile notifications, task handoff | companion apps and local ASR/TTS | recording consent, device pairing, visible mic/camera state |
| Personal memory | preference facts, project context, timeline and recall | scoped storage and search | user view/edit/delete, source, expiry and compartmentalization |

## Agent topology

- **Chief of Staff / planner** decomposes tasks and dispatches work. It does not receive broad credentials.
- **Specialists** have bounded skills, scoped workspace, approved tools, context and budget.
- **Independent reviewer** checks evidence and risks; implementation agents cannot approve their own sensitive work.
- **Execution workers** operate in browser, shell, desktop or sandbox domains with different policies.
- **User control surface** shows status, rationale, evidence, approvals, pause/cancel and final artifacts.

## Long-running task lifecycle

`created → clarified → planned → delegated → running → waiting_for_user / waiting_for_dependency → verifying → completed / failed / cancelled`.

Durable state and idempotency live in ORBIT. Workers can restart without losing the task record. Every consequential action includes a preview, policy decision, approval token and result event. Background work is opt-in, bounded by schedule, budget, scope and expiry.

## Competitor acceptance

For each benchmark scenario, compare ORBIT with public competitor claims and a reproducible task: multi-agent delegation, computer persistence, browser task, connected app workflow, recurring routine, feedback correction, memory retrieval/deletion, task pause/restart and action approvals. Measure completion quality, latency, cost, failure recovery, unauthorized side effects and user control. Public marketing statements are not a substitute for running the test.
