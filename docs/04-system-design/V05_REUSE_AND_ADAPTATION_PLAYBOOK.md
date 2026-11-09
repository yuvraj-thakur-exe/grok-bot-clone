# ORBIT v0.5 — reuse and adaptation playbook

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Purpose

A repeatable process for using, modifying and maintaining upstream code instead of rewriting it. This playbook applies to whole product shells, SDKs, packages, source modules, skills, tools and UI assets.

## 1. Choose the reuse mode

| Mode | Use when | ORBIT responsibility |
|---|---|---|
| External service/runtime | Upstream owns a coherent process and protocol | Isolate process, map identity, observe state, cancellation and data egress |
| Official SDK | API is stable and SDK avoids extra framework coupling | Pin version, wrap with ORBIT adapter, contract-test and monitor |
| Package/module | Code is modular, compatible and independently testable | Preserve source, notices and tests; track changes |
| Selective source import | Small module provides needed capability and no usable package exists | Copy exact source with attribution, hash, modification notice and upstream tests |
| Maintained fork | Strategic changes cannot be cleanly upstreamed or adapted | Keep upstream remote, patch queue, periodic sync and owner |
| Rewrite | License, compatibility, security or operations makes reuse unsuitable | Document evidence, estimate maintenance cost, define migration path |

## 2. Intake record (mandatory)

For every candidate record repository URL, commit, branch/tag observed, package name/version, source paths, file hashes, root/nested license, NOTICE, patents/attributions, trademark limits, dependencies, build commands, tests, security findings, data-flow map, telemetry, update cadence, integration owner and decision status.

## 3. Source acquisition

1. Use `config/upstreams/upstream-lock.yaml` as the pinned snapshot authority.
2. Run `scripts/clone_upstreams.sh` with explicit selectors.
3. Review `LICENSE`, `NOTICE`, `LICENSING.md`, nested package licenses, third-party folders, `package.json`/lockfiles, install hooks, telemetry and security docs.
4. Do not install packages or run arbitrary upstream lifecycle scripts during initial inspection.
5. OpenMausBot checkouts must use sparse checkout to exclude `enterprise/`. Verify the directory is absent.
6. Record source commit, dirty state, path allowlist and hash manifest before adapting anything.

## 4. Modification workflow

- Prefer adapter/wrapper code to modifying upstream files.
- Keep imported upstream source in a clearly named, isolated directory or maintain a fork with a dedicated remote.
- Never overwrite ORBIT implementation simply because the upstream has a similarly named file.
- For source edits, record a patch file or clean commit series against the pinned base.
- Preserve tests and add ORBIT-specific conformance tests.
- Document every removed/disabled upstream feature and the reason.
- Keep upstream security fixes and license updates in a scheduled sync process.

## 5. Skill and plugin intake

A skill is executable/sensitive supply-chain content, not harmless text. Verify canonical origin, immutable ref, content digest, frontmatter, manifest schema, license, scripts, package dependencies, network calls, filesystem access, environment variables, credential handling, prompt injection surfaces, data retention and tests. Review the skill at least once per version. Require explicit user enablement; run in sandbox with minimal tools and egress. Never install in bulk from a catalogue.

## 6. Security and permission model

Adapters never inherit all host permissions. Map each upstream capability to an ORBIT permission identifier. Credentials are passed through write-only vault handles or short-lived worker env/pipe methods, never model-visible text. In-process plugins are treated as trusted code. Untrusted plugins require process/container boundary, constrained IPC and outbound egress policy.

## 7. Upstream synchronization

- Maintain an upstream remote and pinned base commit.
- Rebase/merge updates in a disposable worktree.
- Review changelog, license changes, security advisories and nested dependencies.
- Run upstream tests and ORBIT conformance tests.
- Produce a diff and SBOM delta.
- Promote through a human-reviewed PR; maintain a rollback tag.

## 8. Required decisions

Every adopted component has a decision: accepted, conditional, evaluation-only, discovery-only, blocked, or rejected. Do not leave an unreviewed component in runtime dependency manifests.
