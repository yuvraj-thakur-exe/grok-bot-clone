# ORBIT v0.5 — capability benchmarks and acceptance gates

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Evaluation philosophy

A feature counts as implemented only when a reproducible test demonstrates it in the target build. Marketing parity or upstream screenshots are not acceptance evidence. Track task success, safety, recovery, cost, latency and user intervention together.

## Core benchmark dimensions

| Dimension | Metric examples | Release requirement |
|---|---|---|
| Task completion | objective success, partial completion, postcondition accuracy | Evidence-backed completion on a frozen evaluation set |
| Tool choice | correct tool selection, invalid arguments, unnecessary tool calls | Typed schema and policy tests pass |
| Reliability | crash recovery, reconnect, duplicate suppression, cancellation latency | No silent task loss; mutation idempotency/reconciliation verified |
| Safety | unauthorized action rate, approval bypass, prompt injection success | Zero known approval bypass in release-blocking test suite |
| Memory | retrieval precision, source attribution, cross-scope leakage, deletion propagation | No cross-workspace leakage; deletion verified end-to-end |
| Browser | task success, domain policy, egress isolation, stale page handling | BrowserDriver conformance and prompt-injection tests pass |
| Coding | build/test success, diff quality, workspace escape, secret leakage | Disposable workspace containment and repeatable test receipt |
| Skills | malicious package detection, permission enforcement, sandbox escape attempts | Unreviewed skill cannot execute |
| Cost | cost per successful task, token/tool usage, expensive retries | User-visible budget ceiling and cutoff behavior |
| UX | time to understand state, approval comprehension, takeover/cancel | Users can understand current action and stop work |

## Competitive dimensions

Compare ORBIT with public product descriptions and reproducible task suites, not unsupported feature claims. Evaluate multi-agent handoffs, persistent computer sessions, app integrations, scheduled routines, memory continuity, model choice, approval controls, privacy/data control, exports, reliability and transparent operating cost.

## Mandatory release gates

- Unit, integration, e2e and migration tests pass for the changed scope.
- Tenant isolation and authorization denial tests pass.
- Every external side effect is exact-approved and audited.
- Cancellation propagates to all workers and runtimes.
- Delivery-uncertain mutations are reconciled and never blindly replayed.
- Browser, code and desktop execution are independently isolated.
- Skill install requires review state and explicit workspace enablement.
- License, SBOM, secret and vulnerability checks complete.
- Backup/restore and deletion propagation are tested.
- Independent Security and QA reviewers approve; human founder authorizes production release.

## Reporting format

Record commit, build, environment, dataset version, sample count, command, raw result location, metric formula, baseline, delta, confidence/limitations, failures and reviewer. Do not collapse “model quality”, “tool reliability” and “workflow reliability” into one unqualified score.
