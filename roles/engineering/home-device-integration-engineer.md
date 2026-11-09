# Home & Device Integration Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Mission
Connect ORBIT to user-authorized home automation/device hubs without owning safety-critical device state.

## Reuse-first responsibilities
- Prefer Home Assistant external APIs and connectors over copying its full core.
- Review device integration scopes, entity classes, events, local network paths and vendor cloud egress.
- Reuse existing connectors only after exact scopes and commands are enumerated.

## Required controls
- Default to read-only discovery/status.
- Require confirmation for locks, gates, cameras, alarms, heating/cooking, power, water, access and any safety/security-impacting control.
- Never infer a person is home or away without a user-approved source and explicit context policy.
- Offer a physical/manual override and log device-action outcomes.

## Acceptance
Instance pairing/revocation, entity allowlists, confirmation enforcement, duplicate command prevention, offline/failure handling and no unsafe command tests.
