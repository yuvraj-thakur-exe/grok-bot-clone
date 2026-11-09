# GROKBOT-RE: Verified Facts

The following facts have been cryptographically verified, observed through permitted local runtime artifacts, or extracted directly from official documentation:

## 1. Product Identity & Multi-Party Architecture
- **Publisher Discrepancy**: The installer `Grok_Bot_0.78.1_Setup.exe` and `Grok Bot.exe` carry PE version metadata stating `SpaceXAI` as the company and product owner, while Authenticode digital signatures are signed by **Anysphere, Inc.** using a certificate issued by `Microsoft ID Verified CS AOC CA 03`.
- **Anysphere Integration**: The application uses Cursor/Anysphere desktop infrastructure (`@anysphere` monorepo modules, `cursor-proclist`, `cursor.com` registry entries). However, official terms and documentation confirm Grok Bot is a distinct user-facing product built on top of Cursor's platform, utilizing Anysphere third-party components rather than being a mere rebranding.

## 2. Desktop & Process Runtime
- **Electron Packaging**: Built on Electron (x86_64 main host), bundled with Rolldown/Vite. The main bundle resides in `resources/app.asar`, while native Node addons and auxiliary executables (`elevate.exe`, `sand-webauthn-signer.exe`) reside outside the archive in `resources/app.asar.unpacked/`.
- **Dual Execution Topology**:
  1. **Local Agent Bridge**: Powered by `local-exec-daemon` and `local-exec-supervisor`. Discovered running under PIDs with dedicated files key IDs and shell code page fallbacks (OEMCP 437, ACP 1252).
  2. **Remote Cloud Computer**: Documented in official docs as persistent cloud-hosted working environments providing browser isolation, cloud filesystem persistence, and background agent execution.
- **Local IPC Handshake**: Communicates between Electron Main, Preload, and Renderer using `sand:boot-snapshot-sync` and transfers high-bandwidth agent traffic via dedicated MessagePort channels (`sand:coordinator-port`).

## 3. Configuration & Feature Gating
- **Local Computer Use Gate**: `local-computer-use-gate.json` contains `{"isOn": false}`, proving that local computer-use/desktop automation is explicitly feature-gated and disabled by default.
- **Mac Device Gate**: `mac-device-tools-gate.json` contains `{"isOn": false}`, isolating platform-specific tools on Windows hosts.
- **Active Settings**: `settings.json` explicitly tracks `autoUpdateWhenIdle: true`, `localEgressAllowed: true`, `webauthnProxyEnabled: true`, `messagesReadEnabled: true`, and `messagesSendEnabled: true`.

## 4. Native Capabilities & Tools
- **Native Bindings**: Unpacked `.node` binaries verified:
  - `cursor_proclist.node`: Process monitoring.
  - `sand_window_capture.node`: Window/region desktop capture.
  - `sand_card_text_recognition.node`: OCR engine.
  - `sand_devicecheck.node`: Hardware/device attestation.
  - `tree_sitter_runtime_binding.node` & `tree-sitter-bash.node`: AST-level shell/code parsing.

