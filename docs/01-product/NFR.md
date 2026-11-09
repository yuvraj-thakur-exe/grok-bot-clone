# Non-Functional Requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Requirement |
|---|---|
| NFR-001 | Server-side tenant/workspace authorization on every path |
| NFR-002 | Secrets excluded from prompts, ordinary logs and artifacts |
| NFR-003 | Browser/code workers isolated from API and host |
| NFR-004 | Long-running tasks durable and recoverable |
| NFR-005 | Bounded retries and idempotency for side effects |
| NFR-006 | Near-real-time task progress, measured under load |
| NFR-007 | Provider latency reported per model/provider |
| NFR-008 | API and workers scale independently |
| NFR-009 | Correlation IDs and safe structured telemetry |
| NFR-010 | User inspect/export/correct/delete controls for memory/data |
| NFR-011 | Domain logic independent of vendor SDKs |
| NFR-012 | Local Compose and documented self-hosting |
| NFR-013 | Keyboard/screen-reader/contrast accessibility |
| NFR-014 | Per-workspace/task cost and resource budgets |
| NFR-015 | Pinned compatible dependency versions |

Initial internal targets only: API read p95 <250 ms under documented local test load; event delivery p95 <1 s; zero silent task loss in recovery tests. These are not published SLOs until measured.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.

## v0.3 ecosystem non-functional requirements

- External agent backends must be tenant-isolated, capability-declared, cancelable where supported and event-replayable or explicitly disclose replay gaps.
- Sandbox runtimes must enforce CPU, memory, storage, PID, time and egress constraints at the runtime/network layer.
- Skills must be reproducible by immutable source reference and content digest; unreviewed executable content remains quarantined.
- Generated UI must be schema-valid, size-bounded, accessible and incapable of evaluating model-generated code.
- Release artifacts must be reproducible enough to identify exact software components and preserve required notices.
- Brand assets must have source and license provenance; trademark clearance status must not be represented as approved when unresolved.
