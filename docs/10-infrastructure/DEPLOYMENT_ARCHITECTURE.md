# Deployment architecture

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Initial deployment topology

For the first self-hostable release, use Docker Compose for one-host deployment: reverse proxy/TLS termination, web app, API, workflow engine, worker pools, PostgreSQL, Redis, object storage, and telemetry collector. Keep browser and code workers on isolated networks with explicit egress policy. Do not expose database, Redis, MinIO admin or worker control ports publicly.

## Environments

- Local: mock providers and synthetic data.
- Development: shared non-production services and test credentials.
- Staging: production-like topology, synthetic/scrubbed data.
- Production: secrets manager, TLS, backups, network policy, monitoring, alerting, controlled release and rollback.

## Scale path

Split worker pools and stateless API replicas before decomposing control-plane modules into microservices. Kubernetes is not an MVP requirement. Adopt it only when multi-host scheduling, availability, isolation or operational needs justify its cost. High-risk code execution may require a separate VM/microVM worker pool.

## Local Desktop Node is not a cloud service

The Local Desktop Node is installed separately on the user's machine and runs in their interactive session. Cloud deployment hosts the broker and policy services only. Do not package the node into a generic backend container and assume it can control a user's desktop. Use dedicated interactive test hosts for desktop CI, with fake driver for standard CI.

## ORBIT v0.2 alignment

The v0.2 deployment topology keeps the Local Desktop Node on the user’s interactive host; the cloud control plane only brokers authenticated leased tasks. See `DESKTOP_NODE_DEPLOYMENT.md`.
