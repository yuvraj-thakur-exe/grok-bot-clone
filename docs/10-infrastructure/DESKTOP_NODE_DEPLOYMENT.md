# Local Desktop Node deployment

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Deployment model

The Local Desktop Node is an optional companion installed on the machine whose native applications ORBIT is permitted to control. It runs as the signed-in user's normal account in the active graphical session. It is not a cloud VM agent and not a system service.

## Installation design

- Package per OS/architecture with signed installer/update metadata where practical.
- Install `agent-desktop` as a pinned dependency or bundled verified binary; publish checksum and provenance.
- Register a per-user launch mechanism (not privileged startup service).
- Create a private config/state directory with restrictive permissions.
- Store node identity key using OS credential storage; avoid secrets in `.env`.
- Provide CLI/headless status mode but require explicit user consent for desktop-control activation.
- Provide uninstaller that revokes device and removes local secrets/config with clear user confirmation.

## Node runtime configuration

Required values: control-plane WSS endpoint, public device identity/certificate, workspace/device registration ID, driver executable path and approved version, local policy profile, log level and resource limits. Avoid long-lived model/provider keys on the node.

See `.env.example` and `DESKTOP_COMMAND_ALLOWLIST.yaml`. Config parsing must reject unknown fields for security-critical settings.

## Network

- Outbound TLS/WSS only; standard proxy support may be configurable.
- No inbound port; no UPnP or router port forwarding.
- Authenticate node and broker; rotate credentials; include nonce/request ID and task lease in every message.
- No command is accepted without a current signed/validated lease.
- Rate-limit reconnect and pair attempts.

## Updates and rollback

- Verify package signature/checksum before activation.
- Stage update, run `status` + capability/contract self-test, then switch version.
- Retain last known good binary; rollback if self-test fails.
- Do not silently auto-update across an incompatible JSON contract; coordinate backend compatibility.

## Container/dev environment

The control plane and brokers can be containerized. A desktop node generally cannot run in the same standard container as the control plane if it needs the user's real display/accessibility session. For CI, use fake-driver integration tests and dedicated interactive test VMs. Never mount host X11/Wayland sockets or `/dev` into a multi-tenant agent worker as a convenience shortcut.

## ORBIT v0.2 alignment

The v0.2 deployment topology keeps the Local Desktop Node on the user’s interactive host; the cloud control plane only brokers authenticated leased tasks. See `DESKTOP_NODE_DEPLOYMENT.md`.
