# Local Desktop Node quickstart (implementation target)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

> This guide describes the planned workflow. The Local Desktop Node is not implemented by this documentation package.

1. Install ORBIT Desktop Node for your operating system from a verified release.
2. Open ORBIT Settings → Devices → Add desktop.
3. Start the local pairing flow and confirm the short-lived pairing code in both the node and ORBIT UI.
4. Review the requested capabilities. Initially enable read-only observation only.
5. Grant the minimum OS Accessibility permission required. Grant Screen Recording separately only when screenshots are specifically needed.
6. Confirm the device reports online, OS session interactive and expected driver version.
7. In a test workspace, ask the agent to inspect a harmless test application and report its visible state.
8. Review the task timeline, observations and local node activity indicator.
9. Pause or revoke the device and verify that all new actions are denied.

Do not pair a personal device to an untrusted ORBIT server. Do not use a main email/banking session for first tests. Use a disposable user account and test app. Never disable OS safeguards to make the feature work.

## ORBIT v0.2 alignment

The v0.2 guide set adds a Local Desktop Node setup target. Treat it as planned until code, installers and OS tests exist; see `DESKTOP_NODE_QUICKSTART.md` and `FEATURE_STATUS.md`.
