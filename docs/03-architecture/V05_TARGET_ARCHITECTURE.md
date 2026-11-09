# ORBIT v0.5 target architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## 1. The product is a workspace, not a chat clone

The workspace is composed of projects, agent identities, conversations, durable tasks, connected tools, files/artifacts, memory, skills, schedules, approvals and activity history. Every user-visible object belongs to a user/workspace/project scope with explicit sharing rules.

## 2. Single source of truth

ORBIT owns task/workspace identity, permissions, policy decisions, user approvals, business-level task status, audit, artifact metadata, memory consent, skill trust and connector grants. Agent runtimes may store their internal context, but that state is mapped to the ORBIT task and is never a substitute for ORBIT authorization.

## 3. Reference composition

```text
ORBIT clients (web / desktop / mobile / API)
                 |
          ORBIT API + Auth
                 |
     Workspace / Project / Agent Registry
                 |
     Task State + Event Store + Workflow
                 |
     Planner / Specialist Coordinator
                 |
        Policy + Approval Gateway
       /          |            \
  AgentRuntime  ToolRegistry    Memory/RAG
   adapters       |              |
   /   |   \   isolated workers  |
OpenClaw Hermes OpenHands   Browser / Code / Docs
                             Sandbox / Desktop
                 |
        Artifacts + Evidence
                 |
           UI + Audit
```

The diagram expresses logical ownership, not mandatory service deployment. A single process may implement multiple control-plane modules initially.

## 4. Core contracts

- `AgentRuntimeAdapter`: start/resume/cancel task execution; emit normalized text, tool, progress, usage, error and artifact events.
- `BrowserDriver`: open, observe, act, extract, screenshot and close within an ORBIT-controlled browser context.
- `SandboxProvider`: create, inspect, execute, stream, cancel, export and destroy disposable workspace.
- `MemoryProvider`: search/upsert/archive/retrieve; every operation includes user/workspace/project/agent scope and provenance.
- `SkillInstaller`: resolve immutable source, verify digest and license evidence, inspect permissions, stage for review, then activate after approval.
- `WorkflowProvider`: durable timers, retries, checkpoint and recovery while ORBIT retains task-state authority.
- `ConnectorProvider`: OAuth/account linking or secret references with explicit scopes and revocation.

## 5. Computer-use boundaries

Browser automation is not native desktop control. Code execution is not browser automation. Remote sandbox desktop is not a local device. Each has separate credentials, filesystem access, network policy, lifecycle, logs, stop controls and user consent.

## 6. Agent team design

Each specialist has a role description, model/runtime preference, context scope, skill allowlist, tool grants, memory namespace, budget and max parallel tasks. The coordinator provides bounded subtasks with explicit input/output schemas. Agents cannot enlarge their own capabilities, approve their own risky operations, or grant permissions to other agents.

## 7. Personal/work context model

Personal, study, family/household, project, client and employer contexts are separate namespaces. Cross-context transfer is explicit and logged. Users can inspect and delete memories, connectors, files and routines in a context. Do not mix employer/private data or unrelated projects by default.

## 8. Product experience

The UI includes global task inbox, agent roster, project spaces, live activity, approvals, artifact gallery, integration/skill catalogue, routines, memory controls, cost/usage and device trust. A task should show status, plan, active agent, tool calls, approval waits, checkpoints and evidence. Users can take over or cancel without losing history.

## 9. Non-functional gates

Tenant isolation, permission correctness, cancellation propagation, delivery certainty, recovery, prompt injection resilience, skill sandboxing, browser egress, secret hygiene, provenance and backup/restore are release blockers. Performance claims require reproducible benchmarks, not upstream README numbers.
