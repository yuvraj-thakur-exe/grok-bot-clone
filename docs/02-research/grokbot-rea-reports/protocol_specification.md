# GROKBOT-RE: Protocol Specification

- **Transport**: HTTP/1.1 with Server-Sent Events (SSE) and WebSockets.
- **Streaming Event Types**:
  - `event: token`: Text chunk for assistant response.
  - `event: tool_call`: Emitted when agent decides to execute a tool.
  - `event: tool_result`: Emitted upon tool completion with success flag and output.
  - `event: complete`: Final full message object with updated timestamp.
