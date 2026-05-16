#!/usr/bin/env python3
"""Validate the published portal artifact and root-entrypoint contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root))
    parser.add_argument("--site-root", default=str(repo_root / "_site"))
    return parser.parse_args()


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def require_file(path: Path, label: str, errors: list[str]) -> None:
    if not path.is_file():
        add_error(errors, f"Missing {label}: {path}")


def validate_repo_artifact(repo_root: Path, artifact: dict[str, object], label: str, errors: list[str]) -> None:
    if artifact.get("delivery") != "repo":
        return
    repo_path = artifact.get("repoPath")
    if repo_path and not (repo_root / str(repo_path)).is_file():
        add_error(errors, f"Missing repo artifact for {label}: {repo_root / str(repo_path)}")
    repo_paths = artifact.get("repoPaths") or []
    for item in repo_paths:
        if not (repo_root / str(item)).is_file():
            add_error(errors, f"Missing repo artifact for {label}: {repo_root / str(item)}")


def validate_pages_artifact(site_root: Path, artifact: dict[str, object], label: str, errors: list[str]) -> None:
    if artifact.get("delivery") != "pages":
        return
    href = artifact.get("href")
    if href and not (site_root / str(href)).is_file():
        add_error(errors, f"Missing published artifact for {label}: {site_root / str(href)}")
    downloads = artifact.get("downloads") or {}
    for format_name, relative_path in downloads.items():
        if relative_path and not (site_root / str(relative_path)).is_file():
            add_error(errors, f"Missing published {format_name} download for {label}: {site_root / str(relative_path)}")


def validate_manifest(repo_root: Path, site_root: Path, errors: list[str]) -> None:
    manifest_path = site_root / "slides" / "shared" / "portal" / "course-manifest.json"
    require_file(manifest_path, "published portal manifest", errors)
    if errors:
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    support_root = manifest.get("supportingPages", {}).get("root")
    if support_root != "index.html":
        add_error(errors, f"Unexpected supportingPages.root value: {support_root!r}")
    printable_index = manifest.get("supportingPages", {}).get("printableIndex")
    if printable_index:
        require_file(site_root / str(printable_index), "published printable index", errors)
    not_found = manifest.get("supportingPages", {}).get("notFound")
    if not_found:
        require_file(site_root / str(not_found), "published 404 page", errors)

    modules = manifest.get("modules", [])
    if not modules:
        add_error(errors, "Manifest contains no modules.")
        return

    for module in modules:
        landing_page = module.get("landingPage")
        if landing_page and not (site_root / str(landing_page)).is_file():
            add_error(errors, f"Missing module landing page for {module.get('id')}: {site_root / str(landing_page)}")

        primary_href = module.get("primaryHref")
        if primary_href and not (site_root / str(primary_href)).is_file():
            add_error(errors, f"Missing module primary href for {module.get('id')}: {site_root / str(primary_href)}")

        for day in module.get("days", []):
            validate_pages_artifact(site_root, day["artifacts"]["slides"], f"{module['id']} {day['id']} slides", errors)
            validate_repo_artifact(repo_root, day["artifacts"]["lecture"], f"{module['id']} {day['id']} lecture", errors)
            validate_repo_artifact(repo_root, day["artifacts"]["assignment"], f"{module['id']} {day['id']} assignment", errors)
            validate_repo_artifact(repo_root, day["artifacts"]["quiz"], f"{module['id']} {day['id']} quiz", errors)


def validate_root_decoupling(repo_root: Path, site_root: Path, errors: list[str]) -> None:
    published_root = site_root / "index.html"
    require_file(published_root, "published root entrypoint", errors)
    if errors:
        return

    root_html = published_root.read_text(encoding="utf-8")
    is_portal_root = 'data-portal-root="course"' in root_html
    is_redirect_fallback = 'http-equiv="refresh"' in root_html and "Redirecting to slides" in root_html and 'href="./' in root_html

    if not is_portal_root and not is_redirect_fallback:
        add_error(errors, "Published root entrypoint is neither the dedicated portal root nor the validated redirect fallback.")
    if is_portal_root and "slides/shared/portal/portal.css" not in root_html:
        add_error(errors, "Published root entrypoint does not reference the shared portal asset kit.")
    if is_portal_root and "Python Course Slides - Index" in root_html:
        add_error(errors, "Published root entrypoint still exposes the legacy Basics landing heading.")


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    site_root = Path(args.site_root).resolve()

    errors: list[str] = []
    require_file(site_root / "slides" / "shared" / "portal" / "portal.css", "published portal CSS", errors)
    require_file(site_root / "slides" / "shared" / "portal" / "portal.js", "published portal JS", errors)
    validate_manifest(repo_root, site_root, errors)
    validate_root_decoupling(repo_root, site_root, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Portal publish checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
