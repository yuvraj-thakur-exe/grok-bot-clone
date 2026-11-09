# AI quality and agent evaluation

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Evaluation dimensions

- Goal completion and partial completion quality.
- Factual correctness and citation support.
- Tool choice and argument validity.
- Browser task success and recovery.
- Code change correctness and regression rate.
- Policy compliance and approval enforcement.
- Prompt-injection resistance.
- Latency, model calls, token use and cost per successful task.

## Test set

Maintain versioned tasks for chat, research, file Q&A, browsing, coding, memory retrieval, delegation, cancellation, recovery and security. Include positive, negative, ambiguous, adversarial and provider-failure cases. Store expected properties and scoring rubric, not brittle exact wording alone.

## Method

Run baseline and candidate on the same dataset. Pin model, prompt, tool and dataset versions. Record raw structured output and scorer version. Human-review high-impact samples. Report confidence intervals where sample sizes justify them. Never fabricate benchmarks or compare unlike settings.

## Release gates

No release may regress critical safety tests. Establish minimum thresholds for functional success, source coverage and latency after collecting baseline data. Thresholds are currently TBD; do not invent passing rates without measurement.

## Desktop evaluation metrics

Add task-level desktop measures: successful observation rate, snapshot completeness, target ambiguity rate, stale-ref recovery, action delivery classification accuracy, postcondition verification rate, policy-denial correctness, approval correctness, duplicate-side-effect rate (target zero), privacy-redaction coverage, action latency and human handoff rate. Use disposable apps and repeatable fixtures; do not benchmark on real personal accounts.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
