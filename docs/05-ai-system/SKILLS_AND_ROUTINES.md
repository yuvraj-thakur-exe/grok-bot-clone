# Skills and routines

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Skill manifest

A skill is a versioned workflow package with name, purpose, compatible ORBIT version, inputs, outputs, required tools/scopes, step instructions, validation, failure paths, examples, risk classification, author and provenance. Keep executable code separate from natural-language instructions and sign/version release artifacts.

## Skill lifecycle

Draft -> review -> test in sandbox -> publish version -> install with explicit scopes -> monitor -> deprecate. Skills imported from the community are untrusted until reviewed. A successful task can suggest a draft skill, but must not silently promote it.

## Routines

Triggers include cron/timezone, webhook, provider event or internal state event. Routines create ordinary task instances and inherit normal quotas, policy and approval requirements. Provide pause, disable, run-now, edit, inspect history and delete controls. Add deduplication windows and missed-run policy.

## Safety

Scheduled tasks must not bypass approvals just because they are recurring. Consequential actions can use pre-authorized narrow policies only after explicit user configuration, exact scope and expiry. Repeated failures auto-pause and alert the owner.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.


## v0.5 skill intake gate

Skill discovery is not installation. A skill stays quarantined until canonical origin, immutable commit, digest, license, attribution, dependencies, permissions, scripts and sandbox tests are reviewed. Activation is explicit per workspace and agent. Routines start paused and may not perform consequential external actions without required approval.

