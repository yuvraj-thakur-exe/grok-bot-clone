# GROKBOT-RE: Behaviour Specification

- **Startup Behaviour**: Evaluates settings and local workspace directory; establishes synchronous boot handshake (`sand:boot-snapshot-sync`).
- **Streaming Behaviour**: Progressive token rendering with chunk coalescing.
- **Error Recovery**: Automatically catches provider errors and gracefully switches to local agent reasoning engine without interrupting session state.
- **Offline Mode**: Operates fully offline using built-in system tools and local engine when network is disconnected.
