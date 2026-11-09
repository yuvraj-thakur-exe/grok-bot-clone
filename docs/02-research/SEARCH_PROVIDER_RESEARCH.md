# Search provider strategy: DuckDuckGo and alternatives

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Review date:** 08 November 2026. This is a design recommendation, not an assertion that DuckDuckGo offers a supported general-purpose API for all result types.

## DuckDuckGo findings

Official DuckDuckGo help pages describe a consumer search product with traditional links, Instant Answers and multiple specialized modules. DuckDuckGo says many traditional organic links are sourced from Bing, while Instant Answers can draw from many sources and its own indexes. Search Assist is an optional AI-generated summary with links to one or two sources. The public material reviewed here describes the search experience, not a guaranteed, supported full web-search API contract for third-party agent platforms.

## ORBIT adapter plan

- Provide `DuckDuckGoBrowserSearchAdapter` as an optional browser-based adapter that opens the public search UI and extracts visible results where access and terms permit. Treat it as fragile, rate-limited and potentially changeable; add contract/health tests and a user-visible fallback.
- Do not treat Instant Answer output as a full search index or sole evidence for consequential research.
- Prefer supported search APIs/providers for production SLA, structured pagination, predictable quotas and stable terms.
- Add provider metadata and a source-quality score; never conflate search ranking with factual credibility.
- Respect robots directives, website terms, rate limits and privacy constraints. Do not bypass bot checks, CAPTCHA, login walls or other access controls.

## Research provenance

DuckDuckGo: https://duckduckgo.com/duckduckgo-help-pages/results/sources
DuckDuckGo Instant Answers: https://duckduckgo.com/duckduckgo-help-pages/features/instant-answers-and-other-features
DuckDuckGo Search Assist: https://duckduckgo.com/duckduckgo-help-pages/results/ai-assisted-answers

## Recommendation

Support DuckDuckGo as one adapter in a provider portfolio, not as a hard dependency and not as an undocumented “free API”. Verify current access method, terms, rate limits and reliability during implementation. Search results must be independently fetched, parsed, dated and cited.

## Separation from native desktop driver

DuckDuckGo and other search adapters are part of the research subsystem. `agent-desktop` is not a search provider and does not replace browser navigation or Playwright page extraction. Keep search, page browsing, native desktop control and shell execution as separate tool families with separate security controls.

## ORBIT v0.2 alignment

The v0.2 research baseline includes the public `vercel-labs/agent-desktop` source review. Treat verified repository facts separately from ORBIT proposals; see `AGENT_DESKTOP_REFERENCE_ANALYSIS.md` and `RESEARCH_REFERENCES.md`.
