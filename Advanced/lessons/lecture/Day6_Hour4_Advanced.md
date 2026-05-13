# Day 6 Hour 4 Advanced — Checkpoint 3: GUI Milestone Demo Facilitation Script

## Hour identity and facilitation purpose

This document is the instructor facilitation script for Hour 24 in the Advanced Python runbook, defined as Checkpoint 3: GUI milestone demo. It is intentionally written as a checkpoint operations guide, not as a normal concept lecture. Your primary role in this hour is to collect evidence of milestone readiness, score consistently, coach quickly, and route learners to the right remediation path without derailing the whole cohort.

Use this script as both your speaking guide and your grading operations playbook. You can read large portions nearly verbatim. The language is designed to keep the room calm, focused, and fair while still enforcing concrete technical standards.

The runbook source of truth for this hour defines these core expectations and they are treated as non negotiable:

- Outcome: deliver a working GUI CRUD app wired to the service layer.
- Talk points window: 10 to 20 minutes, with grading focus on UI works, CRUD complete, errors handled, and code organization.
- Live demo window: 5 to 10 minutes, featuring a fast grading checklist run.
- Hands on lab window: 25 to 35 minutes.
- Checkpoint 3 block: 45 to 60 minutes in operational terms, where demo evidence is collected and scored.
- Deliverables: GUI launches reliably, CRUD works through UI, load and save works with JSON allowed, clean separation between ui and core, and a short demo flow add then list then update then delete then restart then load.
- Completion criteria: end to end workflow demonstrated and no crashes in typical use.
- Required pitfalls to evaluate: UI only validation with no service validation, and unstable IDs causing wrong updates or deletes.
- Optional extension: search and filter UI.
- Closing quick check prompt: If you had one more hour, what would you improve first in your GUI?

Keep scope strictly inside Hour 24 checkpoint facilitation. Do not teach new persistence technology in this hour and do not pivot into next session content.

## Contract alignment note for Day 6 artifact consistency

Contract alignment note: this script preserves canonical Hour 24 language and the canonical demo sequence used across Day 6 artifacts. The milestone wording remains consistent with the runbook phrase “Checkpoint 3: GUI milestone demo,” and the required short demo path remains exactly “add -> list -> update -> delete -> restart -> load.” If you adapt local classroom phrasing, keep those two anchors unchanged so rubric evidence remains comparable across sections and instructors.

## What success looks like in this checkpoint hour

At the end of this hour, you should be able to answer yes to the following operational questions for each learner or team submission:

1. Can the GUI be launched reliably from a normal project start command without instructor patching?
2. Can the learner perform all CRUD actions through UI controls and show visible state changes that match intent?
3. Can the learner demonstrate load and save behavior with JSON accepted, including restart and reload evidence?
4. Can the learner explain where service or core logic lives, and show that UI callbacks delegate to that layer?
5. Can the learner handle common error paths without crashing in typical use?
6. Does update and delete target stable IDs, not transient row indexes, including after restart and load?

If all six are supported by direct evidence, the learner is checkpoint ready. If some are partial, use the partial credit and remediation routing sections in this script.

## Instructor stance for this hour

Use a coaching evaluator stance. You are rigorous on evidence, calm on process, and precise on feedback.

Recommended opening language:

“This checkpoint is a proof of working software and maintainable structure, not a perfection contest. I will score what you demonstrate. If something breaks, narrate your expected behavior and what you would inspect first. Good engineering communication still earns credit.”

“Today I care most about five things: GUI reliability, complete CRUD through the interface, persistence behavior, error handling, and clean organization between UI and service logic.”

“I am also enforcing two must pass technical gates: stable identity for update and delete, and business validation in service or core rather than only inside UI widgets.”

This language sets a fair tone and reduces fear while still preserving standards.

## Explicit timing crosswalk from runbook windows to checkpoint schedule

The runbook defines four windows that overlap in practical delivery. Use the crosswalk below to show where each required window is satisfied inside your 60 minute checkpoint block. This table is mandatory for consistency and for issue traceability.

| Runbook requirement window | Required duration | Where it appears in Hour 24 checkpoint schedule | Evidence that window is satisfied |
| --- | --- | --- | --- |
| Instructor talk points | 10 to 20 min | Minute 0 to minute 14 whole group briefing, rubric framing, and risk reminders | Learners hear grading focus: UI works, CRUD complete, errors handled, code organization. Instructor confirms must pass gates and demo sequence. |
| Live demo | 5 to 10 min | Minute 14 to minute 21 instructor fast checklist run using canonical flow | Instructor demonstrates fast grading checklist run add then list then update then delete then restart then load and narrates what counts as evidence. |
| Hands on lab | 25 to 35 min | Minute 21 to minute 52 supervised prep and execution sprint while instructor circulates with triage prompts | Learners run their own demo path, fix blockers, and gather evidence. Instructor performs rapid coaching and captures provisional scoring notes. |
| Checkpoint 3 block | 45 to 60 min | Minute 0 to minute 60 entire hour is treated as checkpoint operations | Formal scoring decisions are made during demos and spot checks, with pass, partial, or not yet outcomes plus remediation routes. |

Important facilitation clarification: these windows are not four separate standalone hours. They are operational components inside one checkpoint hour. The crosswalk above documents compliance explicitly.

## Run of show with minute by minute facilitation language

### Minute 0 to 3: reset and expectation lock

Say:

“We are now in Checkpoint 3, the GUI milestone demo. Your goal is to show a working GUI CRUD app wired to your service layer.”

“I will score based on observable evidence, not on claims. If your app does not show a behavior in demo, I cannot award full credit for that behavior.”

“This is not punitive. It is a quality gate to ensure you can safely continue the capstone.”

Then display:

- Canonical demo sequence.
- Deliverables list.
- Must pass gates.
- Rubric bands.

### Minute 3 to 8: grading focus briefing

Say:

“Grading focus is exactly this: UI works, CRUD complete, errors handled, code organization.”

“You can still earn strong partial credit if one area fails but your architecture is explainable and your troubleshooting is coherent.”

“Two critical failures can cap your score: unstable IDs for update and delete, and business rules that only exist in the UI layer.”

Reinforce:

- Stable IDs must remain stable after restart and load.
- Validation must exist in service or core, not only in button handlers.
- Typical error paths must not crash.

### Minute 8 to 14: demo protocol and fairness protocol

Explain exact protocol:

1. Each learner or team gets a short evidence window.
2. They must run the canonical flow in order unless a technical blocker forces a recovery step.
3. They answer one architecture question and one reliability question.
4. Instructor records evidence and score decision immediately.

Fairness protocol:

- Same prompts for all learners.
- Same must pass gates for all learners.
- Same evidence to score rules for all learners.
- No hidden bonus for speaking style alone.

### Minute 14 to 21: instructor live demo, fast checklist run

Use your own minimal sample or a prepared reference build. Demonstrate quickly:

1. Launch app.
2. Add record.
3. Confirm list update.
4. Update selected record.
5. Delete selected record.
6. Restart app.
7. Confirm load.

Narrate what the checklist captures:

- Visible state change after each action.
- Correct record targeted.
- Persistence confirmed after restart.
- No crash on a typical error path.
- Architecture explanation tied to actual files.

State explicitly:

“This is what a fast grading checklist run looks like. Your demo should produce this level of evidence.”

### Minute 21 to 35: hands on lab sprint part one

This is structured lab time, not free drift. Learners prepare demo readiness while you circulate.

Instructor circulation prompts:

- “Show me where the selected record ID is captured.”
- “What layer enforces non empty name and numeric bounds?”
- “If no row is selected and user clicks update, what happens?”
- “If the JSON file cannot parse, what does the user see?”

Use a triage card mindset:

- Green: likely checkpoint pass with minor polish.
- Yellow: partial risk, one critical area shaky.
- Red: must pass gate at risk.

### Minute 35 to 52: hands on lab sprint part two with rolling checkpoint checks

Start rolling checks while others continue fixing.

For each learner:

1. Observe canonical flow.
2. Trigger one typical error path.
3. Ask one architecture question.
4. Record evidence and provisional score.

When a learner is blocked:

- Stop debugging depth after two minutes.
- Assign a specific remediation target.
- Move on and return in rotation.

This prevents one team from consuming the entire checkpoint.

### Minute 52 to 57: score finalize and feedback delivery

Give concise decision language:

- “Checkpoint pass: working and stable, continue as planned.”
- “Checkpoint partial: core works but must pass gate unresolved.”
- “Checkpoint not yet: significant reliability gaps, remediation required before next milestone.”

Always include:

- One strength statement.
- One highest priority fix.
- One concrete next action within 30 minutes of independent work.

### Minute 57 to 60: quick check and close

Ask every learner:

“If you had one more hour, what would you improve first in your GUI?”

Collect short answers verbally or in chat. Prioritize answers that mention reliability, architecture boundaries, and user trust over cosmetic tweaks.

## Required runbook coverage translated into operational checklist language

Use this section to ensure all required runbook elements are explicitly present in your facilitation.

### Outcomes coverage

Required outcome statement to read:

“Today the expected outcome is a working GUI CRUD app wired to the service layer.”

Operational interpretation:

- UI does not contain all business logic.
- CRUD commands route through service calls.
- Service remains source of truth for validation and data mutation.

### Talk points coverage, 10 to 20 minutes

Required focus phrase:

“Grading focus is UI works, CRUD complete, errors handled, code organization.”

Elaboration prompts:

- UI works means launch reliability and usable controls.
- CRUD complete means add list update delete all through GUI.
- Errors handled means expected user mistakes do not crash app.
- Code organization means clean separation between ui and core responsibilities.

### Live demo coverage, 5 to 10 minutes

Required activity:

Fast grading checklist run by instructor before learner demos begin.

Purpose:

- Set shared expectation for acceptable evidence.
- Reduce ambiguity.
- Lower anxiety through concrete demonstration.

### Hands on lab coverage, 25 to 35 minutes

Required shape:

Guided prep plus supervised execution where learners run their own demos and resolve blockers.

Your job:

- Route fixes toward must pass gates first.
- Avoid deep refactor detours.
- Capture evidence while coaching.

### Checkpoint 3 block coverage, 45 to 60 minutes

Required shape:

The hour is treated as a checkpoint operations block with scoring decisions and remediation routing.

Your job:

- Make explicit pass or partial or not yet decisions.
- Tie every decision to observed evidence.
- Keep milestone language consistent with Day 6 artifacts.

### Deliverables coverage

Each learner must demonstrate, not just describe, these items:

- GUI launches reliably.
- CRUD works through UI.
- Load and save works with JSON accepted.
- Clean separation between ui and core.
- Short demo flow add then list then update then delete then restart then load.

### Completion coverage

Explicit completion statements:

- End to end workflow demonstrated.
- No crashes in typical use.

### Pitfalls coverage

Required pitfalls to evaluate explicitly:

- UI only validation with no service validation.
- Unstable IDs causing wrong updates or deletes.

### Optional extension coverage

Optional only:

- Search and filter UI.

Only evaluate this for bonus commentary, never as a baseline requirement for checkpoint pass.

### Quick check coverage

Required closing prompt:

“If you had one more hour, what would you improve first in your GUI?”

## Must pass gates for critical reliability and architecture risks

These gates come from blocker findings and must be applied consistently.

### Gate 1: stable identity gate for update and delete

Gate statement:

Update and delete must target stable IDs, not row index, including after restart and load.

Minimum evidence:

1. Learner selects a visible row.
2. App maps selection to stable record ID.
3. Update affects correct entity even if list ordering changes.
4. Delete removes intended entity.
5. After restart and load, same record ID mapping still holds.

Fail indicators:

- App uses list position as identity.
- Wrong record changes after insertion or sorting.
- Update or delete behavior changes incorrectly after reload.

Score impact rule:

If Gate 1 fails, full checkpoint pass is not allowed. Maximum decision is partial until corrected.

### Gate 2: service or core validation gate

Gate statement:

Validation and business rules must exist in service or core, not only in UI callbacks.

Minimum evidence:

1. Learner shows at least one business rule in service or model layer.
2. UI calls service and handles raised errors.
3. Equivalent invalid input through different UI paths yields consistent rule enforcement.

Fail indicators:

- All validation only in entry widget checks.
- Service accepts invalid states when called directly.
- Different UI paths bypass rules.

Score impact rule:

If Gate 2 fails, architecture band cannot exceed partial credit band. Learner must receive remediation route before next checkpoint.

### Gate 3: typical error path resilience gate

Gate statement:

At least one typical error path must be demonstrated without crash.

Examples of typical error path:

- Update with no selected item.
- Delete with no selected item.
- Invalid field value.
- Missing JSON file on first launch.

Pass evidence:

- User gets clear message.
- App remains responsive.
- State remains coherent.

Fail indicators:

- Traceback shown to end user during normal mistakes.
- App terminates or freezes on expected user error.

Score impact rule:

If Gate 3 fails, error handling category is capped at low band and checkpoint pass requires immediate recovery proof or targeted remediation assignment.

## Canonical demo protocol for learner evidence collection

Use this as your standard prompt for every learner.

Say:

“Please run the canonical Hour 24 sequence now: add, list, update, delete, restart, load.”

Then ask:

1. “Show where your service layer performs validation.”
2. “Show how selected rows map to stable IDs.”
3. “Trigger one typical error path and show no crash behavior.”

Time discipline:

- Core flow target: five minutes.
- Question and explanation target: two to three minutes.
- Recovery overhead target: two minutes maximum.

If a learner exceeds time:

- Stop and mark unobserved criteria as unproven.
- Offer a follow up remediation slot.

## Evidence to score decision rules for consistent grading

This section defines explicit decision logic so grading remains consistent across instructors and sections.

### Evidence first rule

Only score behaviors directly observed in the checkpoint or clearly demonstrated in a required artifact run within the same hour.

Do not award full points for:

- “It worked earlier.”
- “The code should do this.”
- “I can explain how it would work.”

Explanation can support partial understanding credit but not replace execution evidence.

### Decision matrix for final checkpoint status

| Status | Required evidence conditions | Typical action |
| --- | --- | --- |
| Pass | Canonical flow completed, all deliverables observed, all three must pass gates satisfied, no crash in typical use | Mark checkpoint pass and provide one stretch recommendation |
| Partial | Core workflow mostly works but one must pass gate unresolved or one major deliverable not fully demonstrated | Mark partial, assign targeted remediation route and recheck deadline |
| Not yet | Multiple core failures, canonical flow incomplete, or repeated crashes in typical use | Mark not yet, require structured recovery plan and focused coaching block |

### Category scoring rules

Use this weighted rubric for consistency:

- GUI launch and usability: 15 points.
- CRUD through UI: 30 points.
- Persistence and restart load: 20 points.
- Code organization and ui core separation: 20 points.
- Error handling and reliability: 10 points.
- Demo clarity and engineering reflection: 5 points.

Total: 100 points.

### Hard cap rules tied to must pass gates

1. If stable ID gate fails, maximum overall status is Partial, regardless of point total.
2. If service validation gate fails, architecture category capped at 10 out of 20.
3. If typical error path resilience fails, error handling category capped at 3 out of 10 unless fixed live during checkpoint.

These caps prevent inflated scores for fragile apps.

### Point band interpretation rules

For each major category, use consistent band language:

- Strong band: behavior repeatable, explainable, and reliable under mild perturbation.
- Partial band: behavior works in basic path but brittle in edge path.
- Low band: behavior missing, incorrect, or untrustworthy.

Never jump directly from low to full points based only on confident explanation.

### Handling unobserved criteria

If time expires before a criterion is observed:

- Mark criterion as unobserved.
- Assign provisional zero for that criterion at checkpoint close.
- Offer optional recheck window if course policy allows.

This keeps grading evidence based and transparent.

## Detailed rubric with behavioral anchors

### Category 1: GUI launches reliably and is operable, 15 points

Strong evidence:

- Launch succeeds first attempt.
- Main controls visible and labeled.
- User can identify form and list quickly.
- No manual interpreter switching or path surgery during demo.

Partial evidence:

- Launch works but requires minor workaround.
- Layout usable but confusing in spots.

Low evidence:

- Repeated launch failure.
- App opens but key controls unusable.

Scoring suggestion:

- 13 to 15 strong.
- 8 to 12 partial.
- 0 to 7 low.

### Category 2: CRUD through UI complete and correct, 30 points

Strong evidence:

- Add creates new record through form.
- List reflects add without stale state.
- Update modifies intended record.
- Delete removes intended record.
- Selection state and refresh behavior remain coherent.

Partial evidence:

- Add and list stable, one of update or delete unreliable.
- Refresh requires manual workaround.

Low evidence:

- Only add works.
- Update or delete targets wrong records.

Scoring suggestion:

- 26 to 30 strong.
- 16 to 25 partial.
- 0 to 15 low.

### Category 3: Load and save persistence through restart, 20 points

Strong evidence:

- Save occurs on command or auto save path.
- Restart and load restore expected records.
- ID continuity preserved after reload.

Partial evidence:

- Persistence works for some operations only.
- Restart requires undocumented manual step.

Low evidence:

- No persistence proof.
- Data lost on restart.

Scoring suggestion:

- 17 to 20 strong.
- 10 to 16 partial.
- 0 to 9 low.

### Category 4: clean separation between ui and core, 20 points

Strong evidence:

- UI handlers call service operations.
- Service or model hosts core validation and mutation rules.
- Learner can point to files and responsibilities clearly.

Partial evidence:

- Some separation present but with boundary leakage.
- UI still carries some business logic.

Low evidence:

- Callbacks directly mutate storage structures with little abstraction.
- Responsibilities not explainable.

Scoring suggestion:

- 17 to 20 strong.
- 10 to 16 partial.
- 0 to 9 low.

### Category 5: error handling and no crash in typical use, 10 points

Strong evidence:

- One typical error path demonstrated without crash.
- User feedback is actionable.
- App continues operation after error.

Partial evidence:

- Some error paths safe, others crash or confuse.

Low evidence:

- Typical mistakes terminate app.

Scoring suggestion:

- 8 to 10 strong.
- 4 to 7 partial.
- 0 to 3 low.

### Category 6: demo clarity and reflection quality, 5 points

Strong evidence:

- Learner explains design choices concisely.
- Learner identifies highest leverage next improvement.

Partial evidence:

- Explanation present but vague or incomplete.

Low evidence:

- No coherent explanation.

Scoring suggestion:

- 5 strong.
- 3 to 4 partial.
- 0 to 2 low.

## Partial credit handling and fairness mechanics

Partial credit is expected in a checkpoint environment. Use it to distinguish progress while preserving standards.

### Partial credit principles

1. Reward demonstrated progress, not promise.
2. Preserve must pass gates as quality boundaries.
3. Give remediation targets that are specific and short horizon.

### Common partial credit patterns

Pattern A: everything works except stable IDs after reload.

- Expected status: Partial.
- Feedback anchor: “Your UI flow is strong, but identity mapping is brittle after load.”
- Required fix: persist stable IDs and map selection by ID.

Pattern B: UI path validates but service accepts invalid state.

- Expected status: Partial.
- Feedback anchor: “Validation is visible in UI, but business rule is not enforced in service.”
- Required fix: move or duplicate rule to service and normalize error handling.

Pattern C: crash on no selection update.

- Expected status: Partial or Not yet depending on severity.
- Feedback anchor: “Typical error path must not crash.”
- Required fix: guard selection and show message while keeping app responsive.

Pattern D: add list update works, delete missing.

- Expected status: Partial.
- Feedback anchor: “CRUD incomplete at checkpoint.”
- Required fix: finish delete path with confirmation and refresh.

### Recheck policy suggestion

If your local delivery policy allows recheck:

- Offer one short recheck slot within 24 to 48 hours.
- Reevaluate only failed criteria plus dependent criteria.
- Preserve original observed strengths.

If no recheck policy exists, still provide written remediation route for coaching continuity.

## Triage playbooks for common checkpoint blockers

Use these playbooks during circulation and during live scoring to keep interventions short and effective.

### Blocker playbook 1: unstable IDs and wrong row updates

Symptoms:

- Update changes wrong row after insert.
- Delete removes wrong item when sorted or filtered.
- Behavior changes after restart.

Rapid diagnostic questions:

1. “What value uniquely identifies a record in your core model?”
2. “Where is that value stored in the UI list state?”
3. “When you select a row, what exact ID do you pass to service update?”

Two minute triage action:

- Have learner print or log selected ID and target ID before update.
- Compare with visual row position.
- Confirm service call uses ID argument.

Remediation route:

- Persist IDs in stored records.
- Bind UI selection to ID, not visual index.
- Re run canonical flow after restart to confirm stability.

### Blocker playbook 2: UI only validation and service bypass risk

Symptoms:

- Entry fields prevent bad input, but backend accepts invalid values when called through alternate path.
- Different buttons enforce different rules.

Rapid diagnostic questions:

1. “Where is the authoritative validation function?”
2. “If another UI view calls service directly, does the rule still hold?”
3. “What exception or error object is raised for invalid data?”

Two minute triage action:

- Request direct service invocation through a quick test harness or debug console call.
- Feed known invalid value.
- Observe acceptance or rejection.

Remediation route:

- Move rule into service or model validator.
- UI handles error and displays message.
- Keep lightweight UI pre validation for user experience, but not as only guard.

### Blocker playbook 3: crash on typical error path

Symptoms:

- Clicking update with no selection crashes.
- Loading malformed JSON crashes.
- Invalid number conversion throws uncaught exception.

Rapid diagnostic questions:

1. “Which exception is thrown here?”
2. “Where is it caught?”
3. “What does user see and can they continue?”

Two minute triage action:

- Wrap fragile boundary in targeted exception handling.
- Return user feedback message.
- Preserve event loop responsiveness.

Remediation route:

- Add guard clauses before service calls.
- Add targeted catches for expected failures.
- Keep broad catch only as last resort with visible message and logging.

### Blocker playbook 4: launch reliability inconsistency

Symptoms:

- App only starts from one specific folder.
- Relative file path assumptions break on different launch context.

Rapid diagnostic questions:

1. “How do you resolve your data file path at runtime?”
2. “What working directory assumptions are hard coded?”
3. “Can you launch from project root cleanly?”

Two minute triage action:

- Normalize path resolution strategy.
- Re launch from standard course location.

Remediation route:

- Establish one canonical start command.
- Centralize path resolution.
- Verify persistence path consistently.

## Facilitation prompts that reveal understanding quickly

Use short high signal questions. Avoid long theory detours.

### Architecture prompts

- “Walk me through one button click from UI event to service mutation and back to list refresh.”
- “Which file owns business rule X?”
- “If I changed the input form tomorrow, which layer would remain unchanged?”

### Reliability prompts

- “Show me one expected user mistake and how the app recovers.”
- “How do you know update changed the intended record?”
- “What data survives restart and why?”

### Maintainability prompts

- “What code duplication did you remove during polish?”
- “What one part is still messy and what is your refactor plan?”

### Reflection prompt, required quick check

- “If you had one more hour, what would you improve first in your GUI?”

Encourage responses that tie to trust, correctness, and usability.

## Demonstration evidence template you can use live

Use this concise structure in your notes for each learner:

- Launch reliable: yes or no and any caveat.
- Add and list evidence: observed action and result.
- Update evidence: observed target correctness.
- Delete evidence: observed target correctness.
- Restart and load evidence: observed continuity.
- Stable ID gate: pass or fail with reason.
- Service validation gate: pass or fail with reason.
- Error resilience gate: pass or fail with reason.
- Architecture explanation quality: clear, partial, unclear.
- Final decision: pass, partial, not yet.
- One strength.
- One priority fix.

This format helps preserve consistency across multiple demos.

## Evidence to score examples for calibration

These examples are for instructor calibration and consistency.

### Calibration example 1: strong pass

Observed:

- App launches first try.
- Full canonical flow completed smoothly.
- Restart load works.
- Learner shows service validator and ID mapping structure.
- No selection delete shows warning and app continues.

Decision:

- Status pass.
- Likely score band 88 to 98 depending on polish and explanation depth.

### Calibration example 2: partial due to ID instability

Observed:

- Add list update delete appear to work initially.
- After restart, update changes wrong record.
- Learner admits row index mapping.

Decision:

- Status partial due to Gate 1 fail.
- Score likely 65 to 79 depending on other strengths.
- Required remediation: stable ID mapping and reload proof.

### Calibration example 3: partial due to service validation gap

Observed:

- UI blocks empty fields.
- Service direct call accepts invalid record.
- Learner cannot show central rule.

Decision:

- Status partial due to Gate 2 fail.
- Architecture score capped.
- Required remediation: move rule to service and re demonstrate.

### Calibration example 4: not yet due to repeated crash

Observed:

- Launch unstable.
- Update with no selection crashes.
- Restart load not demonstrated.

Decision:

- Status not yet.
- Focused recovery plan required.
- Coaching priority on launch and error resilience before feature expansion.

## Remediation routing matrix after checkpoint decisions

Use this routing matrix immediately after each decision.

| Decision profile | Immediate remediation route | Timebox guidance |
| --- | --- | --- |
| Pass with minor polish gaps | Assign optional extension search or filter UI and one maintainability cleanup task | 20 to 40 minutes independent follow through |
| Partial due to stable ID gate | Pair with identity mapping mini clinic and require restart load retest | 30 to 60 minutes focused |
| Partial due to service validation gate | Service boundary mini clinic and rule centralization exercise | 30 to 60 minutes focused |
| Partial due to error resilience gate | Error path hardening checklist and guard clause patch cycle | 20 to 45 minutes focused |
| Not yet due to multiple failures | Structured rebuild path: launch path, add list, stable update, stable delete, restart load | 60 to 120 minutes with instructor checkpoints |

Keep remediation specific and sequential. Do not give broad “clean up everything” guidance.

## Instructor language for high pressure moments

Use these scripts when learners are stressed or defensive.

### When learner says “it worked before class”

Say:

“I believe you. For scoring, I need live evidence now. Let us reproduce quickly and score what we can observe.”

### When learner says “I know the bug but cannot fix now”

Say:

“That is useful context. I will score demonstrated behavior today and tag a remediation target so you know the shortest path to upgrade this result.”

### When learner freezes during demo

Say:

“Take ten seconds and narrate your expected result. We can continue from there. Clear reasoning still earns credit.”

### When pair dynamics are uneven

Say:

“I need each person to answer one architecture question and one reliability question so scoring is fair.”

## Checkpoint operations for different class sizes

### Small cohort operations

If cohort size is small, run full live demos for all learners. Advantages:

- Richer evidence per learner.
- Better coaching precision.
- Easier calibration.

Use full rubric scoring in real time and provide verbal feedback immediately.

### Medium cohort operations

For medium groups:

- Run half class live, half in rotating stations.
- Use peer observer checklist to maintain activity.
- Instructor performs spot checks plus full checks for borderline cases.

Ensure every learner still demonstrates must pass gates directly.

### Large cohort operations

For large groups:

- Use timed stations with strict canonical sequence.
- Assign assistants or peer leads for evidence capture.
- Instructor validates all gate decisions personally.

Do not delegate final gate pass or fail to peers. Gate decisions remain instructor responsibility.

## Peer observation integration without weakening standards

Peer observation can increase learning if structured carefully.

Peer checklist items:

1. Did launch succeed?
2. Did canonical flow run in order?
3. Did update or delete target correct record?
4. Did restart and load show persistence?
5. Was one error path handled without crash?
6. Could learner explain service versus UI responsibilities?

Peer comments should be descriptive and evidence based:

- “When update was clicked, selected record ID remained X and changed title only.”
- “No selection delete showed warning and app remained usable.”

Discourage vague praise without evidence.

## Preventing rubric drift across instructors

If multiple instructors teach different sections, run a five minute rubric calibration before demos begin.

Calibration protocol:

1. Read must pass gates aloud.
2. Review cap rules tied to gate failures.
3. Agree on one sample partial case and one sample pass case.
4. Confirm unobserved criteria policy.

This prevents section to section score inflation or deflation.

## Boundaries and out of scope reminders for Hour 24

Keep this hour focused on GUI milestone evidence. Out of scope in this checkpoint:

- New data storage architecture overhauls.
- Long redesign discussions.
- Introducing next session implementation details.
- Non essential feature expansions that risk core reliability.

If a learner proposes major architecture changes mid demo, redirect:

“Great future idea. For this checkpoint, show reliable baseline behavior first.”

## Optional extension handling: search or filter UI

Search and filter UI is an optional extension in this hour. Treat it as bonus commentary only after baseline deliverables and must pass gates are met.

If learner includes it:

- Ask how filtering interacts with stable IDs.
- Confirm filtered views do not break update and delete targeting.
- Praise extension, but do not let it mask baseline weaknesses.

If learner does not include it:

- No penalty.
- Encourage as next improvement candidate if baseline is strong.

## High quality feedback phrasing examples

### Feedback for pass

“Your checkpoint evidence is strong. Launch was reliable, CRUD was complete through UI, restart load worked, and your service boundary is clear. Your highest leverage next step is improving user feedback messages for edge cases.”

### Feedback for partial due to stable IDs

“You are close. Core flow works, but update and delete depend on row position after reload, which creates correctness risk. Move selection mapping to stable IDs and rerun canonical flow to convert this to full pass.”

### Feedback for partial due to validation boundary

“Your UI validation is thoughtful, but business rules are not yet authoritative in service or core. Centralize validation there and keep UI as presentation and feedback. Once that is done, your architecture score will rise quickly.”

### Feedback for not yet

“You have a workable starting shell, but today we need a reliable baseline. Focus first on launch consistency and one safe error path. Then complete canonical flow in order. We will recheck once those are stable.”

## Debrief script for final group close

Use this debrief language in the final minutes:

“Checkpoint 3 is where your GUI becomes trustworthy. The strongest demos today did not just click buttons. They showed predictable behavior, stable identity, and clear responsibility boundaries.”

“The two biggest risk patterns remain the same every cohort: using row index as identity, and placing business validation only in UI code. If you address those two, your project reliability rises sharply.”

“Remember the quick check: if you had one more hour, what would you improve first in your GUI? Choose the change that increases user trust most, not just visual polish.”

## Instructor self audit before ending the hour

Before closing the session, confirm you can answer yes to each item:

- Did I run the required timing windows and crosswalk components?
- Did I state grading focus exactly as runbook language requires?
- Did I demonstrate the fast grading checklist run?
- Did learners have hands on lab time with active coaching?
- Did I evaluate all required deliverables explicitly?
- Did I enforce all three must pass gates?
- Did I use evidence to score rules consistently?
- Did I capture partial credit and remediation routes clearly?
- Did I close with the required quick check prompt?

If any answer is no, document it and adjust next cohort delivery immediately.

## Appendix: practical checkpoint checklist for rapid use

This appendix is a concise checkpoint script you can keep visible while facilitating.

Phase 1, kickoff briefing:

- State outcome and grading focus.
- Show canonical sequence.
- State must pass gates.

Phase 2, live model demo:

- Run add list update delete restart load.
- Narrate checklist evidence.

Phase 3, lab and circulation:

- Ask stable ID question.
- Ask service validation question.
- Ask no crash question.

Phase 4, scoring:

- Record evidence first.
- Apply gate caps if needed.
- Mark pass partial or not yet.

Phase 5, close:

- Deliver one strength and one priority fix.
- Ask quick check question.

## Final instructor reminder

This hour is successful when learners leave with clear truth about their current software quality and a concrete path forward. Your consistency is more important than speed, and your evidence discipline is more important than presentation polish. Keep the milestone language canonical, keep the demo sequence canonical, enforce the gates, and coach with precision.

End of Hour 24 checkpoint facilitation script.

(agent_id: issue299-hour4-rewrite — use write_agent to send follow-up messages)