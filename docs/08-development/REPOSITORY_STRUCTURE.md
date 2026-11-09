# Repository structure proposal

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Use a monorepo only if shared contracts and release coordination justify it. Proposed structure:

```text
orbit/
  apps/web/                  # Next.js UI
  services/api/              # FastAPI control plane
  workers/agent/              # agent workflow activities
  workers/browser/            # isolated Playwright worker
  workers/code/               # sandbox executor
  workers/documents/          # parsing/indexing
  packages/contracts/         # generated OpenAPI/types
  packages/skills/            # built-in reviewed skills
  infrastructure/compose/    # local dependencies
  infrastructure/deploy/     # deployment manifests
  docs/                       # this documentation set
  tests/e2e/                  # cross-service tests
  scripts/                    # dev, migration, release utilities
```

Keep module boundaries explicit. Do not create empty folders before there is a real module. Avoid circular imports and cross-layer database access. API handlers call application services; workers call typed service/activities; domain logic does not depend on FastAPI, React or provider SDKs.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
