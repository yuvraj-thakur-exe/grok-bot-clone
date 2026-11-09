# Starting ORBIT with the virtual company team

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## First IDE agent session

Use the virtual roles as review lenses, not as a reason to run many agents concurrently. Start with one primary IDE agent and sequential specialist reviews.

1. Founder/CEO brief: define the one user problem and budget boundary.
2. COO/PM: write the first milestone and acceptance criteria.
3. CTO: inspect repository and write a current-state architecture map.
4. Security lead: review trust boundaries, secrets, sandbox and tool policy.
5. Engineering owner: implement one vertical slice.
6. QA: independently run tests and verify acceptance.
7. CTO: record any ADR/risks and package the release evidence.

## First milestone recommendation

Authenticated workspace → persisted conversation → provider adapter → streaming → durable task and event timeline → cancel/reconnect → one policy-authorized low-risk tool → audit record → integration tests.

Do not begin by building a multi-agent company simulator UI. Build the workflow and audit primitives that make role agents reliable.

## Human approval gates

The founder must approve: paid API/vendor activation; legal/terms acceptance; public posts/releases; purchases/payments; real customer messaging; deletion of important data; production deployment; privilege changes; and any exception to security policy.
