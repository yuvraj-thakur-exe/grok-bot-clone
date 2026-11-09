# ORBIT v0.8 — repository operations, source reuse and modification handbook

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## 1. Purpose and non-negotiable rule

ORBIT must reuse proven upstream implementations wherever that is safe and practical. The development agent must search the existing ORBIT codebase and the pinned upstream catalogue before writing replacement code. It must not regenerate a large module merely because a prompt asks for a feature that an upstream already implements.

This guide defines a controlled path from a GitHub repository to an isolated working tree and, only after review, to a change in the real ORBIT application.

**Important boundary:** cloning a repository, reading its README, or staging a source folder is not integration. The application repo must build, tests must pass, notices and dependencies must be handled, and a reviewed PR must land before a feature can be called integrated.

## 2. The 41-source catalogue and its purpose

The lock is the exact source of truth for repository ID, canonical URL, reference, immutable commit SHA, observed root license and adoption cautions. Use `python scripts/orbit_repo_ops.py list` and `show <id>` rather than maintaining private copies of the registry.

### Personal assistant and product foundation

- OpenMausBot: desktop/product-shell and multiple-agent chat patterns. Its public OSS core is Apache-2.0; `enterprise/` is separately licensed and excluded.
- OpenClaw: gateway, channels, plugins, provider extensions and companion nodes. Use SDKs or an external process adapter; in-process native plugins are trusted code.
- Hermes Agent: alternative agent runtime and CLI. Keep behind an adapter, not as a second canonical ORBIT control plane.
- VoltAgent Awesome OpenClaw Skills: catalogue/discovery only. Each listed skill has an independent source, license and security status.
- Hermes Self-Evolution: offline research for skill/prompt/tool-description optimization; license evidence must be confirmed before redistribution.

### Agent execution, task orchestration and integration

- OpenHands Software Agent SDK: bounded coding worker in a disposable repository workspace.
- Pydantic AI, OpenAI Agents Python, Microsoft Agent Framework, Semantic Kernel: compare typed-agent, handoff and worker SDK capabilities. Do not install all as separate agent managers.
- LangGraph: bounded graph orchestration, interrupts and stateful subflows.
- Temporal: durable business workflows, retries, timers, long-running task recovery.
- MCP Python SDK: tool interoperability, not authorization.
- Composio: connected-app integration catalogue and auth/tool adapter candidate; review each toolkit and hosted service separately.

### Browser, computer and sandbox

- Playwright: browser baseline and browser-driver contract tests.
- Stagehand and Browser Use: alternative semantic browser agents behind the same BrowserDriver adapter.
- OpenSandbox: sandbox-provider candidate after a Docker baseline and isolation tests.
- Native desktop remains a separate device node, consent and lease boundary.

### Memory, retrieval and data

- Mem0 and Letta: alternative stateful memory backends; ORBIT owns consent, access control, deletion and memory provenance.
- Graphiti: time-aware relationship/knowledge graph candidate after basic scoped memory works.
- LlamaIndex and Haystack: alternative document/RAG pipeline frameworks. Benchmark and select one primary pipeline.
- Docling and MarkItDown: document extraction alternatives with different fidelity and performance envelopes.
- Qdrant and Chroma: alternative vector databases; select one for a real workload rather than deploying both by default.
- DuckDB: embedded analytics engine for local event/evaluation analysis, not the transactional identity/task database.

### Models, inference and voice

- Ollama: easy local model-serving adapter candidate.
- llama.cpp: lower-level GGUF inference/runtime option.
- vLLM and SGLang: GPU server alternatives. Benchmark on supported GPU infrastructure; one baseline at a time.
- Hugging Face Transformers: model/tokenizer integration library, not a model entitlement.
- Text Embeddings Inference: embedding model serving.
- faster-whisper and sherpa-onnx: alternative local speech pipelines; compare language, latency, hardware, VAD and diarization requirements.
- Model weights, adapters, tokenizers and datasets need their own licenses, provenance, checksums and usage terms. A software library's MIT or Apache license does not license the weights it downloads.

### Quality, evaluation and security

- DSPy: optimization of prompts, skills and tool descriptions offline.
- Promptfoo: prompt/agent/RAG evaluation and authorized red-team tests.
- garak: LLM failure probes and security testing against owned or explicitly authorized systems.
- OpenTelemetry JS: observability foundation with redaction and retention policies.

The source register contains other candidates in the complete catalogue, including local home integration (Home Assistant) and model/document/search stacks. The lock is authoritative for exact pins.

## 3. Decision hierarchy: don't rewrite first

Apply this order to each feature:

1. **Use an existing ORBIT capability.** Fix or extend it if it meets acceptance criteria.
2. **Use an existing upstream dependency/package.** Prefer stable public APIs and an adapter.
3. **Integrate an external runtime.** Use process isolation and versioned protocol boundaries.
4. **Adapt a small source module.** Stage exact files, dependency closure, tests and license notices.
5. **Maintain a fork.** Only when a substantive long-lived product change cannot be expressed through extension APIs.
6. **Rewrite.** Only after the CTO records why upstream reuse is unsuitable, the performance/security requirements, and the estimated maintenance cost.

For every proposed rewrite, the developer writes a reuse-decision note with: feature, existing ORBIT module, upstream matches, files inspected, public APIs considered, license, build/test results, security findings, maintenance burden, recommendation and CTO approval.

## 4. Set up the dedicated 500 GB drive

Use the physical disk only after verifying its drive letter/mount. A marketed 500 GB disk may display around 465 GiB in Windows; this is normal. The setup script refuses a target below its configured minimum and never formats or partitions the disk.

### Windows

```powershell
Get-Disk | Format-Table Number,FriendlyName,SerialNumber,OperationalStatus,Size
Get-Volume | Format-Table DriveLetter,FileSystem,Size,SizeRemaining,HealthStatus
# Verify the intended physical disk and drive letter before proceeding.
.\scripts\init_orbit_storage.ps1 -Path 'E:\ORBIT-Storage'
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
$env:ORBIT_UPSTREAM_DIR = "$env:ORBIT_HOME\01-upstream-checkouts"
```

### Linux / WSL

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,LABEL
findmnt /mnt/orbit-storage
python3 scripts/orbit_storage.py init /mnt/orbit-storage
export ORBIT_HOME=/mnt/orbit-storage
export ORBIT_UPSTREAM_DIR="$ORBIT_HOME/01-upstream-checkouts"
```

Do not use `--skip-capacity-check` on the real disk. It exists only for automated tests.

### Allocation policy

| Directory | Target | Use |
|---|---:|---|
| `00-control` | 10 GB | lockfiles, audit reports, manifests, worktree metadata, runbooks |
| `01-upstream-checkouts` | 100 GB | pinned Git source checkouts, mirrors and selected sparse/partial clones |
| `02-workspaces` | 100 GB | real ORBIT repo worktrees, upstream patch worktrees, builds and ephemeral tasks |
| `03-models` | 90 GB | approved model artifacts, tokenizer and inference caches |
| `04-data-memory` | 35 GB | user-authorized data, memory and indexes; encrypted and scoped |
| `05-artifacts` | 25 GB | documents, media and exports |
| `06-evaluations` | 20 GB | benchmarks, promptfoo/garak results, golden sets and trace data |
| `07-logs-cache` | 5 GB | redacted logs and rebuildable caches |
| `08-backups` | 25 GB | encrypted local snapshots and restore tests |
| `09-quarantine` | 10 GB | untrusted source/skill intake, no execution |
| `10-source-intake` | 20 GB | reviewed source paths awaiting ORBIT integration |
| **Free reserve** | **60 GB** | growth, updates, build headroom and safe operation |

The targets total 440 GB plus 60 GB reserve. They are soft targets; the scripts do not enforce quotas. Keep critical backups on a separate physical drive or approved remote destination. A same-disk backup is not disaster recovery.

## 5. Acquire source selectively

First list the pinned sources:

```bash
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py show openmausbot
python scripts/orbit_repo_ops.py show openclaw
```

Start with a small slice, not all 41 repositories:

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --playwright --opensandbox
```

Other bundles:

```bash
# Messaging, agent gateway and connected tools
bash scripts/clone_upstreams.sh --openclaw --hermes --mcp-python-sdk --composio

# Documents and scoped retrieval
bash scripts/clone_upstreams.sh --docling --markitdown --llamaindex --qdrant

# Local model/voice path
bash scripts/clone_upstreams.sh --ollama --llama-cpp --faster-whisper --sherpa-onnx

# GPU serving comparison only on supported GPU infrastructure
bash scripts/clone_upstreams.sh --vllm --sglang

# Evaluation and security suite
bash scripts/clone_upstreams.sh --promptfoo --garak --dspy

# Local analytics and RAG comparison
bash scripts/clone_upstreams.sh --duckdb --haystack --chroma
```

Avoid bulk-cloning all repositories without checking size, network bandwidth and disk headroom. Do not run upstream install scripts or execute code as part of cloning.

Verify commits and origins:

```bash
python scripts/orbit_repo_ops.py verify
```

## 6. Inspect a repository before using code

Run the static inventory:

```bash
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openmausbot"
python scripts/orbit_repo_ops.py audit "$ORBIT_HOME/01-upstream-checkouts/openclaw"
```

Read the repository in this order:

1. Root `LICENSE`, `NOTICE`, `LICENSING.md`, `COPYING`, plus nested package licenses and third-party notices.
2. `SECURITY.md`, threat model, permissions, credential flows, sandbox and egress policies.
3. Root/package `README`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `pyproject.toml`, lockfiles, Dockerfiles and build scripts.
4. Module paths from `V07_REPOSITORY_FILE_LEVEL_ADOPTION_MAP.md` and `V08_OPEN_SOURCE_EXTENSION_REVIEW.md`.
5. The exact source file and adjacent unit/integration tests.
6. Dependency closure, install hooks, downloaded binaries, model files, generated assets and telemetry.
7. The upstream project's build/test commands, but only in a disposable isolated environment after reviewing scripts.

A static report is not malware detection, legal clearance or a build test.

## 7. Create a worktree for actual code modification

Never modify the pinned inspection checkout. Use the guarded helper:

```bash
python scripts/create_upstream_worktree.py \\
  --repo-id openmausbot \\
  --task approval-mode-adapter \\
  --created-by "Human reviewer"
```

It checks the locked origin, exact commit and clean worktree state before creating a new Git branch under `02-workspaces/upstream-worktrees`. It writes metadata under `00-control/worktrees`. It does not merge or push anything. For a task that belongs in ORBIT rather than in the upstream repository, use a separate worktree of the actual ORBIT application repository and adapt code there.

## 8. Stage a small reviewed source path

Inspect the module first. Then stage it with the pinned source commit and human review acknowledgements:

```bash
python scripts/import_upstream_path.py \\
  --repo-id openmausbot \\
  --checkout "$ORBIT_HOME/01-upstream-checkouts/openmausbot" \\
  --path shared/approval-mode.ts \\
  --approved-by "Human reviewer" \\
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \\
  --license-reviewed --security-reviewed --tests-reviewed
```

The importer verifies that the checkout origin and commit match the YAML lock, refuses `enterprise/`, path traversal, symlinks, secret-like files and common dependency/generated folders, then writes a SHA-256 import manifest. This is a staged copy, not a merge. Human flags are review acknowledgements, not an automatic legal determination.

For directory imports, inspect every copied file and dependency. The importer does not automatically copy dependencies or infer compatible versions. The reviewer owns that work.

## 9. Modify source without losing upstream lineage

For each adapted feature:

1. Create an ORBIT feature branch/worktree.
2. Preserve the original upstream URL, commit, path, and hash.
3. Add a thin ORBIT adapter rather than forking an upstream interface where possible.
4. Keep upstream changes under a visibly separated `third_party/` or documented package boundary if copied.
5. Preserve copyright, license, NOTICE and modification notices; never strip them to rebrand the UI.
6. Add source tests where feasible and ORBIT contract/security tests.
7. Add/update SBOM and component register; inspect transitive dependencies.
8. Run build, lint, typecheck, unit, integration, e2e, conformance and security tests.
9. Ask QA and Security for independent review; resolve all blockers.
10. Human founder approves any uncertain licensing, public release, production deployment or consequential external action.

Record upstream-to-ORBIT mapping in an import manifest, with a patch series or commit references. When syncing upstream later, compare the source base commit and the changed lines, not just directory contents.

## 10. Upstream update and sync procedure

Never change a pin silently. Create a planned update PR containing old/new commits, upstream release notes, changed files, license/NOTICE delta, SBOM delta, CVEs, deprecations, API breakage, build/test results and rollback plan. If local patches exist, rebase/cherry-pick them in an isolated worktree. Run the full conformance suite before refreshing the lock. Emergency security updates may be prioritized, but still need documented evidence.

## 11. Human and virtual team operating model

- Founder/CEO (human): approves spend, external commitments, legal decisions, production release and user-facing consequences.
- CTO/Principal Architect: selects one implementation per capability, approves source architecture and blocks duplicate runtimes.
- Repository Operations Engineer: maintains pins, clones, audits, worktrees, import manifests and upstream syncs.
- Open Source/IP Analyst: reviews license files, nested packages, notices, attribution, trademark and distribution obligations.
- Security/Privacy Lead: reviews secrets, egress, plugin isolation, data flow, skill threats and vulnerability findings.
- Developer/Feature Owner: adapts the smallest viable module and adds ORBIT adapters/tests.
- QA/Benchmark Engineer: runs reproducible success, reliability, latency, cost, safety and recovery tasks.
- SRE/DevOps: handles drive, backup, build cache, sandbox, metrics, recovery and capacity.
- Product/UX: validates that a capability removes real user effort and provides an understandable consent/approval surface.

AI role agents may research and propose changes. They are not legal employees or human approvers; they cannot self-approve licenses, secrets, payments, external publication or releases.

## 12. Competitor capability benchmark

Build tests around actual jobs rather than UI resemblance: persistent agent continuity, multiple specialist agents, own computer/browser workspace, safe connected apps, durable routines, user-controlled approvals, memory that can be corrected/deleted, coding tasks with passing tests, document research with citations, and cross-device continuation. Compare Grok Bot, Muse and dots only with public product claims and reproducible ORBIT task results. Do not claim ORBIT is better before measured evidence.

## 13. Useful commands

```bash
# catalogue and source integrity
python scripts/orbit_repo_ops.py list
python scripts/orbit_repo_ops.py verify

# inspect and audit
python scripts/orbit_repo_ops.py show promptfoo
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/promptfoo"

# isolated branch/worktree
python scripts/create_upstream_worktree.py --repo-id promptfoo --task orbit-eval-gate --created-by "Human reviewer"

# stage reviewed source
python scripts/import_upstream_path.py --help

# storage health and regression tests
python scripts/orbit_storage.py status "$ORBIT_HOME"
python -m unittest discover -s tests/operations -v
python scripts/validate_package.py
```

## 14. Completion definition

A repository operation is complete only when the report identifies the exact source commit and origin, license/notice evidence, source path and hash, dependency and security findings, isolated worktree/branch, change summary, tests, ORBIT conformance evidence, reviewer, rollback and upstream-sync plan. “Cloned” is only acquisition status, not feature delivery.
