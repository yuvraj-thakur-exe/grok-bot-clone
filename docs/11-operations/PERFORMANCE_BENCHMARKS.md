# Performance benchmark plan

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Targets proposed; no performance benchmarks have been run in this documentation-only handoff.

## Metrics

UI usable time; API p50/p95/p99; task enqueue delay; first-token latency; event delivery delay; task completion time by task class; provider latency/error rate; browser action success/latency; worker cold start; RAG recall/latency; concurrent task throughput; cost per successful task; cancellation latency; recovery time and lost/duplicated actions.

## Workload profiles

- Interactive chat: short, medium and long prompts, streaming.
- Research: 5/10/20 source tasks with mixed source latency.
- File QA: small and large supported files, multiple documents.
- Browser: read-only search/navigation, screenshot-heavy and login-persisted profile (test account only).
- Coding: small repository inspect/test/edit workflow in isolated sandbox.
- Concurrency: ramp users and tasks by worker type.

## Suggested initial hypotheses

Use the product's initial internal targets in `NFR.md` as hypotheses only. Record hardware, OS, deployment topology, provider/model/version, input size, dataset, concurrency, warm/cold state, sample count and percentile. Report local and cloud results separately. Set production SLOs only after representative measurements and an error-budget review.

## Regression policy

Keep benchmark fixtures/version stable. Alert on material latency, failure or cost regressions. Do not optimize by removing citations, reducing security checks, silently downgrading models or skipping verification.

## Desktop performance metrics

Measure process-start latency, snapshot time, tree completeness vs node count, semantic action latency, postcondition verification latency, CPU/memory of Local Desktop Node, WSS reconnect behavior and action throughput under per-session serialization. Report by OS, app toolkit, driver version and operation. Do not compare numbers across different machines/sessions without normalization. Performance is subordinate to safety and completeness.

## ORBIT v0.2 alignment

The v0.2 operations plan adds node offline, permission, driver version, unknown delivery and desktop data exposure runbooks. Never replay an uncertain mutation; see `DESKTOP_NODE_RUNBOOK.md`.
