# ORBIT threat model

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Assets

Provider/API credentials, OAuth tokens, browser cookies, user documents, repository source, workspace data, generated artifacts, task instructions, approval records, model context, and infrastructure credentials.

## Trust boundaries

Browser/user <-> API; API <-> workflow engine; workflow engine <-> workers; workers <-> external websites; model <-> tool gateway; workspace <-> workspace; host <-> sandbox; plugin/MCP server <-> ORBIT; uploaded/retrieved content <-> trusted system policy.

## Threats and mitigations

| Threat | Primary mitigation |
|---|---|
| Prompt injection in web/file content | treat content as untrusted; policy gateway; source labels; no tool authority in retrieved text |
| Cross-tenant access | workspace-scoped queries, RLS, service identities, adversarial isolation tests |
| Credential leakage | secret manager, isolated connector broker, redacted logs, scoped tokens |
| SSRF and malicious URL | egress proxy, private IP/metadata blocks, DNS revalidation, scheme allowlist |
| Malicious repository code | disposable sandbox, no host mounts/socket, resource quotas, restricted network |
| Browser session theft | per-workspace/per-task contexts, encrypted storage, short retention, access audit |
| Malicious plugin/MCP server | allowlist, declared permissions, review, isolated process, version pinning |
| Runaway agent | step/time/cost limits, concurrency caps, kill switch |
| Supply-chain compromise | lockfiles, provenance, dependency scanning, pinned images, signed releases |
| Data deletion gap | deletion workflow across object/vector/cache/derived data with verification |

## Abuse cases

Test a webpage instructing the agent to upload secrets; a repository README requesting shell access; a document with embedded tool instructions; a workspace-ID swap; an expired approval replay; a symlink/path traversal; a DNS rebinding SSRF; and a worker crash after an external write.

## Residual risks

No sandbox makes arbitrary untrusted code perfectly safe. High-risk multi-tenant execution requires a hardened isolation boundary, network policy and operational monitoring. Document residual risk and restrict feature availability until tested.

## v0.2 desktop threat boundary

Add Local Desktop Node, device private key, WSS channel, active OS session, accessibility APIs, screenshots, clipboard and visible native app content to the asset inventory. Threats include malicious UI prompt injection, node-key theft, replayed pairing, session takeover, local command injection, stale-ref targeting, ambiguous identity, duplicate mutation after timeout, screen-content exfiltration and multi-agent UI races. Controls are detailed in `DESKTOP_CONTROL_SECURITY.md`.

## ORBIT v0.2 alignment

The v0.2 security model treats the Local Desktop Node and active OS session as a separate trust boundary. Require dual policy checks, exact approvals, data minimization, leases and local stop; see `DESKTOP_CONTROL_SECURITY.md`.


## v0.5 additional attack surfaces

Threat-model upstream dependency compromise, malicious skill packages, plugin code running inside the gateway, tool-description prompt injection, cross-agent memory leakage, unsafe self-evolution, connector webhook spoofing, upstream update drift, compromised build artifacts and supply-chain provenance tampering. Include abuse cases for one agent attempting to grant another agent more permissions or to route a personal context into a work context.

