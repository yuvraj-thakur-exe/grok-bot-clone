# Mobile Companion Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Mission
Build secure mobile companion capabilities for chat, voice capture, notifications, approvals, device pairing and human takeover.

## Reuse-first responsibilities
- Inspect the existing ORBIT client before creating a new app.
- Compare existing OpenMausBot companion patterns and platform-native APIs; reuse only reviewed protocol/contracts and preserve notices.
- Keep mobile device grants separate from desktop and cloud computer grants.
- Use push payloads that do not leak sensitive task content by default.

## Required controls
- Device binding/revocation, biometric/OS unlock where available, short-lived pairing, encrypted transport and no secret in push notification.
- App foreground/background state must not be an authorization signal.
- Explicit human approval for purchases, external messages, bookings, destructive actions and sensitive account changes.

## Acceptance
Pair/revoke, notification redaction, offline/reconnect, approval confirmation, lost-device recovery, accessibility and mobile data-retention tests.
