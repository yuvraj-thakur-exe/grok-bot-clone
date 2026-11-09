# ORBIT v0.5 — start here

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Read in order

1. `README.md` — product thesis and boundaries.
2. `AGENTS.md` — mandatory coding and security rules.
3. `RUN_FIRST_IN_IDE_AGENT.md` — read-only repository audit.
4. `CODING_AGENT_MASTER_PROMPT.md` — CTO/team execution directive.
5. `docs/02-research/V05_SOURCE_DECISION_MATRIX.md` — upstream choices and risks.
6. `docs/03-architecture/V05_TARGET_ARCHITECTURE.md` — system ownership and adapters.
7. `docs/04-system-design/V05_REUSE_AND_ADAPTATION_PLAYBOOK.md` — source acquisition and modification workflow.
8. `docs/06-security/V05_SUPPLY_CHAIN_AND_SKILL_SECURITY.md` — skills, dependencies, notices and isolation.
9. `docs/12-project-management/V05_IMPLEMENTATION_PLAN.md` — phase sequence and exit gates.
10. `config/upstreams/upstream-lock.yaml` — exact source pins.

## Audit first

Run the read-only audit against the actual ORBIT repository. Keep existing code and user changes safe. Do not choose an upstream shell before understanding the current project.

## Acquire pinned sources for inspection

```bash
# Product-shell candidate only; enterprise/ is excluded from checkout.
bash scripts/clone_upstreams.sh --product-base

# Recommended focused review set.
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox --stagehand

# Five repositories supplied by the user.
bash scripts/clone_upstreams.sh --all-supplied

# Inspect selector list.
bash scripts/clone_upstreams.sh --help
```

Source is placed in `upstream/` unless `ORBIT_UPSTREAM_DIR` overrides it. The helper pins commits, verifies the checked-out SHA and never installs dependencies, runs upstream scripts or merges code. The OpenMausBot sparse checkout excludes `enterprise/`; verify that exclusion. Do not commit full upstream trees unless vendoring/submodules were explicitly selected.

## Validate the pack

```bash
python scripts/validate_package.py
bash -n scripts/clone_upstreams.sh
python scripts/audit_skill_package.py --help
```

These commands validate this engineering pack and the skill-audit helper. They do not test an ORBIT production runtime.

## First implementation milestone

After audit and approval, implement one complete task path: login/workspace → create task → choose one runtime → stream progress → invoke one safe read-only tool → persist evidence/artifact → reconnect → cancel. Then test an exact-approval write action. Only then scale the roster, integrations, routines and desktop access.

## Status honesty

This archive is a source-acquisition and engineering baseline, not a built ORBIT application. Upstream repositories are not bundled. Build and integration tests have not been run against ORBIT because its application repository was not supplied.
