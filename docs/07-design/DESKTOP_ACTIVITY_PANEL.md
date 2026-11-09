# Desktop activity panel UX requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Required UI

- Device list: device name, OS/platform, driver version, last seen, permissions and online/paused/revoked state.
- Active task card: task title, agent name, current app/window, current action, lease expiry, progress and stop button.
- Observation viewer: redacted accessible tree, semantic roles/labels, completeness badge and snapshot age; raw text not default for unrelated controls.
- Approval card: exact target, operation, reason/risk, normalized arguments summary, workspace/device, expiry and approve/deny controls.
- Timeline: observation, tool request, approval, action receipt, verification, failure and recovery events.
- Privacy settings: separate toggles for screenshots, clipboard and debug artifacts; all disabled by default.
- Permission guide with OS-specific instructions; never imply permissions were granted until capability probe confirms it.

## UX rules

- Always show when desktop control is active. Never hide it in a background agent status.
- Distinguish “action dispatched”, “UI state verified” and “task completed”.
- Show delivery uncertainty prominently and advise manual inspection rather than a retry button.
- Stop/pause must be reachable within one interaction from the node and main ORBIT interface.
- Show which device is being controlled before starting a task and allow the user to select another device.
- Avoid showing screenshots or private app content in generic analytics or notification previews.

## ORBIT v0.2 alignment

The v0.2 experience adds explicit device pairing, visible desktop activity and immediate stop/pause. Show action delivery separately from UI verification; see `DESKTOP_ACTIVITY_PANEL.md`.
