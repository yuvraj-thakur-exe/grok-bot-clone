# Open-source license and third-party compliance policy

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**This is an engineering process, not legal advice.** A qualified lawyer should review the intended distribution model, license choice, trademark usage and any unclear components before commercial distribution.

## 1. Baseline rules

- Never remove third-party copyright notices, LICENSE files, NOTICE files, attribution headers or required change notices.
- Rebranding ORBIT's interface does not transfer ownership of upstream code/assets and does not erase legal attribution obligations.
- A public repository does not mean public-domain content.
- A repository-level license may not cover every asset, model, dataset, documentation page, skill or dependency. Review individual paths and package metadata.
- Do not copy code, docs, prompts, skills, images, icons, screenshots, logos or fonts unless a compatible license or written permission covers the exact material.
- Maintain a Software Bill of Materials (SBOM) for direct and transitive dependencies, container images, binary drivers and bundled assets.

## 2. Preliminary reference license inventory

| Reference | Observed root-license status | Proposed treatment | Notes |
|---|---|---|---|
| vercel-labs/agent-desktop | Apache-2.0 | Optional driver integration; preserve LICENSE/NOTICE and modified-file notices | Previously reviewed in v0.2; pin executable and hash |
| vercel-labs/agent-browser | README identifies Apache-2.0; check exact root LICENSE during implementation | Optional browser driver; preserve notices | Do not treat README badge as a substitute for license file review |
| vercel-labs/json-render | Apache-2.0 root LICENSE fetched | Evaluate package or patterns; preserve notices | Check each package's package metadata and transitive licenses |
| vercel-labs/agent-skills | No root `LICENSE` found at checked path; some individual skill frontmatter says MIT | Do not copy wholesale; review each skill/file | Repository license status is unresolved at package level |
| vercel-labs/skills | MIT root LICENSE fetched | Optional installer/discovery tool | README discloses anonymous telemetry and security-audit requests; assess privacy/disable controls |
| vercel-labs/portless | Apache-2.0 root LICENSE fetched | Optional local developer tool | Preserve CA/security warnings; no production use |
| OpenHands/OpenHands | MIT root LICENSE fetched | Study Agent Canvas/backend patterns; optional integration | Review package subdirectories and bundled assets separately |
| opensandbox-group/OpenSandbox | Apache-2.0 root LICENSE fetched | Sandbox adapter candidate | Review image licensing, sidecars, SDKs and all transitive components separately |

The above is a preliminary public-source inventory as of 08 November 2026. It is not a compatibility opinion and must be rechecked at the precise release/commit ORBIT adopts.

## 3. Allowed dependency classes

- **Class A — permissive approved:** license and notices validated; compatible with ORBIT distribution model; SBOM entry present.
- **Class B — conditional:** legal review, attribution, network use, copyleft implications, trademark or model terms need review.
- **Class C — internal-only:** used as a hosted service/tool or studied as a reference; source/assets not redistributed.
- **Class D — prohibited:** license unknown/incompatible, provenance unclear, unacceptable security/telemetry, or no permission.

No Class B/C/D dependency is bundled into a public release without the required approval.

## 4. License workflow

1. Inventory exact package/image/binary/model/dataset/skill and immutable source.
2. Retrieve root license plus all nested `LICENSE`, `NOTICE`, headers, package license metadata and model/data terms.
3. Parse SPDX expression where available; record exceptions and custom terms.
4. Check source provenance, copyright holder, trademark and patent clauses.
5. Scan direct/transitive dependencies; resolve ambiguous or conflicting licenses.
6. Decide whether code is linked, copied, modified, bundled, hosted or merely used as a reference.
7. Generate SBOM and third-party notices for the actual release artifact.
8. Record approval, evidence, review date, reviewer and conditions.
9. Re-run on version upgrades and before publication.
10. Remove a dependency by replacing code, not by deleting its required attribution while still using it.

## 5. License compatibility gate

CI must fail release for: missing license metadata; an unapproved license class; missing required NOTICE; untracked vendored source; unknown binary provenance; checksum mismatch; license file removed from a bundled component; or SBOM not generated. Warnings may be allowed during development but must be resolved before release.

## 6. Model and dataset terms

Model weights, datasets, embeddings, generated content and API services can have terms different from software licenses. Store model card/license URL, acceptable use policy, commercial use status, redistribution rules, attribution requirements, training restrictions, geography and version. Do not claim a model is open-source based only on source-available weights.

## v0.3 component register cross-reference

See `THIRD_PARTY_COMPONENT_REGISTER.yaml` for the initial research-only inventory, including exact evidence notes and adoption boundaries. A root license does not automatically cover subpackages, model weights, datasets, fonts, icons, container images, downloaded binaries or skill contents. Re-verify all layers at the commit/version actually used.

The `agent-skills` repository is marked `NOASSERTION` at repository level in the current inventory: the checked root LICENSE paths were not found, although an inspected individual skill declares MIT in frontmatter. Do not copy the collection wholesale. Review each exact file and associated assets independently.


## v0.5 reuse-specific controls

- OpenMausBot public OSS source may be evaluated under Apache-2.0, excluding `enterprise/` and preserving LICENSE, NOTICE, LICENSING.md and third-party notices. Trademark and mascot rights are not granted.
- OpenClaw and Hermes use MIT repository metadata in the inspected pinned snapshots; review each package and nested dependency separately.
- Hermes self-evolution declares MIT in README and `pyproject.toml`, but root LICENSE was absent in the inspected snapshot. Require rights-holder confirmation before redistribution.
- VoltAgent's MIT catalogue license does not apply automatically to linked skill repositories.
- Never infer permission for an asset, model, dataset, font, logo or linked package from its parent repository's license.
- Every imported file records source commit, path, digest, changes and required attribution.

