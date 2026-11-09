> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

---
name: orbit-repository-audit
description: Read-only audit of an existing ORBIT codebase before implementation changes.
version: 1.0.0
author: ORBIT
license: LicenseRef-ORBIT-Pending-Decision
metadata:
  risk: low
  allowed-tools: ["repo.read", "git.status", "test.list"]
---

# ORBIT repository audit

## When to use
Before starting a new feature, architecture migration or unfamiliar repository task.

## Procedure
1. Read root agent instructions and relevant docs.
2. Record branch, working tree status and recent commits.
3. Map apps, packages, service entrypoints, database, tests, CI and deployment.
4. Search for existing implementations before proposing new modules.
5. Identify secrets or risky files by metadata only; never print secret values.
6. Run safe read-only checks and report exact commands/results.
7. Produce a gap matrix: existing, partial, stub, missing, blocked.
8. Recommend next vertical slice; do not edit files in audit mode.

## Output
Repository map, current-state architecture, test baseline, security concerns, dependency/license concerns, prioritized gaps and open questions.
