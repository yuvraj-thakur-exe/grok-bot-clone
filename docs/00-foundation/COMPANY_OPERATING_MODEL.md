# ORBIT company operating model

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Version:** 0.3.0-draft  
**Status:** Proposed operating model; not a legal corporate structure or employment record.

## 1. Purpose

ORBIT is planned as a product company building a provider-neutral, self-hostable AI execution platform. This document defines how a small founder-led team and a set of AI-assisted role agents should coordinate product, engineering, security, legal, operations and community work.

**Important:** Role agents are software workflows/personas, not human employees, directors, officers, legal counsel or fiduciaries. They cannot bind the company, sign contracts, hire people, move money, publish legal claims or make production releases unless an authorized human explicitly approves the exact action.

## 2. Founder and accountability model

The human founder is the final accountable owner for company strategy, budget, product direction, hiring, legal commitments, public statements, customer data policy and production risk acceptance. ORBIT's virtual executive council advises and prepares decisions; it does not supersede the founder.

| Role | Accountable scope | Decision rights | Cannot do alone |
|---|---|---|---|
| Founder / CEO (human) | Mission, strategy, capital, company and product accountability | Final product, budget, hiring, legal and release approvals | Delegate statutory or fiduciary duties to an AI role |
| CTO / Chief Architect (AI-assisted role) | Technical strategy, architecture, engineering standards | Recommend architecture, technical sequencing and acceptance gates | Override security veto, approve its own production change, claim test evidence it lacks |
| Chief Product Officer | User problem, product scope, prioritisation | Recommend roadmap, requirements and product trade-offs | Expand scope without capacity/cost review |
| Chief AI / Research Officer | Model strategy, evaluations, research quality | Recommend providers, agent design and experiments | Claim model capability without measured evidence |
| Chief Operating Officer / Delivery Lead | Execution, milestones, operating cadence | Coordinate work and report status | Hide blockers or redefine acceptance criteria silently |
| Security & Privacy Lead | Threat model, access policy, privacy and incident readiness | Block unsafe work pending mitigation | Waive material risk on behalf of the founder |
| Finance & Commercial Lead | Cost, usage, vendor commitments and runway model | Recommend spend limits and procurement | Execute purchases or payments |
| Legal / IP / OSS Compliance Advisor | License, trademark, contracts and regulatory issue spotting | Flag legal risk and prepare questions for qualified counsel | Give a binding legal opinion or approve legal acceptance |

## 3. Functional departments

### Product and Design
- Product strategy, personas, customer discovery and requirements.
- Information architecture, interaction design, accessibility and usability research.
- Product analytics and prioritisation based on outcomes, not feature count.

### AI Research and Agent Intelligence
- Model/provider evaluation and routing.
- Agent planning/execution, context management, retrieval, memory and evaluations.
- Tool-use reliability, research grounding, hallucination analysis and red-team testing.

### Core Platform Engineering
- API/control plane, persistence, identity, workspaces, durable tasks and event streaming.
- Typed tool gateway, authorization, approvals, audit trail and connector platform.
- Database migrations, contracts, versioning and backward compatibility.

### Execution and Computer Use
- Browser worker, native desktop node, code/repository worker and file processing worker.
- Sandbox lifecycle, worker images, resource quotas, network egress and artifact transport.
- Execution replay, cancellation, checkpointing and recovery.

### Security, Privacy and Trust
- Threat modeling, secure defaults, secrets, authentication, authorization and isolation.
- Software supply-chain security, SBOMs, dependency/license review and vulnerability response.
- Privacy controls, retention/deletion, incident response and security testing.

### DevOps, SRE and Infrastructure
- Local development, staging, production deployment, CI/CD, observability and reliability.
- Backups, recovery drills, service objectives, capacity and cost efficiency.

### Quality and Evaluation
- Functional, integration, end-to-end, cross-platform and performance testing.
- Agent task evaluation, failure taxonomy, regression datasets and release gates.
- Independent verification of delivery and security acceptance criteria.

### Open Source, Community and Developer Relations
- Contributor experience, docs, examples, issue triage, release notes and ecosystem integrations.
- Public roadmap and governance proposals, subject to founder approval.

### Finance, Commercial and Legal Operations
- Cloud/model spend tracking, procurement approval workflow and commercial analysis.
- Contract and license review coordination with qualified professionals.

## 4. Virtual workforce roles

The organisation chart is implemented as role charters and task queues, not as an assumption that many independent models are running at once. An orchestrator may instantiate a role only when required, pass a scoped brief and collect an auditable result.

| Agent role | Primary deliverable | Review partner |
|---|---|---|
| CEO Strategy Analyst | Strategic options, business assumptions, decision memo | Human founder |
| CTO / Principal Architect | Architecture, ADRs, technical plan | Security lead + founder for material decisions |
| Product Manager | PRD, story map, acceptance criteria | Founder / design lead |
| AI Research Scientist | Model and agent experiments, eval design | AI lead + QA |
| AI/ML Engineer | Router, inference adapters, retrieval and eval implementation | Principal architect |
| Backend Engineer | APIs, persistence, auth, workflow state | Backend lead / QA |
| Frontend Engineer | Workspace UI, streaming, artifacts and accessible components | Design lead / QA |
| Browser Automation Engineer | Browser driver, isolation, navigation policy | Security lead |
| Desktop/Computer-Use Engineer | Desktop node, accessibility driver and OS test matrix | Security lead |
| Sandbox Engineer | Runtime adapters, isolation, egress controls and quotas | Security + SRE |
| DevOps/SRE Engineer | CI/CD, deployment, telemetry, backup and SLOs | CTO + security |
| Security Engineer | Threat tests, access-control tests and remediation | Security lead |
| QA / Evaluation Engineer | Test suites, acceptance evidence, regression evaluation | Product + CTO |
| Data/RAG Engineer | Ingestion, chunking, embeddings, retrieval and provenance | AI research + privacy |
| UX/UI Designer | Design system, flows, interaction specs | Product lead |
| Technical Writer | Developer documentation and runbooks | Owning engineering lead |
| OSS Maintainer | Contributor workflow, release checklist and license notices | Founder + compliance advisor |
| Finance Analyst | Unit economics, provider budgets and usage report | Founder |
| Legal/IP Research Analyst | License/trademark inventory and counsel brief | Qualified lawyer for final advice |

## 5. Decision forums

- **Product review:** weekly; founder + product + delivery + design. Output: prioritised backlog and acceptance changes.
- **Architecture review:** for any cross-module, data, runtime, protocol, provider or deployment change. Output: ADR and migration plan.
- **Security review:** mandatory for new tools, external integrations, sandbox changes, secrets, network egress, desktop access or sensitive data.
- **Release review:** QA evidence, security status, dependency/license status, rollback plan, observability and owner approval.
- **Incident review:** blameless review after containment; track root cause, impact, response and corrective actions.

## 6. RACI rules

R = responsible for preparing/executing; A = accountable; C = consulted; I = informed.

| Activity | Founder | CTO | Product | Security | QA/SRE | Legal advisor |
|---|---:|---:|---:|---:|---:|---:|
| Product strategy | A | C | R | I | I | I |
| Architecture | I/A* | R | C | C / veto on unsafe design | C | I |
| Backlog priority | A | C | R | C | C | I |
| Tool permission policy | A for risk acceptance | R | C | R / block unsafe design | C | C |
| Production deploy | A | R | I | C / release gate | R | I |
| Procurement / spend | A | C | I | C | C | C |
| Open-source license choice | A | C | I | C | I | R / qualified counsel |
| External legal acceptance | A (human) | I | I | C | I | R / counsel |

*The founder may act as technical decision owner while the company is small; as the engineering organisation grows, preserve independent security and QA review.

## 7. Minimum process for any task

1. A role owner receives a task with goal, constraints, expected output and requirement IDs.
2. It inspects current code/docs before proposing changes.
3. It produces a plan, affected modules, risks and tests.
4. It works in a branch/worktree and does not overwrite unrelated work.
5. An independent reviewer checks correctness, security and scope.
6. The owning lead updates docs, status and traceability.
7. Human approval is required for external side effects and production releases.

## 8. Hiring transition

Do not confuse AI role charters with a staffing plan. Real human hires should be triggered by sustained workload, security/accountability requirements, support obligations or the need for independent review. Initial high-value human responsibilities are founder/product ownership, senior engineering review, security/legal review and customer support once external users exist.
