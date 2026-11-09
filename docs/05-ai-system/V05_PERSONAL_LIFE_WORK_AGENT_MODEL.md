# ORBIT v0.5 — personal life and work agent model

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Mission

ORBIT helps users get work done across their digital life while keeping them in control of context, permissions, data and irreversible decisions. Capabilities are modular and only enabled after connectors, providers and quality gates exist.

## Contexts and profiles

Users can define contexts such as Personal, Study, Family/Household, Project, Work/Employer, Client and Community. Each context has separate agent instructions, memory namespace, connected accounts, file collection, retention policy, allowed routines and share rules. Agents may only cross context boundaries when an explicit user request and policy allow it.

## Capability areas

| Area | Examples | Required safeguards |
|---|---|---|
| Research and learning | Research briefs, study schedules, quizzes, source analysis, revision plans | Source provenance, uncertainty, user correction, no fabricated grades/citations |
| Communication | Draft emails/messages, meeting summaries, follow-up drafts | Confirm recipients and exact send content before sending |
| Calendar and planning | Agenda, reminders, schedule proposals, time-zone-aware plans | Confirm changes and invitees; respect recurrence and availability |
| Documents and files | Create/edit docs, sheets, slides, PDFs and project folders | File scope, malware scan, validation and backup/restore |
| Software work | Repo audit, code change, test, PR draft, issue triage | Disposable workspace, credential scope, tests, diff and user approval for push/merge |
| Business operations | CRM summaries, support triage, reports, billing analysis | Workspace ACL, data minimization, no unauthorized financial decisions |
| Travel and local research | Compare options, itinerary, reservation research | Current source checks and user approval for bookings/purchases |
| Shopping and household | Compare products, subscriptions, maintenance research | Transparent price/source/time; never purchase without approval |
| Creative production | Images, video storyboards, presentations and content drafts | Rights review, user approval before public release |
| Health/finance/legal support | Organize documents, explain public information, prepare questions | Not a professional substitute; keep sensitive scopes off by default; qualified expert for decisions |

## Agent roles

Examples include researcher, study coach, software engineer, QA reviewer, project manager, operations analyst, writing assistant, document analyst, calendar planner, travel researcher, household organizer and creative producer. Each has narrow job instructions, tools, budgets and scope. Specialist agents cannot grant capabilities or approve themselves.

## Routine model

A routine has a user-visible purpose, trigger/cadence, context, input permissions, allowed tools, approval requirements, spend/time ceilings, notification settings, failure handling, retry policy and pause/revoke control. New routines start paused until reviewed. A routine may prepare a draft autonomously but does not silently send, purchase, book or delete.

## Memory model

Memory is opt-in and inspectable. Store typed records with source, owner, context, confidence, creation/expiry, consent state and deletion lineage. Distinguish durable user preferences, project facts, episodic task history and derived summaries. Never mix unrelated work/personal data. Provide correction, expiry and delete propagation into vector indexes, caches and derived summaries.

## Reliability and completion

The user sees current state, assigned agent, checkpoint, action/approval requirements and evidence. ORBIT verifies task-specific outcomes before declaring completion. For example: a file must exist and parse; code tests must actually run; a message must have a send receipt; a booking must have a booking confirmation; a reminder must have a durable schedule record.
