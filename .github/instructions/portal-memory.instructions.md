---
applyTo: "slides/**,.github/workflows/marp-action.yml,scripts/generate_portal_manifest.py,scripts/check_portal_publish.py,docs/portal-architecture.md,memory-bank/**"
---

# Portal Memory

Portal root, asset, and publish-contract invariants for the GitHub Pages course site.

## Root ownership and landing pages

- Treat `slides/index.html` as the source-owned course root for GitHub Pages.
- Preserve `Basics/lessons/slides/index.html` and `Advanced/lessons/slides/index.html` as the module landing pages that publish under `_site/slides/basics/` and `_site/slides/advanced/`.
- Update `docs/portal-architecture.md`, `.github/workflows/marp-action.yml`, and the affected portal pages together when changing root-routing or fallback behavior.

## Shared portal asset contract

- Keep shared portal CSS, JS, and manifest files under `slides/shared/portal/**`.
- Treat `slides/shared/portal/course-manifest.json` as the canonical manifest source path and `_site/slides/shared/portal/course-manifest.json` as the staged publish artifact.
- Prefer manifest-driven repo links and supporting-page metadata over hardcoded repository or branch assumptions.

## Publish validation workflow

- Regenerate the staged manifest with `python scripts/generate_portal_manifest.py --repo-root . --site-root _site --output _site/slides/shared/portal/course-manifest.json` when validating a publish-shaped `_site`.
- Validate the staged Pages artifact with `python scripts/check_portal_publish.py --repo-root . --site-root _site`.
- Keep root-entrypoint checks compatible with both the dedicated portal root and the approved redirect fallback.
- For portal-only navigation, manifest, or shared-asset changes, prefer targeted checks before broad slide rebuilds: generator freshness checks, Python/JS syntax checks, link assertions, and a temporary publish-shaped staged tree passed to `scripts/check_portal_publish.py`. Run Marp builds when slide Markdown, deck output, or Marp configuration changes require deck regeneration.
