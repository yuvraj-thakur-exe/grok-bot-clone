# GROKBOT-RE: Unknowns & Investigation Boundaries

The following areas cannot be verified without unauthorized reverse engineering of protected endpoints, proprietary remote infrastructure, or decompilation of protected native binaries:

## 1. Remote Cloud Container Architecture
- **Unknown**: The internal virtualization technology used for the remote cloud computers (e.g. Firecracker microVMs, gVisor containers, or Kubernetes pods).
- **Status**: Boundary respected. We treat the cloud computer as an abstracted, persistent execution environment reachable over secure APIs.

## 2. Proprietary xAI Model Weights & Training
- **Unknown**: The internal neural architecture, training checkpoints, or proprietary inference parameters of Grok-2/Grok-3 models hosted behind xAI endpoints.
- **Status**: Boundary respected. Independent reconstruction uses standard OpenAI-compatible and Anthropic-compatible API interfaces, allowing pluggable external model providers or local LLMs.

## 3. Remote Encryption Key Hierarchy
- **Unknown**: The specific hardware security module (HSM) key rotation schedule on Anysphere/Cursor authentication servers.
- **Status**: Out of scope for independent client reconstruction.

