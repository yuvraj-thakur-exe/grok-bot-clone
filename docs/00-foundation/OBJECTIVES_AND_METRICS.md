# Objectives and Metrics

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| Objective | Metric / initial gate |
|---|---|
| Usability | p75 initial UI usable <3s on a documented reference setup |
| Chat | Report first-token p50/p95 per model/provider; no universal promise |
| Task quality | Establish benchmark; target >=80% success on bounded tasks after rubric stabilizes |
| Recovery | All designed worker-restart cases recover in test |
| Research | >=90% factual claims supported in fixed citation evaluation set |
| Security | No unresolved critical/high tool-policy, tenant-isolation or sandbox finding before public release |
| Isolation | All cross-workspace tests deny access |
| Cost | Track cost per successful task and enforce workspace/task budgets |
| Operations | Complete database/object-storage restore drill |

These are proposed targets, not measured results. Benchmarks must record model, prompt, tools, environment, sample size and failures.

## ORBIT v0.2 alignment

The v0.2 product baseline adds optional native desktop access through a paired Local Desktop Node. It does not change ORBIT’s core mission or move desktop control into the first MVP. Keep product objectives focused on verified, safe task completion.
