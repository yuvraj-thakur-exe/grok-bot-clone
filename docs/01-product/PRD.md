# Product Requirements Document — ORBIT v0.5

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Summary

ORBIT is a planned personal and work AI operating system: a workspace that lets a user create specialist agents, assign multi-step tasks, connect tools and devices, keep scoped memory, collaborate across projects, and review verifiable outcomes. It should integrate mature open-source components rather than independently re-create every gateway, browser, coding agent or connector.

## Problem

People's digital work is scattered across chat, search, browser, email, calendar, project management, code, files, documents and personal devices. Current assistants often lack durable context, useful task continuity, transparent permissions, reliable recovery, and evidence that external work actually completed.

## Product goals

1. Deliver a coherent multi-agent workspace rather than a model chat wrapper.
2. Preserve user control over identity, memory, credentials, data scopes and permissions.
3. Complete bounded multi-step work through durable tasks, checkpoints, cancellation and verification.
4. Support model and agent-runtime portability.
5. Reuse high-quality open-source systems through documented adapters and source provenance.
6. Support personal, education, software engineering, research, creative and business workflows.
7. Make actions and artifacts inspectable, exportable and reversible where possible.
8. Scale capabilities progressively without overloading the first release.

## Primary personas

- Individual builder or researcher managing projects and files.
- Student/learner planning, studying, revising and creating work products.
- Software developer delegating repository research, code changes and tests.
- Knowledge worker handling communication, schedules, documents and research.
- Small team coordinating specialist agent work.
- Self-hosting administrator controlling integrations, security and retention.
- Skill/integration developer extending ORBIT through documented contracts.

## Core user journeys

1. **Ask and complete:** create a task, inspect a plan, watch progress, approve risky action, review evidence and final artifact.
2. **Research:** search sources, extract claims, compare evidence, generate cited report and save into project knowledge.
3. **Build software:** authorize a repository, clone into a disposable workspace, inspect, plan, patch, test, review diff and prepare a PR for approval.
4. **Specialist team:** delegate scoped subtasks to researcher, developer, analyst or writer agents, then verify and consolidate outputs.
5. **Personal organization:** triage calendar/inbox/notes, prepare drafts and reminders; require approval before sending or changing external state.
6. **Study:** make a syllabus plan, create practice questions, evaluate answers and track progress without fabricating grades or results.
7. **Files and artifacts:** generate/edit documents, spreadsheets, presentations, diagrams and project assets; validate the exported file.
8. **Computer use:** choose browser, isolated remote desktop, sandbox or paired local desktop; see capability and permission state; pause/stop at any time.
9. **Routine:** configure an explicit schedule/trigger, review the proposed action scope, pause/revoke, and inspect run history.

## Scope by capability

### Foundation

Authentication, workspaces, projects, role/agent profiles, conversation/task state, durable event stream, model adapter, usage controls, approvals, audit, artifacts and settings.

### Execution and intelligence

Tool gateway, web search and source extraction, code worker, browser driver, document pipeline, sandbox, memory/RAG, skills, connectors, multi-agent delegation, durable routines and native desktop node.

### User-facing surface

Agent roster, project context, task/activity feed, approvals inbox, artifact browser, integrations catalogue, skills marketplace with trust labels, routine manager, memory inspector and privacy settings.

## Reuse policy

The product shell and underlying runtimes are candidates, not approved implementation decisions. Preserve existing ORBIT functionality if present. If no usable shell exists, prototype the public OpenMausBot OSS edition excluding `enterprise/`. Evaluate OpenClaw and Hermes as optional backends. Evaluate OpenHands for coding, one browser driver behind `BrowserDriver`, one sandbox provider behind `SandboxProvider`, one memory implementation behind `MemoryProvider`, and one durable workflow owner.

## Non-functional requirements

- Clear tenant/workspace isolation, strong authorization and auditability.
- Durable task recovery, idempotency, cancellation and bounded concurrency.
- No secrets in prompts, logs, telemetry or committed config.
- Least-privilege credentials and task-scoped worker access.
- Isolation for untrusted code, skills and extensions.
- Responsive UI with clear status, approvals and user takeover.
- Provider/runtime portability and explicit capability discovery.
- Source provenance, SBOM, license and vulnerability gates.
- Data export, retention, correction/deletion and backup/restore.
- Performance and cost measurement on representative completed tasks.

## Product exclusions and boundaries

- No claim that ORBIT itself is a new frontier foundation model.
- No uncontrolled access to the host OS or other users' accounts.
- No bypassing authentication, access controls, paywalls or security prompts.
- No automatic purchase, payment, booking, publishing, sending, deletion or production deployment without explicit applicable approval.
- No mass installation of public skills.
- No unreviewed self-modification or automatic model-weight training.
- No marketing claim of capability until it has passed the defined tests.

## Release strategy

First MVP: one polished workspace, one agent/runtime, one durable task flow, one safe tool, one approval path, one artifact/evidence path and reliable cancellation/reconnect. Specialist agents, many connectors, complex desktop use and autonomous routines are subsequent milestones gated by measured reliability.
