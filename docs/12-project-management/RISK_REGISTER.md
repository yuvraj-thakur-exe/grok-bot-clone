# Risk register

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Risk | Likelihood / impact | Mitigation | Trigger |
|---|---|---|---|---|
| R-01 | Untrusted input prompt injection triggers tools | High / Critical | policy gateway, trust labels, red-team tests | external content asks to exfiltrate or mutate |
| R-02 | Cross-workspace data leak | Medium / Critical | RLS, scoped identities, IDOR tests | tenant-boundary test fails |
| R-03 | Untrusted code escapes sandbox | Medium / Critical | microVM/hardened isolation, no host mounts, restricted egress | isolation test or CVE |
| R-04 | Provider outage/rate limits | High / Medium | adapters, compatible fallback, budgets | provider health threshold |
| R-05 | Long tasks lose state | Medium / High | durable workflow, checkpoints, idempotency | worker crash duplicates or loses work |
| R-06 | Costs exceed available budget | High / High | per-task caps, quotas, usage metering | spend threshold exceeded |
| R-07 | Over-expansion delays MVP | High / High | phased roadmap and P0 gates | too many parallel feature epics |
| R-08 | Legal/ToS issue during competitor research | Low / High | public docs, permitted UI access, no control bypass | auth/anti-bot restrictions |
| R-09 | Unmaintained dependencies / supply chain | Medium / High | lockfiles, scans, SBOM, pinned images | critical advisory |
| R-10 | False completion claims | Medium / High | evidence-based Definition of Done | feature lacks live test evidence |

Review each sprint. Assign an owner and residual-risk rating when real implementation begins.

## v0.2 desktop risks

| ID | Risk | Likelihood / Impact | Mitigation | Trigger |
|---|---|---|---|---|
| R-11 | Local node becomes remote-control attack surface | Medium / Critical | Pairing, local policy, outbound WSS, leases, pause/stop, no privileged service | unauthorized action or node credential leak |
| R-12 | Accessibility tree exposes private user content | High / High | Bounded observation, redaction, off-by-default persistence, no raw telemetry | unexpected content in logs/artifacts |
| R-13 | Stale/ambiguous desktop refs cause wrong action | Medium / Critical | Snapshot-scoped refs, identity proof, fail closed, fresh observation | UI mutation or duplicate controls |
| R-14 | OS/platform behavior differs from documentation | High / Medium | Capability discovery, release pinning, per-platform interactive tests | unsupported capability claim |
| R-15 | Action delivery unknown leads to duplicate side effect | Medium / Critical | Disposition semantics, no automatic retry, manual state check | disconnect/timeout during mutation |
| R-16 | Third-party driver supply-chain compromise | Low / Critical | Signed/checksummed pinned artifacts, SBOM, staged update and rollback | checksum mismatch/advisory |
| R-17 | UI content prompt-injects agent | Medium / High | Treat UI as untrusted, tool isolation, deterministic policy, red-team tests | malicious UI instruction observed |

## ORBIT v0.2 alignment

The v0.2 roadmap adds a gated desktop workstream after core auth, durable tasks and policy gateway. See `DESKTOP_INTEGRATION_PLAN.md`; desktop is not the first MVP path.

## v0.3 ecosystem / company risks

| ID | Risk | Likelihood / Impact | Mitigation | Trigger |
|---|---|---|---|---|
| R-18 | Mixing browser, desktop and shell runtimes causes privilege bleed | Medium / Critical | separate driver contracts, identities and execution domains | worker accesses wrong session/filesystem |
| R-19 | ACP/external agent backend leaks workspace or credentials | Medium / Critical | per-task identity, explicit artifact transfer, short-lived credentials and contract tests | backend sees unrelated tenant data |
| R-20 | Skill installation executes untrusted scripts | High / Critical | immutable source, license review, sandbox, tool/egress manifests and human activation | unexpected script or network action |
| R-21 | Generative UI action binding bypasses authorization | Medium / Critical | named action catalog and server-side policy/approval recheck | model-generated UI triggers privileged operation |
| R-22 | Dependency/skill license unclear or incompatible | Medium / High | license inventory, per-file review, SBOM and release gate | missing/unknown license or notice |
| R-23 | Removing third-party attribution during rebrand breaches license | Low / High | automated notices audit and human release review | missing required NOTICE/copyright |
| R-24 | ORBIT name conflicts with an existing trademark | Medium / High | clearance search and qualified legal review before commercial use | cease-and-desist or confusing similarity finding |
| R-25 | AI role agents are treated as actual officers/decision makers | Medium / High | clear human ownership and mandatory approval gates | agent sends/accepts a binding commitment |
| R-26 | Too many reference integrations inflate attack surface and MVP scope | High / High | scorecard, phased adoption, measure before integrating | dependency count grows without verified outcomes |
| R-27 | Developer localhost CA trust creates unintended machine-wide trust | Low / High | opt-in, local dev only, explain and document reversal | CA added without explicit user decision |
