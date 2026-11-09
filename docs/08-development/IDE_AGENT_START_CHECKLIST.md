# IDE coding-agent start checklist

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Before changing files

- [ ] Open the real ORBIT repository root, not just this documentation ZIP folder.
- [ ] Read `AGENTS.md` and `CODING_AGENT_MASTER_PROMPT.md`.
- [ ] Read project charter, PRD, MVP, architecture, ADRs and threat model.
- [ ] Run `pwd`, list root files and inspect package manifests/lockfiles.
- [ ] Run `git status --short --branch`; preserve all local modifications.
- [ ] Identify current app entrypoints, scripts, CI, migrations and test suites.
- [ ] Search TODO/FIXME and existing feature implementations.
- [ ] Run safe baseline checks and record exact pass/fail output.
- [ ] Never print `.env` values, browser cookies, key files or credential contents.
- [ ] Create `docs/current-state/REPOSITORY_AUDIT.md`.

## First implementation slice

- [ ] Authenticated identity and workspace ownership.
- [ ] Create conversation and task records.
- [ ] One provider adapter with deterministic mock provider.
- [ ] Stream assistant response and persist ordered messages.
- [ ] Persist task lifecycle and replayable event stream.
- [ ] Cancel and reconnect behavior.
- [ ] Tenant isolation tests and provider failure tests.
- [ ] Update README with actual verified commands.

## Review before merge

- [ ] Inspect diff and untracked files.
- [ ] Check dependency and license changes.
- [ ] Check authorization, secrets, logging and external side effects.
- [ ] Run lint, typecheck, tests, build and migrations relevant to the change.
- [ ] Update requirements traceability and ADRs.
- [ ] Report what is implemented, mock, unconfigured, not tested or blocked.

## v0.2 desktop-specific checklist

- [ ] Read the upstream agent-desktop README, AGENTS, CONCEPTS, JSON contract and OS skills.
- [ ] Record exact commit, package version, contract version, checksum, license and target OS support.
- [ ] Implement fake DesktopDriver and contract tests before installing/using real desktop driver.
- [ ] Confirm all tool calls pass through central gateway and node-local policy.
- [ ] Confirm node pairing, outbound WSS, expiring leases, pause/stop and revocation.
- [ ] Ensure no shell string interpolation and no arbitrary command argument tool.
- [ ] Verify read-only output caps, completeness and sensitive-data redaction.
- [ ] Test stale/ambiguous refs and delivery-aware no-retry behavior.
- [ ] Keep screenshot/clipboard and physical input disabled by default.
- [ ] Run tests on dedicated interactive OS sessions, not a personal daily desktop.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
