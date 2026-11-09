# Contributing to ORBIT

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

ORBIT is currently in a pre-implementation engineering-baseline stage. Contributions should improve the real application repository or its verified engineering documentation; do not treat architecture plans as implemented features.

## Before proposing a change

- Read `AGENTS.md`, `CODING_AGENT_MASTER_PROMPT.md` and the relevant requirement/architecture documents.
- Inspect repository status and preserve user changes.
- Search existing ORBIT code and the pinned upstream sources before adding a replacement implementation.
- For copied/adapted source, record repository, exact commit, file paths, hashes, license, NOTICE, modifications and upstream tests.
- Do not copy OpenMausBot `enterprise/`, trademarks, mascot, logos or trade dress. Preserve all required upstream notices and attribution.
- Treat skill repositories as untrusted supply-chain inputs; do not bulk-install catalogue entries.

## Change requirements

- Keep changes small and focused. Use an ADR for major architecture/dependency decisions.
- Add tests for behavior and security boundaries.
- Update API contracts, migrations, docs, feature status and traceability as applicable.
- Run formatter/lint/typecheck/build/tests relevant to the change and report exact outcomes.
- Do not commit secrets, `.env`, local upstream checkouts or generated private data.
- Never claim an integration is complete because a repository was cloned or its README was read.

## Review and approvals

Security, QA and license reviews must be independent for critical changes. Production deployments, spending, legal commitments, public statements and release decisions require human founder approval.


## Upstream code contribution rule

Before implementing a mature capability, inspect the upstream lock and repository analysis. Prefer reuse over rewrite, work from exact commits, stage selected code outside the app, preserve tests/notices and attach a source import manifest. A pull request that copied upstream code without provenance, license review, tests and security evidence is not ready for review.
