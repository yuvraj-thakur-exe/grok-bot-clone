# GROKBOT-RE: Research Report 06 — Product Experience & Interaction Specifications

## 1. Visual Design & Shell Characteristics
- **Theme**: High-contrast dark theme (`#0d0d0f` background, `#16161a` surface, `#2a2b36` border).
- **Accents**: SpaceXAI Orange (`#ff5c00`) brand mark; user-customizable bot accent colors (persisted via `botColorInChatEnabled`).
- **Typography**: Clean sans-serif for UI (`Inter`), monospace for code and logs (`JetBrains Mono`).

## 2. Screen & Window Map
1. **Primary Workspace Window**:
   - Header: Brand avatar, version badge (`0.78.1`), Model Selector dropdown (Grok 2, Grok 3, Claude 3.5, GPT-4o, Local), Daemon Status indicator, Capture shortcut, Desktop Mount toggle, and Settings.
   - Left Sidebar: New Chat button, Conversation Search, Pinned & Recent threads, Workspace directory path.
   - Message Thread: Progressive token streaming, collapsible tool execution cards (`ToolCallCard`), KaTeX math rendering, and copyable code blocks.
   - Prompt Composer: Auto-expanding textarea, file attachments, and capture triggers.
2. **Desktop Mount Quick-Input Panel (`panel.html`)**:
   - Floating widget docked to desktop.
   - Allows typing instant commands and triggering window captures without opening the full window.
3. **Screen Capture Overlay (`capture-overlay.html`)**:
   - Transparent fullscreen view activated via `Alt+Shift+Space`.
   - Allows clicking or dragging a selection box to capture context for the prompt.
4. **Settings Modal**:
   - API keys management.
   - Local daemon permission gates (`workspace_readwrite`, `workspace_readonly`, `insecure_none`).
   - MCP Server registrations (name, command, arguments).
   - Theme and accent color customizer.

