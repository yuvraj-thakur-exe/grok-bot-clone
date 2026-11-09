# Claude Code / instruction-file guide

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

`CLAUDE.md` is a short entry point that directs the agent to `AGENTS.md` and the master prompt. Keep the full security and engineering rules in `AGENTS.md` so IDE-specific files do not drift. Confirm Claude Code's active instruction files for the current repository before editing. Use the read-only Phase 0 audit first; then issue narrow implementation tasks with requirement IDs and acceptance tests.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
