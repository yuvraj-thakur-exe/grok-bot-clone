# ORBIT v1.1 next execution plan

**Planning date:** 2026-11-08. **Owner:** human founder. **Coordination:** virtual CTO and specialist workflows.

## Goal

Move from a validated developer toolkit to a working ORBIT application without replacing useful existing source. The next release must prove one end-to-end user task through durable task state, permission checks, execution, verification and recovery.

## Current baseline

| Area | Evidence | State |
|---|---|---|
| Engineering specification | v1.0 package index, blueprint, source maps and operating documents | Documented |
| Local developer toolkit | `src/orbit_cli/`, launchers, task manifest and tests | Implemented; Linux smoke-tested |
| Cross-platform automation | Windows/macOS/Linux GitHub Actions matrix | Configured; remote runs pending |
| Upstream shortlist | Six exact Git SHAs and observed root-license files | Pinned candidates; no source adoption |
| Actual ORBIT app source | No app Git URL/path was available in this session | Blocked for source audit/integration |
| Production agent runtime | No runtime code was audited or verified in the recovered pack | Not established |

## Execution sequence

### M0 — Obtain and audit the real application source

**Lead:** Repository Operations + CTO. **Mode:** read-only.

1. Clone or access the existing ORBIT application source without changing its branch or dirty state.
2. Record current Git branch/status/history, tree, language/runtime versions, lockfiles, package manager and build/test commands.
3. Map UI, API, auth, tenancy, database, task workers, model providers, tools, memory, browser, desktop and sandbox code paths.
4. Review secrets handling, shell/process execution, filesystem mounts, network egress, dependency and license state.
5. Produce `REPOSITORY_BASELINE.md`, `IMPLEMENTATION_MATRIX.md`, `SECURITY_FINDINGS.md`, `ARCHITECTURE_GAPS.md` and `NEXT_MILESTONE_PLAN.md` based on actual evidence.

**Exit gate:** the human founder reviews the baseline before any invasive source edit. Existing features and dirty work are preserved.

### M1 — Canonical task and event vertical slice

**Lead:** Backend + CTO; QA independently verifies.

Deliver one persisted user workspace, conversation, task, ordered task-event stream, status transitions, cancellation and reconnect/replay. Use one canonical database authority for task, approval and audit state. Redis, if present, is ephemeral coordination only.

**Acceptance:** migrations apply and roll back; task state survives service restart; event ordering is deterministic; cancellation is acknowledged; reconnect returns the last durable event; workspace isolation tests pass.

### M2 — Model adapter and policy gateway

**Lead:** Agent Runtime + Security.

Implement one provider adapter behind the ORBIT-owned interface. Add typed tool schemas and one deterministic read-only tool. Every call checks workspace identity, capability, arguments, rate/budget, timeout and audit policy. Provider/model selection and fallback reasons are visible.

**Acceptance:** invalid schemas and unauthorized workspaces fail closed; provider failure is observable; no silent capability downgrade; tool calls are auditable; API keys never enter task logs or browser/desktop contexts.

### M3 — One approval-gated write workflow

**Lead:** Backend + Security + QA.

Add approval records bound to the exact action, normalized argument hash, target resource, user, workspace, policy version and expiry. Start with one low-risk workspace-local mutation. A changed target or argument hash invalidates prior approval.

**Acceptance:** no mutation executes before approval; stale/replayed approvals fail; duplicate submission is idempotent; audit records show proposed action, decision and final disposition.

### M4 — Disposable coding worker

**Lead:** Coding Worker + Sandbox + Security.

Compare the OpenHands SDK candidate with one simpler subprocess-based coding worker. Clone only selected pinned sources. Use a disposable workspace, resource/time quotas, no Docker socket, no broad host mount and deny-by-default network egress.

**Acceptance:** worker can inspect a repository, create a feature branch, make a small patch, run approved tests, show a diff and produce a reviewable artifact. It cannot commit, push, merge or deploy without explicit permission.

### M5 — Browser worker

**Lead:** Browser + Security + QA.

Use Playwright as the baseline behind `BrowserDriver`. Create isolated per-task browser contexts, domain/network policy, download quarantine and explicit credential/session handling. Keep browser DOM content untrusted.

**Acceptance:** allowed navigation works; disallowed domains and private-network targets are blocked; downloads are quarantined; cancellation closes the context; browser sessions do not leak between workspaces.

### M6 — Native desktop node

**Lead:** Desktop + Security + QA.

Implement a fake `DesktopDriver` contract first. Then prototype a paired local node in one logged-in interactive OS session. Use outbound authenticated WSS, short-lived leases, explicit pairing/revocation, local stop/pause and read-only commands first.

**Acceptance:** lost connection expires the lease; node-local policy rejects unauthorized operations; snapshots/refs are short-lived; no mutation is retried under unknown delivery; no screenshots/clipboard/raw trees enter ordinary telemetry.

### M7 — Memory, skills and routines

**Lead:** Memory/RAG + Workflow + Privacy.

Add user-visible, scope-aware memory with inspect/correct/delete controls; reviewed skill versions and digest pins; durable schedules and event-triggered routines. Do this only after task reliability and audit behavior are established.

### M8 — Multi-agent coordination

**Lead:** CTO + QA + Security.

Add bounded specialist delegation with a dependency DAG, separate workspaces, read-only shared context by default, independent verification, cancellation and cost/time budgets. Multi-agent orchestration is not a substitute for the single-agent reliability gates.

## Cross-workstream invariants

- ORBIT owns identity, workspaces, tasks, approvals, user memory consent, policies and audit.
- Browser, native desktop and code execution are separate security domains.
- Model output and repository content are untrusted proposals, never permissions.
- One writer per mutable resource; parallelize read-only or isolated worktrees.
- Use a single retry owner and explicit delivery disposition for side effects.
- All external operations have bounded time, output, resource use and cancellation.
- Upstream source adoption requires exact commit, path hashes, license/NOTICE review, dependency closure, tests, ADR, security review and rollback plan.
- Human approval remains mandatory for spend, external account connections, legal commitments, public communication, production credentials and production releases.

## Next input required

The actual ORBIT application GitHub URL or local repository path. Without it, we can improve the developer toolkit and source-intake process, but cannot honestly audit or integrate the application itself.
