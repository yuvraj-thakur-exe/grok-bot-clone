# Requirements traceability matrix

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

This is an initial mapping. Extend it when new requirements or implementation tickets are created. A requirement is not verified merely because a design document mentions it.

| Requirement | Design reference | Implementation area (target) | Verification |
|---|---|---|---|
| FR-001 workspace | auth design, DB schema | API/workspaces | tenant isolation integration tests |
| FR-003 streaming chat | API design, task engine | web/API | SSE replay E2E |
| FR-004/005 providers/router | model routing | AI/provider adapters | adapter contract + provider smoke tests |
| FR-006/007 durable tasks | queue/worker design | workflow workers | crash/recovery integration tests |
| FR-008/009 tools/policy | tool registry, approval policy | Tool Gateway | schema, denial and audit tests |
| FR-010 citations | research design | search/extraction | claim-source coverage tests |
| FR-011 file Q&A | storage/files, memory/RAG | document worker | malicious upload and source locator tests |
| FR-014 browser | browser security | browser worker | context isolation + SSRF E2E |
| FR-015 Git/code | browser/sandbox security | code worker | host isolation and diff tests |
| FR-016 memory | memory/RAG | memory service | inspect/edit/delete/ACL tests |
| FR-017/018 skills/routines | skills/routines | skill registry/scheduler | schema validation, dedupe, approval tests |
| FR-019 delegation | multi-agent | coordinator | bounded delegation and cancellation tests |
| FR-020 MCP | tool registry, research | connector gateway | protocol compatibility and scope tests |
| NFR-001 tenant security | auth, threat model | API/data access | IDOR/RLS tests |
| NFR-004 recovery | workflow design | workflow runtime | recovery drill |
| NFR-014 quotas | model cost, tool policy | budget service | denial at threshold tests |

## Status vocabulary

`specified` = documented; `implemented` = code exists; `tested` = relevant test passed; `verified` = acceptance evidence reviewed in target environment; `live-configured` = valid external credentials/config exist; `blocked` = external dependency prevents progress. Keep separate status fields for these dimensions.

## v0.2 desktop traceability

| Requirement | Design reference | Implementation target | Verification |
|---|---|---|---|
| DSK-FR-001/009 pairing/revocation | Desktop architecture/API/security | Device broker + local node | pairing replay/revoke tests |
| DSK-FR-002/003 capabilities/session | Desktop API + platform matrix | node capability probe | OS permission/session integration tests |
| DSK-FR-004 leases | Desktop API + DB schema | broker/lease service | expiry/reconnect/concurrency tests |
| DSK-FR-005 observation | Desktop agent loop + contract | driver adapter | partial/complete/redaction contract tests |
| DSK-FR-006 allowlisted action | command allowlist + tool policy | local and central policy | deny-by-default and schema tests |
| DSK-FR-007 exact approval | approval policy + API contract | approval service | argument hash, expiry and target change tests |
| DSK-FR-008 disposition | JSON/action contract | adapter/task engine | no retry on unknown or unsafe delivery |
| DSK-FR-010 privacy | desktop security + activity UX | local node/storage | clipboard/screenshot denial and retention tests |

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.

## v0.3 requirements

| ID | Requirement | Design / implementation area | Verification |
|---|---|---|---|
| ORG-001 | Role agents have explicit charters and cannot make legal/financial/company commitments | Company operating model; agent role charters; policy engine | Role permission tests and human approval tests |
| ORG-002 | Human founder retains final authority for legal acceptance, spend and production release | Approval service; release workflow | Negative tests for unapproved external action |
| BRAND-001 | ORBIT UI uses original brand identity | Brand tokens/design system | Asset provenance and brand audit |
| BRAND-002 | Third-party legal notices are preserved | License compliance and release pipeline | NOTICE/SBOM checks |
| INT-001 | External agent backends use a versioned ORBIT contract | AgentBackend adapter | Backend contract and event replay tests |
| INT-002 | Sandbox egress defaults to deny | Sandbox provider | Network policy and direct-IP/IPv6 tests |
| INT-003 | Skills have immutable source and digest | Skill registry and lockfile | Checksum/tamper/install tests |
| INT-004 | Skill activation cannot grant undeclared tool authority | Tool gateway | Permission escalation tests |
| UI-001 | Generated UI is limited to catalog schemas | Generative UI engine | Unknown component/prop/binding rejection tests |
| UI-002 | Generated UI actions re-check server policy | Action gateway | Authorization/approval bypass tests |
| LIC-001 | Every release component has SPDX/license evidence and notice status | SBOM and license management | CI compliance gate |


## v0.5 reuse-first requirement mapping

| Requirement | Canonical evidence | Acceptance evidence required in app repo |
|---|---|---|
| Preserve and audit existing code before rewrite | `RUN_FIRST_IN_IDE_AGENT.md` | Repo audit and reproducible baseline |
| Pin and review upstream source | `config/upstreams/upstream-lock.yaml` | Commit and file hashes, license report, SBOM |
| Single task and policy authority | `docs/03-architecture/V05_TARGET_ARCHITECTURE.md` | Contract, auth, event, cancellation tests |
| Safe skill install and execution | `docs/06-security/V05_SUPPLY_CHAIN_AND_SKILL_SECURITY.md` | Quarantine, review, digest, sandbox tests |
| Separate personal/work contexts | `docs/05-ai-system/V05_PERSONAL_LIFE_WORK_AGENT_MODEL.md` | ACL and cross-context isolation tests |
| Competitive parity measured, not assumed | `docs/09-quality/V05_BENCHMARKS_AND_ACCEPTANCE.md` | Frozen task set and evidence report |
