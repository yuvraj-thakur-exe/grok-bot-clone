# ORBIT brand and identity system

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Brand direction:** ORBIT is the product/company working identity for this project. The word and visual identity remain subject to trademark and domain clearance before commercial launch.

## Brand architecture

- **ORBIT** — company/product umbrella.
- **ORBIT Workspace** — primary user interface and projects.
- **ORBIT Agents** — user-defined and specialist agent experiences.
- **ORBIT Runtime** — orchestration and durable task engine.
- **ORBIT Browser Node** — isolated browser execution node.
- **ORBIT Desktop Node** — user-controlled local native desktop bridge.
- **ORBIT Sandbox** — code and task execution isolation layer.
- **ORBIT Skills** — reviewed, versioned workflow packages.
- **ORBIT Connect** — connectors, MCP and API integrations.

These are internal naming proposals, not registered marks.

## Original identity rules

- Use an original ORBIT wordmark, icon, typography, tone, color tokens and illustrations.
- Do not reuse another company's logo, product icon, proprietary screenshots, product name as ORBIT feature branding, badge, badge system, or distinctive trade dress.
- Do not call an ORBIT feature by a competitor's name. Use generic terms such as browser worker, local desktop node, skill registry, sandbox runtime, agent backend and generative UI.
- Do not imply endorsement, partnership or affiliation with Vercel, OpenHands, OpenSandbox, model providers or any reference project.
- Remove third-party logos and vendor-specific branding from ORBIT's own user interface and marketing surfaces unless their use is separately authorized.

## Branding versus legal attribution

“Remove company branding” does **not** mean removing copyright notices, license text, attribution notices, required NOTICE files, trademark disclaimers, third-party dependency names in compliance views, or source provenance. Those must remain wherever the applicable license requires them. A product can have an original ORBIT brand while preserving legally required notices.

## Proposed design tokens

Use tokens rather than hard-coded values; validate contrast and color choices with actual UI testing. Example neutral base tokens:

```json
{
  "brand": "ORBIT",
  "theme": {
    "surface": "#0D1117",
    "surfaceRaised": "#151B23",
    "surfaceSubtle": "#1B2430",
    "textPrimary": "#F2F5F8",
    "textMuted": "#A6B0BE",
    "border": "#303B49",
    "accent": "#7C9CFF",
    "accentStrong": "#5478F5",
    "success": "#35B68A",
    "warning": "#E9B44C",
    "danger": "#E36B75"
  },
  "radius": {"sm": 6, "md": 10, "lg": 16},
  "spacingUnit": 4
}
```

These are starter values, not a finished design system. Use light/dark semantic tokens, test contrast, support reduced motion and do not overuse gradients.

## Trademark and naming gate

Before public commercial release: search relevant trademark registers in target markets, check confusingly similar software marks, domains and package namespaces; ask qualified counsel to review; reserve naming alternatives. Do not state that ORBIT is legally available until clearance is complete.

## v0.3 product-module naming

Use the neutral ORBIT modules listed in `docs/07-design/REBRANDING_EXECUTION_SPEC.md`: Workspace, Core, Agent Runtime, Web Node, Desktop Node, Sandbox, Skills, UI Runtime, Connect and Insights. These are working names only and remain subject to trademark review. Use vendor names only in integration settings, technical documentation and legal notices where truthful identification or attribution is required.
