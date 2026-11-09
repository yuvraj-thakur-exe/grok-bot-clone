# Browser, terminal and sandbox security

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Browser worker

Use Playwright with a fresh isolated BrowserContext per user/workspace/task policy. Contexts isolate cookies, local storage and permissions. Persist authenticated state only after explicit opt-in and encrypt it. Enforce URL scheme allowlist, domain policy, DNS/IP checks and egress proxy controls. Block localhost, private network ranges, cloud metadata endpoints and unexpected redirects. Re-resolve DNS at connection time to reduce rebinding risk.

## Computer-use boundary

Prefer DOM/accessibility-tree interaction for reliability and semantic checks; use screenshots for visual state and fallback. Show user-visible current action and allow cancellation. Pause for CAPTCHA/MFA/human verification. Tor, where later supported, must be an explicit separate profile with separate storage, no credential sharing and no use to evade access controls.

## Code sandbox

Use disposable per-task environments with CPU, memory, process, disk and time quotas. No host Docker socket, no privileged container, no home-directory mount, no host credentials, no unrestricted network. Mount only a task snapshot and an explicit output directory. Destroy environment after artifact collection. Rootless containers reduce risk but are not a complete hostile-code sandbox; evaluate stronger isolation such as gVisor, Kata or Firecracker for multi-tenant execution.

## Acceptance tests

Test path traversal, symlink escape, private-IP SSRF, DNS rebinding, malicious redirects, archive bomb, fork bomb, memory exhaustion, container breakout controls, credential exfiltration and cancellation under load.

## Execution domains must remain separate

The Local Desktop Node is not a browser worker or code sandbox. Do not share its OS permissions, browser cookies, desktop session, clipboard or local home directory with Playwright or code execution. A browser page opened natively on the user's computer does not inherit Playwright's isolation; prefer the isolated browser worker for web tasks. See `DESKTOP_CONTROL_SECURITY.md`.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.
