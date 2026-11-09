# UX and information architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Primary navigation

Workspace switcher; Home/Chat; Projects; Agents; Tasks; Research; Files; Skills; Routines; Connectors; Evaluations; Settings. Keep navigation task-oriented and avoid a dashboard full of decorative empty cards.

## Primary journeys

1. Start a conversation, attach files, select mode, submit.
2. Convert a request into a task, review the plan, monitor progress, approve or cancel, inspect result/artifacts.
3. Create agent, configure role/model/tools, test in sandbox, publish to workspace.
4. Create skill from reviewed workflow, test, version, install, schedule if permitted.
5. Connect provider/service through consent and scope review, test connection, revoke later.

## UX principles

- Make “what is happening now?” visible: current task, agent, step, tool, status, elapsed time and cancel action.
- Distinguish model response, tool activity, source evidence, artifact and approval request.
- Show citations next to the relevant research claim.
- Explain failures with a useful next action and preserve partial work.
- Keep destructive and consequential actions explicit, never hidden behind a generic “continue”.
- Support keyboard navigation, focus visibility, contrast and screen readers.

## v0.2 desktop navigation

Add Settings → Devices for pairing/revocation, and an in-task Desktop activity panel for target device, current app/window, action, lease state, permissions, approval, verification and pause/stop. Desktop should be optional and visibly enabled, not silently assumed. See `DESKTOP_ACTIVITY_PANEL.md`.

## ORBIT v0.2 alignment

The v0.2 experience adds explicit device pairing, visible desktop activity and immediate stop/pause. Show action delivery separately from UI verification; see `DESKTOP_ACTIVITY_PANEL.md`.
