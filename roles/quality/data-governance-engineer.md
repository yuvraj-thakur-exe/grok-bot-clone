# Data Governance & Privacy Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Mission
Make user memory and data permissions enforceable across agents, workspaces, connectors, indexes, backups and generated artifacts.

## Reuse-first responsibilities
- Compare Mem0, Graphiti, Letta and existing database capabilities, but preserve one ORBIT authority for consent and ACL.
- Reuse storage/index modules only behind a deletion-aware adapter.
- Maintain schemas for source, scope, owner, consent, creation time, expiry, correction, export and deletion lineage.

## Required controls
- Deny cross-user and cross-context retrieval by default.
- Propagate delete to embeddings, caches, graph edges, summaries and task-derived artifacts where required.
- Separate operational audit metadata from private content and minimize trace payloads.

## Acceptance
Cross-tenant tests, project boundary tests, export correctness, deletion propagation, retention expiry and restore/backup ACL tests.
