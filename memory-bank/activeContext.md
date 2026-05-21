<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Active Context

## Current objective
Issue #458 lecture HTML rollout closeout is complete for high-confidence candidates: tranche/platform sub-issues plus #419 were closed with merged-on-main evidence (PR #476 / PR #426). Remaining open issues (#433, #436, #437, #439, #452, #459) are intentionally kept open due insufficient confidence.

## Why it matters now
Lecture Markdown is now a first-class published surface alongside slide decks. The new pipeline needs to preserve content fidelity while making lecture pages reachable from the existing portal/day-overview flow and safe for GitHub Pages hosting.

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
    - root featured links now route to day overview pages; the printable index remains a direct deck shortcut
  - GitHub Pages base-path normalization updated across portal entrypoints and generated day overviews so directory-style published URLs keep the `/python_programming_courses/` project prefix when loading shared portal assets
  - `.github/workflows/copilot-setup-steps.yml` now satisfies the Copilot setup-steps contract and performs a real lightweight bootstrap by setting up Python, installing `nbconvert`, and smoke-checking the dependency for Copilot agents
  - Issue #458 foundation platform:
    - `scripts/generate_lecture_pages.py` now generates hourly lecture HTML in natural day/hour order and can mirror pages into `_site`
    - `scripts/validate_lecture_html.py` now validates lecture-page structure, navigation hooks, hash targets, and offline-safe asset/runtime rules
    - `slides/shared/lecture/lecture.css` and `slides/shared/lecture/lecture.js` now provide the shared lecture-page UX layer
    - `.github/workflows/marp-action.yml` now installs pinned `Markdown`, generates lecture HTML into `_site`, and runs lecture validation before publish checks
    - `scripts/generate_portal_manifest.py`, `scripts/check_portal_publish.py`, and `slides/shared/portal/portal.js` now recognize published lecture HTML in the Pages artifact
  - Lecture-to-slide cue rollout:
    - `Basics/lessons/lecture/Day*_Hour*_Basics.md` and `Advanced/lessons/lecture/Day*_Hour*_Advanced.md` now carry explicit `[Instructor slide change: page=...; title=...]` markers at major teaching transitions
    - `scripts/generate_lecture_pages.py` now resolves those cues against the matching session deck HTML, renders linked slide-change callouts, and exposes a persistent current-slide indicator in lecture HTML
    - `scripts/sync_lecture_slide_cues.py` can refresh the source Markdown cue markers from the session deck structure
    - `Basics/generate_slides.py` and `Advanced/generate_slides.py` now emit stable per-slide ids so lecture cues can deep-link to named deck anchors instead of brittle numeric hashes alone
    - `scripts/validate_lecture_html.py` now requires instructor slide cues and verifies each cue rendered a deck deep link
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
- `scripts/generate_lecture_pages.py`
- `scripts/sync_lecture_slide_cues.py`
- `scripts/generate_portal_manifest.py`
- `scripts/check_portal_publish.py`
- `scripts/validate_lecture_html.py`
- `Basics/generate_slides.py`
- `Advanced/generate_slides.py`
- `slides/shared/lecture/lecture.css`
- `slides/shared/lecture/lecture.js`
- `Basics/lessons/lecture/Day*_Hour*_Basics.html`
- `Advanced/lessons/lecture/Day*_Hour*_Advanced.html`
- `Basics/lessons/slides/day-*/day-*-session-*.html`
- `Advanced/lessons/slides/day-*/day-*-session-*.html`
- `Basics/lessons/slides/day-*/index.html`
- `Advanced/lessons/slides/day-*/index.html`

## Portal and slide locations
1. `slides/` — source-owned root dashboard, supporting pages, and shared portal asset kit
2. `Basics/lessons/slides/` and `Advanced/lessons/slides/` — committed module landing pages plus day-level HTML decks
3. `_site/` — staged Pages artifact produced by CI, including `_site/index.html`, `_site/slides/basics/`, `_site/slides/advanced/`, and `_site/slides/shared/portal/`

## Next recommended steps
1. Manually resolve remaining open issue #459 (`01-intro-to-python.md`) because the referenced `Advanced/lessons/lecture/01-intro-to-python.html` artifact is not present and could not be auto-closed with high confidence.
2. Triage remaining non-#458 open issues (#433, #436, #437, #439, #452) with targeted evidence before any additional closures.
<!-- repo-agent-bootstrap:managed:end -->

## Portal baseline

- [2026-05-16] `docs/portal-architecture.md` is the authority for portal information architecture, manifest ownership, and root/module entrypoint rules.
- [2026-05-16] `slides/index.html` owns the published course root, while `Basics/lessons/slides/index.html` and `Advanced/lessons/slides/index.html` remain the module landing pages.
- [2026-05-16] Shared portal assets and the canonical manifest path are reserved as `slides/shared/portal/**`.
- [2026-05-16] `scripts/generate_portal_manifest.py` and `scripts/check_portal_publish.py` define the staged-manifest and publish-contract validation workflow for `_site`.
- [2026-05-16] New day overview work uses structured metadata in `slides/shared/portal/day-overviews.json` and generated source pages in each module `day-XX/index.html`; module day cards route to those pages while root and printable indexes keep direct deck shortcuts.
- [2026-05-17] Portal entrypoints and generated day overview pages normalize trailing-slash directory URLs so published GitHub Pages paths keep the repository subpath when resolving `slides/shared/portal/*`.

## Assignment fixture policy

- [2026-05-18] `submissions/*_test_filled.ipynb` files must remain filled-in copies of each day’s full homework notebook and preserve instructional structure; they are not allowed to be reduced to print-only stubs.
- [2026-05-19] PR #456 fixture repairs restored real filled solutions for the reviewed Basics/Advanced notebooks, corrected mismatched autograder script-name guidance, and reinstated the Advanced Day 8 authenticity guardrail while keeping the repaired fixtures aligned with existing `criteria.json` checks.
