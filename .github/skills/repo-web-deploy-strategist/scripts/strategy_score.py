#!/usr/bin/env python3
"""Score deployment strategies from repo_probe output."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

FIT_MATRIX = {
    "github-pages-actions": {
        "slides": 95,
        "docs": 95,
        "static": 90,
        "spa": 85,
        "api": 25,
        "full-stack": 40,
    },
    "actions-render": {
        "slides": 55,
        "docs": 50,
        "static": 60,
        "spa": 65,
        "api": 90,
        "full-stack": 88,
    },
    "actions-azure-webapp": {
        "slides": 50,
        "docs": 45,
        "static": 55,
        "spa": 70,
        "api": 85,
        "full-stack": 82,
    },
    "actions-cloudflare-pages": {
        "slides": 88,
        "docs": 90,
        "static": 92,
        "spa": 90,
        "api": 55,
        "full-stack": 60,
    },
    "actions-vercel": {
        "slides": 82,
        "docs": 78,
        "static": 88,
        "spa": 92,
        "api": 75,
        "full-stack": 78,
    },
}

BASE_STRATEGIES = {
    "github-pages-actions": {
        "title": "GitHub Pages via Actions",
        "delivery": "github-native",
        "security": 90,
        "ops": 90,
        "cost": 95,
        "required_secrets": [],
        "notes": "Best default for static, docs, or slide repositories.",
    },
    "actions-render": {
        "title": "GitHub Actions to Render",
        "delivery": "actions-to-provider",
        "security": 75,
        "ops": 78,
        "cost": 70,
        "required_secrets": ["RENDER_API_KEY"],
        "notes": "Strong fit for Python APIs, workers, and full-stack apps.",
    },
    "actions-azure-webapp": {
        "title": "GitHub Actions to Azure Web App",
        "delivery": "actions-to-provider",
        "security": 82,
        "ops": 68,
        "cost": 60,
        "required_secrets": ["AZURE_CREDENTIALS", "AZURE_WEBAPP_NAME"],
        "notes": "Good fit when enterprise Azure governance or App Service is desired.",
    },
    "actions-cloudflare-pages": {
        "title": "GitHub Actions to Cloudflare Pages",
        "delivery": "actions-to-provider",
        "security": 84,
        "ops": 80,
        "cost": 85,
        "required_secrets": ["CLOUDFLARE_API_TOKEN", "CLOUDFLARE_ACCOUNT_ID"],
        "notes": "Strong static and SPA hosting option with global edge delivery.",
    },
    "actions-vercel": {
        "title": "GitHub Actions to Vercel",
        "delivery": "actions-to-provider",
        "security": 80,
        "ops": 82,
        "cost": 75,
        "required_secrets": ["VERCEL_TOKEN", "VERCEL_ORG_ID", "VERCEL_PROJECT_ID"],
        "notes": "Great for frontend-heavy projects and Next.js workloads.",
    },
}


def detect_primary_shape(probe: dict[str, Any]) -> tuple[str, list[str]]:
    """Classify repo shape from probe signals."""
    reasons: list[str] = []
    manifests = probe.get("signals", {}).get("manifests", {})
    framework_hints = probe.get("signals", {}).get("framework_hints", {})
    marp_configs = probe.get("marp_configs", [])

    has_marp = "marp" in manifests or bool(marp_configs)
    has_python = "python" in manifests
    has_node = "node" in manifests
    has_docs = any(key in manifests for key in ("mkdocs", "hugo", "jekyll"))

    if has_marp:
        reasons.append("Marp configuration detected")
    if has_docs:
        reasons.append("Documentation/static-site manifest detected")
    if has_python:
        reasons.append("Python manifest detected")
    if has_node:
        reasons.append("Node manifest detected")

    if has_marp:
        return "slides", reasons
    if has_docs:
        return "docs", reasons

    nextjs = bool(framework_hints.get("nextjs"))
    if nextjs:
        reasons.append("Next.js framework hint detected")

    if has_node and not has_python:
        return ("spa" if nextjs else "static"), reasons
    if has_python and has_node:
        return "full-stack", reasons
    if has_python:
        return "api", reasons

    return "static", reasons or ["No strong backend runtime signal; default to static"]


def has_heuristic_warning(probe: dict[str, Any], warning_id: str) -> bool:
    """Check for a specific heuristic warning id in probe payload."""
    warnings = probe.get("heuristics", {}).get("warnings", [])
    return any(item.get("id") == warning_id for item in warnings if isinstance(item, dict))


def has_pages_workflow(probe: dict[str, Any]) -> bool:
    """Return True when any workflow already uses Pages actions."""
    workflows = probe.get("workflows", [])
    return any(wf.get("uses_pages_actions") for wf in workflows if isinstance(wf, dict))


def build_scored_strategies(probe: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Build and score strategy candidates."""
    primary_shape, reasons = detect_primary_shape(probe)

    classification = {
        "primary": primary_shape,
        "reasons": reasons,
    }

    has_python = "python" in probe.get("signals", {}).get("manifests", {})
    has_node = "node" in probe.get("signals", {}).get("manifests", {})
    has_docker = "docker" in probe.get("signals", {}).get("manifests", {})

    pat_warning = has_heuristic_warning(probe, "pat-token-usage")
    existing_pages = has_pages_workflow(probe)

    scored: list[dict[str, Any]] = []

    for strategy_id, meta in BASE_STRATEGIES.items():
        fit = FIT_MATRIX[strategy_id][primary_shape]
        security = meta["security"]
        ops = meta["ops"]
        cost = meta["cost"]
        rationale: list[str] = [meta["notes"]]

        if strategy_id == "github-pages-actions" and existing_pages:
            fit = min(100, fit + 8)
            rationale.append("Existing Pages workflow detected")

        if strategy_id == "github-pages-actions" and pat_warning:
            security = max(0, security - 10)
            rationale.append("Detected PAT token usage; hardening opportunity exists")

        if strategy_id in {"actions-render", "actions-azure-webapp"} and has_python:
            fit = min(100, fit + 4)
            rationale.append("Python runtime signal aligns with provider workflow")

        if strategy_id in {"actions-cloudflare-pages", "actions-vercel"} and has_node:
            fit = min(100, fit + 4)
            rationale.append("Node runtime signal aligns with frontend provider workflow")

        if strategy_id in {"actions-render", "actions-azure-webapp"} and has_docker:
            ops = min(100, ops + 3)
            rationale.append("Docker signal supports portable deployment packaging")

        total = round((fit * 0.55) + (security * 0.20) + (ops * 0.15) + (cost * 0.10))

        scored.append(
            {
                "id": strategy_id,
                "title": meta["title"],
                "delivery": meta["delivery"],
                "fit": fit,
                "security": security,
                "ops": ops,
                "cost": cost,
                "total_score": total,
                "required_secrets": meta["required_secrets"],
                "rationale": rationale,
            }
        )

    scored.sort(key=lambda item: (-item["total_score"], -item["fit"], item["id"]))

    return classification, scored


def build_provider_shortlist(primary_shape: str, scored: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Build a dynamic provider shortlist for non-static paths."""
    provider_only = [item for item in scored if item["delivery"] == "actions-to-provider"]

    if primary_shape in {"api", "full-stack"}:
        return provider_only[:3]

    if primary_shape in {"slides", "docs", "static", "spa"}:
        return provider_only[:2]

    return provider_only[:3]


def markdown_matrix(classification: dict[str, Any], scored: list[dict[str, Any]]) -> str:
    """Render a markdown decision matrix from scored strategies."""
    lines = [
        "## Deployment Decision Matrix",
        "",
        f"Primary shape: `{classification['primary']}`",
        "",
        "| Rank | Strategy | Total | Fit | Security | Ops | Cost | Required Secrets |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]

    for index, strategy in enumerate(scored, start=1):
        secret_cell = ", ".join(strategy["required_secrets"]) if strategy["required_secrets"] else "None"
        lines.append(
            "| "
            + f"{index} | {strategy['title']} | {strategy['total_score']} | {strategy['fit']} | "
            + f"{strategy['security']} | {strategy['ops']} | {strategy['cost']} | {secret_cell} |"
        )

    return "\n".join(lines)


def load_probe(path: str | None) -> dict[str, Any]:
    """Load probe payload from file or stdin."""
    if path:
        return json.loads(open(path, "r", encoding="utf-8").read())

    data = sys.stdin.read().strip()
    if not data:
        raise ValueError("No probe JSON provided via --probe or stdin")
    return json.loads(data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score deployment strategies from repo_probe JSON.")
    parser.add_argument("--probe", help="Path to probe JSON file. If omitted, read JSON from stdin.")
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "both"],
        default="both",
        help="Output format",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    try:
        probe = load_probe(args.probe)
    except Exception as exc:  # pragma: no cover - invalid input handling
        print(json.dumps({"error": str(exc)}), flush=True)
        return 1

    classification, scored = build_scored_strategies(probe)
    providers = build_provider_shortlist(classification["primary"], scored)

    recommended = scored[0]
    matrix_md = markdown_matrix(classification, scored)

    result = {
        "classification": classification,
        "recommended_strategy": {
            "id": recommended["id"],
            "title": recommended["title"],
            "delivery": recommended["delivery"],
            "total_score": recommended["total_score"],
            "required_secrets": recommended["required_secrets"],
            "why": recommended["rationale"],
        },
        "provider_shortlist": [
            {
                "id": item["id"],
                "title": item["title"],
                "total_score": item["total_score"],
            }
            for item in providers
        ],
        "strategies": scored,
        "decision_matrix_markdown": matrix_md,
    }

    if args.format == "markdown":
        print(matrix_md)
        return 0

    if args.format == "json":
        print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
        return 0

    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
