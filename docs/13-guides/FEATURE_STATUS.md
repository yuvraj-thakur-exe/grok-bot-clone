# ORBIT feature status — v0.6 planning baseline

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status date:** 2026-11-08. This file describes the documentation/research pack only, not a built runtime.

| Capability | Planning state | Evidence in this pack | Runtime status |
|---|---|---|---|
| Product workspace and agent roster | Specified | PRD, target architecture, UX specs | Not verified; actual app repo not supplied |
| Reuse-first upstream sourcing | Documented | Commit lock, clone helper, reuse playbook | Source acquisition helper only; no source merge |
| OpenMausBot product shell | Candidate | Repository audit and lock entry | Not selected; requires actual repo comparison and build audit |
| OpenClaw/Hermes runtime adapters | Specified | Adapter contracts and source matrix | Not implemented |
| Coding worker/OpenHands | Candidate | Source matrix and adapter plan | Not implemented |
| BrowserDriver | Specified | Browser research and execution contracts | Not implemented |
| SandboxProvider | Specified | Docker/OpenSandbox research | Not implemented |
| Memory/RAG | Specified | Memory architecture and source shortlist | Not implemented |
| Skill registry/intake | Specified | Policy, schema, example and audit helper | Static package audit helper only; not a malware scanner or runtime sandbox |
| Personal/work routines | Specified | Personal/work agent model and product requirements | Not implemented |
| Native desktop node | Designed | Desktop design, API and runbooks | Not implemented |
| Multi-agent orchestration | Designed | Team model, role registry and coordination docs | Not implemented |
| Security, SBOM and compliance gates | Designed | Policy, checklist and example pipeline | CI not wired into an application repo |

## Status vocabulary

- `not_started`: no code implementation.
- `audit_in_progress`: repository/source inspection underway.
- `prototype`: isolated proof-of-concept exists but not production integrated.
- `implemented`: merged source code exists and relevant tests pass.
- `validated`: integration, security and acceptance evidence is attached.
- `released`: human-approved production distribution.

A clone, document, schema, API draft, diagram or README is not runtime implementation evidence.


| Dedicated storage and repository operations | Specified | v0.6 storage architecture, repository analysis and operations scripts | Scripts created; not run against user's external disk or actual ORBIT repository |
| Upstream code staging with provenance | Prototype utility supplied | `scripts/import_upstream_path.py` and import spec | Script stages selected paths; no app merge performed |
| Static repository audit | Prototype utility supplied | `scripts/repo_audit.py` | Script provided; no actual ORBIT repo audit performed without its path |
| Local model runtime | Candidate | Ollama, llama.cpp pins and hardware requirements | Not installed or benchmarked |
