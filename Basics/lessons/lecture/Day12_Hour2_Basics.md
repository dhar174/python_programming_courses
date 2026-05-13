# Session 12, Hour 2: Capstone Build Sprint

## Hour Intent and Instructor Framing

This hour is a **build sprint**, not a polish hour and not a final assessment hour. Your job is to coach students through completing a working MVP with full CRUD and reliable persistence. Keep the class anchored in Basics scope: clear functions, clean menu flow, predictable JSON read/write, and practical debugging discipline.

Use this language to set tone in the first minute:

> “This hour is about finishing the core engine of your capstone. By the end of this block, your app should reliably create, read, update, and delete records, and those records must still be there after restart. We are not polishing for presentation yet. We are building dependable functionality.”

[Facilitation cue] Write this on the board:

- **Goal 1:** CRUD complete
- **Goal 2:** Persistence across restart
- **Goal 3:** Exactly one quality improvement
- **Goal 4:** Test after each feature

Reinforce the sprint mindset:

- Small steps
- Frequent runs
- Immediate bug fixes
- Keep data schema consistent

If students ask about “nice-to-have” extras early, respond with:

> “Great idea. Park it. If CRUD + persistence are complete and stable, then we can add one optional extension at the end.”

---

## Outcomes (Runbook Alignment)

By the end of Hour 46, students should be able to demonstrate:

1. **Full CRUD implementation** in their capstone CLI:
   - Create (add record)
   - Read (list/search)
   - Update
   - Delete
2. **One UX/robustness improvement** implemented intentionally:
   - sorted output **or**
   - confirmation prompts **or**
   - input validation
3. **Persistence reliability:** data saves and loads correctly across program restarts.

Use this explicit success statement:

> “If I close your app, run it again, and your previously changed records are still correct, you are meeting today’s main technical requirement.”

---

## Pacing Plan for This Hour

Keep timing tight and visible. Announce timeboxes to maintain momentum.

- **10–15 min:** Instructor talk points (iterative build order + test-as-you-go)
- **5–10 min:** Live demo (one mutating feature end-to-end + save/load across restart)
- **25–35 min:** Hands-on lab (students complete required features + exactly one quality improvement)
- **Last 3–5 min:** Spot checks, completion verification, quick check prompt

[Facilitation cue] Put a countdown timer where students can see it. At each transition, narrate:

> “We are moving from instruction to implementation now.”

---

## Technical Baseline for Consistency During the Hour

To prevent debugging chaos, insist on one consistent record schema in all examples and coaching conversations. Use this schema for demonstrations:

```python
{
    "id": 1,
    "name": "Ada Lovelace",
    "category": "VIP",
    "status": "active"
}
```

[Facilitation cue] Tell students:

> “Whatever your project theme is—contacts, books, tasks, inventory—pick one schema and keep it stable. If save and load disagree on structure, everything else becomes unreliable.”

Recommended storage type:

- In memory: `list[dict[str, object]]`
- On disk: JSON array in `capstone_data.json`

Do not introduce advanced architecture patterns here. Keep functions straightforward and testable.

---

## Instructor Talk Points (10–15 min)

### Talking Point 1: Build Order Is a Debugging Strategy

Say this clearly:

> “The order add → list → search → update/delete is not arbitrary. It reduces uncertainty.”

Then explain why:

- **Add first:** proves record creation and write path.
- **List next:** proves what’s really in memory.
- **Search next:** builds targeting logic needed by update/delete.
- **Update/delete last:** mutating operations are safer when targeting is already reliable.

If a student asks to implement delete first, coach with:

> “Delete depends on finding the correct record. Build targeting first; then mutation is easy.”

### Talking Point 2: Test-As-You-Go Discipline

Use this phrase:

> “Do not stack untested code.”

Give them the micro-cycle:

1. Write or change one function.
2. Run program immediately.
3. Execute one realistic scenario.
4. Confirm expected output.
5. Only then move forward.

[Facilitation cue] Model this as a call-and-response:

- Instructor: “What do we do after adding a feature?”
- Class: “Run and test.”

### Talking Point 3: Persistence Is Part of Correctness

Students often think “it works” means “it works in memory.” Correct that assumption:

> “In this capstone, a feature is not complete until it survives restart.”

Define “survives restart” concretely:

1. Make a change (add/update/delete).
2. Save.
3. Exit program.
4. Run again.
5. Load.
6. Verify change still exists exactly as expected.

### Talking Point 4: One Quality Improvement Only

Be explicit to prevent scope creep:

> “This hour requires exactly one quality improvement. Choose one and do it well. We are practicing prioritization.”

Approved options:

- Sorted output
- Delete confirmations
- Input validation

Reinforce decision-making:

> “Shipping one robust improvement is better than starting three partial ones.”

### Talking Point 5: Debugging Priorities

Share a practical priority order when bugs appear:

1. Confirm function was called.
2. Print inspected record or length of list.
3. Validate input conversion (`int(...)`, `.strip()`).
4. Verify `save_data(...)` runs after mutation.
5. Re-open saved JSON and check shape.

Keep language encouraging:

> “A bug during a sprint is normal. The goal is fast diagnosis, not panic.”

---

## Live Demo (5–10 min): One Mutating Feature End-to-End + Restart Proof

### Demo Goal

Implement **update record** end-to-end, then explicitly prove persistence across restart.

Why update? It exercises targeting logic, mutation, and save behavior in one pass.

### Demo Setup Script (before coding)

Say:

> “I already have add/list/search working from earlier steps. I will now implement update, test it immediately, save, restart, and confirm the change persisted.”

### Minimal Supporting Functions (context)

Show students the fixed schema and helper functions. Keep names consistent with lab guidance.

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_FILE = Path("capstone_data.json")
Record = dict[str, Any]


def load_data(path: Path) -> list[Record]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        return []
    return data


def save_data(path: Path, records: list[Record]) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


def find_by_id(records: list[Record], record_id: int) -> Record | None:
    for record in records:
        if record.get("id") == record_id:
            return record
    return None
```

[Facilitation cue] Pause and ask:

> “Why is `find_by_id` helpful before update and delete?”

Expected answer: it centralizes targeting logic and reduces duplicated bugs.

### Live Coding: Mutating Feature (Update)

Code slowly, narrating each line’s purpose:

```python
def prompt_non_empty(label: str) -> str:
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Value cannot be blank. Please try again.")


def update_record(records: list[Record]) -> bool:
    raw_id = input("Enter record ID to update: ").strip()
    if not raw_id.isdigit():
        print("ID must be a number.")
        return False

    record_id = int(raw_id)
    target = find_by_id(records, record_id)
    if target is None:
        print(f"No record found with ID {record_id}.")
        return False

    print(f"Current name: {target['name']}")
    print(f"Current category: {target['category']}")
    print(f"Current status: {target['status']}")

    new_name = prompt_non_empty("New name: ")
    new_category = prompt_non_empty("New category: ")
    new_status = prompt_non_empty("New status: ")

    target["name"] = new_name
    target["category"] = new_category
    target["status"] = new_status
    return True
```

Narration points to include:

- “Validation first, mutation second.”
- “I return `True` only when a real update happened.”
- “This makes main menu logic cleaner.”

### Wire It Into Menu + Save

```python
def main() -> None:
    records = load_data(DATA_FILE)

    while True:
        print("\n1) Add  2) List  3) Search  4) Update  5) Delete  6) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "4":
            changed = update_record(records)
            if changed:
                save_data(DATA_FILE, records)
                print("Record updated and saved.")
            else:
                print("No update performed.")
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Demo menu: only option 4 and 6 shown here.")
```

### Test During Demo (deterministic scenario)

Use a predictable scenario, not random data:

1. Confirm starting list includes:
   - `{"id": 1, "name": "Ada Lovelace", "category": "VIP", "status": "active"}`
2. Update ID `1` to:
   - name: `Ada Byron`
   - category: `Mentor`
   - status: `active`
3. Save and print success.

### Explicit Restart Proof (required)

Narrate every step:

1. Stop the program.
2. Run program again.
3. Load records from file.
4. List/search ID `1`.
5. Confirm updated values appear.

Say this sentence explicitly:

> “The update is now persistent because it survived process restart, not just because it looked correct immediately after editing.”

### Demo Debrief Prompt

Ask:

> “What would break if I removed `save_data(...)` after update?”

Students should answer: change appears in memory only and disappears after restart.

---

## Hands-On Lab (25–35 min): Capstone Build Sprint

### Student Task Statement

Read this out:

> “You now have sprint time. Your deliverable this hour is complete CRUD plus persistence across runs, and exactly one quality improvement. Keep your schema stable and test each step as you go.”

### Required Feature Checklist

Students must complete all required features:

1. **Create**
   Add a new record using the class schema.

2. **Read — List**
   Display records clearly with ID and key fields.

3. **Read — Search**
   Search by at least one field (name is fine).

4. **Update**
   Update an existing record selected by ID.

5. **Delete**
   Delete a record selected by ID.

6. **Persistence**
   Save after each successful mutation and load on program start.

### Exactly One Quality Improvement

Students must choose **one and only one**:

- Sorted output in list view, or
- Confirmation prompt before delete, or
- Input validation for blank or invalid values

[Facilitation cue] Ask each student/team to announce their one choice before coding. This reduces accidental over-scope.

### Recommended Build Order During Lab

Coach students to follow:

1. Finish add
2. Verify list
3. Add search
4. Implement update
5. Implement delete
6. Add one quality improvement
7. Run restart test

Use this recurring reminder every 8–10 minutes:

> “Stop coding. Run it once. Confirm behavior. Then continue.”

### Instructor Circulation Script

When circulating, avoid taking over keyboards immediately. Start with diagnostic questions:

1. “Show me your record schema.”
2. “Where do you call save after mutation?”
3. “Can you show one restart proof scenario right now?”
4. “Which quality improvement did you choose?”

If they are blocked, use graduated support:

- Hint first
- Point to function boundary second
- Only provide code if needed for progress

### Spot-Check Protocol (Required During Lab)

Use this protocol exactly for each student/team check:

1. **Schema check (30–60 sec):**
   - Inspect one in-memory record.
   - Confirm keys are consistent with saved JSON.

2. **Mutation check (1–2 min):**
   - Have student perform one update or delete.
   - Confirm operation returns clear success/failure message.

3. **Save hook check (30 sec):**
   - Ask where `save_data(...)` is called.
   - Verify it runs only on successful mutation.

4. **Restart check (1–2 min):**
   - Exit app.
   - Relaunch app.
   - List/search to confirm change persisted.

5. **Quality improvement check (30–60 sec):**
   - Confirm exactly one improvement is implemented.
   - Ask student to explain why they chose it.

Document quick status mentally or on your roster:

- ✅ CRUD complete
- ✅ persistence verified
- ✅ one quality improvement complete
- ⚠ needs follow-up

### Time Calls You Can Use

At ~20 minutes remaining:

> “You should already have add/list/search stable. If not, freeze extras and finish core.”

At ~10 minutes remaining:

> “Everyone must run restart proof now. No restart proof, no completion.”

At ~5 minutes remaining:

> “Prepare to report one bug you fixed and your debugging method.”

---

## Detailed Facilitation Script for the Lab Window (Instructor Read-Aloud + Moves)

Use this section as a near-verbatim guide during the 25–35 minute sprint. You do not need to read every word, but you can use these lines to keep energy, clarity, and focus.

### Minute 0–3 of Lab: Launch and Commit

Say:

> “You are now in sprint mode. Before writing any code, write down your chosen schema and your one quality improvement. Keep both visible.”

[Facilitation cue] Walk to three different students quickly and ask:

- “Show me your schema keys.”
- “Which one quality improvement did you choose?”

If a student says, “I’ll decide later,” respond:

> “Choose now. Scope decisions made late create rushed bugs.”

### Minute 3–8: Lock in Add/List Reliability

Say:

> “Start by proving add and list are stable. If add and list are unstable, search/update/delete will be unstable too.”

Circulation checks:

- Add one record.
- List records immediately.
- Confirm field names display correctly.

If a record prints like `{'name': 'Ada'}` with missing keys, coach:

> “Great catch. Standardize now so future functions don’t branch on missing fields.”

### Minute 8–14: Build Search as Targeting Foundation

Say:

> “Search is not optional glue. It helps you verify targeting logic before mutation.”

Ask students to run a deterministic query:

- Query `ada` should find `Ada Lovelace` or `Ada Byron`.
- Query `xyz` should return zero matches with a friendly message.

If they skip zero-result handling, coach:

> “In production terms, no-match is normal behavior, not an exception. Handle it clearly.”

### Minute 14–22: Implement Update/Delete + Save Hook

Say:

> “Now implement one mutating function at a time, and test right after each one.”

Required test pattern after update:

1. Update one known ID.
2. List record and verify changed fields.
3. Exit and restart.
4. Verify change remained.

Required test pattern after delete:

1. Delete one known ID.
2. List and confirm removal.
3. Exit and restart.
4. Confirm deleted record does not return.

[Facilitation cue] If time pressure appears, prioritize:

1. update + save reliability
2. delete + save reliability
3. then quality improvement

### Minute 22–30: Apply Exactly One Quality Improvement

Say:

> “Freeze feature expansion. Now complete one quality improvement cleanly.”

Give students these decision rules:

- If their input handling is weak, choose **input validation**.
- If accidental deletes are happening, choose **confirmations**.
- If readability is poor with larger lists, choose **sorted output**.

Remind:

> “Exactly one quality improvement this hour. Do not add a second one now.”

### Minute 30–35: Prove Completion

Say:

> “You are done only after restart proof.”

Have them perform:

- one mutation,
- one save,
- one restart,
- one verification.

Then ask for verbal check:

> “Which requirement did your restart proof validate?”

Expected answer: persistence across runs.

---

## Coaching Playbook: High-Frequency Sprint Scenarios

This section gives you fast, practical responses to common student situations in Hour 46. Use these patterns to keep learners moving without solving everything for them.

### Scenario A: “My update says success but nothing changed after restart.”

Diagnosis path:

1. Ask them to show menu branch for update.
2. Confirm mutation function returns `True`.
3. Confirm `save_data(...)` is called when return is `True`.
4. Confirm file path is consistent (`capstone_data.json` in expected location).

Instructor script:

> “Let’s verify control flow before data flow. Did your function signal success? Then did menu logic save immediately after? Show those two lines first.”

Teaching point:

- Correct behavior depends on both mutation and save hook.

### Scenario B: “Delete removed the wrong record.”

Diagnosis path:

1. Inspect how record is selected (index vs ID).
2. Confirm conversion from input string to integer.
3. Confirm target is found by stable ID, not list position from a filtered subset.

Instructor script:

> “Deletion should target stable identity, not temporary display order. Let’s check whether you’re deleting by ID or by list index.”

Teaching point:

- IDs are safer than positional assumptions.

### Scenario C: “I get key errors when listing or searching.”

Diagnosis path:

1. Print one loaded record.
2. Compare with expected schema keys.
3. Inspect save function to verify shape.

Instructor script:

> “Before we touch list code, let’s inspect one real record from disk. The data shape usually reveals the bug faster than guessing.”

Teaching point:

- Data-shape validation is a first-class debugging step.

### Scenario D: “My search returns weird results.”

Diagnosis path:

1. Confirm `.lower()` on both query and searchable field.
2. Confirm `str(...)` casting if field may not be string.
3. Test with deterministic known values.

Instructor script:

> “Let’s run three known queries: one match, multiple matches if possible, and zero matches. Search quality becomes clear immediately.”

Teaching point:

- Good tests include positive and negative cases.

### Scenario E: “I’m behind; can I skip update or delete?”

Instructor response:

> “For this hour, CRUD completion is required. Let’s implement the smallest working version now: minimal prompts, clear logic, and immediate save. Fancy UX can wait.”

Rescue strategy:

1. Create `find_by_id`.
2. Implement minimal update (one field allowed is acceptable if requirement permits project rubric).
3. Implement minimal delete.
4. Attach save after each.
5. Run restart proof.

Teaching point:

- Shipping a minimal complete solution beats an incomplete ambitious one.

### Scenario F: “Can I add color output/report charts/extra menus right now?”

Instructor response:

> “Great initiative. Park that for later. Right now, the engineering requirement is correctness + persistence + one quality improvement.”

Teaching point:

- Scope control is a professional skill.

---

## Scripted Mini-Conferences (2-Minute Check-ins You Can Reuse)

Use these short scripts to keep interventions consistent and efficient while circulating.

### Mini-Conference Template 1: Progress Calibration

1. “Show me your current menu options.”
2. “Which CRUD actions are fully working now?”
3. “Where is save called after mutation?”
4. “Run one restart proof in front of me.”
5. “What is your one quality improvement?”

Closure line:

> “Your next smallest step is ___; do that now, then test before adding anything else.”

### Mini-Conference Template 2: Bug Triage

1. “What did you expect?”
2. “What happened instead?”
3. “What is the smallest repro step?”
4. “Which function owns that step?”
5. “What one print or check will confirm your hypothesis?”

Closure line:

> “Good. Run that single test and tell me what evidence you get.”

### Mini-Conference Template 3: Near-Complete Validation

1. “Run add, then list.”
2. “Run update, then list.”
3. “Run delete, then list.”
4. “Exit and relaunch.”
5. “Show persisted state.”

Closure line:

> “You’ve met core criteria. If time remains, choose the optional report export only.”

---

## Instructor Demonstration Variants for Different Class Needs

You already demonstrated update as the mutating feature. If you need a backup demo because the room is blocked on a different operation, use one of these deterministic alternatives while keeping the same schema.

### Variant 1: Delete With Confirmation (Use only if class selected confirmations)

If your class trend shows accidental deletes, demo this:

```python
def delete_record_with_confirmation(records: list[Record]) -> bool:
    raw_id = input("Enter record ID to delete: ").strip()
    if not raw_id.isdigit():
        print("ID must be a number.")
        return False

    record_id = int(raw_id)
    target = find_by_id(records, record_id)
    if target is None:
        print(f"No record found with ID {record_id}.")
        return False

    confirm = input(f"Delete '{target['name']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return False

    records.remove(target)
    print(f"Record {record_id} deleted.")
    return True
```

Narration line:

> “Notice that cancellation is a valid path and should not trigger save.”

### Variant 2: Sorted List Output (Use only if class selected sorted output)

```python
def list_records_sorted(records: list[Record]) -> None:
    if not records:
        print("No records found.")
        return

    ordered = sorted(records, key=lambda r: str(r.get("name", "")).lower())
    print("\n--- Records (Sorted by Name) ---")
    for record in ordered:
        print(
            f"ID: {record['id']} | "
            f"Name: {record['name']} | "
            f"Category: {record['category']} | "
            f"Status: {record['status']}"
        )
```

Narration line:

> “Sorted output is a read-only quality improvement. It improves usability without changing stored data.”

[Facilitation cue] Do not combine these variants in the same student project unless they have already satisfied the “exactly one quality improvement” requirement and you intentionally allow extra work after completion.

---

## Accountability Without Anxiety: What to Say When Students Are Stuck

The sprint should feel focused, not stressful. You can maintain standards while reducing panic using language that is specific and actionable.

When a student says “I’m lost,” avoid broad advice like “just debug it.” Instead, say:

> “You’re not lost; you’re at a specific failing step. Show me the exact input and output that fails.”

When a student says “Nothing works,” reply:

> “Let’s find one thing that does work. Can add+list pass right now? We’ll build from that.”

When students compare progress and feel behind:

> “Progress is not measured by number of extra features. It’s measured by reliable CRUD and restart persistence.”

When a student worries about imperfect code style:

> “Readable and correct is the target for this hour. We can polish phrasing and formatting next hour.”

This language keeps confidence up while preserving delivery expectations.

---

## Evidence Collection: What You Need to Observe Before Ending the Hour

For each learner/team, aim to capture direct evidence—not just verbal claims—of completion.

### Minimum Evidence Set

1. They run at least one create operation.
2. They run at least one update or delete operation.
3. They point to save call after successful mutation.
4. They restart the app and prove persisted result.
5. They demonstrate exactly one quality improvement.

### If Evidence Is Incomplete

Provide one immediate next action:

- “Run restart proof now.”
- “Show save hook line.”
- “Choose one quality improvement and remove extra unfinished ones.”

Avoid giving three new tasks at once. One task at a time increases completion rate under time pressure.

### End-of-Lab Status Language

Use one of these concise statements:

- “Core complete: CRUD + persistence verified.”
- “Almost complete: persistence proof still needed.”
- “In progress: finish delete and save hook first.”

These statements help students understand exactly where they stand.

---

## Reference Implementation (Instructor Fallback, Basics Scope)

Use this full example only when you need to unblock multiple learners quickly. Keep it as a reference, not a requirement to copy exactly.

It demonstrates:

- Full CRUD
- JSON persistence
- One quality improvement: **input validation**
- Deterministic behavior

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_FILE = Path("capstone_data.json")
Record = dict[str, Any]


def load_data(path: Path) -> list[Record]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Warning: data file was invalid JSON. Starting with empty data.")
        return []

    if not isinstance(data, list):
        print("Warning: data file did not contain a list. Starting with empty data.")
        return []

    return data


def save_data(path: Path, records: list[Record]) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


def next_id(records: list[Record]) -> int:
    if not records:
        return 1
    highest = max(record.get("id", 0) for record in records)
    return int(highest) + 1


def prompt_non_empty(label: str) -> str:
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Value cannot be blank. Please try again.")


def add_record(records: list[Record]) -> bool:
    name = prompt_non_empty("Name: ")
    category = prompt_non_empty("Category: ")
    status = prompt_non_empty("Status: ")

    record = {
        "id": next_id(records),
        "name": name,
        "category": category,
        "status": status,
    }
    records.append(record)
    print(f"Added record ID {record['id']}.")
    return True


def list_records(records: list[Record]) -> None:
    if not records:
        print("No records found.")
        return

    print("\n--- Records ---")
    for record in records:
        print(
            f"ID: {record['id']} | "
            f"Name: {record['name']} | "
            f"Category: {record['category']} | "
            f"Status: {record['status']}"
        )


def search_records(records: list[Record]) -> None:
    query = input("Search by name: ").strip().lower()
    if not query:
        print("Search text cannot be blank.")
        return

    matches = [r for r in records if query in str(r.get("name", "")).lower()]
    if not matches:
        print("No matching records.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for record in matches:
        print(
            f"ID: {record['id']} | "
            f"Name: {record['name']} | "
            f"Category: {record['category']} | "
            f"Status: {record['status']}"
        )


def find_by_id(records: list[Record], record_id: int) -> Record | None:
    for record in records:
        if record.get("id") == record_id:
            return record
    return None


def update_record(records: list[Record]) -> bool:
    raw_id = input("Enter record ID to update: ").strip()
    if not raw_id.isdigit():
        print("ID must be a number.")
        return False

    record_id = int(raw_id)
    target = find_by_id(records, record_id)
    if target is None:
        print(f"No record found with ID {record_id}.")
        return False

    print("Leave blank to keep current value.")
    new_name = input(f"Name [{target['name']}]: ").strip()
    new_category = input(f"Category [{target['category']}]: ").strip()
    new_status = input(f"Status [{target['status']}]: ").strip()

    if new_name:
        target["name"] = new_name
    if new_category:
        target["category"] = new_category
    if new_status:
        target["status"] = new_status

    print(f"Record {record_id} updated.")
    return True


def delete_record(records: list[Record]) -> bool:
    raw_id = input("Enter record ID to delete: ").strip()
    if not raw_id.isdigit():
        print("ID must be a number.")
        return False

    record_id = int(raw_id)
    target = find_by_id(records, record_id)
    if target is None:
        print(f"No record found with ID {record_id}.")
        return False

    records.remove(target)
    print(f"Record {record_id} deleted.")
    return True


def menu() -> str:
    print("\n--- Capstone Menu ---")
    print("1) Add record")
    print("2) List records")
    print("3) Search records")
    print("4) Update record")
    print("5) Delete record")
    print("6) Exit")
    return input("Choose an option: ").strip()


def main() -> None:
    records = load_data(DATA_FILE)
    print(f"Loaded {len(records)} record(s).")

    while True:
        choice = menu()

        if choice == "1":
            changed = add_record(records)
            if changed:
                save_data(DATA_FILE, records)
        elif choice == "2":
            list_records(records)
        elif choice == "3":
            search_records(records)
        elif choice == "4":
            changed = update_record(records)
            if changed:
                save_data(DATA_FILE, records)
        elif choice == "5":
            changed = delete_record(records)
            if changed:
                save_data(DATA_FILE, records)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1-6.")


if __name__ == "__main__":
    main()
```

[Facilitation cue] If you share this code, still require students to run a restart proof and explain one bug fix from their own process.

---

## Guided Testing Sequence for Students (Use During Lab)

Have students run this exact sequence and read outputs aloud if needed:

1. Start app with empty file.
2. Add two records:
   - `Ada Lovelace`, `VIP`, `active`
   - `Grace Hopper`, `Mentor`, `active`
3. List records and confirm both appear.
4. Search for `Ada` and confirm one match.
5. Update ID `1` name to `Ada Byron`.
6. Delete ID `2`.
7. List records and confirm only ID `1` remains with updated name.
8. Exit app.
9. Relaunch app.
10. List records and confirm state matches step 7.

Explain why this sequence is powerful:

- It covers all CRUD operations.
- It validates both in-memory behavior and disk persistence.
- It exposes save/load mismatch quickly.

---

## Completion Criteria (Must Be Met This Hour)

Use these exact checks for completion:

1. **All required features implemented**
   - add, list, search, update, delete
2. **Persistence across runs**
   - after mutation, restart still shows correct data
3. **Exactly one quality improvement**
   - sorted output or confirmations or input validation

Completion is binary for this hour:

- If CRUD is partial, not complete.
- If persistence is not proven, not complete.
- If quality improvement is missing, not complete.

[Facilitation cue] Keep phrasing neutral and supportive:

> “You are close. Let’s finish the missing requirement in order: first persistence proof, then we can celebrate completion.”

---

## Common Pitfalls (Instructor Eyes Open During Circulation)

### Pitfall 1: Save Not Called After Updates

Symptom:

- Student updates or deletes successfully.
- Data looks correct immediately.
- After restart, old data returns.

Root cause:

- Mutation happened in memory, but `save_data(...)` was not called afterward.

Fast fix:

1. Ensure mutating functions return `True` only on success.
2. In menu logic, call `save_data(...)` when return is `True`.

Coaching line:

> “A mutating feature is incomplete until save is triggered after success.”

### Pitfall 2: Data Structure Mismatch Between Save and Load

Symptom:

- Load errors or weird behavior during list/search.
- Code expects dict keys, but loaded items are strings or wrong shape.

Root cause:

- Save function writes one structure, load/feature functions assume another.

Fast fix:

1. Define schema once (board + top of file comment).
2. Ensure every function uses same keys (`id`, `name`, `category`, `status`).
3. Print one loaded record to verify shape before deeper debugging.

Coaching line:

> “When data shape drifts, every feature becomes fragile. Stabilize schema first.”

---

## Optional Extension (Clearly Optional, Only If Core Is Complete)

If and only if a student has completed all required criteria, offer:

### Optional: Simple Text Report Export

Goal:

- Generate a plain text summary file (for example `report.txt`) showing total record count and current records.

Keep it simple and deterministic. No timestamps required.

```python
from pathlib import Path


def export_report(records: list[dict[str, object]], path: Path) -> None:
    lines = ["Capstone Report", "==============", f"Total records: {len(records)}", ""]
    for record in records:
        lines.append(
            f"ID {record['id']}: {record['name']} | "
            f"{record['category']} | {record['status']}"
        )
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {path}")
```

[Facilitation cue] If offering this extension, say:

> “This is optional. Do not start this unless CRUD and restart persistence are already proven.”

---

## Instructor Language Bank for Sprint Coaching

Use short, repeatable prompts while circulating:

- “Show me where save happens after mutation.”
- “Can you restart now and prove persistence?”
- “What is your one quality improvement?”
- “What does your loaded data look like? Print one record.”
- “Which feature is the next smallest step?”

Use confidence-building responses:

- “Good bug report. You already isolated the failing step.”
- “Great: you tested before adding new code.”
- “Nice recovery—you fixed root cause, not just symptom.”

Avoid accidental drift into Hour 47 by redirecting:

- “README/demo polish is next hour. Right now, finish core behavior.”
- “Keep UI nice enough to use, but prioritize correctness and persistence first.”

---

## End-of-Hour Debrief Flow (3–5 min)

Bring class back together and run this sequence:

1. Ask for one volunteer to show restart proof in under 60 seconds.
2. Ask a second volunteer to show their one quality improvement.
3. Highlight one debugging win from the room.
4. Re-state completion standard for anyone still finishing.

Suggested debrief script:

> “Today’s sprint measured engineering discipline: build order, test cycle, and persistence reliability. If your app can mutate data and survive restart, you built a real foundation.”

---

## Quick Check / Exit Ticket (Required Prompt)

Ask every learner:

> **“What is one bug you fixed during this sprint, and how did you figure it out?”**

If time allows, ask one follow-up:

> “What clue pointed you to the root cause?”

This reinforces debugging process over guesswork and gives you signal for targeted support in the next hour.

---

## Instructor Self-Check Before Ending the Hour

Confirm you stayed aligned to Hour 46 and did not drift:

- [ ] Focus remained on CRUD build sprint
- [ ] Iterative order was taught explicitly: add → list → search → update/delete
- [ ] Test-as-you-go discipline was reinforced repeatedly
- [ ] Live demo included one mutating feature end-to-end
- [ ] Live demo explicitly showed save/load across restart
- [ ] Lab required all features + exactly one quality improvement
- [ ] Spot-check protocol was used during circulation
- [ ] Completion criteria were verified against persistence
- [ ] Common pitfalls were addressed
- [ ] Optional extension was presented as optional only
- [ ] Quick check prompt was delivered

If all boxes are checked, this hour is complete and correctly aligned to the runbook.
