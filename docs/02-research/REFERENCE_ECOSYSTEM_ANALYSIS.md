# ORBIT reference ecosystem analysis

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Research date:** 08 November 2026. **Scope:** public repository metadata, repository-root README/agent instructions, selected architecture/security/specification files and visible license files. This is not a complete code audit, security audit or compatibility test.

## Executive synthesis

The seven repositories add complementary building blocks, not one unified product. ORBIT should preserve its own control plane and contracts, integrating selected tools behind adapters. The strongest opportunities are: robust browser operation; safe constrained UI generation; portable skills; external agent backends; disposable execution sandboxes; and stable local developer routing.

## Findings and ORBIT recommendation

| Reference | What source demonstrates | ORBIT use | Recommendation | License observation |
|---|---|---|---|---|
| [agent-browser](https://github.com/vercel-labs/agent-browser) | Native CLI; background browser daemon; snapshots and refs; semantic actions; persistent sessions; MCP; browser skills; providers; auth vault; domain allowlist and confirmation controls | Browser driver option for web execution, separate from native desktop and shell | Evaluate as adapter alongside Playwright; pin versions; test profile/session, downloads, egress and auth-vault behavior | Root `LICENSE` was fetched and declares Apache-2.0; preserve license/NOTICE and verify exact release |
| [json-render](https://github.com/vercel-labs/json-render) | Schema/catalog-constrained AI-generated UI; renderer packages for several frameworks; progressive SpecStream; named actions; explicit catalogs | Constrained generative UI for reports, task cards, configuration forms and agent-generated dashboards | Adopt architecture/pattern or evaluate package; never render arbitrary code or bind model-chosen arbitrary actions | Root LICENSE is Apache-2.0; retain notices if included |
| [agent-skills](https://github.com/vercel-labs/agent-skills) | Example skill collection including React performance, design, writing, deployment and workflow rules | Study skill content structure and use as research input | Do not wholesale copy collection; repository root license was not found at checked `LICENSE` path. Inspect each skill's license/headers individually | Mixed/unclear at repository level; block copying until cleared |
| [skills CLI](https://github.com/vercel-labs/skills) | CLI discovers, installs, lists, updates, removes and uses Agent Skills across many agent harnesses; documented skill layout and agent paths | Interoperable skill installation/discovery | Adopt Agent Skills-compatible format; evaluate CLI only after telemetry/privacy, supply-chain and version pinning review | Root LICENSE is MIT; preserve notice and telemetry disclosure if distributing/running it |
| [portless](https://github.com/vercel-labs/portless) | Local reverse proxy maps named `.localhost` hosts to changing local dev ports; stable URLs and TLS developer setup | Local development ergonomics for parallel services/worktrees and OAuth callback testing | Optional developer-only tool; never production ingress or a security boundary | Root LICENSE is Apache-2.0; preserve notices |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Current repository README describes Agent Canvas: self-hosted developer control center with local/remote/cloud agent backends, ACP-compatible agents and automations | Agent backend abstraction and self-hosted developer orchestration patterns | Implement ORBIT's own `AgentBackend` contract; optionally connect ACP-compatible backends. Do not clone the UI/brand or make OpenHands required | Root LICENSE is MIT; preserve notices |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox lifecycle/API and SDKs; Docker local and Kubernetes deployment; browser/desktop/code examples; egress policy; credential vault; optional Firecracker fast-sandbox | Isolated code/browser/agent workspaces, secure egress and credential broker patterns | Keep container sandbox for early MVP; introduce OpenSandbox adapter after a real isolation/ops evaluation. Firecracker later and only on supported infrastructure | Root LICENSE is Apache-2.0; preserve notices |

## Specific engineering patterns to adopt

### 1. Browser automation

- Use fresh accessibility/DOM snapshots and short-lived references; do not persist DOM element refs as stable IDs.
- Browser actions should verify target visibility, enabled state and postcondition.
- Browser sessions require explicit isolation and cleanup; saved authentication state is secret material.
- Domain allowlists and action confirmation gates should be enforced by a network/policy boundary, not merely prompt instructions.
- A browser-level allowlist is not an operating-system firewall. Use worker/network egress controls for a strong boundary.
- Treat browser page content as untrusted and label it in model context. Limit output size to reduce prompt flooding.

### 2. Constrained generative UI

- Define an ORBIT-owned catalog of components, props schemas, state bindings and named actions.
- Model can propose a declarative UI spec only within that catalog.
- Validate every stream event and the completed tree; reject unknown component/action identifiers, excessive depth/count, unsafe URLs and invalid binding paths.
- UI actions map to registered backend operations and re-run normal authorization/approval checks. Rendering a button never grants permission to execute it.
- Do not let JSON output embed JavaScript, arbitrary HTML, eval, dynamic imports or untrusted component code.
- Version the catalog and include it in audit events; support safe fallback to static cards/tables.

### 3. Agent skills ecosystem

- Use a portable `SKILL.md` format with required name/description metadata and optional scripts/references.
- Maintain an ORBIT skill registry with source, version, digest, declared tools, required secrets, risk level, license, author, review date and test status.
- Install skills from pinned commit/tag and verify checksums; no automatic installation from untrusted URLs.
- Separate skill instructions from executable scripts. Scripts run in a sandbox and receive only declared capabilities.
- Skill content is untrusted input until reviewed. It cannot elevate agent permissions.

### 4. Agent backend portability

- Create an internal backend interface for OpenHands-style local/remote/VM/container/cloud agents and ACP-compatible processes.
- Do not proxy raw backend execution traffic through an unrelated API if the backend contract requires a direct runtime URL; maintain a typed, authenticated client and explicit backend ownership.
- Backend switching must not leak conversation context, workspace files, secrets or authorization scopes.
- Expose backend capabilities and limitations; never claim every backend supports the same tools.

### 5. Sandbox runtime

- Create, inspect, execute, write/read files, stream logs, pause/resume and destroy workspaces through a single ORBIT runtime abstraction.
- Default outbound network policy to deny; allow explicit hosts/ports and enforce below the browser process.
- Keep real credentials in an external broker/vault. Sandboxed processes receive non-secret placeholders or only scoped ephemeral credentials; credentials are injected at a controlled egress boundary where supported.
- Test behavior on worker crash, sandbox pause/resume, egress component restart and credential rotation.
- Firecracker microVMs are an advanced isolation option, not an MVP dependency. Verify KVM, kernel, cgroup, storage, network and operational prerequisites before adoption.

### 6. Local development routing

- Stable named localhost URLs can improve multi-worktree agent development and OAuth callback stability.
- A locally installed CA and TLS trust action is a privileged trust decision; document and make opt-in.
- Do not route production traffic through a local development proxy.

## What not to do

- Do not merge all reference repositories into a monolith or install their whole dependency trees without a specific need.
- Do not copy third-party code, skill instructions, logos, docs screenshots or assets unless license and trademark conditions allow it.
- Do not treat benchmark figures reported upstream as ORBIT performance claims.
- Do not let ACP, MCP or a skill manifest bypass ORBIT's tool gateway and authorization.
- Do not give an agent's sandbox broad host filesystem, Docker socket, browser profile or credential-store access.

## Revalidation requirement

For each implementation, record the exact upstream URL, commit SHA/release, package version, root/per-file license, dependency tree, platform support, known limitations and local integration test results. Repeat on dependency upgrades and before public releases.

## Additional platform practices researched

- **Durable orchestration:** Temporal documents workflow tasks, workflow history, signals/updates and activity retry policies. ORBIT should place non-deterministic external operations (LLM calls, API calls, browser/desktop actions) in activities/workers, use explicit idempotency and avoid retrying side effects whose delivery is unknown. See https://docs.temporal.io/tasks and https://docs.temporal.io/encyclopedia/retry-policies.
- **Observability:** OpenTelemetry is a vendor-neutral framework for traces, metrics and logs. ORBIT should instrument task, worker, provider and approval spans with stable correlation IDs while redacting secrets and user content. See https://opentelemetry.io/docs/.
- **SBOM and license scanning:** Trivy documents license scanning, including classification of unknown licenses as unknown, and scanning SBOMs in SPDX/CycloneDX formats. Treat scanner output as an automated signal that still needs manual review for ambiguous files and custom terms. See https://www.trivy.dev/docs/latest/scanner/license/ and https://trivy.dev/docs/latest/supply-chain/sbom/.
- **Agent Skills format:** the public specification describes a portable directory with a required `SKILL.md` and optional scripts, references and assets. ORBIT should be interoperable while adding its own immutable lock, provenance, permission and license metadata. See https://agentskills.io/specification.

These are tooling candidates and practices, not a decision to install or depend on those tools immediately.

## License and provenance clarification

The repository-level license observations are preliminary. For `vercel-labs/agent-browser`, the root `LICENSE` was fetched and is Apache-2.0. For `vercel-labs/agent-skills`, the root `LICENSE` and `LICENSE.md` paths checked during review returned not found, although the inspected `react-best-practices` skill frontmatter declares MIT. That does not establish a repository-wide license. `THIRD_PARTY_COMPONENT_REGISTER.yaml` is the current detailed inventory and deliberately marks all candidates `research_only`.
