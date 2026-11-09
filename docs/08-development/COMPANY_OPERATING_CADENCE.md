# ORBIT operating cadence

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Daily execution

- Review task queue, build health, blockers, open approvals and spend alerts.
- Run focused work; avoid all-role roundtables for routine code tasks.
- Every PR has a purpose, requirements IDs, tests, risks and rollback notes.

## Weekly rhythm

| Forum | Participants/roles | Output |
|---|---|---|
| Founder product review | Founder, product, delivery, design | Prioritised objectives and acceptance changes |
| Architecture review | CTO, leads, security, QA as needed | ADR approvals and migration decisions |
| Security / dependency review | Security, SRE, OSS compliance | Threat changes, advisories, license blockers |
| Delivery review | COO, engineering leads, QA | Demonstrated progress, defects, blockers and next milestone |
| Cost review | Finance, CTO, founder | Model/provider/cloud spend and budget adjustments |

## Release train

1. Scope freeze for candidate release.
2. CI, integration and E2E suite pass.
3. Security, license and SBOM gates pass.
4. QA signs evidence; security signs risk controls.
5. Rollback and recovery procedure verified.
6. Human founder/release owner approves production release.
7. Observe canary, then expand rollout.
8. Publish release notes only after approval.

## Decision records

Use ADR for technical decisions, product decision log for scope, compliance register for legal/license decisions and incident records for operational failures. A chat response or model output is not a formal decision record until the owner records and approves it.
