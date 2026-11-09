# Design system requirements

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

Create original ORBIT visual identity; do not copy competitor branding or assets. Define semantic tokens in code for color, type, spacing, radius, elevation, motion and breakpoints. Provide light/dark themes with accessible contrast. Use consistent component states: default, hover, focus-visible, active, disabled, loading, success, warning and error.

## Visual direction

A calm technical workspace: clear typography, neutral surfaces, restrained accent, high information density where it helps execution. Use monospace only for code, IDs and terminal output. Reserve motion for state transitions and streaming; respect reduced-motion preferences.

## Required component families

Navigation/sidebar; workspace switcher; composer; message/source/artifact renderer; task timeline; tool activity; browser preview; terminal view; approval dialog; agent editor; provider picker; file list; skill/routine builder; usage meter; empty/error/loading states.

## Tokens

Tokens are not locked until usability testing. Keep semantic names (`--surface`, `--text-primary`, `--border-subtle`, `--status-danger`) instead of scattering raw colors. Document component behavior and accessibility in Storybook or equivalent when implementation begins.

## ORBIT v0.2 alignment

The v0.2 experience adds explicit device pairing, visible desktop activity and immediate stop/pause. Show action delivery separately from UI verification; see `DESKTOP_ACTIVITY_PANEL.md`.

## v0.3 rebranding implementation

Use `examples/brand/orbit-brand-tokens.json` and `config/branding/orbit-brand-config.json` as working tokens only. Follow `REBRANDING_EXECUTION_SPEC.md` and `BRAND_ASSET_REGISTER.yaml`. Original logo artwork, trademark clearance and accessibility review remain open tasks. Third-party legal notices stay visible in an Open Source Notices surface even though vendor logos and visual identity are excluded from ORBIT first-party branding.
