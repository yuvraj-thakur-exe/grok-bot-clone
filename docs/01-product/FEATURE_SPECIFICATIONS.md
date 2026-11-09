# Feature specifications (initial release map)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Each feature below is a boundary-level specification. Implementation tasks must add screen/API-level acceptance details before work begins.

## F-01 Conversations and task workspace (P0)

Purpose: make model interaction persistent and inspectable. Requirements: create/list/search/rename/archive conversations; store typed messages and attachments; stream responses; reconnect from event cursor; show task state and artifacts. Edge cases: duplicate submit, provider disconnect, token limit, cancelled task, deleted workspace. Acceptance: refresh/reconnect preserves ordered history and task state; duplicate idempotency key does not create duplicate task.

## F-02 Model router (P0)

Purpose: allow provider/model flexibility. Requirements: adapter registry, capability metadata, user/workspace policy, budgets, normalized errors, streaming and safe fallback. Acceptance: unsupported modality is rejected transparently; local-only data never routed to hosted provider; fallback reason is visible and audited.

## F-03 Agent and tool execution (P0)

Purpose: execute bounded tasks. Requirements: plan, policy-check, execute one tool step, persist checkpoint, verify and summarize. Acceptance: no tool bypasses gateway; max budgets enforce; task cancellation works; output is not reported complete without tool/evidence success.

## F-04 Web research (P0)

Purpose: produce source-backed reports. Requirements: multiple queries, normalized sources, fetch/extract, freshness/provenance, claim-source mapping, conflicts and citations. Acceptance: every factual research claim is linked to real source record; blocked/stale/unverified evidence is disclosed.

## F-05 File intelligence (P0)

Purpose: safely answer from user files. Requirements: upload, scan, parse, index, retrieve, page/source locators, export/delete. Acceptance: malformed/oversized file is rejected or quarantined; answers cite page/section; workspace filters applied before retrieval.

## F-06 Browser worker (P1)

Purpose: operate permitted websites. Requirements: isolated Playwright context, visible task progress, screenshots, safe navigation, human takeover, domain policy and downloadable artifacts. Acceptance: session isolation, SSRF controls, CAPTCHA/MFA pause and cancellation pass tests.

## F-07 Repository agent (P1)

Purpose: inspect and modify authorized repositories. Requirements: Git clone/worktree, architecture map, test baseline, scoped code edits, sandbox tests and diff review. Acceptance: no changes outside repo root; uncommitted work preserved; branch/PR writes require permission/approval.

## F-08 Memory (P1)

Purpose: persist user-controlled context. Requirements: provenance, access scope, inspect/correct/delete/export and expiry. Acceptance: ACL tests, correction propagation and deletion across derived indexes pass.

## F-09 Skills and routines (P1/P2)

Purpose: reuse safe workflows. Requirements: manifests, version, inputs/outputs, validation, tool grants, sandbox tests, trigger, timezone, deduplication and pause. Acceptance: imported skills remain untrusted until reviewed; routine uses normal policies and approvals.

## F-10 Multi-agent (P2)

Purpose: delegate independent subtasks. Requirements: child task graph, budget, role scope, cancellation propagation and verifier. Acceptance: no unbounded spawning; child results include evidence and are consolidated with uncertainty.

## ORBIT v0.2 alignment

The v0.2 product boundary adds native desktop control as a later optional device capability. It is separate from web browser automation and code execution, and requires pairing, runtime capability visibility and user-controlled pause/revoke.
