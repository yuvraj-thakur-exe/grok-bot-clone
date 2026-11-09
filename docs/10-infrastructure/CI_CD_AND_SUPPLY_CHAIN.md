# CI/CD and software supply chain

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## CI stages

1. Checkout pinned revision.
2. Install from lockfiles with cache and integrity checks.
3. Format/lint/type check.
4. Unit and integration tests.
5. OpenAPI/schema compatibility validation.
6. Dependency and license scan.
7. Secret scan.
8. Container scan and image build.
9. E2E smoke tests.
10. Package artifacts and publish test results/SBOM.

## CD stages

Promote immutable artifacts from staging to production. Run migration preflight and backups. Use expand/contract migrations. Deploy a small canary where supported, check health and error budgets, then continue or rollback. Database rollback is not always safe after writes; prefer forward-fix and restore plan where appropriate.

## Branch protection

Require CI, review and no unresolved high-risk security finding. Protect signing keys and deployment credentials through CI secret store and OIDC/workload identity where available.

## Desktop driver supply chain

Pin OS/architecture artifact, package version, commit, JSON contract version and SHA-256/signature verification result. Verify license and upstream release provenance. Contract tests run for every dependency upgrade. Node update must be staged, compatible with backend contracts and rollbackable. Never download moving `main`/`latest` binaries at runtime.

## ORBIT v0.2 alignment

The v0.2 deployment topology keeps the Local Desktop Node on the user’s interactive host; the cloud control plane only brokers authenticated leased tasks. See `DESKTOP_NODE_DEPLOYMENT.md`.

## v0.3 release controls

Every release candidate must generate a component SBOM, run vulnerability and license scans, verify checksums for downloaded binaries, validate required notices and fail on unknown licenses or unapproved components. See `docs/06-security/DEPENDENCY_POLICY.yaml`, `THIRD_PARTY_COMPONENT_REGISTER.yaml` and `LICENSE_COMPLIANCE_RELEASE_CHECKLIST.md`. Scanner results are not legal opinions; ambiguous terms are escalated to qualified counsel.


## v0.5 upstream CI gates

Pin full SHAs and package versions, generate SPDX or CycloneDX SBOMs, run license and vulnerability scanners, secret scanning, lockfile integrity and reproducible-build checks. Require review for nested licenses, install scripts, telemetry and binary downloads. Preserve third-party notices and modified-file notices in all distributions. Produce a source manifest for every imported module.

