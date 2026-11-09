# ORBIT v0.4 start here — execute reuse-first

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Read in this order

1. `AGENTS.md` — mandatory repository rules.
2. `docs/02-research/REUSE_FIRST_REPOSITORY_AUDIT_V04.md` — findings on the five newly supplied repositories.
3. `docs/03-architecture/ORBIT_MULTI_AGENT_PERSONAL_OPERATING_SYSTEM_V04.md` — product architecture and life/work scope.
4. `docs/03-architecture/UPSTREAM_RUNTIME_ADAPTERS_V04.md` — runtime integration contract.
5. `docs/04-system-design/UPSTREAM_REUSE_WORKFLOW_V04.md` — how to clone, reuse, patch and maintain upstream code.
6. `docs/06-security/THIRD_PARTY_CODE_REUSE_AND_SKILL_TRUST_V04.md` — license and skill security.
7. `docs/12-project-management/V04_CTO_TEAM_EXECUTION_PLAN.md` — workstreams and responsibilities.
8. `config/upstreams/upstream-lock.yaml` — pinned source revisions.

## First action in the actual ORBIT repository

Run the read-only audit in `RUN_FIRST_IN_IDE_AGENT.md`. Do not replace the repository until the agent reports its current source structure, product shell, dependency tree and build/test baseline.

## Clone pinned upstream source for local review

The `scripts/clone_upstreams.sh` script is a source-acquisition helper. It does not merge any code into ORBIT.

```bash
# Clone only the recommended OpenMausBot product-shell candidate
bash scripts/clone_upstreams.sh --product-base

# Clone the product shell plus selected coding, sandbox and browser components
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox --stagehand

# Or explicitly clone all five user-supplied repositories (can require substantial disk/network)
bash scripts/clone_upstreams.sh --all-supplied

# See all individual selectors
bash scripts/clone_upstreams.sh --help
```

Source checkouts are placed in `upstream/`. The component radar and upstream lock also include Mem0, Letta, LangGraph, DSPy, Temporal, OpenTelemetry, LlamaIndex, Qdrant and Browser Use. Select these individually with `--mem0`, `--letta`, `--langgraph`, `--dspy`, `--temporal`, `--otel`, `--llamaindex`, `--qdrant` and `--browser-use`. Review each upstream at the locked commit before importing. Do not commit the full upstream repositories into the ORBIT application repo unless the integration strategy specifically requires vendoring/submodules.

## Foundation decision

If ORBIT has no working product shell, prototype the public OpenMausBot edition as the desktop/web workspace base, excluding `enterprise/`. Use ORBIT branding, secure credential storage and ORBIT policy enforcement. If existing ORBIT source already performs these jobs, preserve it and selectively adapt the upstream modules. OpenClaw and Hermes remain optional backend runtimes; do not combine all their gateways into one unmaintainable service.

## What this pack does and does not do

This documentation archive now contains a source reuse plan, pinned Git refs, an acquisition script, architecture and team directives. It still does not contain the complete source code of any upstream repository or a working ORBIT runtime. No application tests are claimed to have passed. The actual ORBIT application repository must be supplied/audited before implementation code can be patched in place.

## Superseded by the v0.5 coordinated baseline

Use `docs/13-guides/ORBIT_V05_START_HERE.md`, `docs/12-project-management/V05_IMPLEMENTATION_PLAN.md` and `docs/12-project-management/V05_REUSE_AND_BUILD_WORKSTREAMS.md` as the current implementation order. The v0.4 source analysis remains historical evidence; the actual ORBIT repository audit determines the final product-shell and runtime selection.
