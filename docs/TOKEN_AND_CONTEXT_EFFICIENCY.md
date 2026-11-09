# ORBIT context and token efficiency

## Main principle

Reduce repeated input, not essential evidence. Token savings that remove tests, constraints, source citations or security context are false economy.

## Current toolkit implementation

`context-pack` creates deterministic Markdown and a JSON manifest. It records path, size, SHA-256, redaction count and approximate token cost. It excludes common build/cache directories, credential-oriented paths, `.env` files, key material and binary assets. It supports a configurable budget and max file size.

The estimator is deliberately labelled approximate. Character-count heuristics are not a replacement for the exact tokenizer used by a selected model.

## Production context planner backlog

1. Repository map: maintain a compact symbol/file index keyed by Git commit and file hash.
2. Change-aware retrieval: include changed files, direct imports/callers, interface contracts, nearest tests and relevant ADRs.
3. Task profiles: distinct profiles for architecture, coding, review, bug triage, research and release.
4. Context provenance: attach path, revision, digest, line range and trust class to every chunk.
5. Deduplication: do not resend identical stable content within a task; retain source IDs and version hashes.
6. Progressive disclosure: load summaries/index first, then exact source ranges as needed.
7. Evidence preservation: do not compress away citations, version numbers, error messages, security requirements or acceptance criteria.
8. Cache invalidation: invalidate on content hash/commit/permission change, not merely on filename.
9. Provider-aware budget: use the exact provider tokenizer or token-count API; reserve output and tool-call budget separately.
10. Privacy: do not place secrets, private user files or desktop/browser payloads in shared global caches.

## Model routing

Classify task complexity and required capabilities before provider selection. Track model, provider, input/output token usage, latency, estimated/actual cost, retry reason and fallback reason. Never silently replace a requested reasoning, vision, tool-use or privacy capability with a weaker model.

## Caching

Cache deterministic operations (file hashes, repository metadata, parsed documents, static analysis keyed by commit, reusable search results with expiry). Do not cache permission decisions, expiring approval grants, one-time tokens, private desktop observations or mutable account balances as authoritative state.
