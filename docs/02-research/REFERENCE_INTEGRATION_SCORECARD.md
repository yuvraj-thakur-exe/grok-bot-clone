# Reference integration scorecard

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This scorecard is an engineering proposal, not a compatibility test result. Candidates must pass the shared adapter contracts and conformance matrix before adoption.

| Capability | ORBIT boundary | Candidate(s) | Priority | Adopt condition |
|---|---|---|---|---|
| Browser interaction | `BrowserDriver` | Playwright baseline; agent-browser evaluated adapter | P1 | Shared task tests, isolated profiles, egress, auth and cancellation |
| Native desktop | `DesktopDriver` | agent-desktop | P2 | Local device pairing, interactive OS test and safe observe/action semantics |
| Code sandbox | `SandboxProvider` | Docker dev baseline; OpenSandbox; Daytona | P1 | Escapes, egress, filesystem scope, quotas, secrets, cleanup and resume tests |
| Durable workflow | `WorkflowEngine` | Temporal; compare DBOS/Prefect/Restate | P1 | Replay, signal, cancellation, timer, idempotency and operational PoC |
| Model gateway | `ModelGateway` | LiteLLM or ORBIT-native provider adapter | P1 | Capability parity, virtual keys, budgets, retry ownership and redaction |
| Agent framework | `AgentRuntime` | Pydantic AI or internal agent loop | P1 | Framework types hidden behind ORBIT contract; deterministic tests |
| Generative UI | `UISpecRenderer` | ORBIT-owned schema/catalog; json-render evaluated | P2 | Strict schema, safe actions, no arbitrary code and accessibility tests |
| Skill discovery | `SkillRegistry` | Agent Skills format; skills CLI evaluated | P1 | Immutable revision, lockfile, license, permissions, script sandbox and revocation |
| External coding agent | `AgentBackend` | ACP-compatible agent backends; OpenHands patterns | P2 | Workspace/credential isolation, event stream, cancellation and artifact audit |
| Observability | `ObservabilityExporter` | OpenTelemetry conventions | P1 | Secret/content redaction, cardinality controls, retention and trace correlation |
| SBOM | `SBOMGenerator` | Syft; SPDX/CycloneDX | P1 | Source, package, binary and container coverage |
| Vulnerability scan | `VulnerabilityScanner` | OSV-Scanner plus image scanner | P1 | Triage ownership, fix SLA, exception expiry and false-positive workflow |
| Local dev hostnames | developer tooling only | portless or equivalent | P3 | Localhost-only, opt-in CA trust, reversible setup; never production ingress |

## Build-vs-adopt rules

1. ORBIT owns public APIs, task state, identity, policy, approvals, budgets, audit, event schemas and product UX.
2. All runtimes are replaceable adapters; no public ORBIT contract leaks a framework/provider type.
3. Review exact version, immutable digest, root/nested license, NOTICE, maintenance, provenance, vulnerabilities, telemetry and data handling.
4. Pin versions; do not use moving `main` or `latest` in a release.
5. One retry owner per side effect. Never automatically retry a non-idempotent action when delivery is unknown.
6. Prefer small interfaces with conformance tests over importing an entire upstream product.
7. Do not adopt overlapping workflow engines, multiple provider gateways or multiple sandbox systems without evidence.
