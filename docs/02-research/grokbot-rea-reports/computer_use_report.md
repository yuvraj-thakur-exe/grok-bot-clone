# GROKBOT-RE: Research Report 04 — Computer Use & Local Tool Integrations

## 1. Local vs Remote Computer-Use Boundary
The architecture draws a clear distinction between:
- **Local Machine Execution (Windows)**:
  - Bounded to the workspace directory under explicit user consent.
  - Commands executed via `powershell.exe` / `cmd.exe`.
  - Window and screen capture handled via `sand_window_capture.node` and `capture-overlay.html`.
  - Computer-use automation gate (`local-computer-use-gate.json`) defaults to `false` for security.
- **Remote Cloud Computer**:
  - Headless browser automation (Playwright runtime).
  - Sandboxed Linux micro-environments for long-running batch jobs and internet navigation without risking the user's personal host.

## 2. Tool Execution Sandbox Mechanics
- **Path Canonicalization**: Resolves real paths to prevent directory traversal (`..` escapes).
- **Execution Guardrails**:
  - Empty variable protection.
  - Root drive modification guards (preventing alterations to `C:\Windows` or system directories).
  - Timeout enforcement on all child processes.

## 3. Human Approval & Confirmation
- Critical operations (such as broad file deletions or unrestricted network egress) require interactive user approval in the client interface before dispatching.

