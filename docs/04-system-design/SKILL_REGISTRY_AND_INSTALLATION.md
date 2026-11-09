# Skill registry and installation service

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Skill package format

An ORBIT skill is a versioned directory with:
- `SKILL.md` containing YAML frontmatter (`name`, `description`, version, author, license, compatibility, risk level);
- optional `references/` for static, reviewed material;
- optional `scripts/` that run only in an isolated worker;
- `manifest.yaml` declaring required tools, input/output schema, secrets, permissions, network domains, budgets and tests.

## Lifecycle

Discover → fetch immutable source → verify digest/signature → parse manifest → scan scripts/dependencies → validate license → review risk → install disabled/quarantined → test in sandbox → approve → activate → monitor → update or revoke.

## Registry metadata

`skill_id`, semantic version, source URI, commit/tag, archive SHA-256, publisher, signature, license expression, attribution/notice files, required permissions, network destinations, tool IDs, secrets references, platform requirements, compatible agent harnesses, evaluation results, review timestamp, status and deprecation date.

## Permission model

- Skills cannot add permissions not granted by workspace/user policy.
- External skills are disabled by default until reviewed.
- Script skills run in a disposable sandbox with deny-by-default network egress.
- Skills may declare action requirements; an admin grants them separately.
- Secret values are never stored in the skill archive or exposed to the model.

## Lockfile

Each workspace stores `orbit-skills.lock` with exact skill versions, source commits, archive hashes, license IDs and dependency hashes. Reproducible install must fail on checksum mismatch, license denial, missing attribution or undeclared executable content.

## Skill interoperability

Use the open Agent Skills file convention where compatible, but do not assume every optional field or hook is supported by every IDE agent. Maintain adapter tests for Codex, Claude Code, Antigravity, Gemini CLI, Cursor and GitHub Copilot. Do not silently install all skills into global directories.
