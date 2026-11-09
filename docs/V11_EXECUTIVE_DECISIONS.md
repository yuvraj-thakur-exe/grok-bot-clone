# ORBIT v1.1 executive decisions and next work

## CEO / founder decision rights

The human founder retains final authority for budget, privacy policy, external account connections, licensing decisions, purchases, public communications, production credentials and releases. Virtual executive roles can research, draft, implement within approved boundaries and recommend. They cannot self-approve high-impact work.

## CTO decisions for this increment

1. Keep the existing ORBIT v1.0 specification pack as the architecture baseline; ship this toolkit as a separate additive increment.
2. Use one Python standard-library developer CLI and thin platform launchers. Avoid duplicating implementation in BAT/PowerShell/Bash.
3. Add a small JSON DAG runner with bounded concurrency for local developer tasks. Keep it separate from the future durable production workflow engine.
4. Preserve three execution security domains: browser, native desktop and code sandbox.
5. Treat 500 GB as developer/source/model/cache workspace capacity, not as the required ORBIT install size.
6. Keep the initial parallelism default at three; cap at eight until real hardware benchmarks justify more.
7. Use approximate context packing now; require exact provider tokenizer integration before enforcing model token budgets.
8. Do not merge several global agent frameworks or schedulers. ORBIT remains authoritative for task state, policy, approval and audit.
9. Record selected upstream repositories by immutable commit SHA and sparse source paths; candidate pins do not imply license clearance or adoption.
10. Keep local CLI redaction and token estimates explicitly best-effort; do not represent them as a secret scanner or provider-exact tokenizer.

## P0 next milestone

Audit the actual ORBIT app repository in read-only mode. Identify its present framework, entrypoints, database, worker model, tests, dependencies and security state. Then select one narrow vertical feature, build it in a clean worktree, test it and obtain human review.

## Blocker

The actual ORBIT application Git URL or local source path is not present in this conversation's files. The current v1.0 pack explicitly states that source audit and integration cannot be claimed until that repository is available.

## P1 after audit

- Decide one product shell from evidence, not from competing architecture diagrams.
- Implement canonical task/event/approval contracts and one agent runtime adapter.
- Add one read-only tool through the policy gateway.
- Add a fake desktop driver contract suite before connecting to a real interactive desktop.
- Prove browser, code and desktop trust boundaries separately.
