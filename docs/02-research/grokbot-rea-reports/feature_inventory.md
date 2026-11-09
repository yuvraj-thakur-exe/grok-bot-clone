# GROKBOT-RE: Comprehensive Feature Inventory

| Category | Feature Name | Description | Verification Status |
|---|---|---|---|
| **Chat & Messaging** | Streaming Responses | Real-time token streaming using Server-Sent Events / ConnectRPC | Verified |
| **Chat & Messaging** | Rich Prompt Editor | Tiptap-powered editor with auto-resize, mentions, link pasting, and shortcuts | Verified |
| **Chat & Messaging** | Mathematical Notation | KaTeX math block and inline rendering | Verified |
| **Chat & Messaging** | Code Highlighting | Syntax highlighting with copy, language badge, and execution status | Verified |
| **Model Integration** | Multi-Model Support | Grok-2, Grok-2 Vision, Grok-3, Claude 3.5 Sonnet, GPT-4o compatibility | Verified |
| **Model Integration** | Dynamic Switching | Model selector dropdown with token/context limits and capability badges | Verified |
| **Agent Capabilities** | Local Execution Daemon | Background daemon running shell commands (PowerShell, bash, cmd.exe) | Verified |
| **Agent Capabilities** | Workspace Sandboxing | File system boundaries (workspace_readwrite, workspace_readonly) | Verified |
| **Agent Capabilities** | Model Context Protocol | Full MCP server support (`mcpBoxServers`, tool discovery, elicitation) | Verified |
| **Agent Capabilities** | Screen & Window Capture | Region selection and active window capture via `capture-overlay.html` | Verified |
| **Agent Capabilities** | Desktop Mount Panel | Floating composer widget mounted directly on desktop (`panel.html`) | Verified |
| **UI & UX** | Conversation History | Left sidebar with searchable threads, pin, delete, export | Verified |
| **UI & UX** | Multi-Tab / Popout | Detachable agent popout windows (`sandPopout`) | Verified |
| **UI & UX** | Settings Management | Model configuration, local egress toggles, MCP servers, WebAuthn proxy | Verified |
| **UI & UX** | Theme System | System, Light, Dark themes with customizable bot accent colors | Verified |
| **Security** | OS Secret Storage | Encrypted keys and tokens via DPAPI / `sand-secrets.json` | Verified |
| **Security** | WebAuthn Authentication | Passkey hardware authentication via `sand-webauthn-signer.exe` | Verified |
