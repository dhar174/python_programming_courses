# Security Baseline

Apply these defaults for all generated deployment changes.

## 1) Least Privilege by Default

1. Start workflows with minimal `permissions`.
2. Grant write scopes only to jobs that require them.
3. Prefer short-lived credentials and OIDC where supported.

## 2) Token Precedence

1. Prefer `GITHUB_TOKEN` for repository-internal Actions operations.
2. Use PAT only when a provider/workflow requirement cannot be met with `GITHUB_TOKEN`.
3. If PAT is required, scope it narrowly and document the requirement.

## 3) Secret Handling

1. Never print secret values in logs or reports.
2. Report only secret names and why each is needed.
3. Keep provider credentials in repository or environment secrets, not plaintext config.

## 4) Workflow Hardening

1. Pin actions to stable major versions or commit SHAs where policy requires.
2. Avoid unnecessary write permissions on build-only jobs.
3. Add explicit branch/path triggers to reduce accidental execution.

## 5) Pages/Artifact Safety Checks

1. Ensure artifact upload path matches generated output path.
2. Ensure the Pages root entrypoint exists and is deterministic.
3. Avoid over-broad content conversion that may publish unintended files.

## 6) Reporting Requirements

Always report:

- security improvements applied,
- remaining risks,
- manual steps still required by repository admins.
