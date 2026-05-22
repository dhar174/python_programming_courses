#!/usr/bin/env python3
"""Validate generated hourly lecture HTML pages."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


LECTURE_HTML_RE = re.compile(
    r"^(?:Day\d+_Hour\d+_(?:Basics|Advanced)|\d+-[a-z0-9-]+)\.html$"
)
UNSAFE_RUNTIME_PATTERNS = {
    "fetch": re.compile(r"\bfetch\s*\(", re.IGNORECASE),
    "XMLHttpRequest": re.compile(r"\bXMLHttpRequest\b"),
    "WebSocket": re.compile(r"\bWebSocket\b"),
    "serviceWorker": re.compile(r"\b(?:navigator\.)?serviceWorker(?:\.register)?\b"),
}
REMOTE_PREFIXES = ("http://", "https://", "//")
REMOTE_LINK_RELS = {
    "stylesheet",
    "preload",
    "modulepreload",
    "prefetch",
    "preconnect",
    "dns-prefetch",
}


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(repo_root)],
        help="Lecture HTML files or directories to validate. Defaults to the repository root.",
    )
    return parser.parse_args()


def is_remote_url(value: str) -> bool:
    return value.startswith(REMOTE_PREFIXES)


def is_lecture_output_path(path: Path) -> bool:
    normalized_parts = [part.lower() for part in path.parts]
    return "lessons" in normalized_parts and "lecture" in normalized_parts


class LectureHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self._title_chunks: list[str] = []
        self._in_title = False
        self.id_counts: dict[str, int] = {}
        self.fragment_refs: list[str] = []
        self.skip_targets: list[str] = []
        self.main_ids: list[str] = []
        self.prev_hooks = 0
        self.next_hooks = 0
        self.remote_assets: list[str] = []
        self.slide_cue_count = 0
        self.slide_cue_link_count = 0

    @property
    def title_text(self) -> str:
        return "".join(self._title_chunks).strip()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {name: (value or "") for name, value in attrs}

        identifier = attr_map.get("id", "").strip()
        if identifier:
            self.id_counts[identifier] = self.id_counts.get(identifier, 0) + 1

        if tag == "html":
            self.html_lang = attr_map.get("lang", "").strip()
        elif tag == "title":
            self._in_title = True
        elif tag == "main":
            self.main_ids.append(identifier)
        elif tag == "a":
            href = attr_map.get("href", "").strip()
            classes = set(attr_map.get("class", "").split())
            rels = set(attr_map.get("rel", "").split())
            if href.startswith("#") and len(href) > 1:
                fragment = href[1:]
                self.fragment_refs.append(fragment)
                if "lecture-skip-link" in classes:
                    self.skip_targets.append(fragment)
            if "prev" in rels or "data-lecture-prev" in attr_map:
                self.prev_hooks += 1
            if "next" in rels or "data-lecture-next" in attr_map:
                self.next_hooks += 1
            if "data-slide-deck-link" in attr_map and href:
                self.slide_cue_link_count += 1
        elif tag == "link":
            href = attr_map.get("href", "").strip()
            rels = {part.lower() for part in attr_map.get("rel", "").split()}
            if href.startswith("#") and len(href) > 1:
                self.fragment_refs.append(href[1:])
            if "prev" in rels:
                self.prev_hooks += 1
            if "next" in rels:
                self.next_hooks += 1
            if href and rels.intersection(REMOTE_LINK_RELS) and is_remote_url(href):
                self.remote_assets.append(f"<link href=\"{href}\">")
        elif tag == "script":
            src = attr_map.get("src", "").strip()
            if src and is_remote_url(src):
                self.remote_assets.append(f"<script src=\"{src}\">")
        elif tag == "iframe":
            src = attr_map.get("src", "").strip()
            if src and is_remote_url(src):
                self.remote_assets.append(f"<iframe src=\"{src}\">")
        elif tag == "embed":
            src = attr_map.get("src", "").strip()
            if src and is_remote_url(src):
                self.remote_assets.append(f"<embed src=\"{src}\">")
        elif tag == "object":
            data = attr_map.get("data", "").strip()
            if data and is_remote_url(data):
                self.remote_assets.append(f"<object data=\"{data}\">")
        elif tag == "aside":
            if "data-slide-cue" in attr_map:
                self.slide_cue_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_chunks.append(data)


def discover_lecture_files(paths: list[str]) -> list[Path]:
    lecture_files: list[Path] = []
    seen: set[Path] = set()

    for raw_path in paths:
        candidate = Path(raw_path).resolve()
        if candidate.is_file():
            if (
                LECTURE_HTML_RE.match(candidate.name)
                and is_lecture_output_path(candidate)
                and candidate not in seen
            ):
                lecture_files.append(candidate)
                seen.add(candidate)
            continue

        if not candidate.is_dir():
            continue

        for html_path in sorted(candidate.rglob("*.html")):
            if (
                LECTURE_HTML_RE.match(html_path.name)
                and is_lecture_output_path(html_path)
                and html_path not in seen
            ):
                lecture_files.append(html_path)
                seen.add(html_path)

    return lecture_files


def validate_file(path: Path) -> list[str]:
    html_text = path.read_text(encoding="utf-8")
    parser = LectureHtmlParser()
    parser.feed(html_text)
    parser.close()

    errors: list[str] = []
    if not parser.html_lang:
        errors.append("missing <html lang>")
    if not parser.title_text:
        errors.append("missing non-empty <title>")
    if len(parser.main_ids) != 1:
        errors.append(f"expected exactly one <main>; found {len(parser.main_ids)}")
    else:
        main_id = parser.main_ids[0]
        if not main_id:
            errors.append("main landmark is missing an id for skip-link targeting")
        elif main_id not in parser.skip_targets:
            errors.append(f'missing skip link targeting main id "#{main_id}"')

    duplicates = sorted(identifier for identifier, count in parser.id_counts.items() if count > 1)
    if duplicates:
        errors.append(f"duplicate ids found: {', '.join(duplicates)}")

    known_ids = set(parser.id_counts)
    missing_fragments = sorted(fragment for fragment in parser.fragment_refs if fragment not in known_ids)
    if missing_fragments:
        errors.append(
            "fragment links target missing ids: " + ", ".join(f"#{fragment}" for fragment in missing_fragments)
        )

    if parser.prev_hooks == 0:
        errors.append("missing previous-lecture navigation hook")
    if parser.next_hooks == 0:
        errors.append("missing next-lecture navigation hook")
    if parser.remote_assets:
        errors.append("remote runtime/static asset refs found: " + ", ".join(parser.remote_assets))
    if parser.slide_cue_count == 0:
        errors.append("missing instructor slide cues")
    elif parser.slide_cue_link_count < parser.slide_cue_count:
        errors.append(
            "one or more instructor slide cues are missing deep links into the session deck"
        )

    unsafe_runtime_hits = [
        label for label, pattern in UNSAFE_RUNTIME_PATTERNS.items() if pattern.search(html_text)
    ]
    if unsafe_runtime_hits:
        errors.append("offline-unsafe runtime API usage found: " + ", ".join(unsafe_runtime_hits))

    return errors


def main() -> int:
    args = parse_args()
    lecture_files = discover_lecture_files(args.paths)
    if not lecture_files:
        print("No hourly lecture HTML files were found for validation.", file=sys.stderr)
        return 2

    failures = 0
    for lecture_file in lecture_files:
        errors = validate_file(lecture_file)
        if not errors:
            continue
        failures += 1
        for error in errors:
            print(f"ERROR: {lecture_file}: {error}", file=sys.stderr)

    if failures:
        print(f"Lecture HTML validation failed for {failures} file(s).", file=sys.stderr)
        return 1

    print(f"Lecture HTML validation passed for {len(lecture_files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
