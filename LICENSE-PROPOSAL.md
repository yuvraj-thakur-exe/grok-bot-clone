# License decision — not yet adopted

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Proposed first-party license:** Apache-2.0 for ORBIT-owned application code and SDKs, subject to human founder approval and qualified legal review of the actual distribution model, all first-party contributions, dependency stack, fonts/icons/assets, model/data terms and trademarks.

Do not claim ORBIT is Apache-2.0 licensed until the decision is approved, the complete canonical license text is present, the copyright owner/year is correct, contribution policy is settled and required third-party notices/SBOM process is in place.

## Important distinction

ORBIT's license choice is independent of every upstream dependency. Using an Apache-2.0, MIT or other open-source component does not automatically license ORBIT's code. Keep upstream LICENSE, NOTICE, copyright and attribution obligations wherever required. Never strip legal notices as part of visual rebranding.

## Release prerequisites

1. Approve the intended source/binary/hosted distribution posture with legal review.
2. Complete `docs/06-security/THIRD_PARTY_COMPONENT_REGISTER.yaml` for exact package/image/binary/model/skill versions.
3. Resolve `NOASSERTION` and conditional-license entries or block redistribution.
4. Generate SPDX/CycloneDX SBOM, third-party notices and dependency security evidence.
5. Approve brand/trademark usage and asset provenance.
