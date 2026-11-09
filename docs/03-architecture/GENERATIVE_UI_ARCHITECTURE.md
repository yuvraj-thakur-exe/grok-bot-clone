# Constrained generative UI architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Purpose

Allow ORBIT to produce useful task-specific user interfaces (research report panels, execution timeline, approval requests, configuration forms and data tables) without allowing models to generate arbitrary executable UI code.

## Design

1. ORBIT defines a versioned component catalog with JSON Schemas/Zod-like runtime schemas.
2. Model proposes a JSON UI spec referencing only catalog components, slots, state bindings and named action IDs.
3. Server validates schema, component allowlist, prop types, depth, element count, text limits, links, bindings and action IDs.
4. UI renders declarative components with a safe renderer.
5. User interactions emit named action events; server resolves those IDs to existing API operations and rechecks auth, policy, approvals, budget and resource scope.
6. Every rendered/actionable spec is versioned and attached to task/audit provenance.

## Hard limits

- No `eval`, arbitrary JS, HTML injection, CSS injection, dynamic imports, remote component loading or arbitrary URL execution.
- No component may directly call privileged tools from the browser.
- Action names are capabilities, not arbitrary backend method paths.
- Streaming partial specs render only after incremental validation; invalid fragments are quarantined and never executable.
- Limit maximum elements, nesting, string size and render time.
- Sanitize Markdown and links; disallow `javascript:` and unapproved schemes.
- Provide keyboard, screen-reader, focus, responsive and reduced-motion behavior.

## Catalog design

Separate `display components` from `interactive actions`. Display catalog includes text, metric, badge, table, chart, code block, citation, artifact link and timeline. Action catalog contains narrow operations such as `task.cancel`, `approval.approve`, `artifact.export` and `connector.authorize`; each maps to a backend policy check.

## Package decision

Evaluate `vercel-labs/json-render` as a library or architectural reference, but keep catalog, action policy, event schema, design tokens and product identity owned by ORBIT. Pin an exact release, audit transitive dependencies and preserve Apache-2.0 notices if included. A custom minimal renderer may be lower risk for the first MVP.
