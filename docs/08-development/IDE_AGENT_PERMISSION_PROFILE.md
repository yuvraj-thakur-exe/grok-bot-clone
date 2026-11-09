# IDE agent permission profile

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Phase 0 audit (read-only)

Allowed: list/read repository files, inspect Git metadata, inspect package manifests and CI, run non-mutating test/lint/build commands where safe, browse official documentation. Disallowed: edit/delete/rename files, install packages, change Git state, access unrelated home directories, print secrets, use personal browser profiles, deploy or make external writes.

## Implementation (scoped write)

Allow file edits only under repository root. Permit dependency installs only after reviewing package scripts and lockfile changes. Permit test/build commands inside the repository and approved sandbox. Restrict network access to necessary registries/provider APIs/documentation. Do not expose production credentials.

## Approval-required

Delete/overwrite large or user-authored trees; reset/rebase/force push; install privileged tools; access private repositories not explicitly selected; push commits; create public issues/comments/PRs; send email/messages; publish releases; deploy; alter auth/permissions; read/rotate production secrets; incur paid external spend; execute destructive SQL.

## Stop conditions

Stop and report if Git state is dirty and the task would overwrite it; tests reveal baseline failure; credentials are missing; the request exceeds the authorized repo/domain; a human verification challenge appears; an approval is expired or payload changed; or sandbox isolation is uncertain.

## Desktop capability permissions

IDE agents must not automatically install or launch a local desktop driver, request OS Accessibility/Screen Recording permissions, inspect the user's open apps, or manipulate windows during repository coding tasks. Desktop testing requires a dedicated test session and an explicit task scope. IDE agents may inspect source/docs and build the fake driver by default; native actions are opt-in, local and auditable.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
