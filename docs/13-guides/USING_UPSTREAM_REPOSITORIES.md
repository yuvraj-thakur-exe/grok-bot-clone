# Using the upstream repositories for ORBIT — practical guide v0.6

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## 1. Prepare the 500 GB drive

Windows PowerShell:

```powershell
py -3 scripts/orbit_storage.py init E:\ORBIT-Storage
$env:ORBIT_HOME = 'E:\ORBIT-Storage'
```

Linux:

```bash
python3 scripts/orbit_storage.py init /mnt/orbit-storage
export ORBIT_HOME=/mnt/orbit-storage
```

## 2. Inspect clone options

```bash
bash scripts/clone_upstreams.sh --help
```

The clone helper uses pinned commit SHAs from `config/upstreams/upstream-lock.yaml`. If `ORBIT_HOME` is set, checkouts go to `$ORBIT_HOME/01-upstream-checkouts`; `ORBIT_UPSTREAM_DIR` overrides this. It uses partial/shallow fetch where supported. It does not install dependencies or execute upstream scripts.

## 3. Clone in sensible batches

Begin with the product shell and two execution boundaries:

```bash
bash scripts/clone_upstreams.sh --product-base --openhands-sdk --opensandbox
```

Then runtime/gateway options:

```bash
bash scripts/clone_upstreams.sh --openclaw --hermes --self-evolution --skills-index
```

Then add only the components needed by the next task:

```bash
bash scripts/clone_upstreams.sh --stagehand --docling --mcp-python-sdk --composio
bash scripts/clone_upstreams.sh --ollama --llama-cpp --faster-whisper
```

Do not clone every candidate simply because disk space exists. Start with only the upstreams needed for the milestone. `--all-supplied` acquires the five user-supplied repositories. `--all-new-candidates` acquires the nine v0.6 additions.

## 4. Audit each checkout

```bash
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openmausbot"
python scripts/repo_audit.py "$ORBIT_HOME/01-upstream-checkouts/openclaw"
```

Reports are written to the default local `reports/repo-audits/` folder unless `--output-dir` is supplied. The audit is static inventory and lightweight risk-marker discovery, not a full security scanner.

## 5. Read key source files and their tests

Use GitHub/IDE search and the checked-out source:

- OpenMausBot: `server/agent-tool-policy.ts`, `server/agents-turn.ts`, `server/app-events.ts`, `shared/approval-mode.ts`, `shared/live-approval.ts`, `shared/routine-schedule.ts`, `shared/skill-import.ts` and the associated test files.
- OpenClaw: `packages/plugin-sdk/`, `packages/gateway-client/`, `packages/gateway-protocol/`, `extensions/browser/`, `extensions/duckduckgo/`, `extensions/deep-research/`, `extensions/document-extract/`, `extensions/github/`, `extensions/diagnostics-otel/`.
- Hermes: `agent/`, `gateway/`, `cron/`, `evals/`, `hermes_cli/`, `acp_adapter/`; favor a process/protocol adapter over importing private internals.
- Self-evolution: `evolution/`, `datasets/`, `tests/`; evaluate prompts/skills offline only.
- VoltAgent catalogue: `categories/` and `README.md`; follow every skill to its canonical source and license.

## 6. Copy a selected path into source intake

Only after review, use:

```bash
python scripts/import_upstream_path.py --help
```

Example:

```bash
python scripts/import_upstream_path.py \
  --repo-id openmausbot \
  --checkout "$ORBIT_HOME/01-upstream-checkouts/openmausbot" \
  --path shared/approval-mode.ts \
  --approved-by "human-founder" \
  --license-evidence "https://github.com/milind-soni/OpenMausBot/blob/main/LICENSE" \
  --license-reviewed --security-reviewed --tests-reviewed
```

The tool stages a file/directory under `10-source-intake/` and writes a provenance manifest. It is not an automatic merge. Check source dependencies, tests, nested licenses, modification notices and import hashes before moving code to the real ORBIT application repo.

## 7. Make a focused modification

- Work in a Git worktree on an isolated task branch.
- Keep the original base commit in task metadata.
- Add adapter code rather than modifying upstream interfaces where possible.
- Preserve tests; add ORBIT contract and policy tests.
- Record each source file copied or modified in the source import manifest.
- Run formatter, lint, typecheck, upstream tests and ORBIT conformance tests.
- Review diff, security scan, SBOM and license report before PR.

## 8. What not to do

- Do not import the whole OpenClaw, Hermes or OpenMausBot runtime as a single unreviewed folder.
- Do not use OpenMausBot `enterprise/` without a separate written license.
- Do not strip LICENSE/NOTICE/attribution/modification notices.
- Do not treat VoltAgent's catalogue license as the license of its linked skills.
- Do not run a third-party install script or skill on your host without review and isolation.
- Do not put secrets, private cookies or user data in code samples or model prompts.
- Do not claim ORBIT integrated a repo because it is cloned.

## 9. What to send back after audit

For each cloned project provide the generated report, build/test outcomes, exact SHA, dirty state, selected files, license/notice scan, security observations, reuse mode and a recommended ORBIT adapter. This is the evidence the CTO uses to decide what enters the application.
