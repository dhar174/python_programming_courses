---
name: repo-web-deploy-strategist
description: Analyze connected repositories and deliver end-to-end web deployment strategy with GitHub-native defaults. Use when Codex must (1) research repository structure, workflows, Pages setup, and .github configuration, (2) build a scored decision matrix for deployment options, (3) pause for explicit approval before mutating changes, and (4) implement and verify deployment with local checks plus GitHub CI smoke.
---

# Repo Web Deploy Strategist

Use this skill to turn an unknown repository into a deployable web target with repeatable, auditable steps.

## Operating Mode

- Prefer GitHub-native deployment paths first.
- Treat analysis and implementation as separate phases.
- Do not mutate repository files, branch state, or remote state until explicit user approval is given.
- Use a feature branch plan for implementation (`codex/...` naming when creating branches).
- Apply least-privilege security defaults in generated workflows.
- If GitHub live checks are unavailable, continue with local evidence and mark live checks as skipped.

## Workflow

### 1) Research Repository State

1. Run `scripts/repo_probe.py --repo <path>` first.
2. Inspect:
   - directory structure and key manifests,
   - `.github/**` configs, especially workflow files,
   - Git remotes/branch,
   - existing deployment workflows and token usage,
   - GitHub Pages/workflow status through `gh` when available.
3. Load [research-checklist](references/research-checklist.md) for strict coverage order.

### 2) Classify Deployment Shape

Classify the repository as one primary shape:

- `slides` or `docs` (content-first static output),
- `static` or `spa` (frontend static hosting),
- `api` or `backend` (runtime server),
- `full-stack` (frontend + backend coupling).

Use repository signals, not assumptions.

### 3) Build Decision Matrix

1. Pipe probe output into `scripts/strategy_score.py`.
2. Produce a scored matrix with:
   - strategy fit,
   - operational complexity,
   - security posture,
   - credential requirements,
   - known risks and tradeoffs.
3. Prefer GitHub Pages when fit is strong.
4. If Pages is not a fit, produce a dynamic Actions-to-provider shortlist (for example Render, Azure, or Cloudflare when relevant).

### 4) Gate Before Mutation

Before editing files or triggering deployments, present:

- selected strategy and alternatives,
- exact files to add/change,
- required secrets/permissions,
- verification plan,
- rollback plan.

Request explicit approval before any mutating step.

### 5) Implement Approved Strategy

After approval:

1. Prepare a feature-branch implementation plan.
2. Update workflows/configs with least-privilege defaults.
3. Keep changes minimal and repo-aligned.
4. Apply repo-aware heuristics:
   - flag PAT usage where `GITHUB_TOKEN` is sufficient,
   - verify artifact upload path matches generated output path,
   - tighten build scope to avoid accidental over-build.

### 6) Verify

Run `scripts/ci_smoke.py --repo <path>` after implementation.

Verification baseline:

- local checks (workflow shape and local tooling checks),
- live GitHub checks (`gh`) when available,
- clear pass/warn/fail summary with next actions.

For missing live auth, verify local checks and explicitly report that live checks were skipped.

### 7) Report

Return a concise completion report:

- what changed,
- why this strategy won,
- validation outcomes,
- unresolved risks,
- manual follow-ups.

## Scripts

- `scripts/repo_probe.py`
  - Contract: machine-readable JSON facts about repo, workflow posture, and heuristic warnings.
- `scripts/strategy_score.py`
  - Contract: ranked deployment matrix in JSON and Markdown summary.
- `scripts/ci_smoke.py`
  - Contract: pass/warn/fail smoke-check report with local and optional live checks.

## References

- [research-checklist](references/research-checklist.md)
- [deploy-patterns](references/deploy-patterns.md)
- [security-baseline](references/security-baseline.md)

Use references selectively to keep context lean.

## Prompt Starter

Use `$repo-web-deploy-strategist` to analyze this repository, produce a scored deployment decision matrix, and stop for approval before applying any changes.
