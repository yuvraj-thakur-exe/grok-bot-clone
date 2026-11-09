# v0.3 integration workstreams

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Goal:** turn research into independently testable adapters, not a large vendor merge.

| Workstream | Priority | First outcome | Depends on | Exit criteria |
|---|---|---|---|---|
| A. Current repository audit | P0 | Verified baseline and architecture map | Repository access | No unknown duplicate modules; requirements mapped |
| B. Core task/event contract | P0 | One durable task vertical slice | DB/API baseline | Restart, stream reconnect, cancel, idempotency tests |
| C. Tool Policy Gateway | P0 | Typed read-only tools and audit | Identity/workspaces | Deny-by-default, exact approval binding, cross-tenant tests |
| D. Provider gateway evaluation | P1 | Model capability/cost/fallback PoC | B/C | No nested retry; spend attribution; output parity |
| E. Browser driver comparison | P1 | BrowserDriver conformance PoC | C, sandbox policy | Playwright baseline vs agent-browser; egress tests |
| F. Disposable code sandbox | P1 | Safe repo clone and test workflow | C | no host mounts/socket, deny egress, quota and cleanup |
| G. Durable workflow decision | P1 | Temporal vs simpler engine experiment | B | replay/idempotency/recovery report; ops estimate |
| H. Skill registry | P1 | Validated local skills with lockfile | C, license gate | immutable digest, license metadata, scan, review, rollback |
| I. Generative UI | P2 | Catalog-limited task/report surface | UI design system, tool gateway | malformed JSON and arbitrary actions rejected |
| J. External agent backends | P2 | AgentBackend adapter proof | sandbox, audit, tasks | cancellation, scoped credentials and artifacts verified |
| K. Desktop Node | P2 | Read-only one-OS prototype | Identity/device, local app | paired lease and safe observe/stop; no sensitive mutations |
| L. Rebranding | P1 | ORBIT-only first-party UI foundation | Founder brand approval | original assets, vendor-neutral naming, legal notices retained |
| M. License & SBOM gate | P0/P1 | Component register and release check | Dependency inventory | no unknown or unapproved component in release artifact |
| N. OTel instrumentation | P1 | Task trace across API/model/tool/worker | B/C | correlation and sensitive-data redaction tests |

## Founder decisions needed

1. Approve the brand direction and trademark search budget.
2. Choose ORBIT distribution posture (self-hosted open source, hosted service, commercial enterprise, or dual model).
3. Approve first sandbox threat level (local developer convenience vs hostile-code isolation requirement).
4. Select initial model providers and cost ceilings.
5. Decide if first desktop support is Windows-only for development, then add macOS/Linux after the fake driver contract.
6. Approve the project license only after the exact dependency and asset inventory is reviewed.

## Suggested implementation sequence

1. Audit existing ORBIT repo and protect existing working functionality.
2. Implement task + event + cancellation + audit path.
3. Implement deterministic tool gateway and model provider adapter.
4. Establish sandbox before running repository-supplied code.
5. Implement repository worker and browser driver.
6. Add skill registry with supply-chain policy.
7. Add generative UI after action authorization is stable.
8. Add external agents and multi-agent coordination after one-agent recovery works.
9. Add Local Desktop Node after security, pairing and session requirements are tested.
10. Production readiness, legal review, branding freeze, SBOM, release provenance and restore drills.
