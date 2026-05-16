---
name: create-initial-operating-contract
description: 'Generate an initial operating contract for autonomous Copilot work. Use when starting a new task stream, kickoff session, issue burndown, or multi-step implementation where scope, stop conditions, constraints, acceptance criteria, and execution policy must be explicit before coding.'
---

# Create Initial Operating Contract

Create a concise, execution-ready operating contract the agent can follow from kickoff through completion.

## When to Use This Skill

- User asks for an "operating contract", "working agreement", "execution contract", or "autopilot contract"
- A task has multiple steps and needs explicit boundaries and stop conditions
- A session is resuming after interruption and needs a fresh control plan
- Work involves issue burndown, parallel PR handling, or strict repo constraints

## Contract Outputs

Produce a single contract containing:

1. Mission and success definition
2. Scope in/out
3. Non-negotiable constraints
4. Prioritized work order
5. Verification and merge policy
6. Progress reporting cadence
7. Stop conditions and escalation rules
8. Handoff format

## Step-by-Step Workflow

1. Gather context from the user prompt and repository state.
2. Resolve ambiguous boundaries (include assumptions if user did not specify).
3. Draft the contract using `templates/initial-operating-contract.md`.
4. Fill all required fields with concrete, testable wording.
5. Return:
   - Completed contract
   - Immediate next action list (3-5 items max)
   - Any explicit assumptions made

## Authoring Rules

- Keep contract language operational and measurable, not aspirational.
- Prefer "done when..." criteria over vague quality statements.
- Include explicit failure behavior (retry, fallback, abort, ask user).
- Include repository-specific constraints when known (branching, CI, docs, tests).
- If requirements changed mid-session, include a "supersedes previous contract" note.

## Contract Quality Checklist

- [ ] Scope boundaries are explicit
- [ ] Completion criteria are objectively verifiable
- [ ] Priority order is unambiguous
- [ ] Safety/constraint rules are stated
- [ ] Status update cadence is defined
- [ ] Escalation conditions are defined

## References

- Template: `templates/initial-operating-contract.md`

