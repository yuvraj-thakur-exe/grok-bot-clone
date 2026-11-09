# ORBIT v0.5 — supply-chain, upstream and skill security

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Threat assumptions

Public repositories, dependencies, skills, model outputs, web pages, attachments, app events and tool results may be malicious, compromised, stale or misleading. Popularity and catalogue inclusion are not security certifications.

## Upstream source controls

- Pin full commit hashes; do not build production from floating branches.
- Verify remote URL and commit before source acquisition.
- Generate source file hash manifests and SBOMs.
- Review root and nested license/NOTICE files and exact dependency packages.
- Inspect install scripts, postinstall hooks, telemetry, update checks and executable binaries.
- Keep restricted enterprise source out of selected OSS checkouts.
- Preserve modification notices and attribution.
- Maintain provenance and patch queues; periodically sync upstream security changes.

## Skill trust levels

1. **Discovered:** catalogue entry only; cannot execute.
2. **Fetched:** source downloaded to quarantine; cannot execute.
3. **Reviewed:** source, license, permissions and dependencies checked.
4. **Validated:** static scanning and isolated tests passed.
5. **Enabled:** user enables a specific version for a specific workspace/agent.
6. **Revoked:** disabled and removed from future runs; logs retained only per policy.

## Skill manifest requirements

Every skill needs a stable identifier, semantic version, display name, description, canonical source, immutable commit/tag, content digest, license expression or explicit unknown state, authorship/attribution, required tools, filesystem/network/secret permissions, dependencies, supported runtimes, tests and reviewer status. Missing or ambiguous license means no redistribution. Missing permission declaration means no execution.

## Runtime isolation

Untrusted skill scripts run in disposable sandboxes with deny-by-default network egress, read-only package mounts where feasible, scoped work directory, no host socket, no personal browser profile, no ambient secrets, CPU/memory/time quotas and output scanning. MCP tools are separately authorized. Tool annotations are advisory metadata, not an authorization grant.

## Self-improvement

Prompt, skill and tool-description optimization runs offline against a fixed evaluation dataset with train/validation/holdout separation. No live mutation of deployed prompts or skills. Every candidate needs regression, safety and cost evaluation, human review, versioned artifact, rollout plan and rollback. Code evolution requires disposable branches, comprehensive tests and security review.

## Incident response

A suspected malicious dependency/skill is disabled, version is blocked, all impacted task runs and workspaces are identified, credentials are rotated if exposed, logs/artifacts preserved according to incident policy, and a reviewed replacement or rollback is selected. Notify affected users according to legal obligations and incident policy.
