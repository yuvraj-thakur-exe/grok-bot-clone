# Web research engine

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Components

Query planner; provider adapters; fetch scheduler; URL policy/SSRF guard; page extractor; source normalizer; freshness and provenance store; claim/evidence graph; conflict checker; citation renderer; report generator.

## Source record

Store URL, final URL, page title, publisher/domain, published and updated dates when available, fetched-at timestamp, content hash, content type, extraction method/version, HTTP status, source tier, robots/access result and canonical citation metadata. Avoid storing unnecessary full page content where rights/retention do not permit it.

## Pipeline

Clarify task scope -> generate diverse queries -> retrieve multiple independent sources -> deduplicate canonical URLs -> fetch within URL/e­gress policy -> extract content and dates -> assess source type/authority/relevance -> extract claims with source locators -> compare contradictory claims -> verify high-impact claims against primary sources -> draft answer with citations -> mark gaps/uncertainty.

## Quality rules

- Search ranking is not credibility.
- Prefer primary documentation for implementation facts and laws/policies.
- Report publication date separately from event date.
- Distinguish direct observation, source statement and inference.
- Do not fabricate citations or claim a page was visited when only a search snippet was seen.
- When sources conflict, show disagreement and the evidence quality.
- For time-sensitive information, refresh and record retrieval time.

## Security

URL fetches pass SSRF protections; HTML is untrusted content; scripts are not executed; downloads are quarantined. Browser-based search must not bypass login or anti-bot checks. Citations reference saved source records, not model-generated URLs.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.
