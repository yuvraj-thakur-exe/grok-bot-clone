# ORBIT v1.0 package validation

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

**Scope:** 321 archive files (265 Markdown, 14 Mermaid diagrams, 15 YAML, 10 JSON outside the manifest), 50 pinned upstream repositories, source reuse/register, product/architecture/security docs, 30 role charters, 500 GB storage instructions, repo operations scripts, 19 isolated regression tests and package manifest. This does not validate or claim integration of the ORBIT application runtime.

## Automated checks

- JSON and YAML syntax, Markdown fence balance and local-link resolution.
- Current baseline marker on every non-source Markdown document.
- Original user-provided source files match immutable SHA-256 digests.
- YAML lock, JSON lock and source reuse register contain the same 50 IDs/commit pins.
- Every clone target directory matches its canonical lock ID; selectors exist for all v1.0 projects.
- OpenMausBot sparse checkout excludes `enterprise/`.
- Repository acquisition does not install dependencies or execute upstream scripts.
- Import helper checks exact origin/commit and per-file SHA-256, refuses symlinks/path escapes/secret-like files.
- Apply helper checks reviewed manifest digest, lock provenance, hashes, clean feature worktree and non-overwrite; it never git-adds/commits/merges/pushes.
- Storage and app worktree helpers use temporary test directories; physical 500 GB disk is not modified.
- Python operation regression suite, Bash syntax and PowerShell wrapper static checks.
- Manifest inventory hashes match the package; ZIP integrity checked before and after extraction.

## What is not verified

- Actual ORBIT app source is not included and has not been audited or changed.
- Upstream application builds and dependencies have not been executed in this environment.
- PowerShell wrapper is statically inspected; run it on the intended Windows workstation after Git Bash is installed.
- Static repository scan is not malware scanning or legal clearance.
- Disk initializer does not format, partition, encrypt, mount or enforce quotas.
- Local model performance cannot be estimated from 500 GB disk size alone.

## Human acceptance required

1. Verify actual physical disk identity/capacity and initialize only the intended drive.
2. Supply the real ORBIT application Git repository and run the read-only audit.
3. Pick one product shell and one agent runtime after tests and license/security review.
4. Build selected upstreams in isolated worktrees; approve dependency and model terms.
5. Validate user-data consent, context isolation, OAuth scopes, external-action approvals, restore and incident response.
6. Human founder/maintainer approves legal acceptance, production credentials and release.
