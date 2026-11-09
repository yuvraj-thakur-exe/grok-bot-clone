# Git and release workflow

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

- Start from a clean branch; do not overwrite user changes.
- Use feature branches and reviewed pull requests.
- Protect the main branch with CI, review and signed release/tag policy where practical.
- Commit in small logical units with clear messages.
- Never commit `.env`, credentials, browser profiles, uploads, local databases, build output or customer data.
- Run secret scanning and dependency review before merge.
- Use lockfiles and repeatable builds.
- Tag releases with release notes, migration notes and known issues.
- Publish an SBOM and artifact checksums for public binaries/images.
- Have rollback and database migration compatibility plans before production release.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
