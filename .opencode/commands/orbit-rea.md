---
description: Evidence-based analysis of a repository (clone, inspect, report)
agent: rea
subtask: true
---
Analyse $ARGUMENTS (owner/repo or name from scripts/research-repos.tsv). Steps: `bash scripts/bootstrap-research.sh $ARGUMENTS`; record SHA + licence (check directory-specific licences); map entry points, packages, dependencies, tests, release activity; identify parts reusable under ORBIT's tiers (docs/02-research/OPEN_SOURCE_REUSE_MAP.md). Write `docs/02-research/rea/<name>.md`. UNVERIFIED for anything not seen in source.
