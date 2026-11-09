# Open questions and explicit unknowns

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

These decisions should be answered from repository inspection, product testing or owner decision; this pack does not invent them.

- What code currently exists in the ORBIT repository, and what branches/uncommitted work must be preserved?
- Is the first target desktop-local, self-hosted single-user, or multi-tenant cloud?
- Which operating systems must the computer-use worker support?
- Which authentication provider and deployment region are selected?
- What is the initial cloud budget and expected concurrency?
- Which model providers/accounts are available for live testing?
- What privacy and retention defaults are required?
- Is user-controlled persistent browser sign-in required in MVP?
- Which external connectors are first-class, beyond GitHub and MCP?
- What legal review is required before public hosted service and skill marketplace?
- What license is intended, and are all dependencies compatible?
- What are the measured baseline targets for task success, latency and cost?

Until resolved, use conservative secure defaults and keep the decision configurable where safe.

## Desktop questions to resolve during implementation

- Which OS is the first supported target for the Local Desktop Node and which test machine is available?
- How will installers, code signing/notarization and auto-update be managed for each OS?
- Which package distribution mechanism is approved for the upstream driver, and how will checksum/signature be verified?
- Is outbound WSS sufficient for the target self-hosted deployment and what proxy restrictions matter?
- What exact local presence signal is required before a node accepts actions?
- Which UI actions are safe enough for the first mutation beta, and which remain blocked?
- What retention duration applies to user-approved observation artifacts?
- Does subprocess execution meet latency needs, or does measured evidence justify C FFI?

Do not resolve these by guessing. Record decisions in ADRs after prototype evidence.

## ORBIT v0.2 alignment

The v0.2 guide set adds a Local Desktop Node setup target. Treat it as planned until code, installers and OS tests exist; see `DESKTOP_NODE_QUICKSTART.md` and `FEATURE_STATUS.md`.
