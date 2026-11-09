# Reference repository evidence ledger

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Reviewed:** 08 November 2026. **Method:** GitHub repository metadata + README, selected agent instructions/architecture/security files, and license paths. Blob SHAs below identify the fetched file content, not a repository commit. Recheck current branch, release tag and exact package artifacts before implementation.

| Repository | Inspected source | Blob SHA (prefix) | Findings |
|---|---|---|---|
| [agent-desktop](https://github.com/vercel-labs/agent-desktop) | `README.md` | `32dee9630df91348cb7202f5e4329b30b5237e3c` | Native desktop accessibility CLI/C library; macOS AX, Windows UIA, Linux AT-SPI; no embedded model; no web automation |
| agent-desktop | `AGENTS.md` | `21b6223d1f03c1e9d0987a6b2e2a01abcbe4bd8d` | Platform-neutral core, per-OS adapters, one dispatch path, typed MCP command discovery, test/build discipline |
| agent-desktop | `CONCEPTS.md` | `4b3b179551d1cbb5874040f56a9b50b3676146b5` | Snapshot identity, evidence tri-state, stale refs and platform-normalized accessibility vocabulary |
| agent-desktop | `docs/json-output.md` | `03fadda8cd527f4cae6a478a8a22c8928b5f45f8` | Explicit delivery/retry semantics, structured errors, partial snapshot behavior and versioned payload |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | `README.md` | `53f71fd42a568994479edfa5063c58ca0b5dad8d` | Rust CLI, browser daemon, session persistence, snapshots/refs, MCP, browser skills and cloud provider options |
| agent-browser | `LICENSE` | `8226d363f88a734e52cc79ead7a5588cc55e76f7` | Apache-2.0 root license |
| agent-browser | `docs/content/docs/security.mdx` | `654a67508fedc7c420230ae574f1fd212e63cb61` | Auth vault, content boundaries, domain allowlist, action confirmation and documented limitations; several controls are opt-in |
| [json-render](https://github.com/vercel-labs/json-render) | `README.md` | `9911468eba1a2eceac2dc949a5ca56b6c0934be8` | Schema/catalog-constrained UI generation, multiple renderers, actions and progressive stream |
| json-render | `packages/core/README.md` | `128f520b8e1da292ad1866a1fc699d13cb3f293a` | Candidate-based composition limits, validation and experimental API caveats; a valid tree may still omit required content |
| json-render | `LICENSE` | `8226d363f88a734e52cc79ead7a5588cc55e76f7` | Apache-2.0 root license |
| [agent-skills](https://github.com/vercel-labs/agent-skills) | `README.md` | `396ef38284797174c737942a9cc84fc09680b705` | Collection of agent skills for UI, React performance, writing and deployment |
| agent-skills | `skills/react-best-practices/SKILL.md` | `237988de4a66dd8a71d30a2c24ebe1a86b58d04e` | Inspected skill frontmatter says MIT; no repository-root LICENSE was found at the checked `LICENSE` and `LICENSE.md` paths |
| [skills CLI](https://github.com/vercel-labs/skills) | `README.md` | `f8d3ebcf4b513427efba96cb13097c94ce25eef0` | Skill discover/install/list/update/remove/use and harness compatibility; telemetry documented with opt-out |
| skills CLI | `LICENSE` | `eabe3008f6c0275929faa8b07d406e82717648cc` | MIT root license |
| skills CLI | `docs/creating-skills.md` | `44ef574a99ca39ca40f0888088a6d697ccb53140` | SKILL.md frontmatter and bounded discovery locations |
| skills CLI | `docs/agents.md` | `ba81551f4fb4b25e3a8a6da8bd897f15f477ca32` | Many coding-agent install paths and compatibility differences |
| [portless](https://github.com/vercel-labs/portless) | `README.md` | `c2b9478a9d2a797c4e262ab16560634bca12c6d7` | Local named `.localhost` proxy, dynamic ports, local TLS CA trust setup and worktree naming |
| portless | `LICENSE` | `8226d363f88a734e52cc79ead7a5588cc55e76f7` | Apache-2.0 root license |
| [OpenHands repository](https://github.com/OpenHands/OpenHands) | `README.md` | `d980bc45a7642a9b980aa9a7ca93cc715c31c8bb` | Current README identifies Agent Canvas, local/remote/cloud backends, ACP-compatible agents and automations; no-sandbox mode warns of broad host filesystem access |
| OpenHands repository | `LICENSE` | `f6f60f52368bcc96f82fbe59ec65049c2c3af9db` | MIT root license |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | `README.md` | `d32141a2917f759014d1fcc96271117c9e3992e1` | Docker/Kubernetes sandbox lifecycle, SDKs, agent workspaces, network policy and optional Firecracker runtime |
| OpenSandbox | `LICENSE` | `b09cd7856d58590578ee1a4f3ad45d1310a97f87` | Apache-2.0 root license |
| OpenSandbox | `docs/guides/credential-vault.md` | `eef4776f8841db66e53772c245111f36e56eb6f6` | External credential injection via egress broker; network enforcement and fail-closed behavior are prerequisites |

## Additional technology sources

| Technology | Source | Key research result |
|---|---|---|
| Temporal | https://docs.temporal.io/ | Durable workflow concepts and retry policies inform the workflow-engine evaluation; ORBIT must still prove side-effect idempotency |
| Pydantic AI | https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/ | Documents durable execution adapters and distinguishes durability from ordinary step persistence |
| LiteLLM | https://docs.litellm.ai/ | Gateway, provider normalization, virtual keys, budgets and fallback patterns |
| OpenTelemetry | https://github.com/open-telemetry/semantic-conventions-genai | Reviewed GenAI spans include inference, agent invocation, planning and tools; semantic conventions were marked development/experimental |
| Syft | https://github.com/anchore/syft | SBOM generation from source trees, filesystems, archives and images, with SPDX/CycloneDX output |
| OSV-Scanner | https://github.com/google/osv-scanner | Candidate dependency/SBOM vulnerability scan |
| Daytona | https://www.daytona.io/docs/ | Candidate managed sandbox service with Python/TypeScript lifecycle APIs |

## Limitations

- No source code was cloned, built, executed or security audited in this task.
- License observations apply to the inspected repository path/version at review time; subpackages, bundled assets, fonts, model weights, datasets, containers and transitive dependencies may have separate terms.
- This ledger is research provenance, not legal advice, compatibility proof or adoption approval.
