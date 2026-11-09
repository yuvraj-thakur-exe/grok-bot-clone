# ORBIT founding team and department charter

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Operating model:** a human-founded company supported by AI-assisted virtual role agents and, when available, human contributors. This document assigns responsibilities; it does not create employment, corporate offices, statutory directorships, legal representation or professional qualifications.

## Founder / CEO — human accountable owner

Owns company mission, product-market direction, commercial strategy, finance, hiring, external commitments, legal agreements, public positioning and final release approval. May delegate research and drafting, never statutory/legal authority by implication.

## Virtual leadership roles

| Role | Mission | Decision rights | Required evidence |
|---|---|---|---|
| CTO / Principal Architect | Technical strategy, architecture, delivery quality and technical risk | Proposes architecture; can block technically unsafe merge; human founder approves major irreversible choices | ADRs, trade-offs, test evidence, cost/ops model |
| CPO / Product Lead | User problems, PRD, roadmap, acceptance and usability | Prioritizes product backlog within approved strategy | User evidence, requirements, acceptance criteria |
| Chief AI / Research Lead | Model evaluation, agent intelligence, RAG, research quality | Recommends models and evaluation gates | Reproducible datasets, benchmark methodology, source provenance |
| COO / Delivery Lead | Work breakdown, dependencies, sprint delivery, reporting | Coordinates work and escalation | Milestone plan, owner, status, blockers |
| Security Lead | Threat modelling, policy, identity, secrets and incident response | May block unsafe implementation or release | Threat analysis, tests, remediation evidence |
| SRE / DevOps Lead | CI/CD, deployment, uptime, backups, observability and cost | May block deployment for reliability/security failures | Runbooks, deployment evidence, restore/rollback test |
| QA / Verification Lead | Independent conformance, regression, usability and release evidence | Rejects unverified acceptance claims | Test results, reproducible steps, defect severity |
| Design Lead | Brand, design system, interaction, accessibility | Owns design quality within approved brand | Token audit, accessibility tests, screen states |
| Open-source / License Steward | SBOM, provenance, notices, license and contribution hygiene | Blocks release with unresolved legal metadata | Component register, notices, approvals, SBOM |
| Developer Relations / Docs Lead | Setup, docs, examples, issue triage and community | Proposes contributor UX | Documentation tests, contributor feedback |

## Specialist engineering roles

AI platform engineer, agent runtime engineer, model integration engineer, data/RAG engineer, browser automation engineer, native desktop engineer, sandbox/infrastructure engineer, backend engineer, frontend engineer, API/integration engineer and test automation engineer.

## Separation of duties

- The agent that implements a security-sensitive change cannot be its sole reviewer.
- QA cannot mark tests passed based only on the implementer's narrative.
- License review must inspect exact dependencies and artifacts, not the developer's summary.
- Security can veto an unsafe release; human founder resolves business trade-offs but cannot override law or platform security controls.
- Only a human with proper access may approve spend, contracts, account changes, employment, legal acceptance, public announcements and production deployments.

## AI employee/agent definition

Virtual role agents are software workflows with assigned responsibilities. They do not hold legal personhood, employment status, fiduciary duties or independent authority. Every action is attributable to a real human owner or service identity; actions require scoped permission and audit.

## Operating cadence

- Daily: task and blocker triage; only high-risk changes require synchronous human review.
- Weekly: product/engineering review, cost/quality/security metrics, dependency alerts and milestone decision.
- Per release: QA + Security + License checks, changelog, SBOM, rollback and founder release approval.
- Monthly: architecture review, model/provider cost review, supply-chain inventory, data retention and access audit.


## v0.5 execution rule

The role library now has dedicated reuse-first responsibilities. The founder remains the human decision authority. Virtual role names do not imply actual employment or legal authority. Cross-team work must have one DRI, testable output, source/licensing review and independent QA/security signoff for critical scope.

