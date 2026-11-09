# Work breakdown structure

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Epic | Work packages | Dependencies |
|---|---|---|
| EP-00 Audit | repo audit, user requirements, competitor research, ADRs | none |
| EP-01 Foundation | app shell, API, auth, workspace, database migrations | EP-00 |
| EP-02 Model layer | provider adapters, capability registry, streaming, usage | EP-01 |
| EP-03 Task engine | task model, workflow persistence, event stream, cancellation | EP-01/02 |
| EP-04 Tool gateway | registry, schemas, policy, approval object, audit | EP-03 |
| EP-05 Research | search adapters, fetcher, extraction, citations, verification | EP-02/04 |
| EP-06 Files | upload, quarantine, parsing, object store, retrieval | EP-01/04 |
| EP-07 Computer | browser worker, session store, code sandbox, visual progress | EP-03/04 |
| EP-08 Memory | memory lifecycle, ACL retrieval, user controls | EP-01/02 |
| EP-09 Skills/routines | manifests, tests, scheduler, pause/retry | EP-03/04/08 |
| EP-10 Multi-agent | coordinator, child workflows, shared artifact references | EP-03/04/05 |
| EP-11 Production | telemetry, CI/CD, backup, security and load tests | all preceding |

Each work item must link to requirement IDs, owner, status, dependencies, acceptance criteria, and test evidence. This table is a planning baseline, not a claim that tickets or code already exist.

## Desktop integration workstream

See `DESKTOP_INTEGRATION_PLAN.md` for epics DSK-EPIC-01 through DSK-EPIC-05. This is a separate post-foundation workstream with driver contract, Local Desktop Node, read-only observation, approved semantic mutations and platform readiness. Gate it on core task engine + policy gateway being stable.

## ORBIT v0.2 alignment

The v0.2 roadmap adds a gated desktop workstream after core auth, durable tasks and policy gateway. See `DESKTOP_INTEGRATION_PLAN.md`; desktop is not the first MVP path.
