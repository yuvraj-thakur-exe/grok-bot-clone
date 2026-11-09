# Memory and retrieval architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Separate memory from evidence

Conversation summaries and user-approved preferences are memory. Uploaded documents, retrieved web pages and repository files are evidence. Memory must never be treated as current external truth. Each memory stores origin, subject, scope, confidence, created/updated/expiry times, and consent/retention metadata.

## Memory classes

- User preference (explicit or user-approved).
- Agent configuration and workflow context.
- Workspace/project context.
- Task summary and decisions.
- Episodic history (bounded retention).

Sensitive personal data is excluded by default unless a lawful product need and explicit consent policy are defined. Users can inspect, correct, export and delete memory.

## Retrieval flow

Authorize scope -> lexical/vector/hybrid retrieve -> apply ACL filters before ranking -> rerank if enabled -> include source provenance -> build bounded context -> generate answer -> validate citation coverage. Cross-workspace retrieval is forbidden.

## Chunking and embeddings

Version parser, chunker and embedding model. Preserve page/section offsets and original artifact references. Embeddings are derived and rebuildable. Evaluate recall and precision on a curated dataset before replacing retrieval configuration.

## Prompt injection

Retrieved content is data, not instruction. System policy and tool permissions stay outside retrieved text. Quote/label untrusted regions and require an independent policy check before tool use.

## ORBIT v0.2 alignment

The v0.2 agent architecture adds a native desktop observe-act-verify loop with ephemeral refs, completeness checks, delivery-aware recovery and UI prompt-injection defense. See `DESKTOP_AGENT_LOOP.md`.


## v0.5 memory provider rule

Mem0 and Letta are candidates behind one `MemoryProvider` contract, not simultaneous memory authorities. ORBIT owns consent, scope, source provenance, expiry, correction, export and deletion. Vector indexes are derived; deletion and ACL changes propagate to caches, embeddings and summaries.

