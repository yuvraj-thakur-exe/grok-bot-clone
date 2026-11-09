# License compliance release checklist

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Use this checklist for every distributable binary, container, installer, desktop node, skill pack or source release. This is a process control, not legal advice.

## Component evidence
- [ ] Every direct/transitive dependency has package URL, exact version, source revision and digest.
- [ ] Root and nested license files have been inspected.
- [ ] Per-file licenses are checked for documentation, skills, assets, fonts, icons and datasets.
- [ ] Models and model APIs have separate model/service terms recorded.
- [ ] License expression is mapped to SPDX where possible; custom terms are escalated.
- [ ] Unknown or missing license is blocked pending review.
- [ ] Trademark and attribution obligations are understood.

## Build artifacts
- [ ] SBOM generated for application, containers, desktop drivers and bundled tools.
- [ ] Required LICENSE/NOTICE and copyright text are included.
- [ ] Modified upstream files carry change notices where required.
- [ ] Source provenance and build provenance are recorded.
- [ ] Vulnerability scan and secret scan pass within release policy.
- [ ] Third-party telemetry and data transfer are documented and approved.

## Branding
- [ ] ORBIT UI contains only approved original brand assets or properly licensed generic assets.
- [ ] No third-party logos, screenshots, badges or trade dress were copied without authorization.
- [ ] Required third-party notices remain available in the compliance view and distributed artifacts.
- [ ] ORBIT naming/trademark clearance status is confirmed for target markets or commercial launch remains blocked.

## Approval
- [ ] Engineering owner signs technical inventory.
- [ ] Security signs supply-chain checks.
- [ ] OSS/IP reviewer records outcome; uncertain items go to qualified counsel.
- [ ] Human founder/release owner approves distribution.
