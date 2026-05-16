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

