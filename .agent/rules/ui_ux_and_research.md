# Global Behavioral Rules & UI/UX Standards

## 1. Professional UI/UX Standards (UI/UX Pro)
- When generating frontend code, HTML artifacts, dashboards, components, or UI layouts, always follow the `ui-ux-pro` skill guidelines (`C:\Users\YUVRAJ\.gemini\config\skills\ui-ux-pro\SKILL.md`).
- **Strictly No Amateur Emojis**: Never use casual/cartoonish emojis (e.g., 🚀, 💡, 🔥, 📊, ⚙️, ✅, ❌) inside user interfaces, navigation bars, buttons, badges, status indicators, or data tables.
- **Professional Vector Icons**: Always use clean, accessible vector SVG icons (Lucide / Heroicons / Feather standard with `viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`, `stroke-width="2"`, `stroke-linecap="round"`, `stroke-linejoin="round"`). You can retrieve icons using the bundled CLI at `C:\Users\YUVRAJ\.gemini\config\skills\ui-ux-pro\scripts\icon_cli.py`.
- **Semantic Design Tokens**: Use theme tokens (`var(--background)`, `var(--card)`, `var(--border)`, `var(--foreground)`, `var(--muted-foreground)`, `var(--primary)`) to ensure complete dark/light mode compatibility.
- **Visual Polish**: Ensure clean typographic hierarchy, 8pt spacing rhythm, accessible contrast ratios (WCAG AA compliant), and subtle micro-interactions (`transition-colors duration-150`).

## 2. Web Research & Information Gathering
- When web browsing, searching DuckDuckGo, or gathering online intelligence, use the `duckduckgo-research` skill (`C:\Users\YUVRAJ\.gemini\config\skills\duckduckgo-research\SKILL.md`) and its helper script `ddg_research.py`.

