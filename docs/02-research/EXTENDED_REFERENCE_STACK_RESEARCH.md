# Extended reference stack research

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Research date:** 08 November 2026. **Status:** Public-source desk research; not an integration or security certification.

This supplement evaluates infrastructure ORBIT needs beyond the seven repositories supplied by the founder. Vendor/project names below are research identifiers, not ORBIT product brands. Re-check exact commits, package licenses, release signatures, transitive dependencies and supported versions before adoption.

## Executive decision

ORBIT should own its product contracts and use replaceable providers for the execution substrate. The strongest additions to the reference list are:

- **Durable workflow engine:** evaluate Temporal first for long-running tasks and resumable orchestration. Keep the workflow interface portable and compare operational complexity against a simpler Postgres-backed MVP.
- **Model gateway:** evaluate LiteLLM as an optional provider gateway for normalized model access, key budgets, spend attribution and routing. ORBIT must still own capability policy, task-level quality requirements and approval semantics. Avoid duplicate retry loops.
- **Agent framework:** evaluate Pydantic AI as an implementation option for typed tools, structured output and durable execution adapters. Do not make one framework's abstractions the public ORBIT contract.
- **Observability:** adopt OpenTelemetry-compatible traces, metrics and logs. Use GenAI semantic conventions selectively; the GenAI conventions retrieved during research are marked Development/Experimental, so pin versions and isolate schema mappings.
- **Supply chain:** evaluate Syft for SPDX/CycloneDX SBOM generation and OSV-Scanner for vulnerability analysis. These are candidate tools, not a substitute for license review or threat modelling.
- **Sandbox provider:** compare OpenSandbox, Daytona and local Docker. The initial provider must satisfy egress denial, secret isolation, filesystem constraints, quotas, cancellation, artifact export and reproducible lifecycle tests.

## 1. Durable execution

### Temporal

Official documentation: https://docs.temporal.io/ and https://temporal.io/

**Observed capability:** durable workflows can persist workflow state and resume execution after process or infrastructure interruptions. ORBIT's use case is a multi-hour task that waits for approval, a schedule, a GitHub event or a browser operation and must survive worker restarts.

**ORBIT recommendation:** define a `WorkflowEngine` interface and make a proof of concept with Temporal before selecting it for production. Model activities as short, idempotent, bounded units; keep side effects behind the policy gateway; persist task/audit truth in ORBIT's database; do not let workflow replay duplicate external mutations. Workflow code must be deterministic where the engine requires it. Use explicit activity idempotency keys and human approval signals.

**Adoption gate:** kill workers during every lifecycle stage; prove restart, replay, cancellation, timeout, signal delivery, approval expiry, compensation and safe external-action deduplication. Measure ops burden and local development experience.

### Alternative durable engines

Pydantic AI's durable execution documentation currently describes multiple supported execution backends, including Temporal, DBOS, Prefect, Restate and other integrations. Source: https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/.

Do not add multiple workflow engines to ORBIT. Run the same recovery conformance suite against shortlisted options and choose one. A Postgres task journal is enough for the first thin vertical slice only if the team proves it handles restart/retry semantics and approval waits.

## 2. Model gateway and routing

### LiteLLM

Official docs: https://docs.litellm.ai/ and https://docs.litellm.ai/docs/proxy/budget_fallbacks

**Observed capability:** a unified provider interface/gateway, provider routing, streaming, fallbacks, virtual keys, budget/rate limits and spend tracking. The docs also describe routing and budget-triggered fallback behavior.

**ORBIT recommendation:** place a model gateway behind `ModelProvider`/`ModelGateway`. Store provider credentials only in a trusted gateway or secret manager. Send per-task identifiers, workspace, agent role, budget class and non-sensitive tags. Keep ORBIT's model capability registry authoritative: a provider gateway cannot decide whether a task requires vision, long context, tool calling, JSON mode or a given safety tier. Define one retry owner; avoid nested provider + SDK + gateway retries.

**Risks:** gateway becomes a high-value credential boundary and may normalize away provider-specific features. Keep capability negotiation explicit, redact prompts from telemetry by default, pin the gateway version and run provider contract tests for streaming, tool calls, structured outputs and cancellation.

## 3. Agent framework evaluation

### Pydantic AI

Official docs: https://ai.pydantic.dev/ and https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/

**Observed capability:** typed agent/tool APIs and structured results, with documented durable-execution integrations. It can be evaluated for internal agent loop implementation.

**ORBIT recommendation:** build framework adapters behind an ORBIT-owned `AgentRuntime` contract. Do not expose Pydantic-specific message, tool or graph types through public APIs or persisted event schemas. Use typed schemas at all external boundaries. Keep prompt construction, authorization, durable state, evidence provenance and audit in ORBIT-owned components.

## 4. Observability

### OpenTelemetry

GenAI semantic convention sources reviewed:
- https://opentelemetry.io/docs/specs/semconv/gen-ai/
- https://github.com/open-telemetry/semantic-conventions-genai

The reviewed GenAI agent/client semantic convention documents cover model inference, agent invocation, planning and tool execution spans. The source pages were marked Development/Experimental during this research.

**ORBIT recommendation:** instrument every task with a trace and correlate `tenant_id` (opaque/pseudonymous), `workspace_id`, `task_id`, `run_id`, `agent_id`, `tool_call_id`, provider/model, policy decision ID and approval ID. Never emit API keys, access tokens, raw prompts, full tool output, desktop screenshots, clipboard payloads or document content into ordinary telemetry. Create explicit opt-in, short-retention, redacted debug traces for sensitive task data. Keep metric labels low-cardinality; no user IDs, raw URLs or arbitrary error strings as labels.

## 5. SBOM and vulnerability tools

### Syft

Sources: https://github.com/anchore/syft and https://oss.anchore.com/docs/guides/sbom/

**Observed capability:** generate SBOMs from source directories, filesystems, archives and container images; output formats include SPDX and CycloneDX.

**ORBIT recommendation:** create a release SBOM for source/binary/container artifacts and store it beside release provenance. Scan each independently built runtime image; do not assume the source SBOM fully captures a base image or downloaded desktop binary.

### OSV-Scanner

Official source: https://github.com/google/osv-scanner

**ORBIT recommendation:** evaluate it for dependency and SBOM vulnerability scanning. Combine with a separate license scanner and secret scanner. Vulnerability acceptance requires package path, fixed version or mitigation, severity/context, owner and expiry.

### Important distinction

An SBOM is an inventory, not proof that a component's license permits ORBIT's distribution model. License detection is evidence to review; a human-approved legal register remains the policy source of truth.

## 6. Alternative sandbox infrastructure

### Daytona

Official docs: https://www.daytona.io/docs/

The documentation describes API/SDK-managed isolated environments for agent-generated code. Treat Daytona as an optional managed sandbox provider candidate and evaluate data residency, region, egress, persistence, pricing, deletion guarantees, credential handling, auditability and provider lock-in.

### OpenSandbox

Repository: https://github.com/opensandbox-group/OpenSandbox

ORBIT's supplied reference review already covers the self-hosted Docker/Kubernetes lifecycle, egress controls, credential vault pattern and optional Firecracker path. Compare with Daytona using one common sandbox contract and a conformance benchmark.

### Local Docker

Keep local Docker as a developer MVP provider only when its threat boundary is acceptable. A Docker container is not automatically a hostile-code isolation boundary. Never mount the Docker socket into an untrusted agent, mount the host home directory, share credentials, or enable unrestricted network egress.

## Comparative decision table

| Need | Candidate | ORBIT default | Decision gate |
|---|---|---|---|
| Durable tasks | Temporal; DBOS/Prefect/Restate comparison | Workflow interface + Postgres state for initial slice; Temporal PoC | Crash/replay/idempotency and ops test |
| Model gateway | LiteLLM | ORBIT provider interface; gateway optional | Capability parity, key isolation, budgets and retry behavior |
| Agent framework | Pydantic AI and other typed frameworks | ORBIT-owned `AgentRuntime` contract | Framework adapter tests and schema stability |
| Observability | OpenTelemetry | OTel-compatible instrumentation | Redaction, sampling and retention review |
| SBOM | Syft | SPDX + CycloneDX release artifacts | Source, binary and container coverage |
| Vulnerability scan | OSV-Scanner + other scanners | CI scan + triage register | False-positive workflow and patch SLAs |
| Sandbox | OpenSandbox, Daytona, Docker | Provider interface; local Docker for dev only | Escape, egress, quota, deletion and recovery suite |

## Evidence boundary

This review read public documentation and repository files. It did not execute code, audit every package, review cloud terms, probe hosted services, confirm a complete dependency tree, validate security claims or certify compatibility. No benchmark numbers from reference vendors are ORBIT performance claims.
