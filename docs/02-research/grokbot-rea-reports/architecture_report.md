# GROKBOT-RE: Research Report 01 — Desktop Architecture

## 1. Executive Summary
This report analyzes the desktop application architecture of Grok Bot 0.78.1, establishing the separation between host processes, application packaging, native extensions, and renderer presentation layers.

## 2. Packaging & Delivery Layout
- **Container Format**: Standard Windows PE 64-bit Electron package.
- **Archive Boundary**:
  - `resources/app.asar` (52.6 MB): Contains bundled JavaScript application code, StyleX/CSS styles, web worker blobs, and protocol definitions.
  - `resources/app.asar.unpacked/` (~38 MB): Houses components that cannot execute from within a virtualized archive:
    - Native Node-API `.node` binaries (`cursor_proclist.node`, `sand_window_capture.node`, etc.).
    - Standalone executables: `elevate.exe` (UAC privilege elevation), `sand-webauthn-signer.exe` (FIDO2 authentication).

## 3. Process Architecture
1. **Electron Browser Process (`Grok Bot.exe`)**:
   - Manages Window hierarchy (`BrowserWindow`), tray icons, native menus, and global hotkeys (`Alt+Shift+Space`).
   - Brokers IPC message passing.
2. **Local Daemon Process (`local-exec-daemon`)**:
   - Manages local shell executions (PowerShell, Bash, CMD).
   - Monitored by a supervisor watchdog process (`local-exec-supervisor.json`).
3. **Renderer Processes**:
   - Main Chat Workspace (`index.html`).
   - Floating Desktop Mount Panel (`panel.html`).
   - Bounded Region Capture Overlay (`capture-overlay.html`).

## 4. Architectural Relationship: Grok Bot vs Anysphere Stack
Evidence proves Grok Bot is an autonomous agent product with its own brand identity, business terms, and agent persona, built on Anysphere's desktop agent foundation (`sand`). It shares low-level device and execution libraries with Cursor while providing independent agent capabilities.

