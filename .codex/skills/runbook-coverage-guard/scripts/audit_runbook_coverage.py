#!/usr/bin/env python3
"""Audit and scaffold curriculum coverage artifacts for this repository."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Sequence

MODULE_TITLE = {
    "basics": "Basics",
    "advanced": "Advanced",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit lecture, assignment, and quiz coverage by module/day/hour."
    )
    parser.add_argument(
        "--module",
        choices=["basics", "advanced", "both"],
        default="both",
        help="Module scope to audit (default: both).",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=12,
        help="Number of days expected per module (default: 12).",
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=4,
        help="Number of hours expected per day for lecture files (default: 4).",
    )
    parser.add_argument(
        "--scaffold",
        default="",
        help="Comma-separated categories to scaffold: lecture,assignment,quiz,all.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite scaffold files when they already exist.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit report as JSON.",
    )
    return parser.parse_args()


def modules_to_check(module_arg: str) -> List[str]:
    if module_arg == "both":
        return ["basics", "advanced"]
    return [module_arg]


def normalize_scaffold(value: str) -> set[str]:
    if not value.strip():
        return set()
    parts = {item.strip().lower() for item in value.split(",") if item.strip()}
    if "all" in parts:
        return {"lecture", "assignment", "quiz"}
    return {item for item in parts if item in {"lecture", "assignment", "quiz"}}


def write_text(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def write_json(path: Path, obj: object, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    return True


def lecture_template(module_title: str, day: int, hour: int) -> str:
    return (
        f"# {module_title} Day {day} Hour {hour}\n\n"
        "## Learning Objectives\n\n"
        "- TODO: Add hour-specific objectives from instructor runbook.\n\n"
        "## Instructor Script\n\n"
        "TODO: Add instructor-ready narrative and examples.\n\n"
        "## Practice Activity\n\n"
        "TODO: Add a short guided exercise.\n\n"
        "## Checkpoint\n\n"
        "TODO: Add quick formative assessment prompts.\n"
    )


def assignment_notebook_template(module_title: str, day: int) -> Dict[str, object]:
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {module_title} Day {day} Homework\\n",
                    "\\n",
                    "Complete each task below using only concepts covered in class.\\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Write your Day homework solution code here.\\n"
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def criteria_template(module_key: str, day: int) -> Dict[str, object]:
    module_title = MODULE_TITLE[module_key]
    script_name = f"{module_key}_day{day}.py"
    return {
        "tests": [
            {
                "name": f"{module_title} Day {day} placeholder test",
                "command": f"python {script_name}",
                "stdin": "",
                "expected_stdout": "TODO",
                "points": 10,
            }
        ]
    }


def setup_template(module_key: str, day: int) -> Dict[str, object]:
    script_name = f"{module_key}_day{day}.py"
    return {
        "install": ["python -m pip install nbconvert"],
        "pre_test": [
            f"jupyter nbconvert --to script submissions/*{MODULE_TITLE[module_key]}_Day{day}*.ipynb --output {script_name}",
            f"test -f {script_name}",
        ],
    }


def feedback_template(module_title: str, day: int) -> Dict[str, object]:
    return {
        "success": f"{module_title} Day {day}: all placeholder tests passed.",
        "failure": f"{module_title} Day {day}: review output format and expected values.",
    }


def quiz_html_template(module_title: str, day: int) -> str:
    return (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"utf-8\" />\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        f"  <title>{module_title} Day {day} Quiz</title>\n"
        "</head>\n"
        "<body>\n"
        f"  <h1>{module_title} Day {day} Quiz</h1>\n"
        "  <p>TODO: Add 20-40 questions and explanations.</p>\n"
        "  <script>\n"
        "    // Autograder compatibility placeholder. Replace with real answers.\n"
        "    const expectedAnswers = {\"1\": \"A\"};\n"
        "  </script>\n"
        "</body>\n"
        "</html>\n"
    )


def audit_module(root: Path, module_key: str, days: int, hours: int) -> Dict[str, object]:
    module_title = MODULE_TITLE[module_key]

    lecture_missing: List[str] = []
    assignment_missing: List[str] = []
    quiz_missing: List[str] = []

    lecture_expected = 0
    assignment_expected = 0
    quiz_expected = 0

    for day in range(1, days + 1):
        assignment_expected += 4
        quiz_expected += 1

        notebook_path = root / module_title / "assignments" / f"{module_title}_Day{day}_homework.ipynb"
        config_dir = root / module_title / "assignments" / f"{module_title}_Day{day}_homework"
        config_files = ["criteria.json", "setup.json", "feedback.json"]

        if not notebook_path.exists():
            assignment_missing.append(notebook_path.as_posix())

        for config_name in config_files:
            config_path = config_dir / config_name
            if not config_path.exists():
                assignment_missing.append(config_path.as_posix())

        quiz_html = root / module_title / "quizzes" / f"{module_title}_Day{day}_Quiz.html"
        if not quiz_html.exists():
            quiz_missing.append(quiz_html.as_posix())

        for hour in range(1, hours + 1):
            lecture_expected += 1
            lecture_path = (
                root
                / module_title
                / "lessons"
                / "lecture"
                / f"Day{day}_Hour{hour}_{module_title}.md"
            )
            if not lecture_path.exists():
                lecture_missing.append(lecture_path.as_posix())

    return {
        "module": module_title,
        "summary": {
            "lecture": {
                "expected": lecture_expected,
                "missing": len(lecture_missing),
                "present": lecture_expected - len(lecture_missing),
            },
            "assignment": {
                "expected": assignment_expected,
                "missing": len(assignment_missing),
                "present": assignment_expected - len(assignment_missing),
            },
            "quiz": {
                "expected": quiz_expected,
                "missing": len(quiz_missing),
                "present": quiz_expected - len(quiz_missing),
            },
        },
        "missing": {
            "lecture": lecture_missing,
            "assignment": assignment_missing,
            "quiz": quiz_missing,
        },
    }


def scaffold_module(
    root: Path,
    module_key: str,
    days: int,
    hours: int,
    categories: set[str],
    force: bool,
) -> Dict[str, List[str]]:
    module_title = MODULE_TITLE[module_key]
    created: Dict[str, List[str]] = {"lecture": [], "assignment": [], "quiz": []}

    for day in range(1, days + 1):
        if "assignment" in categories:
            notebook_path = root / module_title / "assignments" / f"{module_title}_Day{day}_homework.ipynb"
            if write_json(notebook_path, assignment_notebook_template(module_title, day), force):
                created["assignment"].append(notebook_path.as_posix())

            config_dir = root / module_title / "assignments" / f"{module_title}_Day{day}_homework"
            criteria_path = config_dir / "criteria.json"
            setup_path = config_dir / "setup.json"
            feedback_path = config_dir / "feedback.json"

            if write_json(criteria_path, criteria_template(module_key, day), force):
                created["assignment"].append(criteria_path.as_posix())
            if write_json(setup_path, setup_template(module_key, day), force):
                created["assignment"].append(setup_path.as_posix())
            if write_json(feedback_path, feedback_template(module_title, day), force):
                created["assignment"].append(feedback_path.as_posix())

        if "quiz" in categories:
            quiz_dir = root / module_title / "quizzes"
            quiz_html_path = quiz_dir / f"{module_title}_Day{day}_Quiz.html"

            if write_text(quiz_html_path, quiz_html_template(module_title, day), force):
                created["quiz"].append(quiz_html_path.as_posix())

        if "lecture" in categories:
            for hour in range(1, hours + 1):
                lecture_path = (
                    root
                    / module_title
                    / "lessons"
                    / "lecture"
                    / f"Day{day}_Hour{hour}_{module_title}.md"
                )
                if write_text(lecture_path, lecture_template(module_title, day, hour), force):
                    created["lecture"].append(lecture_path.as_posix())

    return created


def print_text_report(report: Dict[str, object]) -> None:
    print("Runbook Coverage Report")
    print("=======================")
    print(f"Scope: modules={', '.join(report['scope']['modules'])}, days={report['scope']['days']}, hours={report['scope']['hours']}")

    for module_report in report["modules"]:
        module = module_report["module"]
        print()
        print(f"[{module}]")
        for category in ("lecture", "assignment", "quiz"):
            summary = module_report["summary"][category]
            print(
                f"- {category}: present={summary['present']} missing={summary['missing']} expected={summary['expected']}"
            )
        for category in ("lecture", "assignment", "quiz"):
            missing_items = module_report["missing"][category]
            if missing_items:
                print(f"  missing {category} paths:")
                for path in missing_items:
                    print(f"  - {path}")

    created = report.get("scaffold_created", {})
    if created:
        print()
        print("Scaffold Created")
        print("----------------")
        for module, categories in created.items():
            print(f"{module}:")
            for category, paths in categories.items():
                print(f"- {category}: {len(paths)}")


def main() -> None:
    args = parse_args()

    if args.days <= 0:
        raise SystemExit("--days must be >= 1")
    if args.hours <= 0:
        raise SystemExit("--hours must be >= 1")

    root = Path.cwd()
    selected_modules = modules_to_check(args.module)
    scaffold_categories = normalize_scaffold(args.scaffold)

    module_reports: List[Dict[str, object]] = [
        audit_module(root, module_key, args.days, args.hours)
        for module_key in selected_modules
    ]

    report: Dict[str, object] = {
        "scope": {
            "modules": [MODULE_TITLE[key] for key in selected_modules],
            "days": args.days,
            "hours": args.hours,
        },
        "modules": module_reports,
    }

    if scaffold_categories:
        created: Dict[str, Dict[str, List[str]]] = {}
        for module_key in selected_modules:
            created[MODULE_TITLE[module_key]] = scaffold_module(
                root=root,
                module_key=module_key,
                days=args.days,
                hours=args.hours,
                categories=scaffold_categories,
                force=args.force,
            )
        report["scaffold_requested"] = sorted(scaffold_categories)
        report["scaffold_created"] = created
        module_reports = [
            audit_module(root, module_key, args.days, args.hours)
            for module_key in selected_modules
        ]
        report["modules"] = module_reports

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_text_report(report)


if __name__ == "__main__":
    main()
