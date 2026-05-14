<!-- repo-agent-bootstrap:file-kind=architecture-doc -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Architecture

## Overview
An instructor-led **96-hour Python training package** built by **GlobalIT** and taught by **Charles Niswander**. The course delivers two sequential 48-hour modules aligned to the Python Institute certification pathway (PCEP → PCAP), with active remediation tracked in GitHub Issues.

This generated reference is the deeper architecture companion to `AGENTS.md`. Keep broadly applicable instructions in root guidance and reserve this file for subsystem relationships, data flow notes, and longer rationale.

## Modules
### .github
Copilot assets, workflows, prompts, hooks, and repository automation.
### _site
Project-specific directory that should be inspected before large changes.
### Advanced
Project-specific directory that should be inspected before large changes.
### Basics
Project-specific directory that should be inspected before large changes.
### fixtures
Project-specific directory that should be inspected before large changes.

## Request / event lifecycle
1. Maintain CLI flows, prompts, and output contracts.
2. Extend and verify API or service behavior without breaking external callers.
3. Update web UI or static assets while preserving usability and responsiveness.
4. Keep deep documentation, agent guidance, and architecture notes in sync with the codebase.
5. Curate contributor-facing AI assets, skills, prompts, and instructions.
6. Maintain CI/CD workflows, quality gates, and automation entrypoints.

## Security / reliability considerations
- Preserve contributor-authored content outside managed sections during maintenance runs.
- Keep third-party AI assets pinned, attributable, and license-checked before vendoring.
- Use the smallest relevant validation commands before merging automation changes.
<!-- repo-agent-bootstrap:managed:end -->
