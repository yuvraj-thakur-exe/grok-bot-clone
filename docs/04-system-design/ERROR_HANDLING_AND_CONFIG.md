# Error handling and configuration

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## Error taxonomy

Classify failures as validation, authentication, authorization, policy, provider, network, timeout, capacity, parsing, execution, consistency, or internal. Each error has a stable machine code, safe user message, request/task correlation ID, retryability flag, and operator diagnostics. Do not return raw stack traces or secret-bearing provider responses to clients.

## Retry policy

Retry only transient and idempotent operations. Provider `429` uses provider retry hints and bounded backoff. Authentication, policy denial, invalid input, and malformed tool arguments are not retryable without a change. For external writes, require an idempotency key or pause for review if duplicate effects are possible.

## Configuration layers

1. Secure process environment / secret manager.
2. Deployment-level validated configuration.
3. Workspace policy and provider configuration.
4. Agent-level defaults.
5. Task-level overrides allowed by policy.

More specific settings may not weaken security policy. Validate configuration at startup and expose a redacted diagnostics endpoint. Feature flags must be server-side enforced. `.env.example` contains names and safe placeholders only.

## Resilience

Apply timeouts and circuit breakers per provider/tool. Bound request sizes and concurrency. Provide graceful shutdown for workers. Do not silently discard task events or approval states. Health endpoints distinguish liveness from readiness and dependency health.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
