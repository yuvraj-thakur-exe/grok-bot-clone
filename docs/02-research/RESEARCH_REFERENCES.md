# Research references — v0.3

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

The following public materials were inspected for this revision. Exact upstream source and license versions must be rechecked when selecting an implementation release.

- https://github.com/vercel-labs/agent-browser — README, security documentation, Apache-2.0 license indication.
- https://github.com/vercel-labs/json-render — README, core package README, Apache-2.0 root license.
- https://github.com/vercel-labs/agent-skills — README, package manifest and selected skill frontmatter; no root LICENSE found at checked path.
- https://github.com/vercel-labs/skills — README, skill creation docs, supported agent paths, MIT root license; telemetry disclosure.
- https://github.com/vercel-labs/portless — README and Apache-2.0 root license.
- https://github.com/OpenHands/OpenHands — current README describes Agent Canvas and backend choices; MIT root license.
- https://github.com/opensandbox-group/OpenSandbox — README, credential vault guide, egress and sandbox runtime concepts; Apache-2.0 root license.
- https://github.com/vercel-labs/agent-desktop — v0.2 desktop driver baseline, concepts, AGENTS.md, JSON output contract and platform skills.

## Research confidence

High confidence for statements copied from fetched README/license/guide files. Medium confidence for architectural inference from selected code/search excerpts. Low confidence for uninspected internal modules, runtime behavior not executed, performance claims not reproduced, and compatibility with ORBIT. No ORBIT integration has been built or benchmarked as part of this documentation pack.

- https://docs.temporal.io/tasks and https://docs.temporal.io/encyclopedia/retry-policies — durable workflow and activity retry semantics.
- https://opentelemetry.io/docs/ — vendor-neutral traces, metrics and logs.
- https://www.trivy.dev/docs/latest/scanner/license/ and https://trivy.dev/docs/latest/supply-chain/sbom/ — license and SBOM scanning capabilities.
- https://agentskills.io/specification — Agent Skills portable skill directory and frontmatter format.

## v0.3 extended infrastructure research (08 November 2026)

- Temporal workflow docs: https://docs.temporal.io/ and https://docs.temporal.io/tasks
- Pydantic AI durable execution: https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/
- LiteLLM gateway: https://docs.litellm.ai/ and https://docs.litellm.ai/docs/proxy/budget_fallbacks
- OpenTelemetry GenAI conventions: https://opentelemetry.io/docs/specs/semconv/gen-ai/ and https://github.com/open-telemetry/semantic-conventions-genai
- Syft SBOM: https://github.com/anchore/syft and https://oss.anchore.com/docs/guides/sbom/
- OSV-Scanner: https://github.com/google/osv-scanner
- Daytona sandbox docs: https://www.daytona.io/docs/
- Agent Skills specification: https://agentskills.io/specification
