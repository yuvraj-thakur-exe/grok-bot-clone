---
name: ui-ux-pro
description: >-
  Expert UI/UX design and frontend implementation system. Enforces production-grade design standards,
  clean typography, modern layout systems, accessible contrast, smooth micro-interactions,
  and professional vector SVG icons (Lucide / Feather / Heroicons) while strictly eliminating amateur emojis.
  Use whenever designing, building, reviewing, or styling user interfaces, web applications,
  HTML widgets, dashboards, or data visualizations.
---

# UI/UX Pro: Production Design System & Iconography

This skill establishes strict frontend engineering and UI/UX design standards for all web applications, dashboards, HTML artifacts, and chat widgets.

---

## 1. The Cardinal Rule: Professional Vector Icons Only (Zero Emojis)

> [!IMPORTANT]
> **Casual / Cartoonish Emojis are strictly forbidden in UI components.**  
> Emojis (e.g. 🚀, 💡, 🔥, 📊, ⚙️, ❌, ✅, 📌) degrade visual hierarchy, appear differently across OS platforms, have fixed non-themeable colors, and make interfaces feel amateurish.

### Vector SVG Standard:
All iconography must be implemented as clean, scalable vector SVGs adhering to the standard 24x24 or 20x20 grid:
```html
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" 
     fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Clean SVG path elements -->
</svg>
```

### Ready-to-Use Icon CLI Helper:
Use the bundled icon helper to look up or generate any vector icon:
```powershell
# List available icons
python "C:\Users\YUVRAJ\.gemini\config\skills\ui-ux-pro\scripts\icon_cli.py" --list

# Get an icon with Tailwind classes
python "C:\Users\YUVRAJ\.gemini\config\skills\ui-ux-pro\scripts\icon_cli.py" search --class-name "w-4 h-4 text-indigo-500"

# Format for React JSX
python "C:\Users\YUVRAJ\.gemini\config\skills\ui-ux-pro\scripts\icon_cli.py" check --jsx
```

---

## 2. Semantic Design Tokens & Theming

Never hardcode arbitrary palette classes (like `bg-slate-900` or `text-black`) that fail when users toggle between light and dark themes. Always employ semantic design tokens:

Token | CSS Variable | Tailwind Usage | Purpose
:--- | :--- | :--- | :---
**Background** | `var(--background)` | `bg-[var(--background)]` | App canvas & root viewport
**Card** | `var(--card)` | `bg-[var(--card)]` | Content elevation, cards, modals
**Border** | `var(--border)` | `border-[var(--border)]` | Dividers, card edges, input outlines
**Foreground** | `var(--foreground)` | `text-[var(--foreground)]` | Primary text and headings
**Muted Text** | `var(--muted-foreground)` | `text-[var(--muted-foreground)]` | Secondary text, captions, metadata
**Primary** | `var(--primary)` | `bg-[var(--primary)] text-white` | Primary call-to-actions & brand focus
**Accent** | `var(--accent)` | `text-[var(--accent)]` | Subtle indicators, active links

---

## 3. Typographic Hierarchy & Spacing (8pt Grid)

1. **Spacing Rhythm**: Use Tailwind's standard 4px/8px scale (`gap-2` = 8px, `p-4` = 16px, `p-6` = 24px, `space-y-4` = 16px).
2. **Typography Scale**:
   - Page Titles: `text-2xl font-bold tracking-tight`
   - Section / Card Headers: `text-base font-semibold`
   - Body Text: `text-sm text-[var(--foreground)] leading-relaxed`
   - Metadata / Badges: `text-xs font-medium text-[var(--muted-foreground)]`
   - Minimum Floor: Never use sub-12px micro-text (`text-[10px]`); `text-xs` (12px) is the absolute minimum floor.

---

## 4. Component Blueprints

### A. Executive KPI Metric Card
```html
<div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-5 shadow-sm space-y-3">
  <div class="flex items-center justify-between">
    <span class="text-xs font-medium uppercase tracking-wider text-[var(--muted-foreground)]">Metric Title</span>
    <div class="p-2 rounded-lg bg-indigo-500/10 text-indigo-400">
      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>
      </svg>
    </div>
  </div>
  <div class="flex items-baseline justify-between">
    <span class="text-2xl font-bold tracking-tight">4,820</span>
    <span class="inline-flex items-center gap-1 text-xs font-medium text-emerald-500">
      <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>
      </svg>
      +12.4%
    </span>
  </div>
</div>
```

### B. Status Indicator Badge (No Emojis)
```html
<!-- Operational / Success -->
<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
  Operational
</span>

<!-- Warning / Pending -->
<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-amber-500/10 text-amber-400 border border-amber-500/20">
  <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
  Pending Review
</span>
```

### C. Search Input with Vector Icon
```html
<div class="relative max-w-sm">
  <svg class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-[var(--muted-foreground)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
  </svg>
  <input type="text" placeholder="Search resources..." 
         class="w-full pl-9 pr-4 py-2 text-sm bg-[var(--background)] border border-[var(--border)] rounded-lg text-[var(--foreground)] placeholder-[var(--muted-foreground)] focus:outline-none focus:ring-2 focus:ring-[var(--primary)] transition-all">
</div>
```

---

## 5. Micro-interactions & Accessible States

- **Transitions**: Apply `transition-colors duration-150 ease-out` or `transition-all duration-200` to prevent jarring jumps.
- **Focus Rings**: Always support keyboard navigation with `focus-visible:ring-2 focus-visible:ring-[var(--primary)] focus-visible:outline-none`.
- **Hover Feedback**: Elevation with `hover:border-[var(--border)]/80 hover:shadow-md`.
- **Disabled State**: Apply `disabled:opacity-50 disabled:cursor-not-allowed`.

---

## 6. Antigravity Chat Embedding (`<agent-embed>`)

When generating inline widgets for chat:
1. Include the allowlisted Tailwind script in `<head>`:
   ```html
   <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
   ```
2. Set `<body class="bg-transparent text-[var(--foreground)] antialiased p-4">`.
3. Wrap content in a card container with `bg-[var(--card)] border border-[var(--border)] rounded-xl`.
4. Embed in chat using:
   ```html
   <agent-embed src="file:///path/to/artifact.html"></agent-embed>
   ```

