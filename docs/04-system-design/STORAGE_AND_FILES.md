# Storage and file intelligence design

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Storage tiers

- PostgreSQL: metadata, ownership, processing states, permissions, checksums, provenance.
- S3-compatible object storage (MinIO locally): original uploads, derived text, exports, screenshots and generated artifacts.
- Redis: ephemeral cache and short-lived coordination only.
- pgvector: embeddings linked to source chunks and ACL metadata.

## Upload pipeline

1. Authenticate and authorize workspace upload.
2. Enforce size, count, extension and media-type limits.
3. Inspect actual file signature; do not trust extension or browser MIME.
4. Compute SHA-256 and create quarantine object.
5. Run malware scanning where available; mark scan status explicitly.
6. Parse in a constrained worker with CPU/memory/time limits.
7. Extract text/tables/pages with source offsets and page numbers.
8. Chunk and embed with recorded model/version.
9. Mark indexed only after all expected stages succeed.

## Retrieval and citations

Every chunk stores artifact ID, page/section, byte/text offsets, content hash, workspace ACL, parser version, and ingestion timestamp. Responses must cite actual retrieved chunks. If a file is not parseable, say so rather than inventing its contents.

## Security and retention

Reject path traversal, decompression bombs, oversized archives, polyglot files and unsupported executables. Never execute uploaded files automatically. Use short-lived signed download links scoped to one object. Apply deletion to originals, text, chunks, vectors, caches and derived artifacts according to policy.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
