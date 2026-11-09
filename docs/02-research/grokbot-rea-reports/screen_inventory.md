# GROKBOT-RE: Screen & UI Inventory

1. **Main Chat Workspace** (`index.html`):
   - Left Navigation & Conversation History
   - Top Header with Model Selector & System Status
   - Central Message Thread with Markdown & KaTeX Formula Rendering
   - Code Block Display with Language Badge & Copy Button
   - Bottom Prompt Composer with Auto-Resize & Attachment Drawer
2. **Desktop Mount Floating Panel** (`panel.html`):
   - Collapsible Mini Widget mounted directly onto Windows desktop
   - Quick Prompt Input & Send Button
   - Integrated Window Capture Trigger
3. **Region / Screen Capture Overlay** (`capture-overlay.html`):
   - Fullscreen transparent crosshair overlay
   - Interactive region selection bounding box
   - Hotkey triggered (`Alt+Shift+Space`)
4. **Settings Modal**:
   - API Key Configuration (xAI Grok, OpenAI, Anthropic)
   - Local Daemon Sandboxing Permissions
   - MCP Server Registration
   - Theme & Accent Color Customizer
