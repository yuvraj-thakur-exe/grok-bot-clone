# Reference integration conformance matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

No reference integration is “done” until it passes the matching tests against a pinned version. This matrix defines the minimum evidence.

| Area | Core scenarios | Security tests | Reliability tests | Evidence required |
|---|---|---|---|---|
| Browser driver | Navigate, observe, semantic select, fill, wait, download quarantine, close | Domain allowlist, subresource egress, prompt injection, credential redaction, profile isolation, upload/eval approval | Browser crash, daemon loss, stale refs, timeout, cancellation, network block | Version, browser build, test matrix, traces redacted |
| Native desktop driver | Status, permissions, app/window listing, complete snapshot, semantic low-risk action | Local pairing, lease expiry, cross-workspace denial, no physical input by default, sensitive-content redaction | App exits, accessibility bus unavailable, stale/ambiguous refs, OS permission change, node disconnect | OS/version, live interactive session evidence, test app and exact driver release |
| Generative UI | Parse, validate, stream, render, state update, action event | Unknown component/action rejection, prop schema mismatch, HTML/script injection, action authorization, cross-tenant data | Partial stream, malformed patch, renderer error, cancellation | Catalog version, fixture set, accessibility results |
| Skill registry | Discover, resolve, install, lock, update, remove, invoke | Source pin, checksum, license, secret scan, script sandbox, manifest tool scope | Upstream branch drift, missing asset, rollback, stale lockfile | Skill digest, license evidence, approval, test results |
| External agent backend | Start, input, event stream, cancel, artifacts, finish | Task credential scope, path/workspace isolation, action approval, output redaction | Backend restart, protocol mismatch, event disconnect, cancellation race | Backend version, ACP/MCP protocol version, conformance report |
| Sandbox provider | Create, exec, read/write, artifact export, terminate | Escape tests, egress deny, no Docker socket, no host home, credential broker, tenant isolation | Quota exhaustion, worker kill, TTL, pause/resume, image drift, cleanup | Image digest, runtime config, kernel/host profile, egress test logs |
| Model gateway | Streaming, tools, structured output, vision/audio capabilities, usage cost | API key isolation, tenant quotas, prompt retention, provider data path | 429/5xx fallback, slow model, stream disconnect, idempotency of request logging | Provider/model/version, cost/latency, capability contract results |
| Local development routing | Named app route, parallel worktree, OAuth callback, stop proxy | Loopback-only, CA consent, no external ingress, cert removal | Port collision, proxy restart, stale mapping | Developer-only acceptance; excluded from production architecture |
| Supply-chain CI | Lockfile, SBOM, license inventory, vulnerability scan, attestations | Missing license, unknown binary, secret leak, tampered digest | Scanner unavailable, advisory feed outage, exception expiry | SBOM files, scan reports, signed artifact/provenance where supported |

## Test data requirements

Use synthetic repositories, fake credentials and disposable test accounts. Do not conduct GUI tests against a human's live personal session. The CI fake provider may be used for deterministic contract tests, but it does not replace a real isolated staging test.

## Go/no-go

A failed security test is a release blocker. A provider-specific unsupported action must be visible as unsupported, not emulated silently by a riskier action. Any accepted limitation receives an owner, user-facing statement, mitigation and review date.


## v0.5 evidence rule

Conformance rows must be marked not tested until an adapter has been built against the pinned upstream and exercised in the target ORBIT repository. README claims and source checkout success are not acceptance evidence. Include runtime version, commit, test command, result, latency/cost where relevant and known failure modes.

