# Desktop automation validation matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Test tiers

| Tier | Runner | Purpose |
|---|---|---|
| Unit | Pure tests | Policy, schemas, risk classifier, ref lifecycle, disposition parser, lease state machine |
| Contract | Fake driver fixtures | CLI JSON envelopes, malformed response, old/new contract, partial snapshots, retry semantics |
| Integration | Local mock broker/node | Pairing, authentication, lease expiry, reconnect, cancellation and audit |
| OS integration | Dedicated interactive VM/host | Real accessibility APIs, permissions, apps and platform limits |
| E2E | Exclusive disposable desktop account | End-to-end task with visible UI and screenshots only under explicit test consent |
| Security | Red-team harness | Prompt injection, replay, command injection, cross-tenant and data leakage |

## Required test cases

| ID | Scenario | Expected |
|---|---|---|
| DESK-001 | Device unpaired | No lease or action; clear pairing guidance |
| DESK-002 | Invalid/replayed pairing token | Reject; audit event |
| DESK-003 | Revoked device uses old lease | Reject immediately |
| DESK-004 | Lease expires during idle | New mutation refused |
| DESK-005 | WSS disconnect during action | Action disposition unknown unless driver proves non-delivery; no retry |
| DESK-006 | Permission denied | No bypass; status and manual OS guide |
| DESK-007 | Unsupported OS/app capability | Capability-unavailable response |
| DESK-008 | Complete accessibility snapshot | Parse and preserve refs/metadata |
| DESK-009 | Partial snapshot | `complete=false`; no absence inference |
| DESK-010 | Stale ref after click | Reobserve; do not retry stale ref |
| DESK-011 | Ambiguous identical controls | Fail closed; no coordinate fallback automatically |
| DESK-012 | Check state already satisfied | Idempotent success or no-op after state observation |
| DESK-013 | Toggle action loses response | Do not repeat; inspect current state |
| DESK-014 | Explicit not-delivered + safe retry | Retry only within bounded policy |
| DESK-015 | Unknown or malformed disposition | Retry unsafe; pause and raise error |
| DESK-016 | Click Send/Delete/Purchase | Risk classifier requires approval or denies |
| DESK-017 | Approval argument hash changed | Approval invalidated |
| DESK-018 | UI prompt injection | No policy/secret/tool escalation |
| DESK-019 | Two agent tasks request mutation | Serialize; second waits or refuses |
| DESK-020 | Screenshot without grant | Denied; no artifact stored |
| DESK-021 | Clipboard request with no grant | Denied; content not logged |
| DESK-022 | Driver prints > max output | Truncate/refuse safely; no unbounded memory |
| DESK-023 | Argument contains shell metacharacters | Passed only as validated literal argv or rejected; never interpreted by shell |
| DESK-024 | Node pause pressed during active task | Block new actions and show in-flight disposition |
| DESK-025 | Device OS session changes/locks | Pause, invalidate lease and refs |
| DESK-026 | Cross-workspace device lookup | 403/404; no metadata leak |
| DESK-027 | Unsupported driver contract version | Refuse mutation and request compatible upgrade |
| DESK-028 | User removes node package | Device becomes offline; tasks recover without false completion |

## Platform validation

- macOS: Accessibility permissions, Screen Recording separately, native AX tree, headless semantic operations, menu/sheet/dialog, multiple windows, app restart and permission revocation.
- Windows: UIA tree, interactive user session, stale/ambiguous identity, elevated process boundary and locked/secure desktop refusal.
- Linux: AT-SPI availability, Ubuntu baseline, GNOME apps, X11/Wayland capability differences, sandboxed app visibility and missing accessibility bridge.

Do not mark a platform supported from compile-only CI. A real desktop integration lane is required for each advertised platform and capability.

## ORBIT v0.2 alignment

The v0.2 quality plan adds real interactive OS tests separate from browser/API tests. Cover permission, incomplete trees, stale refs, ambiguous target, unknown delivery and local stop; see `DESKTOP_AUTOMATION_TEST_MATRIX.md`.
