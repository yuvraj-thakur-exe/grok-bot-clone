# License approval workflow and exception register

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Owner:** License & Supply-Chain Steward. **Approver:** human founder / delegated legal counsel. **Status:** Proposed internal policy; not legal advice.

## Release gate

No source, package, binary, container layer, font, icon, skill, model, dataset, documentation asset or hosted integration is approved merely because it is public, popular or appears on GitHub.

Each component must have an immutable identity:

- repository/package/image/model/dataset URL and supplier;
- exact commit, tag, package version or image digest;
- file/package SHA-256 and acquisition time;
- root license plus nested license/NOTICE/copyright headers;
- SPDX expression where determinable, or `NOASSERTION`;
- usage classification: reference only, build-time tool, runtime dependency, bundled, modified, hosted service or copied source;
- redistribution and modification conditions;
- attribution/NOTICE obligations;
- security review, telemetry and data-processing review;
- approval owner, status, review date and expiration/revisit trigger.

## Approval states

`DISCOVERED` → `EVIDENCE_COLLECTED` → `TECHNICAL_REVIEWED` → `LICENSE_REVIEWED` → `SECURITY_REVIEWED` → `APPROVED_FOR_USE` → `RELEASED`.

Possible terminal states: `REJECTED`, `REPLACED`, `EXPIRED`, `BLOCKED_UNKNOWN_LICENSE`. Approval must be scoped to the exact version and use mode. A new version or use mode reopens review.

## Risk classes

| Class | Meaning | Release handling |
|---|---|---|
| A | Permissive license and conditions verified for intended use | May proceed after technical/security approval and notices |
| B | Copyleft, file-level, network-use, patent, model/data or attribution terms require legal interpretation | Block bundling/distribution pending legal approval |
| C | External service/reference-only integration; no source redistribution | Service privacy, contract, data-processing and export review still required |
| D | License absent/unclear/incompatible, malware/provenance concern or unacceptable terms | Prohibited until resolved; usually replace |

The labels are risk triage, not a substitute for interpreting license text. GPL-family treatment, linking, derivative-work status and hosted use require counsel for the actual product/distribution model.

## Exception record schema

Every exception contains `exception_id`, component ID, exact version/digest, affected artifact, reason, legal owner, security owner, mitigations, approval evidence, expiry date, and removal plan. No wildcard or perpetual blanket exception. Expired exception fails release.

## Required automation

- Generate SPDX or CycloneDX SBOM for source, application packages and each shipped container/image/binary.
- Check dependency license expressions and missing metadata.
- Scan known vulnerabilities and secrets.
- Verify checksums/signatures/provenance where available.
- Fail on unapproved `NOASSERTION`, missing mandatory notices, banned license class, unpinned VCS branch or untracked vendored source.
- Export human-readable third-party notices and a license dashboard.

## Rebranding boundary

ORBIT product UI, marketing, documentation layout and first-party asset system must be original. Legal notices, upstream package names in the SBOM, required copyright headers, LICENSE and NOTICE content, attribution and modified-file notices must remain. Never rename third-party author/copyright details to ORBIT.
