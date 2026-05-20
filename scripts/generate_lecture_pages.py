#!/usr/bin/env python3
"""Generate long-form HTML lecture pages for hourly lecture Markdown files."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from xml.etree.ElementTree import Element

try:
    from markdown import Markdown
    from markdown.extensions import Extension
    from markdown.treeprocessors import Treeprocessor
except ImportError as exc:  # pragma: no cover - import failure is environment-specific
    raise SystemExit(
        "Missing dependency 'Markdown'. Install it with: python -m pip install Markdown"
    ) from exc


MODULES = {
    "basics": {
        "label": "Basics",
        "title": "Python Programming Basics",
        "lecture_root": Path("Basics/lessons/lecture"),
    },
    "advanced": {
        "label": "Advanced",
        "title": "Python Programming Advanced",
        "lecture_root": Path("Advanced/lessons/lecture"),
    },
}

HOURLY_FILENAME_RE = re.compile(
    r"^Day(?P<day>\d+)_Hour(?P<hour>\d+)_(?P<module>Basics|Advanced)\.md$"
)
HEADING_TAG_RE = re.compile(r"h([1-6])$")


@dataclass(frozen=True)
class LectureSource:
    module_id: str
    module_label: str
    module_title: str
    markdown_path: Path
    markdown_relative_path: Path
    html_relative_path: Path
    day: int
    hour: int


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    identifier: str


@dataclass(frozen=True)
class RenderedLecture:
    title: str
    headings: list[Heading]
    html: str


@dataclass
class HeadingState:
    page_title: str | None = None
    headings: list[Heading] = field(default_factory=list)
    slug_counts: dict[str, int] = field(default_factory=dict)

    def reset(self) -> None:
        self.page_title = None
        self.headings.clear()
        self.slug_counts.clear()


def slugify_heading(value: str, slug_counts: dict[str, int]) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", ascii_value)
    slug = re.sub(r"[\s_-]+", "-", slug).strip("-") or "section"
    count = slug_counts.get(slug, 0)
    slug_counts[slug] = count + 1
    return slug if count == 0 else f"{slug}-{count + 1}"


def element_text(element: Element) -> str:
    return "".join(element.itertext()).strip()


class HeadingTreeprocessor(Treeprocessor):
    def __init__(self, md: Markdown, state: HeadingState) -> None:
        super().__init__(md)
        self.state = state

    def run(self, root: Element) -> Element:
        self.state.reset()

        if len(root) and root[0].tag == "h1":
            self.state.page_title = element_text(root[0]) or None
            root.remove(root[0])

        for element in root.iter():
            tag_match = HEADING_TAG_RE.fullmatch(element.tag)
            if tag_match is None:
                continue

            text = element_text(element)
            if not text:
                continue

            identifier = slugify_heading(text, self.state.slug_counts)
            element.set("id", identifier)
            self.state.headings.append(
                Heading(level=int(tag_match.group(1)), text=text, identifier=identifier)
            )

        if self.state.page_title is None and self.state.headings:
            self.state.page_title = self.state.headings[0].text

        return root


class HeadingIdExtension(Extension):
    def __init__(self) -> None:
        super().__init__()
        self.state = HeadingState()

    def extendMarkdown(self, md: Markdown) -> None:
        md.treeprocessors.register(
            HeadingTreeprocessor(md, self.state),
            "pyc_heading_ids",
            15,
        )


def render_markdown(markdown_text: str) -> RenderedLecture:
    if markdown_text.startswith("\ufeff"):
        markdown_text = markdown_text[1:]
    heading_extension = HeadingIdExtension()
    renderer = Markdown(
        extensions=[
            "extra",
            "sane_lists",
            heading_extension,
        ],
        output_format="html5",
    )
    html = renderer.convert(markdown_text)
    title = heading_extension.state.page_title or "Lecture"
    return RenderedLecture(
        title=title,
        headings=list(heading_extension.state.headings),
        html=html,
    )


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root))
    parser.add_argument(
        "--output-root",
        help="Mirror generated files under this root. Defaults to repo-root for source-owned output.",
    )
    parser.add_argument(
        "--module",
        choices=("all", "basics", "advanced"),
        default="all",
        help="Limit generation to a single module.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated lecture HTML (and mirrored shared assets) are not up to date.",
    )
    return parser.parse_args()


def load_hourly_sources(repo_root: Path, module_filter: str) -> list[LectureSource]:
    sources: list[LectureSource] = []
    module_ids = list(MODULES) if module_filter == "all" else [module_filter]
    for module_id in module_ids:
        module = MODULES[module_id]
        lecture_root = repo_root / module["lecture_root"]
        for markdown_path in lecture_root.glob("*.md"):
            match = HOURLY_FILENAME_RE.match(markdown_path.name)
            if match is None:
                continue
            relative_path = markdown_path.relative_to(repo_root)
            sources.append(
                LectureSource(
                    module_id=module_id,
                    module_label=module["label"],
                    module_title=module["title"],
                    markdown_path=markdown_path,
                    markdown_relative_path=relative_path,
                    html_relative_path=relative_path.with_suffix(".html"),
                    day=int(match.group("day")),
                    hour=int(match.group("hour")),
                )
            )
    return sorted(sources, key=lambda item: (item.module_id, item.day, item.hour, item.markdown_path.name))


def relative_href(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_path.parent).replace("\\", "/")


def display_root(repo_root: Path, output_root: Path) -> str:
    if output_root == repo_root:
        return "."
    try:
        return output_root.relative_to(repo_root).as_posix()
    except ValueError:
        return str(output_root)


def render_toc(headings: list[Heading]) -> str:
    if not headings:
        return '<p class="lecture-status">No subsection headings were found in this lecture.</p>'

    items = [
        (
            f'<li><a href="#{escape(heading.identifier)}" '
            f'class="depth-{heading.level}">{escape(heading.text)}</a></li>'
        )
        for heading in headings
    ]
    return "<ol class=\"lecture-toc-list\">\n" + "\n".join(items) + "\n</ol>"


def render_page(
    source: LectureSource,
    rendered: RenderedLecture,
    *,
    repo_root: Path,
    output_file: Path,
    output_root: Path,
    prev_source: LectureSource | None,
    next_source: LectureSource | None,
) -> str:
    asset_root = output_root / "slides" / "shared" / "lecture"
    stylesheet_href = relative_href(output_file, asset_root / "lecture.css")
    script_href = relative_href(output_file, asset_root / "lecture.js")
    prev_href = relative_href(output_file, output_root / prev_source.html_relative_path) if prev_source else ""
    next_href = relative_href(output_file, output_root / next_source.html_relative_path) if next_source else ""
    page_title = f"{rendered.title} | {source.module_label} Lecture"
    prev_nav = (
        f'<a class="lecture-button" data-lecture-prev data-variant="secondary" rel="prev" href="{escape(prev_href)}">Previous lecture</a>'
        if prev_source
        else '<a class="lecture-button is-disabled" data-lecture-prev data-variant="secondary" rel="prev" aria-disabled="true">Previous lecture</a>'
    )
    next_nav = (
        f'<a class="lecture-button" data-lecture-next data-variant="primary" rel="next" href="{escape(next_href)}">Next lecture</a>'
        if next_source
        else '<a class="lecture-button is-disabled" data-lecture-next data-variant="primary" rel="next" aria-disabled="true">Next lecture</a>'
    )
    prev_link_tag = f'\n    <link rel="prev" href="{escape(prev_href)}">' if prev_href else ""
    next_link_tag = f'\n    <link rel="next" href="{escape(next_href)}">' if next_href else ""
    if output_root / source.markdown_relative_path == source.markdown_path:
        source_action = (
            f'<a class="lecture-button" data-variant="secondary" '
            f'href="{escape(relative_href(output_file, output_root / source.markdown_relative_path))}">'
            "View source Markdown</a>"
        )
    else:
        source_action = (
            f'<span class="lecture-status-pill" aria-label="Source markdown path">'
            f"{escape(source.markdown_relative_path.as_posix())}</span>"
        )

    if output_root == repo_root:
        course_root_target = output_root / "slides" / "index.html"
        module_portal_target = (
            output_root / source.module_label / "lessons" / "slides" / "index.html"
        )
        day_overview_target = (
            output_root
            / source.module_label
            / "lessons"
            / "slides"
            / f"day-{source.day:02d}"
            / "index.html"
        )
    else:
        course_root_target = output_root / "index.html"
        module_portal_target = output_root / "slides" / source.module_id / "index.html"
        day_overview_target = (
            output_root / "slides" / source.module_id / f"day-{source.day:02d}" / "index.html"
        )

    course_root_href = relative_href(output_file, course_root_target)
    module_portal_href = relative_href(output_file, module_portal_target)
    day_overview_href = relative_href(output_file, day_overview_target)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(page_title)}</title>
    <meta name="generator" content="scripts/generate_lecture_pages.py">
    <meta name="lecture-module" content="{escape(source.module_id)}">
    <meta name="lecture-day" content="{source.day}">
    <meta name="lecture-hour" content="{source.hour}">
    <meta name="lecture-source" content="{escape(source.markdown_relative_path.as_posix())}">
{prev_link_tag}{next_link_tag}
    <link rel="stylesheet" href="{escape(stylesheet_href)}">
    <script defer src="{escape(script_href)}"></script>
</head>
<body class="lecture-page" data-page-kind="lecture" data-module="{escape(source.module_id)}" data-day="{source.day}" data-hour="{source.hour}">
    <a class="lecture-skip-link" href="#lecture-content">Skip to lecture content</a>
    <div class="lecture-shell">
        <nav class="lecture-breadcrumbs" aria-label="Breadcrumb">
            <a href="{escape(course_root_href)}">Course materials</a>
            <span class="lecture-breadcrumb-separator" aria-hidden="true">/</span>
            <a href="{escape(module_portal_href)}">{escape(source.module_label)}</a>
            <span class="lecture-breadcrumb-separator" aria-hidden="true">/</span>
            <a href="{escape(day_overview_href)}">Day {source.day}</a>
            <span class="lecture-breadcrumb-separator" aria-hidden="true">/</span>
            <span aria-current="page">Hour {source.hour}</span>
        </nav>
        <header class="lecture-header">
            <section class="lecture-hero">
                <span class="lecture-kicker">{escape(source.module_title)}</span>
                <h1 class="lecture-title">{escape(rendered.title)}</h1>
                <p class="lecture-summary">Long-form lecture page generated from the hourly Markdown source with stable section anchors and natural day/hour navigation.</p>
                <div class="lecture-meta" aria-label="Lecture metadata">
                    <span class="lecture-meta-item">Day {source.day}</span>
                    <span class="lecture-meta-item">Hour {source.hour}</span>
                    <span class="lecture-meta-item">Hourly lecture page</span>
                </div>
                <div class="lecture-actions">
                    {prev_nav}
                    {next_nav}
                    {source_action}
                </div>
            </section>
            <aside class="lecture-panel" aria-label="Lecture controls">
                <h2>Reading tools</h2>
                <div class="lecture-theme-row">
                    <label for="lecture-theme-select">Theme</label>
                    <select id="lecture-theme-select" data-theme-toggle>
                        <option value="auto">Auto</option>
                        <option value="light">Light</option>
                        <option value="dark">Dark</option>
                    </select>
                </div>
                <p class="lecture-status">Use ← and → to move between lectures. Press ? for the shortcut help.</p>
                <p class="lecture-status" data-lecture-current-section>Current section: lecture overview</p>
                <ul class="lecture-shortcuts-list">
                   <li><code>ArrowLeft</code> Previous lecture</li>
                   <li><code>ArrowRight</code> Next lecture</li>
                    <li><code>?</code> Shortcut help</li>
                    <li><code>Home</code> Top of page</li>
                    <li><code>End</code> Bottom of page</li>
                </ul>
            </aside>
        </header>
        <main id="lecture-content" class="lecture-layout" role="main" data-lecture-content>
            <article class="lecture-content" data-lecture-article>
                <div class="lecture-prose">
                    {rendered.html}
                </div>
                <nav class="lecture-nav" aria-label="Lecture navigation">
                    {prev_nav}
                    {next_nav}
                </nav>
            </article>
            <aside class="lecture-sidebar" aria-label="Lecture outline and tools">
                <section class="lecture-panel">
                    <h2>On this page</h2>
                    <div data-lecture-toc>
                        {render_toc(rendered.headings)}
                    </div>
                </section>
                <section class="lecture-panel">
                    <h2>Session reference</h2>
                    <div class="lecture-chip-list">
                        <span class="lecture-chip">{escape(source.markdown_path.name)}</span>
                        <span class="lecture-chip">{escape(source.module_label)}</span>
                    </div>
                    <p class="lecture-status">Generated from <code>{escape(source.markdown_relative_path.as_posix())}</code>.</p>
                </section>
            </aside>
        </main>
        <footer class="lecture-nav" aria-label="Lecture footer navigation">
            {prev_nav}
            {next_nav}
        </footer>
    </div>
</body>
</html>
"""


def ensure_assets(repo_root: Path, output_root: Path, *, check_only: bool) -> list[str]:
    source_asset_dir = repo_root / "slides" / "shared" / "lecture"
    output_asset_dir = output_root / "slides" / "shared" / "lecture"
    issues: list[str] = []

    for asset_name in ("lecture.css", "lecture.js"):
        source_path = source_asset_dir / asset_name
        if not source_path.is_file():
            issues.append(source_path.relative_to(repo_root).as_posix())
            continue

        if output_root == repo_root:
            continue

        output_path = output_asset_dir / asset_name
        if check_only:
            if not output_path.exists():
                issues.append(output_path.relative_to(output_root).as_posix())
                continue
            if output_path.read_text(encoding="utf-8") != source_path.read_text(encoding="utf-8"):
                issues.append(output_path.relative_to(output_root).as_posix())
            continue

        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, output_path)

    return issues


def generate(repo_root: Path, output_root: Path, module_filter: str, *, check_only: bool) -> int:
    sources = load_hourly_sources(repo_root, module_filter)
    grouped: dict[str, list[LectureSource]] = {module_id: [] for module_id in MODULES}
    for source in sources:
        grouped[source.module_id].append(source)

    stale_paths: list[str] = []
    for module_sources in grouped.values():
        for index, source in enumerate(module_sources):
            rendered = render_markdown(source.markdown_path.read_text(encoding="utf-8"))
            output_file = output_root / source.html_relative_path
            prev_source = module_sources[index - 1] if index > 0 else None
            next_source = module_sources[index + 1] if index + 1 < len(module_sources) else None
            html = render_page(
                source,
                rendered,
                repo_root=repo_root,
                output_file=output_file,
                output_root=output_root,
                prev_source=prev_source,
                next_source=next_source,
            )
            if check_only:
                if not output_file.exists() or output_file.read_text(encoding="utf-8") != html:
                    stale_paths.append(source.html_relative_path.as_posix())
                continue

            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(html, encoding="utf-8")

    asset_issues = ensure_assets(repo_root, output_root, check_only=check_only)
    if check_only:
        stale_paths.extend(asset_issues)
        if stale_paths:
            print("Lecture pages are out of date:", file=sys.stderr)
            for stale_path in stale_paths:
                print(f" - {stale_path}", file=sys.stderr)
            return 1
        print(f"Lecture pages are up to date for {len(sources)} hourly Markdown files.")
        return 0

    if asset_issues:
        print("Missing shared lecture assets:", file=sys.stderr)
        for issue in asset_issues:
            print(f" - {issue}", file=sys.stderr)
        return 1

    print(
        f"Generated {len(sources)} lecture pages under "
        f"{display_root(repo_root, output_root)}"
    )
    return 0


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    output_root = Path(args.output_root).resolve() if args.output_root else repo_root
    return generate(repo_root, output_root, args.module, check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
