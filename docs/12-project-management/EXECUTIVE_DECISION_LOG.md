# Executive decision log — v0.3 proposals

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Decision | Rationale | Status |
|---|---|---|---|
| ED-001 | ORBIT is the single product identity; reference company/product branding is not used as ORBIT UI branding | Distinct identity and no misleading affiliation | Proposed; trademark clearance outstanding |
| ED-002 | Third-party copyright, license and NOTICE obligations are preserved | Branding and legal attribution are different | Mandatory policy |
| ED-003 | Role charters represent virtual work functions, not legal employees/directors | Clear accountability and truthful status | Mandatory policy |
| ED-004 | Human founder retains final authority for spend, legal, hiring and production release | Legal and operational accountability | Mandatory policy |
| ED-005 | External agent backends use ORBIT-owned `AgentBackend` contract | Reduce coupling and enable local/remote/cloud choice | Proposed |
| ED-006 | Sandbox is isolated behind `SandboxProvider`; Docker first, OpenSandbox candidate | Keep MVP tractable while allowing stronger isolation | Proposed |
| ED-007 | Generative UI must use a constrained catalog and server-authorized action IDs | Prevent arbitrary model-authored code/actions | Proposed |
| ED-008 | Skills use a portable format plus immutable lock metadata | Interoperability and reproducibility | Proposed |
| ED-009 | Third-party dependencies require license and SBOM gates | Prevent unlawful/untracked distribution | Mandatory release gate |
| ED-010 | Portless-style named localhost routing is optional development tooling only | Useful dev ergonomics but not production ingress | Proposed |

Decisions affecting product scope, architecture or security require an ADR or recorded founder approval before implementation.
