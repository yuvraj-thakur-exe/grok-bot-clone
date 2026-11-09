# Research Method

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Competitor research
1. Start with official product/developer docs.
2. Label findings as documented, publicly observed, inferred or unknown.
3. Use authenticated access only when the user provides legitimate access.
4. Capture permitted public screenshots with URL/date/viewport/browser metadata.
5. Never bypass logins, subscriptions, CAPTCHA, rate limits or other access controls.
6. Do not inspect private endpoints or collect private user data.
7. Benchmark equivalent tasks with identical inputs/environment and independent verification.

## Technology research
Prefer official docs/release notes. Verify maintenance status, support matrix, license, security advisories and upgrade policy. Prototype high-risk dependencies. Record versions and dates in ADRs. Re-run compatibility checks on upgrades.

## Evidence labels
- **Verified:** official documentation or reproducible test supports claim.
- **Observed:** publicly visible behavior, not internal implementation.
- **Inferred:** plausible engineering conclusion, marked as inference.
- **Unknown:** not available or not investigated.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
