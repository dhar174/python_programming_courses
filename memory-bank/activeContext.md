<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Active Context

## Current objective
No active implementation objective is currently in flight. Epic #419's portal rollout merged in PR #426, and generated day overview index pages are now part of the portal baseline.

## Why it matters now
Future portal work should preserve the module portal → day overview → slide deck navigation path while keeping root featured links and the printable index as direct deck shortcuts.

## Current status
- Done:
  - All 48 Basics lecture scripts (Days 1–12, 4 hours each, ~3000+ words each)
  - All 48 Advanced lecture scripts (Days 1–12, 4 hours each)
  - Per-deck Basics slide regeneration for materially changed days
  - `marp-action.yml` `sudo chown` permission fix (PR #418)
  - Epic #419 portal rollout merged in PR #426:
    - `slides/index.html` now owns the published course root
    - `Basics/lessons/slides/index.html` and `Advanced/lessons/slides/index.html` publish as the module landing pages
    - shared portal assets and the canonical manifest live under `slides/shared/portal/**`
    - `slides/printable-index.html` and `slides/404.html` are part of the published portal contract
    - `.github/workflows/marp-action.yml` regenerates the staged manifest and validates `_site` with `scripts/check_portal_publish.py`
  - Day overview index pages for Basics and Advanced module portals:
    - source-owned generated pages under `Basics/lessons/slides/day-XX/index.html` and `Advanced/lessons/slides/day-XX/index.html`
    - module day cards route to overviews before opening decks
    - root featured links and printable index remain direct deck shortcuts
- In progress:
  - none
- Blocked:
  - none

## Relevant files
- `README.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `CLAUDE.md`
- `.github/workflows/marp-action.yml`
- `docs/portal-architecture.md`
- `slides/index.html`
- `Basics/lessons/slides/index.html`
- `Advanced/lessons/slides/index.html`
- `slides/shared/portal/portal.css`
- `slides/shared/portal/portal.js`
- `slides/shared/portal/course-manifest.json`
- `slides/shared/portal/day-overviews.json`
- `scripts/generate_day_overviews.py`
- `scripts/generate_portal_manifest.py`
- `scripts/check_portal_publish.py`
- `Basics/lessons/slides/day-*/day-*-session-*.html`
- `Advanced/lessons/slides/day-*/day-*-session-*.html`
- `Basics/lessons/slides/day-*/index.html`
- `Advanced/lessons/slides/day-*/index.html`

## Portal and slide locations
1. `slides/` — source-owned root dashboard, supporting pages, and shared portal asset kit
2. `Basics/lessons/slides/` and `Advanced/lessons/slides/` — committed module landing pages plus day-level HTML decks
3. `_site/` — staged Pages artifact produced by CI, including `_site/index.html`, `_site/slides/basics/`, `_site/slides/advanced/`, and `_site/slides/shared/portal/`

## Next recommended steps
1. No portal follow-up is currently required from Epic #419.
2. If root routing, shared portal assets, or publish validation change later, update `docs/portal-architecture.md`, `.github/workflows/marp-action.yml`, and the affected portal pages together.
<!-- repo-agent-bootstrap:managed:end -->

## Portal baseline

- [2026-05-16] `docs/portal-architecture.md` is the authority for portal information architecture, manifest ownership, and root/module entrypoint rules.
- [2026-05-16] `slides/index.html` owns the published course root, while `Basics/lessons/slides/index.html` and `Advanced/lessons/slides/index.html` remain the module landing pages.
- [2026-05-16] Shared portal assets and the canonical manifest path are reserved as `slides/shared/portal/**`.
- [2026-05-16] `scripts/generate_portal_manifest.py` and `scripts/check_portal_publish.py` define the staged-manifest and publish-contract validation workflow for `_site`.
- [2026-05-16] New day overview work uses structured metadata in `slides/shared/portal/day-overviews.json` and generated source pages in each module `day-XX/index.html`; module day cards route to those pages while root and printable indexes keep direct deck shortcuts.
