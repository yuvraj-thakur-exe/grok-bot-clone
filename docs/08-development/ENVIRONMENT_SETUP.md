# Local development setup

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Prerequisites

Git; Docker Engine/Desktop with Compose; Node.js LTS compatible with the selected Next.js version; Python version pinned by the backend lockfile; package managers from repository policy. Exact versions must be selected and recorded during repository audit rather than guessed in advance.

## Expected local services

PostgreSQL with pgvector, Redis, MinIO/S3-compatible storage, Temporal (or chosen durable workflow engine), API, web app and workers. Provide a `.env.example` with safe placeholders and document which services are optional for basic chat.

## Setup flow (commands are placeholders until project code exists)

```bash
cp .env.example .env
# edit local, non-production values
 docker compose up -d postgres redis minio temporal
# install dependencies with the committed lockfiles
# apply database migrations
# start API, web and workers using documented package scripts
```

Never put real secrets in repository docs. The initial coding agent must reconcile commands with the actual package scripts and update this guide after the first vertical slice.

## ORBIT v0.2 alignment

The v0.2 implementation guidance requires a fake driver first, pinned upstream driver, fixed argv invocation, pairing/lease tests and local + central policy. See `AGENT_DESKTOP_INTEGRATION_GUIDE.md`.
