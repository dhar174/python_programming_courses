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

## What works
- Repo-wide instructions, memory-bank scaffolding, and specialist agents exist.
- Managed sections allow maintenance runs to update generated content safely.
- All 96 hours of lecture content written and committed.
- Marp CI builds Basics slides to `_site/slides/basics/` and Advanced to `_site/slides/advanced/`.
- Pages workflow deploys successfully; slide subtree is live.
- Root `_site/index.html` is now a meta-refresh redirect to `./slides/basics/`.
- `_site/slides/basics/index.html` lists all 12 days with correct links.

## What is incomplete
- Advanced slide index is not linked from the Basics index (could add a nav link in a future pass).
- Third-party imports remain optional until a pinned, licensed source is selected.

## Validation status
- Install: `python -m pip install nbconvert`
- Test: `./validate_slides.sh`

## Last meaningful update
[2026-05-14] All content complete; Pages root 404 fix applied and pushed
<!-- repo-agent-bootstrap:managed:end -->

## Portal rollout milestone

- [2026-05-16] Issue #420 architecture contract drafted in `docs/portal-architecture.md`, including sitemap, route rules, manifest schema, shared asset location, and the root-decoupling requirement ahead of #422.
- [2026-05-16] Issue #421 shared portal foundation implemented: root portal source added at `slides/index.html`, manifest generation/validation scripts added, shared portal assets added under `slides/shared/portal/`, and the Pages workflow updated to publish and validate the new root-entrypoint contract.
- [2026-05-16] Issue #422 Basics portal rebuilt as a production module portal in `Basics/lessons/slides/index.html`, with manifest-backed badges/repository artifact links, source-preview bootstrap logic, and validated published/source preview behavior.
- [2026-05-16] Issue #423 Advanced portal added at `Advanced/lessons/slides/index.html`, validated in source and published previews, and cross-module navigation from the Basics portal now targets the new Advanced landing page.
- [2026-05-16] Issue #424 root dashboard upgraded and supporting pages added: `slides/index.html` now points at both module portals plus course-material categories, `slides/printable-index.html` provides the approved full-course deck index, and `slides/404.html` is now part of the published portal contract.
