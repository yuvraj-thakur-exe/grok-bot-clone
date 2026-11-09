# Low-Level Design Guidelines

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Modules: `identity`, `conversations`, `tasks`, `agents`, `llm`, `orchestration`, `tools`, `policy`, `approvals`, `research`, `files`, `browser`, `code`, `memory`, `skills`, `routines`, `connectors`, `telemetry`.

Domain services define interfaces; infrastructure adapters implement DB/provider/storage/workflow access. Use explicit state machines, typed contracts and stable errors. Tenant-owned records include `workspace_id`; authorization is applied in services/repositories. Persist results before notifying clients. Never hold DB transaction open across LLM or external network call. Use transactional outbox for event delivery. Store only necessary provider raw output and apply retention/redaction.

## v0.2 desktop module boundaries

`desktop_broker/` owns device enrollment, lease lifecycle, event routing and authorization metadata. `desktop_node/` owns local pairing, outbound connection, session detection, local policy, process runner and UI status. `desktop_driver/` normalizes the upstream CLI/C ABI contract. `desktop_policy/` owns allowlist, semantic risk and approval context. `desktop_contracts/` owns schemas and fixtures. Keep platform-specific code in the upstream driver; ORBIT's adapter must not import AX/UIA/AT-SPI APIs in the initial version.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
