# Agent evaluation and team metrics

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Operational metrics

- Verified task completion rate by task class.
- Acceptance criteria pass rate on first attempt.
- Rework rate and escaped defect rate.
- Unsafe tool request count and policy denial reason.
- Approval latency and stale approval rate.
- Worker timeout, cancellation latency and retry safety compliance.
- Cost per verified task, token usage and provider distribution.
- Evidence precision/recall and citation support rate for research tasks.
- Skill pass rate by version and runtime profile.
- Backend contract conformance and capability mismatch rate.
- Sandbox startup, execution, pause/resume and destroy latency.

## Role scorecards

| Role | Outcome metric | Quality guardrail |
|---|---|---|
| Product | user-validated objective progress | no scope expansion without evidence |
| CTO | architecture fitness and delivery predictability | no unreviewed critical ADR |
| AI Research | reproducible evaluation gains | disclose data, prompts and limitations |
| Backend | API/data correctness | tenant isolation and migration safety |
| Frontend | task completion UX and accessibility | no direct privileged action from UI |
| Browser/Desktop | reliable verified interaction | unsafe action and secret exposure must be zero |
| Sandbox | isolation and recovery | escape/egress violations must be zero in tests |
| Security | risk reduction and remediation time | no unresolved critical finding at release |
| QA | acceptance and regression coverage | independent review; don't test own assumptions only |
| SRE | SLO, recovery time and availability | tested restore and rollback |
| OSS/Legal | compliant releases | no missing license/NOTICE approvals |

## Avoid vanity metrics

Agent count, code lines, tool count, tokens spent, model size and number of generated files are not success metrics by themselves. Optimise for verified user outcomes and safe cost.
