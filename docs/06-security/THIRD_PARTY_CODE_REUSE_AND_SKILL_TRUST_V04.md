# Third-party code reuse and skill trust — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Threat model

ORBIT integrates a large, changing ecosystem of source repositories, packages, extensions, skills, MCP servers, agent runtimes, native binaries, cloud services and user-authored prompts. Each can introduce vulnerabilities, prompt injection, supply-chain compromise, license obligations, data exfiltration, remote code execution or unexpected side effects.

## Code and package intake

1. Pin exact release/commit and digest.
2. Record canonical repository, maintainer, source tree, SPDX expression, license text and NOTICE.
3. Generate SBOM including transitive dependencies and native binaries.
4. Run vulnerability and secret scanning; inspect install/postinstall scripts and telemetry.
5. Build in isolated CI and compare artifact checksums.
6. Review permissions, network egress, filesystem access and subprocess behavior.
7. Add integration tests and rollback path.
8. Obtain legal/security approval for custom, unknown, missing or source-available licenses.

## Skill package trust

A skill is treated as untrusted input until reviewed. It may contain prompt instructions, scripts, executable binaries, MCP endpoint definitions, environment variable access or remote download commands.

### Required manifest fields

- immutable `source` and `revision`;
- full file inventory and SHA-256 digest;
- SPDX license or explicit blocked status;
- author, repository, maintainer and last-reviewed time;
- tool/capability requests, filesystem scope and network domains;
- script entrypoints, runtime and dependencies;
- security scan and isolated test result;
- ORBIT policy profile and human reviewer;
- active/revoked state and previous safe version.

### Install lifecycle

`discover → fetch → inspect → license_review → scan → sandbox_test → permission_review → approve → pin → activate`

Never install from a skill name alone. Do not execute install scripts at discovery time. Resolve all remote URLs, inspect redirects and block private/link-local/cloud metadata IPs. Disable auto-update for active skills; updates create a new immutable version and repeat the intake process.

### Runtime controls

- Load skill content as reference instructions, never as system-level policy.
- Tool permissions come from ORBIT policy, not skill frontmatter.
- Script execution occurs in an isolated sandbox with read-only package mount where possible.
- Deny credential file reads, host filesystem traversal and unrestricted network by default.
- Apply per-skill CPU, memory, wall-time, output and tool quotas.
- Log skill identity/version and redacted execution evidence.
- Provide immediate disable/revoke and rollback.

## Upstream-specific notes

- **OpenClaw:** native plugins share the Gateway process trust boundary and are not sandboxed. Treat them as trusted code, review and pin them; isolate untrusted extensions in a separate process.
- **OpenMausBot:** its `enterprise/` subtree has a separate source-available license and must be excluded from ORBIT source reuse unless separately licensed. Keep root and nested notices.
- **OpenMausBot secrets:** do not inherit CLI plaintext key persistence (`config.json`, mode `0600` on Unix) without a security decision. The packaged desktop flow documents OS-backed encryption where supported; validate platform-by-platform and route ORBIT secrets through its approved vault.
- **Hermes self-evolution:** current README and `pyproject.toml` declare MIT while a root LICENSE file was not found in the pinned source snapshot; confirm with the rights holder before redistribution. Keep the AGPL Darwinian Evolver out of the main process/distribution unless separately approved.
- **VoltAgent catalogue:** repository MIT license covers its own catalogue content; each linked skill keeps its own terms and source provenance.

## Self-improving agent controls

- Optimize only in an isolated branch/workspace.
- Keep baseline, dataset version, training/validation/holdout split, model/provider, cost and optimizer settings.
- Never evaluate on sensitive user history without explicit consent, redaction and retention approval.
- Holdout set must remain unseen during optimization.
- Candidate must pass tests, safety evals, skill permission validation and regression checks.
- Compare success rate, failure class, policy violation, tool selection, cost and latency.
- Require reviewer approval and a pull request before promotion.
- Roll back automatically when safety/quality metrics regress beyond approved limits.
- Never let an agent edit its own permissions, audit records, release policy, credential scope or evaluation gate.

## Required artifacts

`config/upstreams/upstream-lock.yaml`, `docs/06-security/THIRD_PARTY_COMPONENT_REGISTER.yaml`, SBOM, NOTICE, license review, vulnerability report, skill lockfile, policy review, test evidence and release approval.
