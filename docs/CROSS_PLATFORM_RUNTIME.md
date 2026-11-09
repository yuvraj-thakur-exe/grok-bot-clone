# ORBIT cross-platform runtime strategy

## Design rule

One ORBIT product, one set of public contracts, multiple platform adapters. Windows, macOS and Linux launchers are thin entry points only. They must not contain duplicated business logic.

## Supported development baseline

| Tier | Environment | Status in this toolkit |
|---|---|---|
| Tier 1 | Windows 10/11 x64 with Python 3.11+ | Shared Python CLI; PowerShell/CMD launchers |
| Tier 1 | macOS with Python 3.11+ | Shared Python CLI; POSIX launcher |
| CI target | Windows x64 with Python 3.11+ | Shared Python CLI; CMD and PowerShell launchers; configured CI job |
| CI target | macOS runner with Python 3.11+ | Shared Python CLI; POSIX launcher; configured CI job |
| CI target | Ubuntu runner with Python 3.11+ | Shared Python CLI; POSIX launcher; configured CI job |
| Evaluate | Linux ARM64, Windows ARM64, WSL2, BSD and other Unix variants | Build and run platform-specific CI before claiming support; WSL2 does not bridge to the Windows interactive desktop |

This matrix describes configured CI targets, not completed remote CI evidence. The current toolkit has been executed only in the Linux container used for this build. It does not promise that every ORBIT feature or third-party dependency works on every operating system.

## Runtime domains remain separate

1. Browser: Playwright worker and isolated browser context. Web pages are not native desktop apps.
2. Native desktop: paired Local Desktop Node in the logged-in interactive user session, using a platform accessibility adapter. No generic cloud worker can inherit a user's physical desktop.
3. Code: disposable sandbox or microVM with scoped mounts, network policy and resource ceilings. Never execute upstream/model-generated code on the host.
4. Control plane: canonical workspace/task/approval/audit state, independent of which OS executes a worker.

## Platform adapters

- Windows: `.bat` for CMD, `.ps1` for PowerShell, Python `subprocess` with `shell=False`, Windows UI Automation for the future desktop adapter.
- macOS: `.sh`/zsh-compatible launcher, Python `subprocess` with argument arrays, Accessibility APIs behind `DesktopDriver`.
- Linux: `.sh` launcher, XDG paths, AT-SPI behind `DesktopDriver`; Wayland/X11 capabilities must be detected, not assumed.
- WSL2: treated as a Linux code/browser development environment, not as the Windows interactive desktop bridge.

## Capability negotiation

The OS name is not enough. Each worker reports an explicit capability document: OS release, architecture, display/session availability, accessibility permissions, browser install, sandbox provider, GPU/VRAM, RAM and network policy. The planner may use only reported capabilities. Missing or unknown capability means unavailable.

## Dependencies

- Core developer helper: Python standard library, Python >=3.11.
- Optional Python project management: uv; consult its current supported-platform matrix before standardizing it on a given architecture. The project does not require uv for the core CLI. See [uv platform support](https://docs.astral.sh/uv/reference/platforms/) and [uv lockfiles](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile).
- Browser: Playwright; follow its current supported Node.js and OS matrix and pin browser binaries to the Playwright package version. See [Playwright system requirements](https://playwright.dev/docs/intro#system-requirements).
- Task runner: ORBIT's own JSON DAG runner for the minimal local workflow. Do not introduce a second general scheduler without a specific need.
- Node.js: pin the supported version in `.node-version` / tool-version metadata after the actual product shell and upstream runtime are selected.

## CI gate

Run lint/typecheck/unit/contract tests on `windows-latest`, `ubuntu-latest` and `macos-latest`. Real desktop automation requires isolated GUI sessions and separate platform-specific integration tests; a passing compile job does not prove desktop automation support.
