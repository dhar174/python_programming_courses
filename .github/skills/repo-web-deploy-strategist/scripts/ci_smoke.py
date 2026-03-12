#!/usr/bin/env python3
"""Run local and optional GitHub live smoke checks for deployment workflows."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any


def run_cmd(command: list[str], cwd: Path, timeout: int = 60) -> dict[str, Any]:
    """Run a command and normalize output."""
    try:
        completed = subprocess.run(  # noqa: S603
            command,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except Exception as exc:  # pragma: no cover - environment defensive path
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


def run_shell(command: str, cwd: Path, timeout: int = 90) -> dict[str, Any]:
    """Run a shell command for optional custom checks."""
    try:
        completed = subprocess.run(  # noqa: S602
            command,
            cwd=str(cwd),
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except Exception as exc:  # pragma: no cover
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


def parse_github_slug(remote_url: str) -> str | None:
    """Extract GitHub slug from origin remote URL."""
    patterns = [
        r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$",
        r"https?://[^@]+@github\.com/(?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, remote_url)
        if match:
            return f"{match.group('owner')}/{match.group('repo')}"
    return None


def safe_json(text: str) -> Any:
    """Parse JSON text safely."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def local_checks(root: Path, custom_commands: list[str]) -> list[dict[str, Any]]:
    """Run baseline local checks."""
    checks: list[dict[str, Any]] = []

    workflow_dir = root / ".github" / "workflows"
    workflow_files = sorted(workflow_dir.glob("*.y*ml")) if workflow_dir.exists() else []

    checks.append(
        {
            "name": "workflow_files_present",
            "status": "pass" if workflow_files else "warn",
            "details": f"Found {len(workflow_files)} workflow file(s)",
        }
    )

    invalid_shape = []
    for workflow in workflow_files:
        text = workflow.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"(?m)^\s*on\s*:", text) or not re.search(r"(?m)^\s*jobs\s*:", text):
            invalid_shape.append(str(workflow.relative_to(root)).replace("\\", "/"))

    checks.append(
        {
            "name": "workflow_yaml_shape",
            "status": "pass" if not invalid_shape else "fail",
            "details": "All workflows contain 'on' and 'jobs'" if not invalid_shape else f"Invalid shape: {invalid_shape}",
        }
    )

    marp_configs = list(root.glob(".marprc*.yml")) + list(root.glob(".marprc*.yaml"))
    npx_available = shutil.which("npx") is not None
    if marp_configs and npx_available:
        npx_version = run_cmd(["npx", "--version"], root)
        checks.append(
            {
                "name": "npx_available",
                "status": "pass" if npx_version["ok"] else "warn",
                "details": npx_version["stdout"] if npx_version["ok"] else npx_version["stderr"],
            }
        )

        marp_local = run_cmd(["npx", "--no-install", "@marp-team/marp-cli", "--version"], root)
        checks.append(
            {
                "name": "marp_cli_local",
                "status": "pass" if marp_local["ok"] else "warn",
                "details": (
                    marp_local["stdout"]
                    if marp_local["ok"]
                    else "Marp CLI is not locally installed; install it or rely on GitHub Action image."
                ),
            }
        )
    elif marp_configs:
        checks.append(
            {
                "name": "marp_cli_available",
                "status": "warn",
                "details": "Marp config detected but npx is unavailable.",
            }
        )

    for command in custom_commands:
        result = run_shell(command, root)
        checks.append(
            {
                "name": f"custom:{command}",
                "status": "pass" if result["ok"] else "fail",
                "details": result["stdout"] if result["ok"] else result["stderr"],
            }
        )

    return checks


def live_checks(root: Path, no_live: bool) -> dict[str, Any]:
    """Run GitHub live checks using gh when available."""
    if no_live:
        return {
            "enabled": False,
            "status": "skipped",
            "reason": "disabled_by_flag",
            "checks": [],
        }

    if shutil.which("gh") is None:
        return {
            "enabled": True,
            "status": "skipped",
            "reason": "gh_cli_not_found",
            "checks": [],
        }

    auth = run_cmd(["gh", "auth", "status"], root)
    if not auth["ok"]:
        return {
            "enabled": True,
            "status": "skipped",
            "reason": "gh_auth_not_available",
            "checks": [],
        }

    origin = run_cmd(["git", "remote", "get-url", "origin"], root)
    slug = parse_github_slug(origin["stdout"]) if origin["ok"] else None

    if not slug:
        return {
            "enabled": True,
            "status": "skipped",
            "reason": "github_remote_not_detected",
            "checks": [],
        }

    checks: list[dict[str, Any]] = []

    pages = run_cmd(["gh", "api", f"repos/{slug}/pages"], root)
    pages_data = safe_json(pages["stdout"]) if pages["ok"] else None
    pages_status = pages_data.get("status") if isinstance(pages_data, dict) else None
    checks.append(
        {
            "name": "pages_status",
            "status": "pass" if pages_status in {"built", "building"} else "warn",
            "details": pages_status or pages.get("stderr", "unknown"),
        }
    )

    workflows = run_cmd(["gh", "api", f"repos/{slug}/actions/workflows"], root)
    workflows_data = safe_json(workflows["stdout"]) if workflows["ok"] else None
    workflow_count = workflows_data.get("total_count") if isinstance(workflows_data, dict) else None
    checks.append(
        {
            "name": "workflows_visible",
            "status": "pass" if isinstance(workflow_count, int) and workflow_count > 0 else "warn",
            "details": f"total_count={workflow_count}",
        }
    )

    runs = run_cmd(["gh", "api", f"repos/{slug}/actions/runs?per_page=10"], root)
    runs_data = safe_json(runs["stdout"]) if runs["ok"] else None
    run_items = runs_data.get("workflow_runs") if isinstance(runs_data, dict) else None

    has_recent_success = False
    if isinstance(run_items, list):
        has_recent_success = any(item.get("conclusion") == "success" for item in run_items)

    checks.append(
        {
            "name": "recent_successful_run",
            "status": "pass" if has_recent_success else "warn",
            "details": "success found in recent runs" if has_recent_success else "no recent success found",
        }
    )

    overall = "pass" if all(item["status"] == "pass" for item in checks) else "warn"
    return {
        "enabled": True,
        "status": overall,
        "reason": None,
        "checks": checks,
    }


def summarize(local: list[dict[str, Any]], live: dict[str, Any]) -> tuple[str, list[str], list[str]]:
    """Compute overall smoke status and issue lists."""
    failures: list[str] = []
    warnings: list[str] = []

    for check in local:
        if check["status"] == "fail":
            failures.append(f"local:{check['name']}")
        elif check["status"] == "warn":
            warnings.append(f"local:{check['name']}")

    if live["status"] == "skipped":
        warnings.append(f"live:skipped:{live.get('reason')}")
    else:
        for check in live.get("checks", []):
            if check["status"] == "fail":
                failures.append(f"live:{check['name']}")
            elif check["status"] == "warn":
                warnings.append(f"live:{check['name']}")

    if failures:
        return "fail", failures, warnings
    if warnings:
        return "warn", failures, warnings
    return "pass", failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local + CI smoke checks for deployment readiness.")
    parser.add_argument("--repo", default=".", help="Repository path (default: current directory)")
    parser.add_argument("--no-live", action="store_true", help="Skip GitHub live checks")
    parser.add_argument(
        "--local-check",
        action="append",
        default=[],
        help="Optional additional local shell check command (repeatable)",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    if not root.exists() or not root.is_dir():
        print(json.dumps({"error": f"Repository path does not exist: {root}"}))
        return 1

    local = local_checks(root, args.local_check)
    live = live_checks(root, args.no_live)
    overall, failures, warnings = summarize(local, live)

    payload = {
        "repo": str(root),
        "overall_status": overall,
        "local_checks": local,
        "live_checks": live,
        "failures": failures,
        "warnings": warnings,
    }

    print(json.dumps(payload, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if overall != "fail" else 1


if __name__ == "__main__":
    raise SystemExit(main())
