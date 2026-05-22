#!/usr/bin/env python3
"""Generate module resource index Markdown/HTML pages for published portal use."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import markdown


RESOURCE_TYPES = [
    ("videos", "videos.md", "Videos"),
    ("interactive", "interactive-web-apps.md", "Interactive apps"),
    ("infographics", "infographics.md", "Infographics"),
    ("flashcards", "flashcards.md", "Flashcards"),
    ("quizzes", "practice-quizzes.md", "Practice quizzes"),
    ("mind_maps", "mind-maps.md", "Mind maps"),
    ("notebooklm", "notebooklm.md", "NotebookLM"),
]

MODULES = [
    {
        "name": "Basics",
        "label": "Python Programming: Basic",
        "resource_dir": Path("Basics/lessons/resources"),
        "day_count": 12,
        "module_portal": "../slides/index.html",
    },
    {
        "name": "Advanced",
        "label": "Python Programming: Advanced",
        "resource_dir": Path("Advanced/lessons/resources"),
        "day_count": 12,
        "module_portal": "../slides/index.html",
    },
]

DAY_HEADING_RE = re.compile(r"^### Day (\d+)\b")
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")
MD_LINK_RE = re.compile(r'href="([^"#?]+)\.md([#?][^"]*)?"')


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root))
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated files are not up to date.",
    )
    return parser.parse_args()


def write_if_changed(path: Path, content: str, check: bool, changed: list[Path]) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    if check:
        changed.append(path)
        return
    path.write_text(content, encoding="utf-8")
    changed.append(path)


def ensure_day_hour_links(md_content: str) -> str:
    lines = md_content.splitlines()
    current_day: int | None = None
    output: list[str] = []
    for line in lines:
        match = DAY_HEADING_RE.match(line)
        if match:
            current_day = int(match.group(1))
            output.append(line)
            continue

        if "Back to resource hub" in line and "day-hour-index.md" not in line:
            line = line.replace(
                " · [Back to course portal](../../../slides/index.html)",
                " · [Day/hour resource map](day-hour-index.md) · [Back to course portal](../../../slides/index.html)",
            )
            line = line.replace(
                " · [course portal](../../../slides/index.html)",
                " · [day/hour resource map](day-hour-index.md) · [course portal](../../../slides/index.html)",
            )

        if current_day is not None:
            row_match = ROW_RE.match(line)
            if row_match and "<a id=" not in line:
                absolute_hour = int(row_match.group(1))
                hour_in_day = absolute_hour - ((current_day - 1) * 4)
                if 1 <= hour_in_day <= 4:
                    anchor = f"day-{current_day:02d}-hour-{hour_in_day:02d}"
                    line = re.sub(
                        r"^\|\s*\d+\s*\|",
                        f'| <a id="{anchor}"></a>{absolute_hour} |',
                        line,
                        count=1,
                    )

        output.append(line)

    normalized = "\n".join(output) + "\n"
    normalized = normalized.replace("(../slides/index.html)", "(../index.html)")
    normalized = normalized.replace("(../../../slides/index.html)", "(../../../index.html)")
    return normalized


def build_day_hour_index(module_name: str, module_label: str, day_count: int) -> str:
    lines: list[str] = []
    lines.append(f"# {module_name} day/hour resource index")
    lines.append("")
    lines.append(
        "[Back to resource hub][hub] · [Back to module portal][module-portal] · [Back to course portal][course-portal]"
    )
    lines.append("")
    lines.append(f"## Module — {module_label}")
    lines.append("")
    lines.append(
        "Use this page to jump from a specific Day/Hour directly to each resource index slot."
    )
    lines.append("All links are placeholders until concrete assets are added.")
    lines.append("")
    lines.append("<!-- Maintainer note: keep Day/Hour rows in order and update link refs in the definitions block. -->")
    lines.append("")

    for day in range(1, day_count + 1):
        start_hour = ((day - 1) * 4) + 1
        end_hour = start_hour + 3
        lines.append(f"<a id=\"day-{day:02d}\"></a>")
        lines.append(f"### Day {day} — Session {day} (Hours {start_hour}–{end_hour})")
        lines.append("")
        lines.append(
            "| Hour | Videos | Interactive apps | Infographics | Flashcards | Practice quizzes | Mind maps | NotebookLM |"
        )
        lines.append("|---|---|---|---|---|---|---|---|")
        for hour in range(1, 5):
            absolute = ((day - 1) * 4) + hour
            slot = f"day-{day:02d}-hour-{hour:02d}"
            lines.append(
                f"| <a id=\"{slot}\"></a>{absolute} | "
                f"[Video][videos-{slot}] | "
                f"[Interactive][interactive-{slot}] | "
                f"[Infographic][infographics-{slot}] | "
                f"[Flashcards][flashcards-{slot}] | "
                f"[Quiz][quizzes-{slot}] | "
                f"[Mind map][mind_maps-{slot}] | "
                f"[NotebookLM][notebooklm-{slot}] |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Link reference definitions")
    lines.append("")
    lines.append("<!-- Maintainer note: these refs are intentionally centralized for easier updates. -->")
    lines.append("")
    lines.append("[hub]: README.md")
    lines.append("[module-portal]: ../index.html")
    lines.append("[course-portal]: ../../../index.html")
    lines.append("")

    for key, filename, _ in RESOURCE_TYPES:
        for day in range(1, day_count + 1):
            for hour in range(1, 5):
                slot = f"day-{day:02d}-hour-{hour:02d}"
                lines.append(f"[{key}-{slot}]: {filename}#{slot}")
    lines.append("")
    return "\n".join(lines)


def markdown_to_html(md_content: str, title: str) -> str:
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
    )
    html_body = MD_LINK_RE.sub(lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html_body)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light dark;
    }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
      line-height: 1.6;
      background: #f5f7fb;
      color: #0f172a;
    }}
    main {{
      width: min(1180px, calc(100% - 32px));
      margin: 24px auto 48px;
      background: #fff;
      border: 1px solid #dbe3f1;
      border-radius: 16px;
      box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
      padding: 24px;
      overflow-x: auto;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 1rem 0;
    }}
    th, td {{
      border: 1px solid #d1d5db;
      padding: 0.4rem 0.55rem;
      text-align: left;
      vertical-align: top;
    }}
    a {{
      color: #1d4ed8;
    }}
    code {{
      background: #eef2ff;
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
    }}
  </style>
  <script>
    (function () {{
      var path = window.location.pathname;
      if (path.includes('/Basics/lessons/resources/') || path.includes('/Advanced/lessons/resources/')) {{
        document.addEventListener('DOMContentLoaded', function () {{
          document.querySelectorAll('a[href=\"../index.html\"]').forEach(function (node) {{
            node.setAttribute('href', '../slides/index.html');
          }});
          document.querySelectorAll('a[href=\"../../../index.html\"]').forEach(function (node) {{
            node.setAttribute('href', '../../../slides/index.html');
          }});
        }});
      }}
    }})();
  </script>
</head>
<body>
  <main>
{html_body}
  </main>
</body>
</html>
"""


def title_from_markdown(md_content: str, fallback: str) -> str:
    for line in md_content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    changed: list[Path] = []

    for module in MODULES:
        resource_dir = repo_root / module["resource_dir"]
        resource_dir.mkdir(parents=True, exist_ok=True)

        day_hour_content = build_day_hour_index(module["name"], module["label"], int(module["day_count"]))
        day_hour_path = resource_dir / "day-hour-index.md"
        write_if_changed(day_hour_path, day_hour_content, args.check, changed)

        for md_path in sorted(resource_dir.glob("*.md")):
            if md_path.name != "day-hour-index.md":
                enriched = ensure_day_hour_links(md_path.read_text(encoding="utf-8"))
                write_if_changed(md_path, enriched, args.check, changed)
                md_content = enriched
            else:
                md_content = day_hour_content if md_path == day_hour_path else md_path.read_text(encoding="utf-8")
                if md_path != day_hour_path:
                    write_if_changed(md_path, md_content, args.check, changed)

            title = title_from_markdown(md_content, md_path.stem)
            html = markdown_to_html(md_content, title)
            html_path = md_path.with_suffix(".html")
            write_if_changed(html_path, html, args.check, changed)

    if args.check and changed:
        for path in changed:
            print(f"Out-of-date generated file: {path}")
        return 1

    if not args.check:
        print(f"Updated {len(changed)} generated resource file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
