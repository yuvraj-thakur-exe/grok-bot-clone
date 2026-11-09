# Upstream source reuse workflow — ORBIT v0.4

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Non-negotiable instruction to coding agents

**Reuse existing tested code before writing a replacement.** Do not rebuild a capability just because its implementation lives in another language, repository or package. First inspect the upstream repository, find the smallest suitable package/module, read its tests and license, build it, and adapt it behind an ORBIT-owned interface.

The preferred order is:

1. Use the upstream project unchanged as a separate executable/service/library.
2. Use an official package, SDK or plugin API.
3. Add a thin ORBIT adapter or wrapper.
4. Vendor a small module with its upstream notices and test suite.
5. Cherry-pick a small source change with provenance and a patch record.
6. Fork the upstream project only when ORBIT needs broad, sustained product-level changes.
7. Reimplement only when no compatible upstream exists, its license blocks use, its security model is unacceptable, or integration cost demonstrably exceeds a clean implementation.

Never choose rewrite as the default.

## Required source investigation

For every candidate:

- inspect repo tree, default branch, exact commit SHA and release status;
- inspect README, architecture docs, API/SDK, tests, build pipeline and security policy;
- inspect root and nested LICENSE/NOTICE/COPYING, SPDX headers, assets, models and prebuilt binary notices;
- inspect install scripts, telemetry, subprocesses, network egress, authentication and secret storage;
- identify package boundaries and dependency graph;
- build/test upstream at the pinned revision where practical;
- record exact file paths to reuse, adapt, wrap or reject;
- compare runtime, language, data model and deployment fit;
- assign a maintainer, rollback plan and update strategy.

## Import method selection

| Method | Use when | Required controls |
|---|---|---|
| Package dependency | Stable package/API is published | Exact version, lockfile, integrity hash, package provenance, license scan |
| Git submodule | ORBIT needs a pinned external checkout with upstream history | Pin commit, document update owner, CI checkout, security review |
| Git subtree | ORBIT needs a vendored source snapshot in one tree | Keep upstream remote, subtree merge workflow, source NOTICE and diff history |
| Fork | ORBIT will maintain a long-lived product-specific branch | Upstream sync cadence, patch queue, CODEOWNERS, tests, changelog, license policy |
| Selective vendoring | Only a few files/modules are needed | File-level license/provenance review, changed-file notices, dependency closure, original tests |
| External process/service | Separate runtime or heavy dependency is more stable | Authenticated narrow RPC, process limits, task-scoped secrets, health and cancellation |

Avoid copy/paste from rendered GitHub pages. Clone the exact commit and preserve the source file's history where possible. If copying files, include a `THIRD_PARTY_NOTICES.md` entry listing upstream repo, commit, paths, license, copyright and modifications.

## Patch policy

- Make minimal patches. Keep upstream code recognizable and avoid mass renames that destroy future mergeability.
- Keep ORBIT branding/configuration separate from upstream internals.
- Do not delete upstream license, attribution, security or copyright headers.
- Keep `patches/` or a documented commit range for every fork delta.
- Use one pull request/commit for each capability integration, not one unreviewable mega-merge.
- Add contract tests before changing behavior.
- Upstream updates must be tested against ORBIT's conformance suite before merge.

## ORBIT-specific exclusions

- OpenMausBot: exclude `enterprise/` unless separately licensed; retain root Apache-2.0, `NOTICE`, `LICENSING.md` and third-party notices. The upstream CLI onboarding documentation describes API keys in plaintext `config.json` (owner-only mode `0600` on Unix); the packaged desktop application documents OS-backed encryption where supported, and some login credentials use a separate sealed store. Audit each path independently and route all ORBIT credentials through its approved OS-backed/encrypted vault.
- OpenClaw: native plugins load in-process and are trusted code. Do not describe them as sandboxed. Isolate less-trusted extensions out of process.
- Hermes self-evolution: confirm MIT license text with rights holder; exclude AGPL Darwinian Evolver from ORBIT process/distribution unless an explicit legal review approves a separate CLI use model.
- VoltAgent skill index: catalogue license does not cover skill repositories it links to. Review every skill individually.
- Any `NOASSERTION`, custom, source-available, missing or incompatible license is blocked from redistribution until resolved.

## Required integration record

Each adoption PR updates `config/upstreams/upstream-lock.yaml`, component register, SBOM, NOTICE, license review, dependency lock, architecture ADR, integration contract tests, operational runbook and feature status.

## Coding agent execution protocol

Before coding, search for current code and tests. If an upstream already contains the capability, provide a short adoption comparison:

- upstream path(s) and commit;
- license and transitive dependency notes;
- current ORBIT equivalent (if any);
- import method;
- minimal adapter changes;
- tests to keep/add;
- security gaps and compensating controls;
- cost/latency/operational trade-offs;
- rollback method.

Then implement the smallest vertical slice. Do not create a new `XManager`, `XService`, `XRuntime` module if a suitable existing module can be wrapped and tested.
