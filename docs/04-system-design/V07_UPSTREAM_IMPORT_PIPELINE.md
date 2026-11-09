# ORBIT v0.7 upstream import pipeline

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Pipeline states

`DISCOVERED → PINNED → CLONED → STATIC_AUDITED → LICENSE_REVIEWED → SECURITY_REVIEWED → TESTED_UPSTREAM → SELECTED_PATHS → STAGED → ADAPTED → ORBIT_TESTED → REVIEWED → MERGED → MONITORED`

No state is skipped by simply copying code. Any blocked or unknown license/security state stops redistribution and production integration.

## Required records

Every imported module gets `upstream_id`, canonical URL, source commit, source path, source digest, license evidence, notice references, import date, reviewer, modification summary, destination path, tests and merge commit. `IMPORT_MANIFEST.json` is the minimum file-level provenance artifact. The final ORBIT repository also keeps a source attribution register and SBOM.

## Reuse modes

| Mode | Appropriate when | Maintenance risk |
|---|---|---|
| Dependency/package | Maintained public API exists | Version updates and transitive license/security review |
| External service/runtime | A full existing product already provides the capability | Process/API compatibility, isolation and resource usage |
| Adapter | ORBIT needs one stable interface across backends | Adapter maintenance, lower upstream coupling |
| Selective source import | Small cohesive module must be customized | Copied-code drift; record origin and upstream sync plan |
| Fork | Core needs deep changes and upstream cadence must be tracked | Long-term merge burden; keep fork remote and patch stack |
| Reimplementation | License/architecture/integration makes reuse unsuitable | Higher initial cost, but ORBIT owns implementation |

## Import decision algorithm

1. Search ORBIT code for an existing equivalent and tests.
2. Search upstream documented APIs and package exports.
3. Prefer a dependency when it meets requirements and is actively maintained.
4. Prefer external adapter where upstream is a whole product/runtime.
5. Copy only a self-contained module with tests and notices when API reuse is impossible.
6. Use a fork only if source-level changes are recurrent and worth the rebase burden.
7. Reimplement only after CTO records the rejected reuse reasons and estimates cost.

## Mandatory controls

- Use an immutable commit pin, not a moving branch.
- Never import enterprise/restricted directories or private assets.
- Do not import `.env`, key files, private certificates, runtime state, logs, user data or tokens.
- Preserve licenses, copyright, attribution and modification notices.
- Run imported code in isolated, least-privilege environments before review.
- Treat upstream tests as one input, not proof of ORBIT compatibility.
- Require ORBIT contract tests and security tests before merge.
- No agent can approve its own risky import, security exception or production release.
