# ORBIT upstream runtime adapters — v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Goal

Import and operate existing runtimes without leaking their internal types across ORBIT boundaries. ORBIT controls task state and permissions; upstream backends provide execution capability.

## Adapter contracts

### AgentRuntimeAdapter

```ts
export interface AgentRuntimeAdapter {
  id: string;
  capabilities(): Promise<RuntimeCapabilities>;
  start(input: StartAgentTask): Promise<RuntimeSession>;
  send(sessionId: string, input: AgentMessage): Promise<void>;
  interrupt(sessionId: string, reason: string): Promise<InterruptResult>;
  events(sessionId: string, cursor?: string): AsyncIterable<RuntimeEvent>;
  exportArtifacts(sessionId: string): Promise<RuntimeArtifact[]>;
  close(sessionId: string): Promise<void>;
  health(): Promise<RuntimeHealth>;
}
```

### RuntimeCapabilities

Declare model providers, modalities, streaming, structured outputs, tool support, memory behavior, subagents, file access, browser/desktop access, cancellation quality, session persistence, usage accounting and known restrictions. Unknown is not equivalent to supported.

### RuntimeSession

ORBIT-generated stable session ID, backend session handle (secret or opaque), task ID, agent ID, workspace ID, backend ID, created/updated timestamps and policy profile. Do not expose backend session bearer values to the client.

### RuntimeEvent

`message_delta`, `tool_requested`, `tool_authorized`, `approval_required`, `tool_started`, `tool_progress`, `tool_completed`, `artifact_created`, `usage_reported`, `needs_input`, `failed`, `cancelled`, `completed`. Every event has an ORBIT task ID, sequence, timestamp, backend source and redacted payload.

## Backend decisions

| Backend | Initial role | Integration mode | Excluded ownership |
|---|---|---|---|
| OpenMausBot-derived harness | Desktop product shell and local agent process lifecycle | First-party fork/adaptation if chosen after audit | Does not own ORBIT identity/central permissions outside delegated scopes |
| OpenClaw | Channel/gateway/plugin runtime or optional agent backend | Process/container + gateway client/protocol adapter | Does not become ORBIT's canonical task DB, user DB or approval authority |
| Hermes Agent | Optional model/agent execution backend | CLI/ACP/process or supported API adapter | Does not become a second ORBIT control plane |
| OpenHands SDK | Coding/software engineering worker | SDK/Agent Server adapter with disposable workspace | No access to unrelated personal data |
| Stagehand / Playwright | Browser automation | One selected `BrowserDriver` implementation | Browser session is not the user's native desktop or shell |
| Mem0 | Memory extraction/retrieval | `MemoryProvider` adapter under ORBIT governance | No direct authority over profile, consent or retention |
| LlamaIndex + Qdrant | Document ingestion and vector retrieval | `KnowledgeIngestionAdapter` + `VectorIndexAdapter` | PostgreSQL/source metadata remains canonical; enforce document ACLs |
| Temporal / LangGraph | Durable workflows / agent graph logic | One chosen workflow owner plus optional graph planner | No overlapping retry or business-state authority |
| OpenTelemetry | Instrumentation | Shared ORBIT telemetry SDKs/exporters | No raw prompt, secret or personal-content export |

## Memory, knowledge and workflow adapter rules

- ORBIT owns consent, visibility, memory scope, source provenance, confidence, expiry, correction and deletion.
- Mem0 is a candidate extraction/retrieval adapter; Letta is an alternative stateful-agent backend. Benchmark before choosing one. Never allow both to become independent profile stores.
- LlamaIndex may normalize/ingest documents, but every chunk retains tenant, project, document ACL, source URI, page/offset and content hash. Qdrant is an index, not the authoritative document or memory store. Deletion must propagate to source chunks and vector points.
- Temporal is the durable schedule/retry/workflow candidate. LangGraph is the agent graph/control candidate. Pick one owner for each retryable side effect and document checkpoint/replay behavior.

## Runtime isolation requirements

- Run each backend with a distinct service identity and OS/container boundary where supported.
- Use one short-lived task-scoped credential set; inject secrets at runtime, never into prompts or workspace files.
- Restrict process arguments, environment, workspace and egress. Never pass the Docker socket or broad host mounts.
- Treat backend tool calls as proposals. ORBIT reauthorizes them at its own policy gateway.
- Backend event payloads and transcripts are untrusted data; redact and normalize before storing.
- Set per-task wall time, output size, token/cost, tool count and concurrency limits.
- Preserve exact cancellation semantics: requested, accepted, completed, unknown. Do not report cancelled before execution has stopped or been fenced off.
- Reconcile backend artifacts by checksum and allowed output path.

## State ownership and sync

ORBIT is authoritative for user, agent, task, approval, budget, artifact metadata, external-account links and audit records. Backends may own private execution sessions and internal conversation state. A bridge maps backend messages/events to ORBIT events. Do not dual-write user profile or canonical task state.

## Retry ownership

There must be one retry owner per operation. The runtime must declare whether it automatically retries model/tool calls. ORBIT may retry only idempotent operations with a known delivery state and idempotency key. A write whose delivery is unknown is reconciled by reading external state before any retry.

## Contract test suite

1. start/resume/close session with stable IDs;
2. stream sequence monotonicity and reconnect cursor;
3. cancellation at planning, tool-started and long-running execution;
4. task/workspace identity mismatch rejection;
5. scoped tool proposal forwarded to central policy gateway;
6. expired/revoked credential rejection;
7. backend outage and process crash recovery;
8. no duplicated side effects after replay/retry;
9. artifact path traversal and oversized output rejection;
10. backend event prompt-injection containment;
11. cost and usage reconciliation;
12. capability negotiation correctly reports unsupported features.
