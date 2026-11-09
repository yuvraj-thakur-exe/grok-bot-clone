# Use Cases

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## UC-01 Research report
Create task → plan queries → search sources → fetch pages → extract evidence → dedupe/compare → check contradictions → draft claim-source-linked report → verify citations → store artifact. Handle throttling, missing pages and low evidence transparently.

## UC-02 Coding task
Authorize repo → clone to disposable worktree → inspect stack/tests → plan → edit → run tests in sandbox → review diff/secrets/dependencies → present patch → require separate approval for push/PR. Never run repository code on host.

## UC-03 Browser task
Check domain scope → create isolated Playwright context → inspect DOM/accessibility tree → act within policy → pause at login/MFA/CAPTCHA/payment/approval → attach sanitized evidence and summary.

## UC-04 Skill creation
Review successful run → redact secrets/PII → define inputs/tools/steps/validation/failure/approval boundaries → test with fixtures → owner approves version → enable. One successful run does not establish trust.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.
