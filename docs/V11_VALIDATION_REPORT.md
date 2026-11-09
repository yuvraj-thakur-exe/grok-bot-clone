# ORBIT v1.1 validation report

**Build date:** 2026-11-08. **Environment:** Linux x86_64 container, Python 3.13.5.

## Results

| Check | Result | Evidence |
|---|---|---|
| Python compilation | PASS | `PYTHONPATH=src python -m compileall -q src tests` |
| Unit tests | PASS | 17 tests; `PYTHONPATH=src python -m unittest discover -s tests -v` |
| Task manifest JSON | PASS | `python -m json.tool configs/tasks.example.json` |
| Upstream pin-lock JSON | PASS | `python -m json.tool configs/upstream-candidates.lock.json` |
| CLI version | PASS | `./orbit.sh --version` → `ORBIT DevKit 1.1.0` |
| Host doctor | PASS | Linux x86_64, Python 3.13.5; Git, Node, npm, uv and Bash detected |
| Task DAG validation | PASS | Four-task example accepted |
| Four-task execution | PASS | `host-doctor`, `config-parse`, `unit-tests`, `post-check` all returned status `passed` and return code 0 |
| Context budget smoke test | PASS | Generated context manifest reported 2,500 / 2,500 estimated tokens |
| POSIX launcher | PASS | `./orbit.sh` used for version, doctor, validation, task execution and context pack |

## Test coverage added

- Context pack: selected source inclusion; sensitive directory exclusion; common token-shaped secret redaction; strict approximate token-budget cap; previously generated output and manifest are not re-ingested.
- Storage: decimal-GB layout totals 440 GB of soft targets; 60 GB reserve is distinct; directories and manifest are created; repeated initialization does not report existing directories as newly created; relative paths and invalid reserves are rejected; manifest root mismatch is refused.
- Task runner: valid DAG accepted; shell-string field rejected; workspace path escape rejected; dependency cycles and unknown dependencies rejected; sensitive environment allowlist rejected; sensitive parent environment values are not inherited by default; task execution writes per-task logs and a summary; workspace-write task does not execute without explicit acknowledgement.

## Environment notes

Detected in the build container: Python 3.13.5, Node.js 22.16.0, Git, npm, uv and Bash. Docker, pnpm, PowerShell (`pwsh`/`powershell`), zsh and Task were not detected.

## Not yet validated

- Python 3.11 specifically. The package declares Python >=3.11; local validation used 3.13.5.
- Execution of `.bat` on Windows, `.ps1` under PowerShell, or `.sh` on macOS.
- Remote GitHub Actions results on Windows, Ubuntu or macOS. The matrix is configured but was not remotely executed in this session.
- Real 500 GB physical drive identification or initialization. Only temporary directories were used in unit tests. The user must verify the physical disk before initialization.
- Repository clone or source import. The six repositories are pinned candidates only.
- Any integration into the real ORBIT application. Its Git URL/path is not available in this session.
- Browser automation, native desktop automation, production model adapters, policy broker, remote sandbox or multi-agent execution.

## Security scope

This developer task runner invokes local processes with `shell=False`, an argument array, bounded output/runtime and minimal environment inheritance. It is not a hardened sandbox for hostile code. Context redaction is best-effort and not a secret scanner. Do not use either component to process untrusted repository code without the planned isolated worker and security controls.
