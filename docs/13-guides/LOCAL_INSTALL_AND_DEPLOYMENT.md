# Installation and deployment guide (target state)

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

The repository code has not yet been audited, so this is a target-state outline rather than a verified command sequence.

1. Install the pinned Node.js, Python, Git and Docker versions chosen in the repo.
2. Clone the ORBIT repository and inspect `README.md` and `AGENTS.md`.
3. Copy `.env.example` to `.env`; configure local mock provider first.
4. Start PostgreSQL, Redis, MinIO and the workflow engine through Compose.
5. Apply Alembic migrations.
6. Install frontend/backend dependencies from lockfiles.
7. Start API, web, and worker processes using actual committed scripts.
8. Run health checks, unit/integration tests and E2E smoke test.
9. Configure one provider key only in local secret storage for live inference.
10. Before production, configure TLS, secret manager, isolated worker network, backups, monitoring and security review.

Update this guide after the first executable baseline is committed. Do not publish unverified commands as tested setup instructions.

## ORBIT v0.2 alignment

The v0.2 guide set adds a Local Desktop Node setup target. Treat it as planned until code, installers and OS tests exist; see `DESKTOP_NODE_QUICKSTART.md` and `FEATURE_STATUS.md`.
