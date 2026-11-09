# Codex / repository agent guide

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

`AGENTS.md` is the canonical repository-level policy file. Before implementation, open the repository root and verify the agent has loaded it; explicitly attach `CODING_AGENT_MASTER_PROMPT.md` and the relevant product/architecture/security documents. Run the Phase 0 audit prompt in `RUN_FIRST_IN_IDE_AGENT.md`.

Work one issue/vertical slice at a time. Ask the agent to inspect Git status, preserve user changes, implement tests and show the final diff. Keep approvals enabled for destructive shell commands and all external side effects. Never grant unrestricted host filesystem or Docker socket access to code-execution workers.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
