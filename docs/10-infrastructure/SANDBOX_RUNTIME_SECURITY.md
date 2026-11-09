# Sandbox runtime security and lifecycle

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Runtime interface

`SandboxProvider` exposes create, inspect, execute, stream logs, read/write files, pause, resume, checkpoint, destroy and health methods. Each request has tenant/workspace/task identity, runtime profile, resource quota, image digest, network policy and expiry.

## Lifecycle state machine

`requested → policy_checked → provisioning → ready → running → pausing/paused → resuming → completed/failed/cancelling → destroyed`.

No untrusted task enters `running` before policy, image digest, mount list, egress and secrets have been validated.

## Security defaults

- Disposable environment per task or narrowly scoped session.
- Non-root user, read-only base image, bounded writable volume, CPU/memory/PID/ephemeral-storage limits.
- No host Docker/container runtime socket, host PID/network namespace, privileged mode or broad host mount.
- Egress deny by default; allowlist destinations and ports at network layer.
- Credential broker stays outside guest; secrets are never baked into images, env dumps, command args or snapshots.
- Artifact upload scans file type, size, archive depth, malware and path traversal.
- Cancellation kills descendants and revokes credentials/leases.
- Destroy removes ephemeral volumes, session cookies and scratch credentials unless retention explicitly requires artifact export.

## OpenSandbox evaluation

OpenSandbox is an adapter candidate for common lifecycle API and local Docker-to-Kubernetes deployment. Its credential vault and egress sidecar patterns are relevant. The ORBIT team must validate exact release versions, CNI/network enforcement, fail-closed behavior, sidecar trust, SDKs and restore behavior. Firecracker/high-density runtime is a later stage requiring KVM-capable infrastructure and independent security review.

## Failure tests

- Worker killed during task.
- Scheduler restart with active lease.
- Egress service unavailable.
- Credential vault unavailable or stale.
- Sandbox paused/resumed after credential rotation.
- File path traversal and symlink escape attempts.
- DNS rebinding/direct-IP/IPv6 bypass attempts.
- CPU/memory/PID exhaustion.
- Malicious archive and oversized response.
- Concurrent tasks attempting to access each other's workspace.
