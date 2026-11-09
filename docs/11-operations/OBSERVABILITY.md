# Observability

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Use OpenTelemetry-compatible traces, metrics and logs with one correlation context across API -> workflow -> worker -> provider/tool. Instrument task queue delay, task duration, model latency, first token, tool duration, browser failures, retries, approvals, cancellation, token/cost use, sandbox resource use, and error class.

Logs should be structured and redacted. Avoid prompt/file bodies and secrets by default. Traces must not include authorization headers or private content. Define dashboard and alert thresholds after collecting baseline traffic. Alert on task backlog, repeated worker failure, provider outage, unexpected cost spikes, security denials, storage failures and backup errors.

## Desktop observability

Capture device heartbeat, online/paused/revoked state, lease age/expiry, OS/session capability, driver/contract version, action latency, delivery classification, stale/ambiguous refusal, approval outcomes and redacted error codes. Do not log raw screenshot, clipboard text, full accessibility tree, passwords, tokens or arbitrary text fields. Trace IDs must connect task → gateway → broker → node → driver without embedding screen content.

## ORBIT v0.2 alignment

The v0.2 operations plan adds node offline, permission, driver version, unknown delivery and desktop data exposure runbooks. Never replay an uncertain mutation; see `DESKTOP_NODE_RUNBOOK.md`.

## v0.3 telemetry baseline

Use OpenTelemetry-compatible traces, metrics and logs behind an exporter abstraction. Propagate `trace_id`, `task_id`, `workspace_id` (pseudonymous where needed), `worker_id`, `backend_id` and `provider_request_id`. Do not record prompts, secrets, clipboard text, raw desktop snapshots or private file contents as span attributes. Reference: https://opentelemetry.io/docs/.


## v0.5 agent and upstream observability

Add task-level counters for success/postcondition accuracy, runtime backend, fallback reason, agent handoffs, skill version, connector errors, approvals, external side effects, delivery certainty and cost per successful task. Do not place raw prompt, memory, browser, desktop, file or credential content in traces. Provide user-visible task history and privacy-safe operational traces separately.

