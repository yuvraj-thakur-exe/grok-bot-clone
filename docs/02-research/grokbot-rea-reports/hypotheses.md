# GROKBOT-RE: Hypotheses & Inferences

The following technical deductions are strongly supported by structural patterns, naming conventions, and published specifications, but represent technical inferences rather than decompiled source facts:

## 1. Local Daemon vs Cloud Execution Partitioning
- **Hypothesis**: The client application delegates tasks requiring remote web navigation, long-running batch processing, and non-local container workflows to the persistent cloud computer (`api2.cursor.sh` / cloud backend). When explicit local tasks are requested (terminal execution in a local repo, local file editing, or local MCP servers), the UI routes commands through the local execution gateway (`local-exec-daemon`).
- **Support**: `local-exec-daemon.log` shows the daemon serving local execution over a local gateway with `EPERM` discovery fallbacks; `local-computer-use-gate.json` exists as a specific gate for local desktop automation.

## 2. Multi-Agent Coordination Protocol
- **Hypothesis**: `node-agent-coordinator` functions as a local coordinator for multiple parallel agents ("Bots"), inter-agent communication, and scheduling, acting as the client-side broker for task decomposition and handoffs.
- **Support**: Identified coordinator RPC strings include `agent-exchange`, `agent-meetings`, `agents-automation`, `agents-todos`, and `agent-tasks`.

## 3. WebAuthn Proxy & Enterprise Security
- **Hypothesis**: The binary `sand-webauthn-signer.exe` acts as a secure local cryptographic broker for FIDO2/WebAuthn hardware tokens and passkeys, allowing the agent to authenticate against cloud resources without exposing raw private keys to JavaScript runtime heaps.
- **Support**: Observed `webauthnProxyEnabled: true` in `settings.json`, and presence of signed `sand-webauthn-signer.exe` in `app.asar.unpacked/dist/native/`.

