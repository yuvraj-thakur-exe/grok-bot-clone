# Critical acceptance test cases

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Scenario | Expected result |
|---|---|---|
| QA-001 | Create basic chat task | Task persisted and response streams |
| QA-002 | Reconnect SSE after disconnect | Events resume without duplication or gap |
| QA-003 | Provider returns rate limit | bounded retry/fallback or transparent pause |
| QA-004 | Workspace ID tampered | request denied and audited |
| QA-005 | Browser page contains prompt injection | page text cannot grant tools or expose secrets |
| QA-006 | Task requires outbound message | exact approval presented before send |
| QA-007 | Approval args changed after review | execution denied; new approval required |
| QA-008 | Worker crashes after checkpoint | workflow resumes without duplicate side effect |
| QA-009 | Upload archive bomb | quarantined/rejected within resource limits |
| QA-010 | Code worker attempts host access | denied by sandbox boundary |
| QA-011 | Routine runs twice on same event | deduplicated by idempotency key |
| QA-012 | User deletes memory | memory and derived vectors removed per policy |
| QA-013 | MCP tool declares excessive scope | rejected or requires explicit policy review |
| QA-014 | User cancels task | cancellation propagated and terminal status recorded |
| QA-015 | Provider lacks vision | route rejected or capability limitation disclosed |

Expand each test with setup, exact commands, fixtures, assertion and evidence location before a release.

## Desktop test case reference

Use `DESKTOP_AUTOMATION_TEST_MATRIX.md` as the authoritative desktop case set. Tests must include stale/ambiguous refs, incomplete snapshots, session lock, node disconnect mid-action, replayed lease, high-impact button click, privacy controls and no automatic retry on unknown delivery.

## ORBIT v0.2 alignment

The v0.2 quality plan adds real interactive OS tests separate from browser/API tests. Cover permission, incomplete trees, stale refs, ambiguous target, unknown delivery and local stop; see `DESKTOP_AUTOMATION_TEST_MATRIX.md`.
