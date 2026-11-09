# ORBIT v1.0 open-source additions and exclusions

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Six additional pinned repositories

- Google ADK Python (Apache-2.0): compare typed worker/tool/eval patterns with Pydantic AI and Microsoft Agent Framework.
- OpenAI Codex (Apache-2.0): study CLI coding worker, patch lifecycle, SDK and worktree behavior. Review `NOTICE` and nested third-party code.
- Gemini CLI (Apache-2.0): compare terminal-agent extension and tool patterns; integrate only behind a worker adapter.
- OpenSearch (Apache-2.0): consider only if Postgres full-text plus one selected vector backend fail retrieval benchmarks; its operating cost is material.
- SWE-agent (MIT): candidate issue-to-patch worker and SWE benchmark. The pinned revision is older than other v1.0 additions, so verify maintenance and advisories before adoption.
- FAISS (MIT): vector ANN library for local retrieval comparisons; it is not a drop-in distributed database replacement for Qdrant/Milvus.

## Sources considered but not promoted

- Microsoft AutoGen repository metadata showed CC-BY-4.0; this is not treated as an approved code dependency in this pack. Its current successor/recommended direction must be verified separately before consideration.
- Langfuse repository reports `NOASSERTION` at the inspected API surface and has license/feature conditions to inspect; it is not silently approved by this catalogue.
- Weaviate repository metadata returned `NOASSERTION` in the inspection, so no adoption pin was added.
- Firecrawl and other hosted/browser scraping vendors may add service terms, usage charges and egress implications; evaluate only for a concrete need.
- The 50-project list is already larger than a realistic initial build selection. More repos do not automatically increase product capability.

## Decision policy

Pin exact commits; classify repository root license; review nested code, assets, dependencies, model/data weights and trademarks; inspect security advisories; identify the precise code paths; run source-specific tests; integrate via adapter; record owner and sync plan. A `NOASSERTION`, nonstandard, source-available or unclear license means stop and request legal review before copying.
