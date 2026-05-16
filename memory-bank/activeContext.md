<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Active Context

## Current objective
All 96 hours of course content are written. The final task was fixing the GitHub Pages root 404. That fix has been applied and pushed.

## Why it matters now
The repository is now in a maintenance state. All lecture scripts, slides, and CI/CD are complete. Future work is incremental updates or Advanced slide regeneration.

## Current status
- Done:
  - All 48 Basics lecture scripts (Days 1–12, 4 hours each, ~3000+ words each)
  - All 48 Advanced lecture scripts (Days 1–12, 4 hours each)
  - Per-deck Basics slide regeneration for materially changed days
  - `marp-action.yml` `sudo chown` permission fix (PR #418)
  - Pages root 404 root-cause identified and fixed:
    - `marp-action.yml` now writes root `_site/index.html` as meta-refresh → `./slides/basics/`
    - `marp-action.yml` now copies source index to `_site/slides/basics/index.html` (not root)
    - `Basics/lessons/slides/index.html` updated with Days 5–12 cards and correct Day 2 link
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
- `Basics/lessons/slides/index.html`
- `Basics/lessons/slides/day-*/day-*-session-*.html`
- `Advanced/lessons/slides/day-*/day-*-session-*.html`

## Slide locations (three kinds)
1. `Basics/lessons/slides/day-NN/` — committed agent-built HTML slides (source of truth for Basics)
2. `Advanced/lessons/slides/day-NN/` — committed agent-built HTML slides (source of truth for Advanced)
3. `_site/slides/basics/` + `_site/slides/advanced/` — CI Marp build output, gitignored, deployed to Pages

## Next recommended steps
1. Wait for CI to complete and verify `https://dhar174.github.io/python_programming_courses/` redirects to `/slides/basics/`.
2. Regenerate Advanced slides if Advanced lecture content was changed since generation.
3. Update `README.md` badges/links if the Pages URL is confirmed working.
<!-- repo-agent-bootstrap:managed:end -->

## Portal architecture update

- [2026-05-16] Issue #420 architecture contract added in `docs/portal-architecture.md`.
- Root ownership is now specified to move to `slides/index.html` in #421 before the Basics portal rebuild in #422.
- Shared portal assets and the canonical manifest path are reserved as `slides/shared/portal/**`.
- [2026-05-16] Issue #421 shared portal foundation implemented in the working tree: `slides/index.html` now owns the course root, shared portal CSS/JS live under `slides/shared/portal/`, and publish validation is codified in `scripts/check_portal_publish.py`.
- [2026-05-16] Issue #422 Basics portal rebuild is now implemented in the working tree. `Basics/lessons/slides/index.html` is a static-first module portal with root breadcrumbs, theme controls, preserved day descriptions, static relative deck links, and manifest-enhanced repository artifact chips.
- [2026-05-16] Issue #423 Advanced portal is now implemented in the working tree. `Advanced/lessons/slides/index.html` now exists as the Advanced module landing page, and the Basics portal now routes its "Continue to Advanced" CTA to the new module page.
- [2026-05-16] Issue #424 root dashboard/supporting pages are now implemented in the working tree. `slides/index.html` reflects both live module portals, `slides/printable-index.html` provides the approved full-course deck index, and `slides/404.html` provides the approved recovery page.
- [2026-05-16] Current active portal objective: finish issue #425 by aligning docs and remaining workflow/QA notes with the now-complete root + module portal surfaces.
