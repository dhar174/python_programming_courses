# Deploy Patterns

Use this decision logic after repository research is complete.

## 1) GitHub-Native First

Prioritize GitHub Pages when the repository is primarily:

- slides or docs output,
- static HTML/CSS/JS,
- SPA that can be built to static assets.

## 2) Strategy Selection Rules

1. Build a scored matrix for all supported strategies.
2. Recommend the highest score, but include at least two alternatives.
3. Keep tradeoffs explicit: fit, security, operations, and required secrets.

## 3) Primary Strategies

- `github-pages-actions`
  - Best for static output and educational/documentation repositories.
- `actions-render`
  - Strong default for API/backend or Python-heavy full-stack repositories.
- `actions-azure-webapp`
  - Useful where Azure governance/compliance is preferred.
- `actions-cloudflare-pages`
  - Strong for static sites and SPA edge delivery.
- `actions-vercel`
  - Strong for frontend-heavy and Next.js workflows.

## 4) Dynamic Provider Shortlist

When Pages is not a fit:

1. Keep Pages in the matrix for transparency.
2. Build a provider shortlist from top-scoring Actions-to-provider options.
3. Return a dynamic shortlist sized to project type:
   - non-static (`api`, `full-stack`): top 3 providers,
   - static-like repos: top 2 providers.

## 5) Approval Gate Requirements

Before implementation, present:

- chosen strategy and rationale,
- exact files/workflows to change,
- required secrets and permissions,
- verification steps,
- rollback plan.

Do not mutate until explicit approval is granted.
