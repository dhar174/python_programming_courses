#!/usr/bin/env python3
"""Insert instructor slide-change cues into hourly lecture Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


HOURLY_FILENAME_RE = re.compile(
    r"^Day(?P<day>\d+)_Hour(?P<hour>\d+)_(?P<module>Basics|Advanced)\.md$"
)
HEADING_RE = re.compile(r"^(?P<level>#{2,4})\s+(?P<title>.+?)\s*$")
HOUR_START_RE = re.compile(r"^hour\s+(?P<hour>\d+)(?:\s*[-:–—]\s*|\s*$)", re.IGNORECASE)
CUE_LINE_RE = re.compile(
    r"^\[Instructor slide change:\s*page=(?P<page>\d+);\s*title=(?P<title>[^\]]+?)\s*\]$"
)

ALWAYS_ALLOWED = ("hour_start", "learning_outcomes", "demo_start", "lab_start", "pitfalls", "quick_check")
EARLY_BASICS_ALLOWED = ("hour_start", "demo_start", "lab_start", "quick_check")
STOPWORDS = {
    "section",
    "part",
    "timing",
    "overview",
    "lecture",
    "course",
    "session",
    "minutes",
}
ANCHOR_PATTERNS = (
    ("learning_outcomes", re.compile(r"\b(learning outcomes|outcomes)\b", re.IGNORECASE)),
    ("demo_start", re.compile(r"\b(live demo|demo|worked example)\b", re.IGNORECASE)),
    ("lab_start", re.compile(r"\b(lab|hands on|hands-on|guided practice|checkpoint|rotation|drill circuit)\b", re.IGNORECASE)),
    ("quick_check", re.compile(r"\b(quick check|exit ticket|check for understanding)\b", re.IGNORECASE)),
    ("pitfalls", re.compile(r"\b(common pitfalls|troubleshooting|debugging)\b", re.IGNORECASE)),
)


@dataclass(frozen=True)
class Slide:
    page: int
    title: str
    hour: int | None
    anchor_type: str | None


@dataclass(frozen=True)
class HtmlSlide:
    page: int
    title: str


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root))
    parser.add_argument(
        "--module",
        choices=("all", "Basics", "Advanced"),
        default="all",
        help="Limit cue insertion to one module.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would change without writing them.",
    )
    return parser.parse_args()


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    collapsed = re.sub(r"[^a-z0-9]+", " ", ascii_value)
    tokens = [token for token in collapsed.split() if token and token not in STOPWORDS]
    return " ".join(tokens)


def classify_anchor(title: str) -> str | None:
    hour_match = HOUR_START_RE.match(title.strip())
    if hour_match:
        return "hour_start"
    for anchor_type, pattern in ANCHOR_PATTERNS:
        if pattern.search(title):
            return anchor_type
    return None


class SessionDeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[HtmlSlide] = []
        self._current_page: int | None = None
        self._capturing_title = False
        self._title_chunks: list[str] = []
        self._have_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {name: (value or "") for name, value in attrs}
        if tag == "section":
            classes = set(attr_map.get("class", "").split())
            if "slide" in classes:
                page_text = attr_map.get("data-slide-number", "").strip()
                try:
                    page = int(page_text) if page_text else len(self.slides) + 1
                except ValueError:
                    page = len(self.slides) + 1
                self._current_page = page
                self._capturing_title = False
                self._title_chunks = []
                self._have_title = False
                return
        if self._current_page is None:
            return
        if tag in {"h1", "h2", "h3"} and not self._have_title:
            self._capturing_title = True

    def handle_endtag(self, tag: str) -> None:
        if self._current_page is None:
            return
        if tag in {"h1", "h2", "h3"} and self._capturing_title:
            self._capturing_title = False
            self._have_title = True
            return
        if tag == "section":
            title = "".join(self._title_chunks).strip() or f"Slide {self._current_page}"
            self.slides.append(HtmlSlide(page=self._current_page, title=title))
            self._current_page = None
            self._capturing_title = False
            self._title_chunks = []
            self._have_title = False

    def handle_data(self, data: str) -> None:
        if self._capturing_title:
            self._title_chunks.append(data)


def parse_session_deck(deck_path: Path) -> list[Slide]:
    parser = SessionDeckParser()
    parser.feed(deck_path.read_text(encoding="utf-8"))
    parser.close()
    slides: list[Slide] = []
    current_hour: int | None = None
    relative_hour = 0
    for raw_slide in parser.slides:
        title = raw_slide.title
        hour_match = HOUR_START_RE.match(title.strip())
        if hour_match:
            relative_hour += 1
            current_hour = relative_hour
            anchor_type = "hour_start"
        else:
            anchor_type = classify_anchor(title)
        slides.append(
            Slide(
                page=raw_slide.page,
                title=title,
                hour=current_hour,
                anchor_type=anchor_type,
            )
        )
    return slides


def lecture_files(repo_root: Path, module_filter: str) -> list[Path]:
    files: list[Path] = []
    modules = ("Basics", "Advanced") if module_filter == "all" else (module_filter,)
    for module_name in modules:
        lecture_root = repo_root / module_name / "lessons" / "lecture"
        files.extend(sorted(path for path in lecture_root.glob("*.md") if HOURLY_FILENAME_RE.match(path.name)))
    return files


def deck_path_for_lecture(repo_root: Path, lecture_path: Path, day: int) -> Path:
    module_name = lecture_path.parts[-4]
    day_dir = f"day-{day:02d}"
    return repo_root / module_name / "lessons" / "slides" / day_dir / f"{day_dir}-session-{day}.html"


def heading_targets(lines: list[str]) -> list[tuple[int, int, str, str | None]]:
    targets: list[tuple[int, int, str, str | None]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match is None:
            continue
        level = len(match.group("level"))
        title = match.group("title").strip()
        targets.append((index, level, title, classify_anchor(title)))
    return targets


def clean_existing_cues(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    skip_blank = False
    for line in lines:
        if CUE_LINE_RE.fullmatch(line.strip()):
            skip_blank = True
            continue
        if skip_blank and not line.strip():
            skip_blank = False
            continue
        skip_blank = False
        cleaned.append(line)
    return cleaned


def pick_hour_slides(slides: list[Slide], lecture_hour: int) -> tuple[Slide | None, dict[str, Slide]]:
    by_hour = [slide for slide in slides if slide.hour == lecture_hour]
    first_slide = by_hour[0] if by_hour else None
    anchors: dict[str, Slide] = {}
    for slide in by_hour:
        if slide.anchor_type and slide.anchor_type not in anchors:
            anchors[slide.anchor_type] = slide
    return first_slide, anchors


def cue_line(slide: Slide) -> str:
    return f"[Instructor slide change: page={slide.page}; title={slide.title}]"


def update_lecture(lecture_path: Path, repo_root: Path, *, write: bool) -> tuple[bool, str]:
    match = HOURLY_FILENAME_RE.match(lecture_path.name)
    if match is None:
        return False, "skipped (not an hourly lecture)"

    day = int(match.group("day"))
    lecture_hour = int(match.group("hour"))
    module_name = match.group("module")
    deck_path = deck_path_for_lecture(repo_root, lecture_path, day)
    if not deck_path.is_file():
        return False, f"missing session deck: {deck_path.relative_to(repo_root)}"

    slides = parse_session_deck(deck_path)
    first_slide, anchor_slides = pick_hour_slides(slides, lecture_hour)
    if first_slide is None:
        return False, f"no session-deck slides found for hour {lecture_hour}"

    lines = clean_existing_cues(lecture_path.read_text(encoding="utf-8").splitlines())
    headings = heading_targets(lines)
    first_major_heading = next((index for index, level, _, _ in headings if level == 2), None)
    if first_major_heading is None and headings:
        first_major_heading = headings[0][0]
    if first_major_heading is None:
        return False, "no lecture headings found"

    allowed = EARLY_BASICS_ALLOWED if module_name == "Basics" and day <= 2 else ALWAYS_ALLOWED
    cues_by_index: dict[int, list[Slide]] = {}
    inserted_anchors: set[str] = set()
    last_page: int | None = None

    def add_cue(line_index: int, anchor_type: str, slide: Slide | None) -> None:
        nonlocal last_page
        if anchor_type in inserted_anchors or slide is None:
            return
        if last_page == slide.page:
            inserted_anchors.add(anchor_type)
            return
        cues_by_index.setdefault(line_index, []).append(slide)
        inserted_anchors.add(anchor_type)
        last_page = slide.page

    add_cue(first_major_heading, "hour_start", anchor_slides.get("hour_start", first_slide))

    for line_index, _, _, anchor_type in headings:
        if anchor_type is None or anchor_type not in allowed:
            continue
        add_cue(line_index, anchor_type, anchor_slides.get(anchor_type))

    if not cues_by_index:
        return False, "no cue anchors resolved"

    new_lines: list[str] = []
    for index, line in enumerate(lines):
        pending = cues_by_index.get(index)
        if pending:
            if new_lines and new_lines[-1].strip():
                new_lines.append("")
            for slide in pending:
                new_lines.append(cue_line(slide))
                new_lines.append("")
        new_lines.append(line)

    updated_text = "\n".join(new_lines).rstrip() + "\n"
    original_text = lecture_path.read_text(encoding="utf-8")
    if updated_text == original_text:
        return False, "already up to date"
    if write:
        lecture_path.write_text(updated_text, encoding="utf-8")
    return True, f"inserted {sum(len(value) for value in cues_by_index.values())} cue(s)"


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    failures: list[str] = []
    changes: list[str] = []

    for lecture_path in lecture_files(repo_root, args.module):
        try:
            changed, message = update_lecture(lecture_path, repo_root, write=not args.check)
        except Exception as exc:  # pragma: no cover - script-level error reporting
            failures.append(f"{lecture_path.relative_to(repo_root)}: {exc}")
            continue
        rel_path = lecture_path.relative_to(repo_root)
        if changed:
            changes.append(f"{rel_path}: {message}")
        elif message.startswith("missing") or message.startswith("no "):
            failures.append(f"{rel_path}: {message}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    if args.check:
        if changes:
            print("Lecture slide cues are out of date:")
            for change in changes:
                print(f" - {change}")
            return 1
        print("Lecture slide cues are up to date.")
        return 0

    if changes:
        print("Updated lecture slide cues:")
        for change in changes:
            print(f" - {change}")
    else:
        print("No lecture slide cue changes were needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
