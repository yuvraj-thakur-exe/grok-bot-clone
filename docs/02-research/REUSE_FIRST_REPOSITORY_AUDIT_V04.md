# Reuse-first repository audit — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Snapshot date:** 08 November 2026 (UTC)  
**Purpose:** select existing code and runtime foundations for ORBIT instead of recreating mature capabilities.  
**Evidence boundary:** GitHub default-branch metadata, repository READMEs, selected source paths, license files/metadata and official project documentation were inspected. This is not a complete line-by-line security audit or legal opinion.

## Executive decision

**Primary product-shell candidate: OpenMausBot's public Apache-2.0 edition.** It is the closest inspected codebase to the desired multi-agent personal workspace: desktop chat UI, per-agent profiles/models, local harness, connected apps, computer sessions, approvals, schedules/routines, team workflows and a bounded MCP control interface. Start from its source if the actual ORBIT repository has no comparable working product shell. If ORBIT already contains useful UI or backend code, audit and reuse selectively instead of replacing it wholesale.

**Runtime options, not another product fork:** OpenClaw is a candidate gateway/channel/plugin runtime; Hermes Agent is an optional external agent backend. ORBIT must keep one authoritative task, user, workspace, approval and audit plane. Do not run three independent chat databases and gateways and call the resulting knot an architecture.

**Self-improvement:** use the Hermes self-evolution repository as an offline research/evaluation pipeline for skill and prompt optimization. Promote variants only after held-out evaluation, policy tests, human review and a normal pull request.

**Skill discovery:** use VoltAgent's list as a discovery catalogue. Do not copy the index and assume every listed skill is licensed or safe. Every skill has its own source, license, digest and permission review.

## Pinned source snapshots

The `config/upstreams/upstream-lock.yaml` file records the exact commit SHAs inspected on 08 November 2026. Re-fetch them before actual adoption; default branches move.

| Source | Observed license | Relevant code surfaces | ORBIT decision |
|---|---|---|---|
| [OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Apache-2.0 outside `enterprise/` | `src/`, `server/`, `shared/`, `electron/`, `companion/`, `connector/`, `skills/`, `third_party/` | Preferred product-shell candidate; fork or selective subtree reuse after audit |
| [OpenClaw](https://github.com/openclaw/openclaw) | MIT | `packages/plugin-sdk/`, `packages/gateway-client/`, `packages/gateway-protocol/`, `extensions/`, `skills/`, `src/` | Reuse plugin protocol/client code selectively; run as optional external runtime where useful |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | MIT | `agent/`, `gateway/`, `cron/`, `evals/`, `hermes_cli/`, `hermes_agent/` | Optional backend adapter; avoid cherry-picking coupled internals |
| [Hermes self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | MIT declared in README and `pyproject.toml`; no root `LICENSE` file at inspected snapshot | `evolution/`, `datasets/`, `tests/`, `PLAN.md` | Offline optimizer prototype only; confirm license evidence before redistribution |
| [VoltAgent awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | MIT for the catalogue repository | `categories/`, `README.md` | Discovery index only; the index's license does not relicense linked skills |

## 1. OpenMausBot: strongest starting point for the user-facing product

### Why it is the best first product-shell candidate

Its public README and directory structure show a complete TypeScript/Electron product rather than a few agent examples. The visible architecture includes a server-owned chat/task state, bot roster, model/provider catalogue, per-agent working folders, approval cards, computer lifecycle, connector events, routines, desktop shell and companion surfaces. The repository also provides an MCP server and a CLI for controlling a running workspace.

### First code-review targets

These are **review targets**, not an instruction to paste code without reading dependencies and tests:

| Upstream path | What the inspected code demonstrates | Proposed ORBIT use |
|---|---|---|
| `server/agent-tool-policy.ts` | Explicit allowlist of read-only team-control tools with annotations | Reuse policy pattern; expand only through ORBIT authorization |
| `server/agents-turn.ts` | Per-turn capability flags, generation scope, bearer handoff and constraints on computer/skill actions | Reuse turn-scoped capability design and tests |
| `server/app-events.ts` | Bounded event batching, provenance labeling and explicit untrusted-event blocks | Reuse event-boundary and prompt-injection containment patterns |
| `shared/approval-mode.ts`, `shared/live-approval.ts` | Approval domain model candidates | Review with their tests and server enforcement before adopting |
| `shared/routine-schedule.ts`, `shared/routine-run.ts` | Routine/schedule data contracts | Review for timezone, retries, duplicate trigger and cancellation semantics |
| `shared/skill-import.ts`, `shared/skill-md.ts`, `shared/written-skill.ts` | Skill import/formatting surface | Reuse parser/format patterns only after skill trust model integration |
| `src/` | Product chat and team UI | Adopt as the UI baseline if the ORBIT app has no stronger existing frontend |
| `electron/`, `companion/` | Desktop/companion packaging and device access | Selectively adopt; preserve platform-specific permission boundaries |
| `third_party/`, `NOTICE`, `LICENSING.md` | Third-party provenance and license records | Retain and merge notices; generate ORBIT SBOM |

### Hard restrictions discovered

1. `enterprise/` is **not** Apache-2.0. The upstream licensing file says production use requires a separate license and redistribution/white-labelling is restricted. Exclude this directory from any ORBIT fork or derived distribution unless separately licensed. Never bypass its entitlement check.
2. The OpenMausBot/MausBot product names and mascot are trademarks. Use ORBIT's original brand, but keep the legally required attribution and third-party notices.
3. Upstream documentation says API keys may be stored in a private local `config.json` with filesystem permissions rather than encrypted. ORBIT must not inherit that storage design unchanged. Use OS keychain or a dedicated encrypted secret vault; the UI must never receive secret values after initial input.
4. The app bundles and adapts third-party components. Retain `NOTICE`, `third_party/` provenance, license texts and SBOM data. Re-check every file before moving it out of its original package.
5. Computer access is platform-specific. Keep physical desktop access behind a paired local node, local pause/stop and explicit per-action permission checks.

**Decision:** use OpenMausBot as the first product-shell prototype/fork candidate. Do not automatically adopt its entire source tree until the ORBIT repository baseline, dependency tree, nested licenses, secrets handling and build/test commands are reviewed.

## 2. OpenClaw: gateway and extension ecosystem

Inspected repository surfaces include `packages/plugin-sdk/`, `packages/gateway-client/`, `packages/gateway-protocol/`, `packages/agent-core/`, `packages/acp-core/`, `packages/net-policy/`, `extensions/` and `skills/`. The extension tree includes browser, DuckDuckGo, deep research, GitHub, document extraction, OpenTelemetry, memory, voice, messaging and numerous model providers. This is a substantial reuse opportunity.

### Recommended reuse

- Prefer the official gateway client, protocol types and stable plugin SDK contracts over private helper imports.
- Where ORBIT needs a matching channel/provider connector, first test whether its official extension can run as an isolated OpenClaw backend. If not, inspect a small extension package for a legal, technically clean adapter reuse.
- Reuse skill discovery/manifest patterns, not arbitrary skill code.
- Use OpenClaw as an optional backend or channel bridge; do not duplicate ORBIT-owned user/workspace/task state.

### Security finding

OpenClaw's plugin architecture documentation states that native plugins load in-process with the Gateway and are **not sandboxed**; a plugin therefore has process-level trust. Allowlist and review every native plugin. For less trusted community additions, prefer an out-of-process adapter with a narrow RPC contract and sandboxed worker. OpenClaw's own README also warns that host tools run on the host unless sandboxing is configured.

**Decision:** MIT candidate. Select packages by file and dependency graph; do not treat the full repository license as sufficient for every nested dependency or prebuilt asset.

## 3. Hermes Agent: optional runtime and memory/skill research

The repository declares MIT and exposes a Python agent implementation with `agent/`, `gateway/`, `cron/`, CLI, evaluation and platform surfaces. Official Hermes documentation advertises long-term memory, cross-session recall, skill creation/improvement, subagents, scheduled automation, multiple messaging platforms and MCP integration.

**Decision:** make Hermes an optional external `AgentBackend` / ACP or CLI adapter. It is a useful second runtime to test portability and model/provider diversity. Do not copy its internal agent loop, memory database and gateway into ORBIT until a concrete code-level advantage is proven. ORBIT remains the owner of identity, task, policy, approval and artifact contracts.

## 4. Hermes self-evolution: offline agent improvement

The source README and `pyproject.toml` declare MIT, but a root `LICENSE` file was not present in the inspected default-branch root. Its README describes DSPy + GEPA optimization of skills, prompts, tool descriptions and code, with a baseline → dataset → optimize → holdout test → review/PR loop. The plan identifies Darwinian Evolver as AGPL-3.0 and specifies external CLI only.

**Decision:** use its workflow and tests as a research reference. For code reuse, obtain/confirm the full MIT license text, record provenance and dependencies, and review each file. Do not include AGPL components in the ORBIT process or distribution unless the legal model is explicitly approved. No live self-editing production prompts or tool code.

## 5. VoltAgent skill collection: discovery, not a trusted package manager

The catalogue repository is MIT, but its README says entries originate from ClawHub. It reports filtering spam, duplicates, low-quality entries and malicious entries found by published audits, while still being a discovery index. That filter is useful triage; it is not a security certification or a license grant for each upstream folder.

**Decision:** ingest catalogue metadata only. Fetch each candidate skill from canonical source and record per-skill:

- repository, author, exact commit/release and content SHA-256;
- `SKILL.md` plus scripts/assets and nested license files;
- SPDX expression, NOTICE/attribution and author provenance;
- requested permissions, declared domains, connectors and data scopes;
- static scan, malware/dependency checks, secret scan and sandbox smoke test;
- reviewer decision, version lock, revocation and rollback status.

Skills are instruction packages, not authority. Tool permissions are enforced by ORBIT policy and never by frontmatter alone.

## What was not verified

- Full runtime builds and tests were not executed.
- No complete source-tree security audit, dependency scan or SBOM was produced for these upstreams.
- No compatibility test was run between these repositories and the ORBIT source code.
- The self-evolution repository's declared MIT metadata needs rights-holder/license-text confirmation before redistribution.
- A product fork requires a separate review of every transitive dependency, native binary, asset and license exception.

**Next decision:** audit the actual ORBIT repository. If it lacks a comparable desktop chat/product shell, start a controlled OpenMausBot OSS fork; otherwise import only the exact upstream components with the best tested fit.


## v0.5 status and implementation boundary

The findings remain tied to the exact commits recorded in `config/upstreams/upstream-lock.yaml`. They are not a source import or runtime integration. The current policy is in `docs/02-research/V05_SOURCE_DECISION_MATRIX.md`. Re-check repository updates, nested dependencies, license files, security advisories and build status before actual adoption. OpenMausBot's restricted directory is excluded at acquisition time by sparse checkout.

