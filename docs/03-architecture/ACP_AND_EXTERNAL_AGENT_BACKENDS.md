# ACP and external agent backends

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Goal

Permit ORBIT to delegate tasks to external coding-agent runtimes without coupling the core task engine to one vendor or agent product.

## Contract boundaries

- `AgentBackend` is ORBIT's interface; ACP is an optional transport/protocol adapter when supported by the external agent.
- ORBIT remains responsible for user/workspace identity, policy, budget, approvals, task persistence and artifact ownership.
- Each backend advertises a versioned capability manifest and emits normalised task events.
- Backends receive only task-scoped workspace credentials and minimum necessary context.
- File transfer is explicit and logged. Avoid implicit sharing of a user's home directory.
- Cancellation and disconnect semantics must be tested; a backend that cannot reliably cancel must be treated as non-cancellable with explicit UI disclosure.

## Backend types

1. Local CLI agent in disposable worktree/container.
2. Local agent server behind loopback/IPC.
3. Remote container or VM agent server.
4. Cloud-managed external agent provider.
5. User-owned ACP-compatible agent.

## Security requirements

- mTLS or short-lived signed credentials for remote backends.
- Per-backend trust policy and allowed outbound destinations.
- No shared long-lived token between tasks.
- No backend may request broad host mounts or Docker socket access as a default.
- Agent event text is untrusted data and may contain prompt injection.
- External backend usage, data processors and residency are disclosed to the user.
- Never silently switch a task to a different processor/backend.

## Reference lesson

The current OpenHands repository README describes Agent Canvas and local, remote, container and cloud agent backends, with ACP as a route for interoperable agents. ORBIT should adopt the abstraction and preserve independent product ownership; it should not reproduce a third-party interface or brand.
