# Software supply-chain governance

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Required controls

- Pin package versions and immutable image digests. Avoid production `main`, `latest` and floating Git branches.
- Use lockfiles and reproducible builds; separate development and production dependencies.
- Generate SPDX or CycloneDX SBOM for application packages, containers, model/runtime bundles and desktop binaries.
- Verify release checksums and signatures where published; verify source-to-binary provenance when available.
- Scan vulnerabilities, secrets, malware, dependency confusion and typosquatting risks.
- Use minimal base images, non-root runtime, read-only root filesystem where possible, seccomp/AppArmor/SELinux and resource limits.
- Isolate build credentials, use short-lived CI tokens and protect release signing keys.
- Review package postinstall hooks and install scripts; disable or allowlist where safe.
- Record dependency owner, update cadence, support/EOL status and fallback/replacement plan.

## Dependency update process

1. Bot opens a version update PR with changelog, diff and advisory report.
2. License/SBOM and API compatibility checks run.
3. Contract tests and security tests run against candidate version.
4. Canary/staging deployment validates runtime behavior.
5. Release manager approves rollout and rollback plan.

## SBOM fields

Component name/version, supplier, package URL (purl), SPDX license expression, source commit, checksum, relationship, scope, direct/transitive, downloaded artifact URI, notice file path, vulnerability status and approval record.

## v0.3 release evidence package

For each release retain: source SBOM (SPDX and/or CycloneDX), per-container SBOM, direct/transitive dependency inventory, license scan output, third-party notices, vulnerability report, secret scan report, artifact checksum/signature, source revision, build provenance and signed approval record. The sample CI workflow in `examples/ci/supply-chain-gate.yml` is illustrative only; replace every placeholder action SHA and pin tool versions before use.
