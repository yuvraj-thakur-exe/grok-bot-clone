# ORBIT v0.5 open-source license and supply-chain release checklist

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Release blocker:** any unresolved license, attribution, source-provenance or high-risk supply-chain issue blocks public distribution unless the human founder accepts a narrowly scoped exception with qualified review.

## Source and dependency inventory

- [ ] Exact release commit and build inputs recorded.
- [ ] Direct/transitive packages, source modules, plugins, skills, fonts, icons, binaries, images, models and datasets inventoried.
- [ ] `docs/06-security/THIRD_PARTY_COMPONENT_REGISTER.yaml` records exact version/revision, digest, package/source, use mode, license evidence, notices and reviewer.
- [ ] `NOASSERTION`, unknown and missing licenses are manually resolved or excluded.
- [ ] Root and nested license/NOTICE files reviewed at the exact imported revision.

## Source reuse and trademarks

- [ ] Imported files have source repository, commit, path, SHA-256 and modification history.
- [ ] Required LICENSE, NOTICE, patent and attribution notices retained.
- [ ] Modified upstream files carry required change notices.
- [ ] OpenMausBot `enterprise/` is absent from the checkout/import and not used.
- [ ] No third-party name, logo, mascot, screenshot or trade dress is represented as ORBIT branding.
- [ ] Linked skills are reviewed under their own source licenses, not the catalogue repository license.

## Security and privacy

- [ ] SBOM generated for each distributed source/runtime artifact, SPDX or CycloneDX.
- [ ] Vulnerability and secret scans completed; findings triaged.
- [ ] Install scripts, telemetry, update checks, binary downloads and external data flows reviewed.
- [ ] Untrusted skill/plugin code is isolated; no unrestricted host, network or secret access.
- [ ] Memory and artifact scopes, deletion propagation and telemetry redaction tested.
- [ ] Browser/code/desktop boundaries and exact external-action approvals tested.

## Product and operations

- [ ] Security and QA reviews are independent for critical changes.
- [ ] Backup/restore, rollback, migration and incident procedures verified.
- [ ] Third-party notices are included in source and binary distributions as applicable.
- [ ] ORBIT About/Legal surface discloses required third-party attribution.
- [ ] Human founder approves release, spend and binding legal/commercial commitments.

## Evidence archive

SBOM, lockfiles, license report, vulnerability report, secret scan, provenance/attestation, checksums, notice bundle, source-import manifest, test results, backup/restore evidence, exception records and human approval.
