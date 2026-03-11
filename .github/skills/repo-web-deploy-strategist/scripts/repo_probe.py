#!/usr/bin/env python3
"""Collect repository deployment signals and heuristics for web deployment planning."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

MAX_LIST_ITEMS = 200


def run_cmd(command: list[str], cwd: Path, timeout: int = 30) -> dict[str, Any]:
    """Run a command and return a normalized result object."""
    try:
        completed = subprocess.run(  # noqa: S603
            command,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except Exception as exc:  # pragma: no cover - defensive for environment issues
        return {
            "ok": False,
            "returncode": None,
            "stdout": "",
            "stderr": str(exc),
        }

    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def read_text(path: Path) -> str:
    """Read a text file with tolerant UTF-8 fallback behavior."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def normalize_path(value: str) -> str:
    """Normalize relative paths for stable comparisons."""
    text = value.strip().strip("\"'")
    text = text.replace("\\", "/")
    text = re.sub(r"^\./", "", text)
    return text.rstrip("/")


def parse_github_slug(remote_url: str) -> dict[str, str] | None:
    """Extract owner/repo from common GitHub remote URL formats."""
    patterns = [
        r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$",
        r"https?://[^@]+@github\.com/(?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, remote_url)
        if match:
            return {
                "owner": match.group("owner"),
                "repo": match.group("repo"),
                "slug": f"{match.group('owner')}/{match.group('repo')}",
            }
    return None


def parse_marp_config(path: Path, root: Path) -> dict[str, Any]:
    """Parse key fields from Marp YAML config files without external dependencies."""
    content = read_text(path)
    input_match = re.search(r"(?m)^\s*inputDir\s*:\s*['\"]?([^'\"\n]+)", content)
    output_match = re.search(r"(?m)^\s*output\s*:\s*['\"]?([^'\"\n]+)", content)

    return {
        "path": str(path.relative_to(root)).replace("\\", "/"),
        "input_dir": normalize_path(input_match.group(1)) if input_match else None,
        "output": normalize_path(output_match.group(1)) if output_match else None,
    }


def parse_workflow(path: Path, root: Path) -> dict[str, Any]:
    """Extract deployment-relevant signals from a workflow file."""
    text = read_text(path)
    lines = text.splitlines()

    actions_used = sorted(set(re.findall(r"(?m)^\s*uses:\s*([^\s#]+)", text)))
    secret_refs = sorted(set(re.findall(r"secrets\.([A-Za-z0-9_]+)", text)))

    triggers = []
    for trigger in ("push", "pull_request", "workflow_dispatch", "schedule", "release"):
        if re.search(rf"(?m)^\s*{re.escape(trigger)}\s*:", text):
            triggers.append(trigger)

    artifact_paths: list[str] = []
    marp_config_files: list[str] = []
    current_action = ""

    for raw_line in lines:
        stripped = raw_line.strip()

        action_match = re.match(r"uses:\s*([^\s#]+)", stripped)
        if action_match:
            current_action = action_match.group(1).lower()
            continue

        path_match = re.match(r"path:\s*([^#]+)", stripped)
        if path_match and "upload-pages-artifact" in current_action:
            artifact_paths.append(normalize_path(path_match.group(1)))

        config_match = re.match(r"config-file:\s*([^#]+)", stripped)
        if config_match and "marp-cli-action" in current_action:
            marp_config_files.append(normalize_path(config_match.group(1)))

    uses_pages = any(
        marker in text
        for marker in (
            "actions/configure-pages",
            "actions/upload-pages-artifact",
            "actions/deploy-pages",
        )
    )

    uses_gh_pat = bool(re.search(r"secrets\.GH_PAT", text))

    return {
        "name": path.name,
        "path": str(path.relative_to(root)).replace("\\", "/"),
        "triggers": triggers,
        "actions_used": actions_used,
        "secrets_referenced": secret_refs,
        "uses_pages_actions": uses_pages,
        "uses_gh_pat": uses_gh_pat,
        "artifact_paths": sorted(set(artifact_paths)),
        "marp_config_files": sorted(set(marp_config_files)),
    }


def safe_json_load(text: str) -> Any:
    """Parse JSON safely and return None on failure."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def collect_live_github_data(root: Path, slug: dict[str, str] | None, no_gh: bool) -> dict[str, Any]:
    """Collect GitHub live data when gh CLI is available and authenticated."""
    live: dict[str, Any] = {
        "enabled": not no_gh,
        "available": False,
        "auth_ok": False,
        "reason": None,
        "pages": None,
        "workflows": None,
        "secrets": None,
        "recent_runs": None,
    }

    if no_gh:
        live["reason"] = "disabled_by_flag"
        return live

    if shutil.which("gh") is None:
        live["reason"] = "gh_cli_not_found"
        return live

    live["available"] = True

    auth = run_cmd(["gh", "auth", "status"], root)
    if not auth["ok"]:
        live["reason"] = "gh_auth_not_available"
        return live

    live["auth_ok"] = True

    if not slug:
        live["reason"] = "github_remote_not_detected"
        return live

    repo_slug = slug["slug"]

    pages = run_cmd(["gh", "api", f"repos/{repo_slug}/pages"], root)
    workflows = run_cmd(["gh", "api", f"repos/{repo_slug}/actions/workflows"], root)
    secrets = run_cmd(["gh", "api", f"repos/{repo_slug}/actions/secrets"], root)
    runs = run_cmd(["gh", "api", f"repos/{repo_slug}/actions/runs?per_page=10"], root)

    live["pages"] = safe_json_load(pages["stdout"]) if pages["ok"] else {"error": pages["stderr"]}
    live["workflows"] = (
        safe_json_load(workflows["stdout"]) if workflows["ok"] else {"error": workflows["stderr"]}
    )
    live["secrets"] = safe_json_load(secrets["stdout"]) if secrets["ok"] else {"error": secrets["stderr"]}
    live["recent_runs"] = safe_json_load(runs["stdout"]) if runs["ok"] else {"error": runs["stderr"]}

    return live


def collect_heuristics(
    workflows: list[dict[str, Any]],
    marp_configs: list[dict[str, Any]],
    root: Path,
) -> dict[str, Any]:
    """Derive deployment heuristics and warnings from gathered signals."""
    warnings: list[dict[str, str]] = []
    checks: list[dict[str, str]] = []

    marp_outputs = [cfg["output"] for cfg in marp_configs if cfg.get("output")]
    marp_inputs = [cfg["input_dir"] for cfg in marp_configs if cfg.get("input_dir")]

    for wf in workflows:
        if wf.get("uses_gh_pat"):
            warnings.append(
                {
                    "id": "pat-token-usage",
                    "workflow": wf["path"],
                    "message": "Workflow references GH_PAT. Prefer GITHUB_TOKEN unless a PAT is strictly required.",
                }
            )

        for artifact_path in wf.get("artifact_paths", []):
            if marp_outputs and not any(
                normalize_path(output).startswith(normalize_path(artifact_path))
                or normalize_path(artifact_path).startswith(normalize_path(output))
                for output in marp_outputs
            ):
                warnings.append(
                    {
                        "id": "artifact-output-mismatch",
                        "workflow": wf["path"],
                        "message": (
                            f"Upload artifact path '{artifact_path}' does not align with discovered Marp outputs {marp_outputs}."
                        ),
                    }
                )

    for input_dir in marp_inputs:
        normalized = normalize_path(input_dir)
        if normalized in {"", "."}:
            warnings.append(
                {
                    "id": "overbuild-risk",
                    "workflow": "n/a",
                    "message": "Marp inputDir targets repository root. Narrow scope to intended slide/content directories.",
                }
            )
            continue

        target_dir = (root / normalized).resolve()
        if target_dir.exists() and target_dir.is_dir():
            md_count = sum(1 for _ in target_dir.rglob("*.md"))
            checks.append(
                {
                    "id": "marp-input-scope",
                    "status": "observed",
                    "message": f"{normalized} contains {md_count} markdown files.",
                }
            )
            if md_count > 250:
                warnings.append(
                    {
                        "id": "large-input-scope",
                        "workflow": "n/a",
                        "message": (
                            f"Marp inputDir '{normalized}' includes {md_count} markdown files; consider narrowing build scope."
                        ),
                    }
                )

    if not warnings:
        checks.append(
            {
                "id": "heuristics-clean",
                "status": "ok",
                "message": "No deployment heuristic warnings detected.",
            }
        )

    return {"warnings": warnings, "checks": checks}


def detect_runtime_signals(root: Path) -> dict[str, Any]:
    """Detect high-level framework/runtime signals from common files."""
    checks = {
        "python": ["pyproject.toml", "requirements.txt", "setup.py", "Pipfile"],
        "node": ["package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json"],
        "docker": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
        "marp": [".marprc.yml", ".marprc.yaml", "marp.config.ts", "marp.config.mjs"],
        "mkdocs": ["mkdocs.yml", "mkdocs.yaml"],
        "hugo": ["hugo.toml", "config.toml"],
        "jekyll": ["_config.yml"],
    }

    found: dict[str, list[str]] = {}
    for key, filenames in checks.items():
        matches = [name for name in filenames if (root / name).exists()]
        if matches:
            found[key] = matches

    framework_hints = {
        "nextjs": (root / "next.config.js").exists() or (root / "next.config.mjs").exists(),
        "django": (root / "manage.py").exists(),
        "flask": (root / "app.py").exists() or (root / "wsgi.py").exists(),
        "fastapi": any((root / candidate).exists() for candidate in ("main.py", "app/main.py")),
    }

    return {
        "manifests": found,
        "framework_hints": framework_hints,
    }


def build_probe(repo_path: Path, no_gh: bool) -> dict[str, Any]:
    """Build the full repository probe payload."""
    root = repo_path.resolve()
    if not root.exists() or not root.is_dir():
        raise FileNotFoundError(f"Repository path does not exist: {root}")

    git_branch = run_cmd(["git", "branch", "--show-current"], root)
    git_origin = run_cmd(["git", "remote", "get-url", "origin"], root)

    slug = parse_github_slug(git_origin["stdout"]) if git_origin["ok"] else None

    top_dirs = sorted(
        [entry.name for entry in root.iterdir() if entry.is_dir() and not entry.name.startswith(".")]
    )[:MAX_LIST_ITEMS]
    top_files = sorted(
        [entry.name for entry in root.iterdir() if entry.is_file() and not entry.name.startswith(".")]
    )[:MAX_LIST_ITEMS]

    github_dir = root / ".github"
    github_files: list[str] = []
    if github_dir.exists():
        github_files = sorted(
            str(path.relative_to(root)).replace("\\", "/")
            for path in github_dir.rglob("*")
            if path.is_file()
        )[:MAX_LIST_ITEMS]

    workflow_dir = github_dir / "workflows"
    workflow_paths = sorted(workflow_dir.glob("*.y*ml")) if workflow_dir.exists() else []
    workflows = [parse_workflow(path, root) for path in workflow_paths]

    marp_config_paths = sorted(root.glob(".marprc*.yml")) + sorted(root.glob(".marprc*.yaml"))
    marp_configs = [parse_marp_config(path, root) for path in marp_config_paths]

    runtime_signals = detect_runtime_signals(root)
    heuristics = collect_heuristics(workflows, marp_configs, root)
    live = collect_live_github_data(root, slug, no_gh)

    return {
        "repo": {
            "path": str(root),
            "name": root.name,
            "git": {
                "branch": git_branch["stdout"] if git_branch["ok"] else None,
                "origin": git_origin["stdout"] if git_origin["ok"] else None,
                "github_slug": slug["slug"] if slug else None,
            },
        },
        "inventory": {
            "top_level_dirs": top_dirs,
            "top_level_files": top_files,
            "github_files": github_files,
            "workflow_count": len(workflows),
            "marp_config_count": len(marp_configs),
        },
        "signals": runtime_signals,
        "marp_configs": marp_configs,
        "workflows": workflows,
        "live": live,
        "heuristics": heuristics,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Collect repository deployment signals and emit machine-readable JSON.",
    )
    parser.add_argument("--repo", default=".", help="Repository path (default: current directory)")
    parser.add_argument(
        "--no-gh",
        action="store_true",
        help="Skip GitHub live checks even if gh CLI is available.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    args = parser.parse_args()

    try:
        probe = build_probe(Path(args.repo), args.no_gh)
    except FileNotFoundError as exc:
        print(json.dumps({"error": str(exc)}, indent=2), flush=True)
        return 1

    output = json.dumps(probe, indent=2 if args.pretty else None, sort_keys=True)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
