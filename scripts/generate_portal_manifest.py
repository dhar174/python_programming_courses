#!/usr/bin/env python3
"""Generate the static portal manifest for the course site."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPOSITORY = {
    "owner": "dhar174",
    "name": "python_programming_courses",
    "defaultBranch": "main",
}

MODULES = (
    {
        "id": "basics",
        "title": "Python Programming: Basic",
        "source_root": "Basics/lessons/slides",
        "lecture_pattern": "Basics/lessons/lecture/Day{day}_Hour*_Basics.md",
        "assignment_path": "Basics/assignments/Basics_Day{day}_homework.ipynb",
        "quiz_path": "Basics/quizzes/Basics_Day{day}_Quiz.html",
    },
    {
        "id": "advanced",
        "title": "Python Programming: Advanced",
        "source_root": "Advanced/lessons/slides",
        "lecture_pattern": "Advanced/lessons/lecture/Day{day}_Hour*_Advanced.md",
        "assignment_path": "Advanced/assignments/Advanced_Day{day}_homework.ipynb",
        "quiz_path": "Advanced/quizzes/Advanced_Day{day}_Quiz.html",
    },
)

DOWNLOAD_SUFFIXES = {
    "html": ".html",
    "pdf": ".pdf",
    "pptx": ".pptx",
    "png": ".png",
}


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    default_output = repo_root / "slides" / "shared" / "portal" / "course-manifest.json"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root))
    parser.add_argument("--site-root", help="Optional _site directory for published artifact discovery.")
    parser.add_argument("--output", default=str(default_output))
    return parser.parse_args()


def find_primary_html(day_dir: Path) -> Path | None:
    html_files = sorted(
        path
        for path in day_dir.glob("*.html")
        if path.name.lower() not in {"index.html", "readme.html"}
    )
    return html_files[0] if html_files else None


def build_downloads(
    *,
    published_dir: str,
    stem: str,
    site_root: Path | None,
) -> dict[str, str | None]:
    downloads: dict[str, str | None] = {}
    for format_name, suffix in DOWNLOAD_SUFFIXES.items():
        relative_path = f"{published_dir}{stem}{suffix}"
        if format_name == "html":
            downloads[format_name] = relative_path
            continue
        if site_root and (site_root / relative_path).is_file():
            downloads[format_name] = relative_path
        else:
            downloads[format_name] = None
    return downloads


def build_repo_artifact(
    *,
    present: bool,
    repo_path: str | None,
    repo_paths: list[str] | None = None,
) -> dict[str, object]:
    artifact: dict[str, object] = {
        "present": present,
        "delivery": "repo" if present else "none",
        "repoPath": repo_path if present else None,
        "href": None,
    }
    if repo_paths:
        artifact["repoPaths"] = repo_paths
        artifact["count"] = len(repo_paths)
    return artifact


def build_pages_artifact(
    *,
    published_href: str | None,
    source_path: str | None,
    site_root: Path | None,
) -> dict[str, object]:
    present = published_href is not None
    downloads = {
        format_name: None for format_name in DOWNLOAD_SUFFIXES
    }
    if present and published_href:
        published_path = Path(published_href)
        downloads = build_downloads(
            published_dir=f"{published_path.parent.as_posix()}/",
            stem=published_path.stem,
            site_root=site_root,
        )
    return {
        "present": present,
        "delivery": "pages" if present else "none",
        "href": published_href,
        "sourcePath": source_path,
        "downloads": downloads,
    }


def build_day(
    *,
    repo_root: Path,
    site_root: Path | None,
    module: dict[str, str],
    day_number: int,
    total_days: int,
) -> dict[str, object]:
    day_id = f"day-{day_number:02d}"
    source_day_dir = repo_root / module["source_root"] / day_id
    primary_html = find_primary_html(source_day_dir) if source_day_dir.is_dir() else None
    published_dir = f"slides/{module['id']}/{day_id}/"
    primary_href = f"{published_dir}{primary_html.name}" if primary_html else None
    source_primary_href = primary_html.relative_to(repo_root).as_posix() if primary_html else None

    lecture_paths = sorted(
        path.relative_to(repo_root).as_posix()
        for path in repo_root.glob(module["lecture_pattern"].format(day=day_number))
    )
    assignment_path = module["assignment_path"].format(day=day_number)
    quiz_path = module["quiz_path"].format(day=day_number)
    assignment_present = (repo_root / assignment_path).is_file()
    quiz_present = (repo_root / quiz_path).is_file()

    day_entry: dict[str, object] = {
        "id": day_id,
        "dayNumber": day_number,
        "title": f"Day {day_number}",
        "order": day_number,
        "primaryHref": primary_href,
        "sourcePrimaryHref": source_primary_href,
        "breadcrumbs": [
            {"label": "Course", "href": "index.html"},
            {"label": module["title"], "href": f"slides/{module['id']}/index.html"},
            {"label": f"Day {day_number}", "href": primary_href},
        ],
        "prev": None,
        "next": None,
        "artifacts": {
            "slides": build_pages_artifact(
                published_href=primary_href,
                source_path=source_primary_href,
                site_root=site_root,
            ),
            "lecture": build_repo_artifact(
                present=bool(lecture_paths),
                repo_path=lecture_paths[0] if lecture_paths else None,
                repo_paths=lecture_paths or None,
            ),
            "assignment": build_repo_artifact(
                present=assignment_present,
                repo_path=assignment_path if assignment_present else None,
            ),
            "quiz": build_repo_artifact(
                present=quiz_present,
                repo_path=quiz_path if quiz_present else None,
            ),
        },
    }

    if day_number > 1:
        prev_id = f"day-{day_number - 1:02d}"
        day_entry["prev"] = {
            "label": f"Day {day_number - 1}",
            "href": f"slides/{module['id']}/{prev_id}/",
        }
    if day_number < total_days:
        next_id = f"day-{day_number + 1:02d}"
        day_entry["next"] = {
            "label": f"Day {day_number + 1}",
            "href": f"slides/{module['id']}/{next_id}/",
        }

    return day_entry


def fill_navigation(days: list[dict[str, object]]) -> None:
    for index, day in enumerate(days):
        primary_href = day.get("primaryHref")
        if index > 0:
            prev_day = days[index - 1]
            day["prev"] = {
                "label": f"Day {prev_day['dayNumber']}",
                "href": prev_day.get("primaryHref") or prev_day["breadcrumbs"][-1]["href"],
            }
        if index < len(days) - 1:
            next_day = days[index + 1]
            day["next"] = {
                "label": f"Day {next_day['dayNumber']}",
                "href": next_day.get("primaryHref") or next_day["breadcrumbs"][-1]["href"],
            }
        day["breadcrumbs"][-1]["href"] = primary_href


def build_module(
    *,
    repo_root: Path,
    site_root: Path | None,
    module: dict[str, str],
    order: int,
) -> dict[str, object]:
    source_root = repo_root / module["source_root"]
    days = [
        build_day(
            repo_root=repo_root,
            site_root=site_root,
            module=module,
            day_number=day_number,
            total_days=12,
        )
        for day_number in range(1, 13)
    ]
    fill_navigation(days)

    module_index = source_root / "index.html"
    landing_page = f"slides/{module['id']}/index.html" if module_index.is_file() else None
    source_landing_page = module_index.relative_to(repo_root).as_posix() if module_index.is_file() else None
    primary_href = landing_page or next(
        (day["primaryHref"] for day in days if day.get("primaryHref")),
        None,
    )
    source_primary_href = source_landing_page or next(
        (day["sourcePrimaryHref"] for day in days if day.get("sourcePrimaryHref")),
        None,
    )

    return {
        "id": module["id"],
        "title": module["title"],
        "order": order,
        "sourceRoot": module["source_root"],
        "publishedRoot": f"slides/{module['id']}/",
        "landingPage": landing_page,
        "primaryHref": primary_href,
        "sourceLandingPage": source_landing_page,
        "sourcePrimaryHref": source_primary_href,
        "theme": "portal",
        "stats": {
            "days": len(days),
            "slides": sum(1 for day in days if day["artifacts"]["slides"]["present"]),
            "lectures": sum(1 for day in days if day["artifacts"]["lecture"]["present"]),
            "assignments": sum(1 for day in days if day["artifacts"]["assignment"]["present"]),
            "quizzes": sum(1 for day in days if day["artifacts"]["quiz"]["present"]),
        },
        "days": days,
    }


def build_manifest(repo_root: Path, site_root: Path | None) -> dict[str, object]:
    modules = [
        build_module(
            repo_root=repo_root,
            site_root=site_root,
            module=module,
            order=index,
        )
        for index, module in enumerate(MODULES, start=1)
    ]

    return {
        "version": 1,
        "repository": REPOSITORY,
        "supportingPages": {
            "root": "index.html",
            "printableIndex": "slides/printable-index.html",
            "notFound": "404.html",
        },
        "stats": {
            "modules": len(modules),
            "days": sum(module["stats"]["days"] for module in modules),
            "slides": sum(module["stats"]["slides"] for module in modules),
            "lectures": sum(module["stats"]["lectures"] for module in modules),
            "assignments": sum(module["stats"]["assignments"] for module in modules),
            "quizzes": sum(module["stats"]["quizzes"] for module in modules),
        },
        "modules": modules,
    }


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    site_root = Path(args.site_root).resolve() if args.site_root else None
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(repo_root=repo_root, site_root=site_root)
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
