# ORBIT rebranding execution specification

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Purpose:** establish a distinctive ORBIT-owned product identity without erasing legal or technical provenance.

## Product-facing identity

Use the ORBIT brand system in `docs/00-foundation/BRAND_AND_IDENTITY.md` and `examples/brand/orbit-brand-tokens.json`. The current visual tokens are a working proposal. Trademark/domain clearance and final logo approval remain open gates.

### First-party surface naming

| ORBIT product name | User-facing function | Do not expose as the feature name |
|---|---|---|
| ORBIT Workspace | Projects, conversations, tasks, files and settings | Vendor chat UI names |
| ORBIT Core | Identity, policy, tasks and durable state | Third-party control-plane branding |
| ORBIT Agent Runtime | Planning, tool loop, specialist orchestration | Framework-specific internal names |
| ORBIT Web Node | Website navigation and web automation | Browser vendor product name as the ORBIT feature |
| ORBIT Desktop Node | Native desktop app control | Upstream CLI name as the product feature |
| ORBIT Sandbox | Disposable code and task execution | Sandbox vendor branding |
| ORBIT Skills | Reviewed workflows and agent instructions | Third-party skill-marketplace branding |
| ORBIT UI Runtime | Constrained, model-generated interfaces | Renderer vendor branding |
| ORBIT Connect | External APIs, MCP and agent backends | Connector framework branding |
| ORBIT Insights | Audit, traces, budgets, evaluation and reliability | Telemetry vendor dashboard branding |

Third-party technology names may be disclosed in a technical integration detail panel or open-source notices page where users need to understand what is operating. They must not be disguised as ORBIT-owned code.

## Visual direction

- Dark-first professional workspace with a complete light theme.
- Original ORBIT orbital/trajectory motif; no copied logos, icons, illustrations, gradients, badge systems or screenshots.
- Use a compact icon family with documented source/licence or original vector artwork.
- Avoid vendor lookalike trade dress, distinctive layouts or signature control patterns.
- Maintain accessibility contrast, keyboard navigation, reduced-motion mode and semantic components.
- Use tokens, not hard-coded colors. Every generated UI component must draw from the ORBIT catalog.

## Branding removal checklist for ORBIT-owned assets

1. Search UI source, CSS, icon sets, docs, marketing pages, repository names, screenshots, sample configs, app metadata and generated bundles for vendor logos and vendor feature labels.
2. Replace only first-party UI/artwork/copy with ORBIT-owned assets and neutral feature labels.
3. Keep legally required notices, copyright headers, license texts, NOTICE files and source attribution untouched.
4. Replace copied screenshots only with original ORBIT captures or diagrams made from scratch; do not remove upstream attribution to make copied art appear original.
5. Confirm providers/integrations are truthfully disclosed in Settings → Integrations / About → Open-source notices.
6. Run automated asset-source and branding lint as part of release review.
7. Obtain trademark review for ORBIT name, icon and tagline before public commercial use.

## Deliverables before branding freeze

- Approved vector logo/wordmark with monochrome and app-icon variants.
- Token set with color, typography, spacing, radius, elevation and motion.
- Component library and usage guidelines.
- Voice/tone and naming guide.
- Asset register with creator, source, license, hash and permitted use.
- Product screenshot pack created from ORBIT itself.
- Trademark/domain clearance status and approval record.
