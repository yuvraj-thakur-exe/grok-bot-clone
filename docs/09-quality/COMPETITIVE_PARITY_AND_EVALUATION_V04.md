# Competitive parity and evaluation — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Position

ORBIT competes in the category of personal AI workspaces and multi-agent assistants. The goal is not to copy another product's appearance or promise every capability immediately. The goal is a reliable, extensible workspace that combines persistent agents, multiple models, computers/tools, connected applications, personal/work memory, routines and verified task outcomes.

## Reference feature surface

| Capability area | Baseline requirement for ORBIT | Evidence / inspiration |
|---|---|---|
| Multi-agent roster | Named agents with separate role, model, context and memory scopes | OpenMausBot public repo |
| Multi-channel presence | Web/desktop first; messaging adapters where demand justifies | OpenClaw and Hermes ecosystems |
| Agent workspaces | Per-agent/project folder, sandbox, browser and optional computer | OpenMausBot / OpenHands / OpenSandbox |
| Connected apps | OAuth/account links, least-privilege tools and revocation | OpenMausBot connector model; MCP standards |
| Persistent memory | User-controlled recall across sessions with provenance | Hermes docs; Mem0/Letta candidates |
| Scheduled work | Durable routines, webhooks, retry/recovery, run history | Hermes cron; Temporal candidate |
| Approval workflow | Exact approval cards for writes and sensitive side effects | OpenMausBot approval patterns |
| Browser/desktop | Separate isolated browser and paired local desktop capabilities | Stagehand/Playwright; agent-desktop |
| Skills ecosystem | Portable import/export, scanning, immutable locks and trust levels | Agent Skills; VoltAgent discovery index |
| Voice and multimodal | Voice input/output and image/document understanding, behind adapters | OpenClaw/Hermes/OpenMausBot ecosystem |
| Software engineering | Repository audit, code agent, isolated execution, test and PR output | OpenHands SDK |
| Self-improvement | Offline skill/tool/prompt optimization with held-out evaluation | Hermes self-evolution + DSPy |
| Audit and safety | Visible execution, cancellation, budgets, redaction and provenance | ORBIT-owned differentiator |

## ORBIT differentiators to build

1. **One source of truth:** user context, task state, agent identity, approvals, memory policy and artifact history live in one user-controlled workspace.
2. **Trust-first actions:** every backend and skill is subordinate to ORBIT's permission gateway; explicit stop/pause and exact approval.
3. **Reliable completion:** end-to-end verification, idempotency, recovery and evidence, not just generated messages.
4. **Portable teams:** export/import agent configurations and skills without transferring secrets, private history or live privileges.
5. **Personal + professional context:** separate scopes, project memory and user-approved routines without building hidden profiles.
6. **Runtime portability:** swap hosted models, local models, OpenClaw, Hermes and coding workers behind stable contracts.
7. **Open-source reuse:** upstream source, tests and improvements are retained instead of re-created as disconnected clones.

## Evaluation protocol

Create a fixed benchmark suite using synthetic or consented, redacted tasks. Include tasks from research, study, repository work, file/document work, communication drafts, scheduling, connected apps, browser workflows, desktop workflows and multi-agent delegation.

Report by task family and risk tier:

- end-to-end completion rate and partial completion rate;
- factual accuracy and evidence/citation correctness;
- side-effect correctness and unauthorized action count;
- approval precision (correctly requested, not bypassed, not over-requested);
- task recovery after process/provider/network failure;
- cancellation latency and confirmed stop rate;
- tool selection accuracy and invalid action rate;
- memory precision, stale-memory correction and cross-agent leakage;
- cost per successfully completed task and median/p95 latency;
- crash-free sessions, queue age, uptime and artifact integrity;
- user intervention rate, user satisfaction and task abandonment.

## Proposed non-negotiable safety gates

- Zero unauthorized high-impact side effects in release acceptance tests.
- 100% of sensitive write actions are policy-checked and audited.
- Every approval is bound to exact target and normalized parameters.
- Every mutating tool has explicit idempotency/delivery semantics or a read-before-retry reconciliation path.
- User can stop an active task and revoke a connector/device capability.
- No skill or plugin can widen its own permissions.
- No raw secrets or private desktop/browser content in logs/evaluation datasets.

Other quality thresholds are set after measuring a baseline; never fabricate competitor benchmark claims. Publish the dataset, model/provider/version, task conditions and confidence intervals for any public performance comparison.

## Release progression

- **Alpha:** one user, one workspace, one reliable agent, task log, model switch, file outputs and approval flow.
- **Beta:** agent roster, reusable skills, memory controls, connected apps, browser worker and scheduled tasks.
- **Public beta:** desktop/phone companion, multi-agent delegation, secure sandbox and selected external runtimes.
- **Competitive release:** cross-platform consistency, deep app connectors, voice, robust routines, portable team packages, recovery, privacy/security audit and measured benchmark performance.
