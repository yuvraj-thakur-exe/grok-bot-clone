# GROK BOT REA — Comprehensive Reverse-Engineering & Architecture Audit

**Target:** `d:\orbit\grok bot rea`  
**Inspected Version:** Grok Bot v0.79.3 / 0.78.1 (`sand`)  
**Publisher:** SpaceXAI / Anysphere  
**Audited Date:** 2026-11-09

---

## 1. Executive Summary

A comprehensive inspection of [`d:\orbit\grok bot rea`](file:///d:/orbit/grok%20bot%20rea/) confirms that Grok Bot is built on Anysphere's desktop agent platform (internal codename `sand`). It directly shares low-level device control, process listing, and native execution libraries with Cursor, while providing an independent autonomous multi-agent experience.

Crucially, **Grok Bot's internal client layer is explicitly named `@anysphere/orbit-client`**, confirming direct architectural alignment with ORBIT's core mission.

---

## 2. Directory Layout & Artifacts in `grok bot rea`

```
d:\orbit\grok bot rea\
├── Grok_Bot_0.78.1_Setup.exe            # Official 124.7 MB Windows installer
├── extracted_original\                  # Unpacked distribution files
│   ├── dist/electron-main/              # main-core.cjs & main-app.cjs
│   └── dist/renderer/assets/            # 716 component chunks (TipTap, StyleX, D3, Three.js)
├── GrokBot-App\                         # Standalone executable workspace with Grok Bot.exe
│   └── launch_grokbot.bat               # Standalone launch wrapper
├── grokbot-re\                          # 19 research reports & analysis test scripts
│   ├── research/                        # Architecture, IPC, protocol, and cloud reports
│   └── scripts/                         # Deep analyzer, packaging, and test runners
├── .grokbot\                            # Local state, session tokens, and feature gates
│   └── settings.json                    # Account scopes, MCP box servers, and egress gates
├── package.json                         # Complete internal package manifest (131 dependencies)
├── inspect_grok_core.js                 # IPC and sand event scanner
├── inventory_renderer_features.js       # Renderer module categorization script
└── analyze_editor.cjs                   # TipTap prompt editor and mention scanner
```

---

## 3. Key Reverse-Engineered Findings

### A. Internal Package Manifest (`package.json`)
The application is structured around Anysphere's workspace packages:
- **Core Orchestration**: `@anysphere/agent`, `@anysphere/agent-core`, `@anysphere/agent-exec`, `@anysphere/grok-bot`, `@anysphere/grok-bot-harness`
- **Internal Client Engine**: `@anysphere/orbit-client`
- **Persistent Computer & Daemon**: `@anysphere/local-exec`, `@sand/local-exec-daemon`, `@sand/local-exec-protocol`, `@anysphere/shell-exec`
- **Browser Automation**: `@anysphere/sand-playwright-runtime`, `@anysphere/browser-smoke`
- **Conversational Voice**: `@anysphere/voice-call-harness`
- **Tool Protocol**: `@anysphere/mcp-agent-exec`, `@anysphere/mcp-core`
- **Streaming RPC**: `@connectrpc/connect`, `@connectrpc/connect-node` (ConnectRPC over HTTP/2 and WebSockets)
- **UI Framework**: React, Meta's `@stylexjs/stylex` (CSS-in-JS), `@tanstack/react-query`, Framer `motion`
- **Rich Text / Prompt Editor**: TipTap (`@tiptap/core`, `@tiptap/react`, `@tiptap/extension-mention`)

### B. IPC & Process Architecture
1. **Main Process (`main-core.cjs` / `main-app.cjs`)**:
   - Primary synchronous handshake: `sand:boot-snapshot-sync`
   - Background coordinator: `sand:coordinator-port-request` & `sand:coordinator-port` (MessagePort)
   - Image offload: `sand:encode-png`
2. **Local Daemon (`local-exec-daemon`)**:
   - Background daemon serving local shell executions (PowerShell, Bash, CMD) over a localhost gateway.
   - Protected by `local-exec-daemon.json` (pid, lease, filesKeyId).
   - Confirmed active in `local-exec-daemon.log`: `[sand-local-exec-daemon] started; serving local exec over the gateway`.
3. **Prompt & Mention System (`analyze_editor.cjs`)**:
   - Multi-entity mentions using `@`:
     - `@agent` (individual specialist bot)
     - `@group` (collaborative teams)
     - `@everyone` (broadcast to all agents)
     - `@person` (human collaborators)
     - `@skill` (attaching reusable taught workflows)
   - Interactive canvas referencing (`canvas-reference`, `canvas-selection`, `data-source-file`).

---

## 4. Mapping Grok Bot to GBC / ORBIT on Antigravity

| Grok Bot Mechanism | Proprietary Implementation | GBC / ORBIT Clean-Room Alternative |
| :--- | :--- | :--- |
| **IDE & Host Platform** | Cursor / Anysphere Host | **Google Antigravity IDE** (`antigravity_platform/`) |
| **Local Daemon** | `sand-local-exec-daemon` | **`antigravity_bridge.py`** + Sandboxed Process Runner |
| **Browser Runtime** | `@anysphere/sand-playwright-runtime` | **Playwright + Stagehand** |
| **Voice Harness** | `@anysphere/voice-call-harness` | **`OmniVoice`** (`k2-fsa/OmniVoice`) |
| **RPC Streaming** | ConnectRPC (`@connectrpc/connect`) | FastAPI / Express WebSockets & SSE |
| **Prompt Editor** | TipTap + StyleX with `@` mentions | React 19 + TipTap + Tailwind CSS |
| **Persona System** | `@anysphere/grok-bot` personas | **OpenGrokBot + ORBIT 30-Role Workforce** |
| **Memory** | `@anysphere/agent-kv` | **Mem0 + PostgreSQL / pgvector** |
| **Tool Execution** | `@anysphere/mcp-agent-exec` | **Antigravity MCP (`.antigravity/mcp_config.json`)** |

---

## 5. Next Steps for Implementation

1. **Adopt TipTap Mention Architecture**: Implement `@agent`, `@skill`, and `@group` mentions in our frontend chat composer.
2. **Implement Local Execution Daemon Protocol**: Wire `antigravity_bridge.py` to handle the standard `sand` daemon message schema (`type: exec`, `permission: workspace_readwrite`, stdout/stderr streaming).
3. **Connect OpenGrokBot UI to Antigravity**: Use OpenGrokBot's React 19 UI with our 30-role persona catalog and Antigravity tool executor.

