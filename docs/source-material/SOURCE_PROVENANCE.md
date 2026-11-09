# Source provenance

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

This directory preserves the two user-supplied text sources used to create the ORBIT engineering pack.

1. `USER_PROVIDED_DOCUMENTATION_BLUEPRINT.md`: catalogue and workflow for pre-development documentation, architecture, security, testing, deployment and operations.
2. `USER_PROVIDED_ORBIT_MASTER_BRIEF.md`: ORBIT AI product brief and master engineering directive, including competitor research scope, product capabilities, proposed technology stack, execution phases, quality/security expectations and final deliverables.

The preserved files are byte-for-byte copies. SHA-256 digests and byte lengths are recorded in `PACKAGE_MANIFEST.json`.

The rest of the pack transforms these sources into an ORBIT-specific specification. It also adds engineering recommendations and public-source research. Those additions are labelled as proposed decisions, assumptions, research findings or unverified areas. Do not treat a recommendation in the generated pack as a requirement stated verbatim in the source files unless it appears in the source.

## v0.2 native desktop reference

3. `https://github.com/vercel-labs/agent-desktop`: public upstream repository inspected on 2026-11-08. Its README, AGENTS, CONCEPTS, JSON output contract, platform skills, dispatcher, policy and adapter interfaces inform the native desktop driver integration. The resulting Local Desktop Node, device broker, leases, API/schema, controls and phased implementation are ORBIT engineering recommendations, not upstream features supplied automatically.

## v0.3 public reference repositories reviewed

- https://github.com/vercel-labs/agent-browser
- https://github.com/vercel-labs/json-render
- https://github.com/vercel-labs/agent-skills
- https://github.com/vercel-labs/skills
- https://github.com/vercel-labs/portless
- https://github.com/OpenHands/OpenHands
- https://github.com/opensandbox-group/OpenSandbox

See `docs/02-research/REFERENCE_ECOSYSTEM_ANALYSIS.md` for findings and license caveats. Research is not integration or legal clearance.

## Additional platform practices

Temporal workflow documentation, OpenTelemetry documentation, Trivy license/SBOM documentation and the Agent Skills specification were consulted for v0.3. They are references only; no installation or integration has been performed.

- https://docs.temporal.io/tasks
- https://docs.temporal.io/encyclopedia/retry-policies
- https://opentelemetry.io/docs/
- https://www.trivy.dev/docs/latest/scanner/license/
- https://trivy.dev/docs/latest/supply-chain/sbom/
- https://agentskills.io/specification
