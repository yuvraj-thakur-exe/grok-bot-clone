# Backup and recovery

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Back up PostgreSQL with point-in-time recovery where supported and object storage with versioning/replication according to the selected deployment. Protect encryption keys separately. Redis is cache and should be rebuildable. Document RPO/RTO only after selecting infrastructure and measuring restore time.

Quarterly minimum recovery drill: restore database and object storage to an isolated environment, verify metadata/object hashes, confirm workspace isolation, run application smoke tests, and document measured RPO/RTO. Include a key-loss/revocation scenario. A backup that has never been restored is an optimistic file collection, not a recovery strategy.

## ORBIT v0.2 alignment

The v0.2 deployment topology keeps the Local Desktop Node on the user’s interactive host; the cloud control plane only brokers authenticated leased tasks. See `DESKTOP_NODE_DEPLOYMENT.md`.
