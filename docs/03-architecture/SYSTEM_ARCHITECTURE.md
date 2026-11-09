# ORBIT System Architecture — v0.5 target

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Architecture style

Use a modular monolith for the first-party control plane with isolated workers for capabilities that execute code, browse the internet, manipulate files or control devices. Adopt existing upstream components behind contracts rather than putting their entire product architecture inside ORBIT.

## Control plane ownership

ORBIT is the canonical authority for:

- user, workspace, project, agent and conversation identities;
- task/run/step state, event ordering, deadlines, retries and cancellation;
- model/runtime selection policy and usage budgets;
- permissions, approvals, policy versioning and audit;
- memory consent, scope, provenance, retention, correction and deletion;
- skill source, digest, trust level, enablement and revocation;
- artifact metadata, lineage, access controls and final evidence;
- connector grants and secret references;
- user-facing UI, notifications and activity history.

External runtimes may maintain their own internal session state, but ORBIT maps every execution to an ORBIT `task_id`, `run_id`, `workspace_id`, policy snapshot and cancellation token.

## Layers

1. **Client workspace:** agents, projects, chat, tasks, activity, approvals, files, skills, routines, connectors, memory/privacy and settings.
2. **API/control plane:** authentication, authorization, workspace services, task state machine, event store, approval service, policy engine and stable API.
3. **Orchestration:** planner, agent coordinator, runtime adapter, context builder, verifier and budget manager.
4. **Tool/policy gateway:** schema validation, risk classification, authorization, approval, idempotency, quota and audit.
5. **Execution workers:** browser, coding/Git, document, research, connector, sandbox, desktop and media generation.
6. **Data services:** PostgreSQL, object storage, optional Redis, vector index and encrypted secret provider.
7. **Operations:** OpenTelemetry-compatible traces/metrics/logs, SBOM, vulnerability and license scanning, backups and release pipeline.

## Runtime composition

- **Product shell:** retain existing ORBIT shell if it already works. Otherwise evaluate a public OSS desktop shell. Do not run two independent product shells.
- **Agent runtime:** choose one default adapter. OpenClaw and Hermes may be optional backends, but neither owns ORBIT authorization or tasks.
- **Workflow:** one durable workflow owner for business task state. Temporal is the initial comparison candidate; LangGraph may model bounded reasoning/delegation graphs but must not duplicate persistence/retry authority.
- **Browser:** one BrowserDriver baseline. Playwright is the control baseline; compare Stagehand and agent-browser; Browser Use is an alternative for Python worker tasks.
- **Code execution:** one coding worker adapter with a disposable workspace. OpenHands SDK is the P1 candidate.
- **Sandbox:** Docker baseline; evaluate OpenSandbox behind a provider contract. Use microVM only after compatible infrastructure and benchmarks exist.
- **Memory:** ORBIT owns governance. Compare Mem0 and Letta; never let a memory library override consent or ACLs.
- **Knowledge:** LlamaIndex can be an ingestion/retrieval adapter. PostgreSQL and source records remain authoritative; Qdrant is optional derived vector storage.
- **Skills:** portable `SKILL.md` packages with ORBIT manifest, content digest, immutable source reference, trust review and permission policy.
- **Observability:** OpenTelemetry-compatible SDKs with redaction and retention enforced by ORBIT.

## Trust boundaries

The model process is not trusted to execute. Web pages, files, skill content, plugin output and connected-app events are untrusted input. Browser workers cannot reach host files. Code workers cannot reach the user's local device or unapproved internet destinations. Local desktop node is paired and runs only in the user's interactive session. External runtime adapters receive only the scoped capabilities required for one task.

Native/in-process plugins share the host process trust boundary. They are accepted only from trusted sources and reviewed before enabling. Untrusted plugins must run out-of-process with constrained IPC and network/filesystem policy.

## Task flow

Authenticate → authorize workspace → create durable task and idempotency key → select agent/runtime → snapshot policy and budget → plan → validate plan → execute typed tool request → require approval where policy says so → run isolated worker → persist normalized event and evidence → verify postcondition → checkpoint → continue/ask/cancel/complete. The UI can reconnect from the last event cursor. A model final answer is not proof of completion.

## Deployment units

Start with `web`, `api`, `workflow-worker`, `agent-runtime-adapter`, `browser-worker`, `code-worker`, `document-worker`, `connector-worker`, `postgres`, `object-storage` and optional `redis`/`otel-collector`. Do not deploy every candidate project as a permanent dependency. Split services only for measurable scale, ownership or isolation reasons.

## Failure and recovery

Each task has a deadline, step budget, cost budget, retry policy, cancellation token and checkpoint. External mutations carry idempotency keys and delivery classification. Unknown delivery is reconciled before any retry. Backend outage may trigger an explicitly permitted fallback model/runtime, but never a silent policy downgrade.
