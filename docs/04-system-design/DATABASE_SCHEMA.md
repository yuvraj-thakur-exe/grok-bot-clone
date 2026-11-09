# Database schema and data ownership

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Proposed baseline · **Owner:** Backend architecture · **Version:** 0.5

## Principles

PostgreSQL is the system of record. Redis is disposable acceleration, never the authority for tasks, permissions, approvals, or billing. Object storage holds bytes; PostgreSQL holds metadata, ownership, hashes, and lifecycle state. Every tenant-owned row carries `workspace_id` and is protected by application authorization plus database row-level security where practical. All IDs are opaque UUIDs. Store timestamps as UTC `timestamptz`.

## Core entities

| Entity | Important fields | Invariants |
|---|---|---|
| `users` | id, email, display_name, status, created_at | unique normalized email; no secrets |
| `workspaces` | id, owner_user_id, name, plan, created_at | owner must be active |
| `workspace_members` | workspace_id, user_id, role | unique pair; role checked on every action |
| `agents` | id, workspace_id, name, role, instructions, model_policy, status | versioned configuration; tool grants are explicit |
| `conversations` | id, workspace_id, agent_id, title, status | workspace ownership immutable |
| `messages` | id, conversation_id, seq, role, content_json, created_at | unique conversation/seq; content parts typed |
| `tasks` | id, workspace_id, conversation_id, status, objective, idempotency_key | state transition validated; unique idempotency scope |
| `task_runs` | id, task_id, attempt, worker_id, started_at, ended_at, outcome | one active attempt per task unless parallelism declared |
| `execution_steps` | id, task_run_id, seq, kind, status, input_ref, output_ref | append-only event history; redact secrets |
| `tool_invocations` | id, execution_step_id, tool_name, args_hash, policy_decision, result_ref | every invocation authorized and auditable |
| `approvals` | id, workspace_id, task_id, action_hash, status, expires_at, decided_by | approval binds to exact action payload and policy version |
| `memories` | id, workspace_id, owner_type, owner_id, kind, text, source_ref, confidence, expires_at | provenance and ACL required; user can inspect/delete |
| `skills` | id, workspace_id, slug, version, manifest_json, status | immutable published versions; reviewed before routine use |
| `routines` | id, workspace_id, skill_version_id, trigger_json, enabled, next_run_at | explicit timezone and owner; disabled on repeated failure |
| `connectors` | id, workspace_id, kind, encrypted_credential_ref, scopes, status | credential material outside database and prompt context |
| `artifacts` | id, workspace_id, task_id, storage_key, media_type, sha256, size | object access via signed short-lived URLs |
| `provider_configs` | id, workspace_id, provider, model, secret_ref, capability_json | secret ref only; capability claims verified |
| `usage_events` | id, workspace_id, task_id, provider, model, input_tokens, output_tokens, cost_estimate | immutable metering events |
| `audit_events` | id, workspace_id, actor, action, target, outcome, created_at | append-only; sensitive values redacted |

## Data rules

- Use migrations for every schema change. Never use startup-time automatic schema mutation in production.
- Add indexes for `(workspace_id, created_at)`, task status/created time, conversation message sequence, due routines, and vector retrieval filters.
- pgvector embeddings are derived data. Record embedding model/version and re-embed safely when changed.
- Use soft deletion only where restore/legal retention requires it; otherwise hard-delete content after the retention workflow completes.
- Cascades must not bypass artifact retention or audit requirements. Prefer explicit deletion workflows.
- Add foreign keys and check constraints for state enums and non-negative counters.
- Enable RLS in production for workspace tables; test with two tenants and a deliberately malicious workspace ID.

## Migrations and retention

Each migration must be backwards-compatible during rolling deployment where possible: expand, backfill, switch reads/writes, then contract in a later release. Backups must include database and object-store metadata. A deletion request must cover primary rows, objects, derived embeddings, caches, and queued work; immutable audit evidence retains only the minimum legally/operationally required metadata.

## Open decisions

Exact billing schema, enterprise SSO, regional data residency, encryption key hierarchy, and retention periods require product/legal decisions before production. Do not guess them in code.

## v0.2 native desktop entities

Add the entities in `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`:

- `desktop_devices`: paired device ownership, platform metadata, public-key fingerprint, lifecycle and revocation timestamps.
- `desktop_sessions`: interactive session generation, state and bounded capability-report reference.
- `desktop_capability_reports`: driver/contract version, OS version, capabilities and permission state; store metadata, not screen contents.
- `desktop_leases`: task/device/session binding, policy version, capability scope and short expiry. Enforce at most one mutating lease per physical session.
- `desktop_action_records`: operation, target-context hash, normalized argument hash, approval reference, delivery/retry/verification disposition. Do not persist ephemeral accessibility refs as durable target IDs.
- `desktop_observation_artifacts`: optional redacted artifact pointer, completeness, hash and expiry. Default to no persisted raw tree/screenshot.

Every new row is workspace-scoped and must enforce device ownership, task ownership and membership. Add indexes on `(workspace_id, status)`, `(device_id, expires_at)`, `task_id`, `(session_id, created_at)` and revocation status as appropriate. Use DB constraints to prevent invalid lease lifetime and enum states. Add migration tests for existing tenant isolation and hard-delete/retention behavior.

## Desktop privacy and data lifecycle

Raw snapshots, screenshots and clipboard content are not normal application data. Keep them out of durable storage unless a specific feature requires them, the user is informed, access is permission-checked and retention is short. Audit rows should store hashes, action context and minimal redacted metadata. A deletion workflow must also remove retained observation artifacts and derived indexes.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.

## v0.3 entities: company roles, integrations and compliance

| Entity | Important fields | Invariants |
|---|---|---|
| `agent_role_definitions` | id, workspace_id nullable, role_key, role_version, charter, owner_user_id, status | Describes an AI workflow role; never represents a legal employee by default |
| `agent_role_assignments` | id, workspace_id, role_id, agent_id, assigned_by, allowed_tool_profile, budget_profile | Scope and permission grants are explicit; immutable history |
| `agent_backend_instances` | id, workspace_id, adapter_type, endpoint_ref, secret_ref, capabilities_json, trust_level, status | Secret values stay in vault; backend disabled until reviewed |
| `backend_sessions` | id, workspace_id, task_id, backend_id, remote_session_ref, state, last_event_seq | Task-bound, replay cursor and explicit terminal state |
| `skills` | id, skill_key, version, source_uri, immutable_revision, sha256, license_expression, manifest_json, status | Immutable version; no activation without digest/license/review/scan |
| `skill_installs` | id, workspace_id, skill_id, granted_permissions, enabled_by, enabled_at, revoked_at | Workspace-scoped explicit approval; cannot elevate policy |
| `sandbox_sessions` | id, workspace_id, task_id, provider, runtime_profile, image_digest, network_policy_id, state, expires_at | Per-task isolation; default-deny egress; credentials not stored in row |
| `sandbox_artifacts` | id, workspace_id, sandbox_id, object_key, sha256, scan_status, classification | Content scanned and tenant-scoped before sharing |
| `ui_catalog_versions` | id, version, schema_hash, component_manifest, action_manifest, published_at | Immutable version; actions map only to registered operations |
| `generated_ui_specs` | id, workspace_id, task_id, catalog_version_id, spec_json, validation_status | Unsafe/invalid spec never becomes interactive |
| `dependency_components` | id, purl, name, version, supplier, source_revision, digest, license_expression, direct_or_transitive | One record per exact resolved component version/artifact |
| `license_reviews` | id, component_id, review_status, reviewer, evidence_uri, conditions, reviewed_at | Unknown license blocks release; legal opinion attributed to qualified counsel only |
| `sbom_artifacts` | id, release_candidate_id, format, version, sha256, object_key, validation_status | Required for every distributable release candidate |
| `brand_assets` | id, asset_path, origin, creator, license, trademark_clearance_status | ORBIT-owned asset provenance recorded; no unlicensed imported logos |
| `compliance_approvals` | id, workspace_id, release_id, reviewer_user_id, gate_type, decision, evidence_hash | Human approval for release/compliance exceptions |

## Employee and role records

Do not create a table called `employees` to store AI personas as if they were hired people. Use `agent_role_definitions` and `agent_role_assignments` for virtual roles. Actual human user/team-member records, if later required, must be modelled separately with explicit legal/employment purpose, access controls, retention and applicable privacy review.


## v0.5 reuse, source and skills entities

Add these proposed entities for safe upstream and skill operations:

| Entity | Important fields | Invariants |
|---|---|---|
| `upstream_sources` | id, repository_url, commit_sha, package_name, license_expression, status, reviewed_at | Immutable source revision; full commit SHA; review state is explicit |
| `upstream_source_files` | id, upstream_source_id, path, sha256, selected_for_import | Hash exact imported files; no source path outside approved allowlist |
| `source_import_reviews` | id, upstream_source_id, reviewer_id, decision, evidence_ref, created_at | Reviewer independent from importer for critical components |
| `upstream_patches` | id, upstream_source_id, patch_ref, base_commit, owner, sync_state | Every local modification is attributable and syncable |
| `third_party_notices` | id, component_id, notice_ref, license_expression, scope | Required notices are retained per distribution scope |
| `skill_imports` | id, workspace_id, source_url, revision, digest, status, scan_report_ref | Quarantined until reviewed; no execution at fetch time |
| `skill_versions` | id, skill_id, version, digest, license_expression, manifest_json | Immutable version and source provenance |
| `skill_reviews` | id, skill_version_id, reviewer_id, permissions, decision, evidence_ref | No missing license or permission can become executable |
| `agent_skill_grants` | agent_id, skill_version_id, granted_capabilities, enabled_at, revoked_at | Per-agent/workspace enablement; default disabled |
| `integration_decisions` | id, capability, component_id, decision, rationale, owner, reviewed_at | One selected default per capability; alternative state is explicit |
| `evaluation_runs` | id, dataset_version, candidate_version, baseline_version, metrics_json, report_ref | Holdout data and promotion decision are recorded |

These are design additions only. Implement with migrations after the real application schema is audited. Every record must be workspace-scoped where user data is involved. Source repository metadata can be globally shared, but user import decisions and enablement must be tenant-scoped. Avoid storing source files directly in PostgreSQL; use content-addressed object storage with access control.


## v0.6 repository operations and storage entities

- `upstream_repository`: canonical URL, owner/project, ref, immutable commit, observed license evidence, enabled/blocked state and recheck date.
- `upstream_audit`: repository ID, checked commit, scan tool/version, report artifact, reviewer and limitations.
- `source_import`: upstream ID, commit, source path, file digest, staged destination, license decision, security decision, test evidence, modifier and merge PR.
- `source_import_file`: source/imported paths, pre/post SHA-256, modification flag, notice reference and generated SBOM component ID.
- `agent_grant`: agent ID, workspace/context scope, capability, resource filter, expiry, approval requirement and revocation timestamp.
- `storage_volume`: volume ID, mount, expected capacity, encryption state, last seen, free bytes and read/write health. Never store mount secrets.
- `storage_allocation`: storage volume, folder ID, soft target bytes, actual bytes, retention policy and cleanup class.

A cloned upstream or copied file is not automatically an adopted dependency. Import records retain provenance after the code is merged. Storage target values are advisory unless an OS quota service is separately configured.
