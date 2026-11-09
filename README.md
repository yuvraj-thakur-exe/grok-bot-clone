# ORBIT AI — Engineering Blueprint & IDE Agent Pack

> **Document baseline:** ORBIT 1.1.0 / 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Coordinated reuse-first engineering baseline and cross-platform developer toolkit.

---

## Quick Start — Developer Toolkit CLI

The repository includes cross-platform launchers (`orbit.bat`, `orbit.ps1`, `orbit.sh`) and standard Python 3.11+ tools in `src/orbit_cli`:

```powershell
# 1. Environment & toolchain diagnostic check
.\orbit.ps1 doctor

# 2. Run test suite
$env:PYTHONPATH = "src"; python -m unittest discover -s tests -v

# 3. Validate task DAG manifest
.\orbit.ps1 run --manifest configs\tasks.example.json --validate-only

# 4. Initialize storage volume (requires verified host disk path)
# .\orbit.ps1 storage init D:\ORBIT-Storage --expected-capacity-gb 500 --reserve-gb 60
```

---

## Workspace Structure & Organization

```
d:\orbit\
├── orbit.bat / orbit.ps1 / orbit.sh     # Portable CLI launchers
├── src/orbit_cli/                       # CLI implementation (doctor, runner, storage, context-pack)
├── configs/                             # CLI configurations and task DAG examples
├── tests/                               # Comprehensive unit test suite
├── docs/                                # Full engineering blueprint (modules 00 to 14)
├── roles/                               # 30-role virtual AI workforce & ROLE_REGISTRY.yaml
├── scripts/                             # Repo operations, audit, clone, and storage tools
├── skills/                              # Canonical agent skills (desktop, implementation, audit)
├── packages/contracts/                  # Core TypeScript types, schemas, and contracts
├── architecture/                        # Mermaid diagrams & system architecture specs
├── examples/                            # Generative UI, MCP configs, brand tokens
├── grok bot rea/                        # Standing by for user instruction
├── _archives/                           # Original ZIP archive packages (v0.1 through v1.1)
└── _history_versions/                   # Isolated historical snapshots of each package version
```

---

ORBIT is designed as a privacy-conscious personal and work operating system powered by specialist AI agents. It should help people study, research, build software, create documents and media, manage projects, coordinate business workflows, use supported applications, operate approved devices and complete multi-step digital work with visible permissions and verifiable evidence.

> **Core principle:** Use existing proven code first. Inspect, pin, reuse, adapt, test and maintain. Rewrite only when a documented technical, legal or safety reason proves reuse unsuitable.

## Start here

1. `docs/13-guides/V10_START_HERE.md` — v1.0 first-run handoff.
2. `RUN_FIRST_IN_IDE_AGENT.md` — read-only audit of the actual ORBIT application repository.
3. `AGENTS.md` and `CODING_AGENT_MASTER_PROMPT.md` — engineering rules and CTO/team directive.
4. `ORBIT_ENGINEERING_BLUEPRINT.md` — product and technical blueprint.
5. `docs/INDEX.md` — documentation navigation.
6. `PACKAGE_VALIDATION.md` — what was validated and what remains human work.

## Core architecture

ORBIT owns canonical user/workspace identity, personal/work context ACLs, task/event state, authorization, approvals, spend limits, memory consent, skill trust, connector scopes, source provenance, audit evidence, notifications and artifact lifecycle. Upstream projects are replaceable adapters, workers or selected source modules. They do not become competing sources of truth.

| Capability | Preferred evaluation path | ORBIT boundary |
|---|---|---|
| Product shell | OpenMausBot public OSS modules vs existing ORBIT app | Identity, workspace, task state, permissions and branded UX stay ORBIT-owned |
| Gateway/runtime | OpenClaw or Hermes, behind one adapter | No duplicate global task or policy authority |
| Coding workers | OpenHands SDK, Codex, Gemini CLI, SWE-agent | Disposable worktrees, limited credentials and test evidence |
| Browser | Playwright baseline; Stagehand/Browser Use alternatives | Egress, profile isolation, approvals and evidence |
| Sandbox | Docker baseline; OpenSandbox evaluation | Resource/network/credential isolation and cleanup |
| Memory/RAG | Mem0/Letta/Graphiti; LlamaIndex/Haystack/GraphRAG | User consent, ACL, provenance, correction and deletion |
| Search/vector | PostgreSQL FTS + one chosen vector engine; compare Qdrant/Chroma/Milvus/FAISS/OpenSearch | No duplicate search stores without workload evidence |
| Local inference | Ollama/llama.cpp; vLLM/SGLang for suitable GPU servers | Model terms, RAM/VRAM and measured quality/cost |
| Connectors | MCP and Composio plus selected direct APIs | OAuth least privilege, revocation and write approval |
| Evaluation/safety | Promptfoo, DSPy, garak, Guardrails, OpenTelemetry | Independent quality/security review and redacted evidence |

## The 50-repository source catalogue

The user-supplied foundations are OpenClaw, VoltAgent's skill discovery index, Hermes Agent, Hermes Self-Evolution and OpenMausBot. The broader 50-source lock also includes coding, sandbox, browser, memory, workflow, document, voice, model-serving, retrieval, connector, safety and evaluation projects. New v1.0 pins are Google ADK, OpenAI Codex, Gemini CLI, OpenSearch, SWE-agent and FAISS.

Exact commits are in `config/upstreams/upstream-lock.yaml`. The catalogue is not an instruction to clone every repository. Select the minimum sources required for one feature. See `docs/02-research/V10_OPEN_SOURCE_FILE_LEVEL_ADOPTION_MAP.md` for module-level targets and boundaries.

Important legal/security boundaries:

- OpenMausBot's `enterprise/` is separately licensed and excluded from source acquisition. Preserve LICENSE/NOTICE/attribution and do not reuse product branding or mascot.
- OpenClaw in-process native plugins are trusted code, not sandboxed plugins.
- VoltAgent's list license does not license individual linked skills.
- Hermes Self-Evolution's inspected snapshot had MIT metadata but no root LICENSE file; confirm license evidence before redistribution.
- Repository root license metadata does not clear nested dependencies, model weights, datasets, assets or trademarks.

## Copy, paste and modify workflow

The operations are executable, not just advice:

```bash
# Choose and verify selected sources
python scripts/orbit_repo_ops.py list --recommended-only
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
python scripts/orbit_repo_ops.py verify

# Audit source without running it
python scripts/repo_audit.py "$ORBIT_UPSTREAM_DIR/openmausbot" --output-dir "$ORBIT_HOME/00-control/audits/openmausbot"

# Create a clean feature worktree from the actual ORBIT app checkout
python scripts/create_orbit_app_worktree.py --repo "$ORBIT_HOME/02-workspaces/orbit-app-source" --task approval-flow --created-by "Human maintainer"
```

Then stage an exact upstream file/path with `scripts/import_upstream_path.py`, copy it into the feature worktree with `scripts/apply_staged_source.py` using the reviewed `manifest_sha256`, adapt imports/contracts, run tests and security review, preserve all required notices, and let a human maintainer create the commit/PR. The helper refuses overwrite and never commits, merges or pushes. Full guide: `docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md`.

## Dedicated 500 GB storage

The proposed allocation uses 440 GB as soft folder targets and preserves 60 GB as free reserve. It includes upstream sources, app worktrees, models, user-authorized data/memory, artifacts, evaluations, backups, quarantine and source intake. Initialize only after verifying the physical disk with Windows `Get-Disk`/`Get-Volume` or Linux `lsblk`. The script creates folders and a manifest only; it does not format, partition, encrypt, mount or enforce quotas. Disk capacity does not add RAM/VRAM. See `docs/10-infrastructure/V10_500GB_STORAGE_OPERATIONS.md`.

## Competing with Grok Bot, Muse and dots

ORBIT's benchmark is persistent task continuity, specialist delegation, user-controlled memory, browser/computer execution, connectors, routines, pause/recovery, approvals, cost transparency and context isolation. It must demonstrate these through reproducible end-to-end scenarios before claiming parity. See `docs/09-quality/V10_COMPETITIVE_PARITY_BENCHMARKS.md`.

## CTO/team execution

`docs/08-development/V10_CTO_IMPLEMENTATION_WARROOM.md` defines the virtual CTO, developer, repository operations, product-shell, agent-runtime, coding, browser, sandbox, connector, memory, model, security, QA, DevOps and product workstreams. The 30 charters in `roles/` are virtual role definitions, not real employees or legal authority. Human approval remains mandatory for external commitments, legal acceptance, purchases, production deploys and releases.

## Delivery status and limitation

This ZIP is the blueprint, research, source acquisition, repository operations, schema, policy and IDE-agent pack. It does not bundle all upstream repos or implement the ORBIT application runtime. The actual ORBIT repository URL/path is still needed for a real codebase audit and for selecting which existing files should be modified. No runtime integration, build or release is claimed here.
