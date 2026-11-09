# Desktop support matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** proposed; revalidate against exact pinned driver release and dedicated OS tests before publishing support claims.

| Platform | Accessibility API | Upstream documented baseline at review | Session / permission constraints | ORBIT launch scope |
|---|---|---|---|---|
| macOS | Accessibility API (AX) | macOS 13+, Intel and Apple Silicon | Accessibility permission for the launching process; Screen Recording separately for screenshot capture; automation prompts only when needed | First implementation target only if available interactive test host; read-only first |
| Windows | UI Automation (UIA) | Windows 10 1809+, x64/ARM64 | Signed-in interactive user desktop required; Session 0, Server Core/locked desktop/secure desktop/other user sessions are not supported | Support after UIA E2E on dedicated VM; never elevate to cross-user |
| Linux | AT-SPI | Ubuntu 24.04+, x86_64/aarch64 in upstream guide | Active graphical user session and accessibility bus; X11 and Wayland differ; sandboxed apps may hide bus | Support only tested distro/desktop/display combinations |

## Capability is multi-dimensional

Store per-device capabilities as `supported`, `unsupported`, `permission_required` or `unknown` per operation and context. The same platform may support semantic `click` but not screenshot, pointer control or window manipulation. Do not infer `supports_all_desktop_commands=true` from a successful status response.

## Decision rules

- If session is not interactive, do not issue mutations.
- If required permission is denied or unknown, do not infer permission or retry repeatedly; provide user instructions.
- If application accessibility tree is empty/incomplete, distinguish “no accessible data” from “application exposes no controls”.
- If pointer/screenshot path is unsupported (notably some Wayland cases), do not silently fall back to physical coordinate injection.
- Update matrix when upstream version changes and attach exact release + OS test evidence.

## ORBIT v0.2 alignment

The v0.2 architecture adds a Local Desktop Node and Desktop Session Broker. Native OS access remains separate from Playwright and the code sandbox; see `DESKTOP_COMPUTER_USE_ARCHITECTURE.md` and ADR-013.
