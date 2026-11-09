# Coding standards

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

- TypeScript strict mode; Python type hints and static checks on public interfaces.
- Format and lint in CI; no ignored lint failures without a tracked decision.
- Small modules with explicit dependency direction; avoid god objects and giant utility files.
- Validate all external data at boundaries (Pydantic/Zod or equivalent).
- Use structured logging with correlation IDs and redaction.
- Avoid mutable global state; make time, provider clients and storage injectable for tests.
- Use parameterized SQL and repository/application boundaries.
- Write meaningful tests with bug fixes and new behavior.
- Use conventional commits or the existing repository convention; never rewrite shared history without authorization.
- Keep generated files clearly marked and regenerated from source contracts.
- Update docs and changelog when behavior, API, configuration or architecture changes.

## Desktop adapter coding standards

No `shell=True` or shell command concatenation. Use fixed executable path + argv vector, strict schemas, bounded output/timeouts and process-tree cancellation. Treat upstream output as untrusted; require JSON contract/version validation and explicit disposition. Avoid storing snapshot refs beyond the current operation sequence. Use enum states rather than boolean success flags. Add tests for unknown and contradictory evidence.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
