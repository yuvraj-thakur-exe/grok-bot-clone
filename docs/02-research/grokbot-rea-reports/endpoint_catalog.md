# GROKBOT-RE: Endpoint Catalog

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/status` | GET | Health, daemon PID, and uptime verification |
| `/api/boot-snapshot` | GET | Synchronous boot snapshot handshake |
| `/api/settings` | GET / POST | Configuration management (keys, permissions, MCP) |
| `/api/conversations` | GET / POST | Conversation lifecycle |
| `/api/conversations/:id` | GET / PATCH / DELETE | Thread retrieval and mutations |
| `/api/conversations/:id/messages` | GET | Historical message retrieval |
| `/api/chat/stream` | POST (SSE) | Server-Sent Events chat & tool streaming |
| `/api/daemon/exec` | POST | Sandboxed command execution over gateway |
