# Antigravity / agentic IDE guide

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Use `AGENTS.md` and `RUN_FIRST_IN_IDE_AGENT.md` as the canonical instruction source. If the IDE supports repository rules, point it to `AGENTS.md`; if it supports only an instruction prompt, paste the content of `RUN_FIRST_IN_IDE_AGENT.md` at the start of the session. The `.agent/rules/orbit.md` file is provided as a portable rules copy, but support and precedence vary by IDE version. Verify the actual IDE's instruction-loading behavior rather than assuming a filename is automatically loaded.

Start in read-only/audit mode. Give file-write permissions only to the ORBIT repository. Keep external browser writes, production deployment, account permission changes, destructive operations and secret access approval-gated. Do not provide the agent with personal browser profiles or production keys during initial development.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
