# Research Checklist

Run these checks in order before proposing any deploy strategy.

## 1) Repository Footprint

1. Confirm repo root, active branch, and origin remote.
2. List top-level directories and files.
3. Identify framework/runtime manifests (Python, Node, Docker, static-site tooling).

## 2) GitHub Configuration Inventory

1. Enumerate `.github/workflows/*.yml`.
2. Enumerate other `.github/**` config files that could affect CI/CD.
3. Record all referenced secrets in workflows.

## 3) Deployment-Specific Signals

1. Detect existing Pages workflow actions (`configure-pages`, `upload-pages-artifact`, `deploy-pages`).
2. Detect existing build generators (Marp, MkDocs, static site generators).
3. Capture build input/output paths and compare against artifact upload path.

## 4) Live GitHub State (When `gh` Is Available)

1. Verify `gh auth status`.
2. Query Pages endpoint and capture status/url.
3. Query workflows and recent runs.
4. Query secret names only (never secret values).

## 5) Risk and Hardening Signals

1. Flag PAT usage where `GITHUB_TOKEN` may be sufficient.
2. Flag artifact/output path mismatch risk.
3. Flag over-broad build scope (for example, root-level markdown conversion).

## 6) Output Contract

Produce machine-readable facts that include:

- repo identity and git metadata,
- inventory and workflow summary,
- runtime/framework signals,
- live state (or explicit skip reason),
- heuristic warnings/checks.
