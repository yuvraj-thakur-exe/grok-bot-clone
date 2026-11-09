# Sequence Diagrams

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Research task
```mermaid
sequenceDiagram
 User->>API: Submit research goal
 API->>DB: Persist task/run
 API->>WF: Start workflow
 WF->>Model: Build plan
 Model-->>WF: Typed plan
 WF->>Gateway: Search request
 Gateway->>Policy: Validate scope/permission
 Gateway->>Search: Execute
 Search-->>Gateway: Sources + metadata
 Gateway->>DB: Persist evidence and audit
 Gateway-->>WF: Normalized results
 WF->>Model: Draft claim/evidence report
 WF->>DB: Persist artifact and completion
 API-->>User: Stream status and artifact
```

## Approved external action
```mermaid
sequenceDiagram
 Agent->>Gateway: Request exact action
 Gateway->>Policy: Evaluate risk
 Policy-->>Gateway: Approval required
 Gateway->>DB: Persist approval with payload hash/expiry
 Gateway-->>WF: Wait for signal
 User->>DB: Approve exact action
 WF->>Gateway: Resume with approval ID
 Gateway->>Policy: Revalidate target/hash/expiry
 Gateway->>Connector: Execute with idempotency key
 Connector-->>Gateway: Receipt/result
 Gateway->>DB: Persist audit/result
```

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
