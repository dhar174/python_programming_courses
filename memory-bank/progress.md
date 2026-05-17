<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Progress

## Milestones
- [x] Repository profile captured
- [x] Hybrid agent stack scaffolded
- [x] All 48 Basics lecture scripts written (Days 1–12, Hours 1–4 each, ~3000+ words each)
- [x] All 48 Advanced lecture scripts written (Days 1–12, Hours 1–4 each)
- [x] Per-deck Basics slide regeneration for materially changed days
- [x] `marp-action.yml` `sudo chown` permission fix (PR #418, merged)
- [x] Pages root 404 investigated and root cause identified
- [x] Pages root 404 fixed: `marp-action.yml` broken index copy logic patched; `Basics/lessons/slides/index.html` updated with Days 5–12 and fixed Day 2 link
- [x] Epic #419 portal rollout merged (PR #426)
- [x] Day overview index pages added between module portals and day decks
- [x] Root dashboard "Start here" links now point at day overview pages instead of slide decks
- [x] GitHub Pages portal entrypoints fixed to preserve the repository subpath for shared portal assets on directory-style URLs

## What works
- Repo-wide instructions, memory-bank scaffolding, and specialist agents exist.
- Managed sections allow maintenance runs to update generated content safely.
- All 96 hours of lecture content written and committed.
- Marp CI builds Basics slides to `_site/slides/basics/` and Advanced to `_site/slides/advanced/`.
- Pages workflow stages a root course dashboard at `_site/index.html`, module portals at `_site/slides/basics/` and `_site/slides/advanced/`, and supporting pages at `_site/slides/printable-index.html` plus `_site/404.html`.
- Shared portal assets publish from `_site/slides/shared/portal/`, including the generated `course-manifest.json`.
- `scripts/check_portal_publish.py` validates the staged `_site` artifact before Pages upload.
- `scripts/generate_day_overviews.py` generates source-owned Basics and Advanced day overview pages from `slides/shared/portal/day-overviews.json`.
- Root, module, printable, and day overview portal pages now preserve the `/python_programming_courses/` GitHub Pages subpath when resolving shared portal CSS/JS from directory-style URLs.

## What is incomplete
- No open gaps remain from the day overview portal polish; future portal changes should preserve the new module card → day overview → deck flow.
- Third-party imports remain optional until a pinned, licensed source is selected.

## Validation status
- Install: `python -m pip install nbconvert`
- Test: `./validate_slides.sh`
- Portal manifest: `python scripts/generate_portal_manifest.py --repo-root . --site-root _site --output _site/slides/shared/portal/course-manifest.json`
- Portal publish contract: `python scripts/check_portal_publish.py --repo-root . --site-root _site`
- Day overview freshness: `python scripts/generate_day_overviews.py --check`

## Last meaningful update
[2026-05-17] Portal entrypoint base-path detection normalized for GitHub Pages directory URLs
<!-- repo-agent-bootstrap:managed:end -->

## Portal rollout milestone

- [2026-05-16] Issue #420 architecture contract drafted in `docs/portal-architecture.md`, including sitemap, route rules, manifest schema, shared asset location, and the root-decoupling requirement ahead of #422.
- [2026-05-16] Issue #421 shared portal foundation implemented: root portal source added at `slides/index.html`, manifest generation/validation scripts added, shared portal assets added under `slides/shared/portal/`, and the Pages workflow updated to publish and validate the new root-entrypoint contract.
- [2026-05-16] Issue #422 Basics portal rebuilt as a production module portal in `Basics/lessons/slides/index.html`, with manifest-backed badges/repository artifact links, source-preview bootstrap logic, and validated published/source preview behavior.
- [2026-05-16] Issue #423 Advanced portal added at `Advanced/lessons/slides/index.html`, validated in source and published previews, and cross-module navigation from the Basics portal now targets the new Advanced landing page.
- [2026-05-16] Issue #424 root dashboard upgraded and supporting pages added: `slides/index.html` now points at both module portals plus course-material categories, `slides/printable-index.html` provides the approved full-course deck index, and `slides/404.html` is now part of the published portal contract.
- [2026-05-16] Issue #425 hardening landed with PR #426: review-selected fixes removed repo-name hardcoding from portal base-path logic, switched repo URLs to manifest-driven metadata/default branch handling, guarded theme persistence storage, widened workflow trigger coverage for portal validation, and kept `scripts/check_portal_publish.py` compatible with both the dedicated portal root and the approved redirect fallback.
- [2026-05-16] PR #426 merged, making the course dashboard, Basics portal, Advanced portal, shared asset kit, supporting pages, manifest generation, and staged publish validation the repository's current Pages baseline.
- [2026-05-16] Day overview work completed on `feature/day-slide-index-pages`: structured metadata drives generated `day-XX/index.html` pages for both modules, module day cards route to overviews, root/printable deck shortcuts remain direct, and publish validation requires the overview pages.
- [2026-05-17] Root dashboard "Start here" links now target day overview pages so the featured day chips open the day landing pages instead of slide decks.
