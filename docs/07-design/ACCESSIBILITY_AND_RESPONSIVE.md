# Accessibility and responsive requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Target WCAG 2.2 AA as the product design goal; perform an actual accessibility audit before claiming conformance. All interactive controls require keyboard operation, visible focus, accessible names, predictable focus order and screen-reader status announcements. Task streaming must not move focus unexpectedly. Color cannot be the only status signal. Honor reduced motion. Provide zoom and reflow without horizontal scrolling for core reading flows.

Desktop is the primary execution workspace because browser preview, terminal and task timeline need space. Tablet should retain chat, approvals and task review. Mobile should prioritize conversation, status, approval review and artifact access; do not attempt a cramped full terminal UI. Validate representative viewport widths and screen readers with automated and manual tests.

## Native desktop UX accessibility

The ORBIT UI that reports desktop permissions and actions must itself be keyboard accessible, screen-reader labelled and usable on small screens. Show incomplete/unknown evidence distinctly from absent data. Provide a textual activity timeline as an alternative to screenshot monitoring. Native desktop accessibility data is not a substitute for testing ORBIT's own UI accessibility.

## ORBIT v0.2 alignment

The v0.2 experience adds explicit device pairing, visible desktop activity and immediate stop/pause. Show action delivery separately from UI verification; see `DESKTOP_ACTIVITY_PANEL.md`.
