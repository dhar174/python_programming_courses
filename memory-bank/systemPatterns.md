<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# System Patterns

## High-level architecture
This repository uses a layered guidance model: root instructions for always-on context, path-specific instructions for targeted rules, focused custom agents for specialist work, and `memory-bank/` files for resumable state.

## Major components
### .github
- Responsibility: Copilot assets, workflows, prompts, hooks, and repository automation.
- Inputs: repo-local changes and contributor requests
- Outputs: validated artifacts or updated guidance
- Dependencies: adjacent docs, tests, and automation
### _site
- Responsibility: Project-specific directory that should be inspected before large changes.
- Inputs: repo-local changes and contributor requests
- Outputs: validated artifacts or updated guidance
- Dependencies: adjacent docs, tests, and automation
### Advanced
- Responsibility: Project-specific directory that should be inspected before large changes.
- Inputs: repo-local changes and contributor requests
- Outputs: validated artifacts or updated guidance
- Dependencies: adjacent docs, tests, and automation
### Basics
- Responsibility: Project-specific directory that should be inspected before large changes.
- Inputs: repo-local changes and contributor requests
- Outputs: validated artifacts or updated guidance
- Dependencies: adjacent docs, tests, and automation

## Key data flows
1. Maintain CLI flows, prompts, and output contracts.
2. Extend and verify API or service behavior without breaking external callers.
3. Update web UI or static assets while preserving usability and responsiveness.
4. Keep deep documentation, agent guidance, and architecture notes in sync with the codebase.

## Extension points
- Add new custom agents only when a repo workflow is specialized and recurring.
- Add new path-specific instructions when a directory or file family has stable rules.
- Add or vendor skills only when the guidance is detailed but not needed on every task.
<!-- repo-agent-bootstrap:managed:end -->
