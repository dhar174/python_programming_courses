# Day 2 — Hour 8 (Session 2): Checkpoint 1 — Fundamentals Mini-Assessment

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 2, Hour 8  
**Duration:** 60 minutes (assessment-centric)  
**Mode:** Brief instructor framing + timeboxed individual checkpoint + debrief

---

## Instructor Deliverable Script (Largely Verbatim)

> This script is designed for direct delivery and aligns with the runbook assessment model for Hour 8.

---

## 0) Learning Outcomes (read aloud)

“By the end of this hour, learners will:
1. Demonstrate practical use of variables, numbers, strings, input, and conversion.
2. Build a small complete program from requirements.
3. Show clear, readable output formatting for a simple receipt.
4. Reflect on one debugging step they used during implementation.”

---

## 1) Agenda + Timing

- **0:00–0:08** Checkpoint framing, rules, rubric walkthrough
- **0:08–0:50** Individual checkpoint lab (Simple Receipt Generator)
- **0:50–0:57** Debrief + quick oral checks
- **0:57–1:00** Session 2 wrap + Session 3 preview

---

## 2) Checkpoint Rules Script (verbatim)

“Welcome to Checkpoint 1. This is open-book and individual. You can use your notes, your previous scripts, and class materials. The purpose is not memorization; the purpose is demonstration of basic competence.

This checkpoint is timeboxed. Focus on correctness first, then formatting. If you get stuck, simplify your approach and make sure the core requirements are working before adding extras.

I can clarify requirements, but I will not provide direct solutions. Think of this as a low-pressure simulation of real coding work: read requirements, build incrementally, test, and submit.”

---

## 3) Assessment Task: Simple Receipt Generator

## 3.1 Problem statement (read aloud slowly)

“Build a Python script that generates a simple receipt for one item purchase.

Your script must:
1. Ask for item name.
2. Ask for quantity.
3. Ask for price per item.
4. Compute **subtotal** as quantity × price per item.
5. Compute **total**. In this baseline version, there is no tax or discount, so **total equals subtotal**.
6. Print a neat receipt that includes item, quantity, unit price, subtotal, and total.
7. Format money values to two decimal places.”

> **Accuracy consistency note for instructor:** In the required version, `total` must be present and must equal `subtotal`. If tax/discount is added, that is extension only, not baseline.

## 3.2 Required output format (example)

```text
=== Receipt Generator ===
Enter item name: Widget
Enter quantity: 3
Enter price per item: 9.99

========== RECEIPT ==========
Item:     Widget
Quantity: 3
Price:    $9.99 each
-----------------------------
Subtotal: $29.97
Total:    $29.97
=============================
```

**Instructor emphasis:**
- “Both subtotal and total are required output lines.”
- “In the baseline, they match.”

---

## 4) Rubric Walkthrough (5–8 minutes)

### Rubric categories

1. **Program runs end-to-end (35%)**
   - Starts and finishes without crash on valid input.
   - Prompts and output appear in logical order.

2. **Correct math and types (35%)**
   - `quantity` converted to integer.
   - `price_per_item` converted to float.
   - `subtotal = quantity * price_per_item`.
   - `total = subtotal` in baseline requirements.

3. **Readable output formatting (20%)**
   - Money shown to 2 decimals.
   - Labels are clear.
   - Receipt structure is easy to read.

4. **Code clarity (10%)**
   - Meaningful variable names.
   - Logical sectioning with minimal helpful comments.

### Rubric script to read aloud

“I will grade for correctness, readability, and basic code quality—not for advanced features. If your script is simple but correct, that is excellent for this stage.”

---

## 5) Suggested Build Sequence (project this as guidance)

1. Print title.
2. Collect inputs as text.
3. Convert numeric fields.
4. Compute subtotal.
5. Set total equal to subtotal (baseline).
6. Print receipt lines with formatting.
7. Test with sample data.

**Say:**
“Build in this order and run after each step. Frequent small runs prevent large debugging sessions.”

---

## 6) Reference Solution (for instructor debrief)

> Do **not** show this at start unless needed for accommodations. Use after checkpoint or for guided recovery.

```python
# Checkpoint 1: Simple Receipt Generator
print("=== Receipt Generator ===")

item_name = input("Enter item name: ").strip()
quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price per item: "))

subtotal = quantity * price_per_item
# Baseline requirement: no tax/discount yet
total = subtotal

print()
print("=" * 28)
print("         RECEIPT")
print("=" * 28)
print(f"Item:     {item_name}")
print(f"Quantity: {quantity}")
print(f"Price:    ${price_per_item:.2f} each")
print("-" * 28)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
print("=" * 28)
```

---

## 7) Instructor Monitoring Script During Work Time

### At minute 10

“Checkpoint: everyone should have prompts and variable assignments complete.”

### At minute 20

“Checkpoint: make sure `quantity` and `price_per_item` are numeric types before multiplication.”

### At minute 30

“Checkpoint: verify your subtotal with a calculator for one sample input.”

### At minute 38

“Checkpoint: add total line and confirm total equals subtotal in baseline version.”

### At minute 45

“Checkpoint: polish output formatting to two decimals and clear labels.”

---

## 8) Common Pitfalls + Instructor Responses

### Pitfall 1: forgetting numeric conversion

```python
price = input("Enter price: ")
subtotal = price * 3
```

**Issue:** text repetition, not arithmetic.

**Response script:**
“Check your variable types with `print(type(variable))`. Convert price with `float()`.”

### Pitfall 2: quantity read as float unnecessarily

Not fatal, but for count values `int` is clearer.

**Response:**
“Use `int` for quantity to communicate that count is whole-number.”

### Pitfall 3: subtotal and total inconsistency

Example bug:

```python
subtotal = quantity * price
total = subtotal + price  # unintended extra item
```

**Response script:**
“Re-read requirement: baseline has no tax/discount. Total should equal subtotal exactly.”

### Pitfall 4: formatting omitted

```python
print("Subtotal:", subtotal)
```

**Response:**
“Use f-strings with `:.2f` for money. It improves clarity and grading consistency.”

### Pitfall 5: unhelpful variable names

```python
a = int(input())
b = float(input())
c = a * b
```

**Response:**
“Choose names that explain purpose: `quantity`, `price_per_item`, `subtotal`.”

---

## 9) Optional 10-minute Quiz Segment (if schedule allows)

Use this only if class pace supports it after coding.

### Sample questions

1. What is the type of `input()` return value?  
   **Answer:** `str`

2. What does `len("Python")` return?  
   **Answer:** `6`

3. Which expression is true for `text = "Hello"`?  
   - A) `"he" in text`
   - B) `"He" in text`  
   **Answer:** B (case-sensitive)

4. What happens with `int("3.5")`?  
   **Answer:** `ValueError`

5. Which line formats price to 2 decimals?  
   **Answer:** `f"${price:.2f}"`

---

## 10) Debrief Script (7 minutes)

“Let’s debrief quickly. This checkpoint tested real fundamentals: input, types, arithmetic, and output formatting.

Raise your hand if your first run worked end-to-end. Great. If it didn’t, that is normal. Debugging is part of coding, not a sign of failure.

Now, pair-share for one minute: what error did you hit first, and how did you fix it?”

After pair-share, ask 2 learners:
1. “What was the issue?”
2. “How did you diagnose it?”
3. “What exact code change fixed it?”

---

## 11) Session 2 Wrap Script (verbatim)

“In Session 2, we built a strong fundamentals stack:
- Hour 5: string indexing, slicing, and `len()`.
- Hour 6: method-based text normalization and search.
- Hour 7: interactive input and numeric conversion.
- Hour 8: a mini-assessment that combines all of the above.

If today felt challenging, that is expected. You are building real programming habits, not memorizing isolated commands.”

---

## 12) Session 3 Preview (must match runbook sequence)

“Next session follows this exact sequence:
1. **Hour 9:** comparisons and boolean logic.
2. **Hour 10:** string formatting with f-strings.
3. **Hour 11:** text operations with `split()` and `join()`.
4. **Hour 12:** debugging habits at Basics level.

That progression will help you write clearer decisions, cleaner output, and stronger troubleshooting workflows.”

---

## 13) Extended Verbatim Facilitation Script (for full instructor support)

“Before you code, pause and translate the requirement into variable language. We need one item name, one quantity, one unit price. That suggests variables named `item_name`, `quantity`, and `price_per_item`. Then we need `subtotal` and `total`. Naming is not cosmetic; naming is thinking.

Next, think type expectations. Item name is text (`str`). Quantity is a count (`int`). Price per item may include decimals (`float`). If we start with correct types, the calculation step becomes straightforward.

Now, build incrementally. Don’t write 30 lines before your first run. Write 5 lines, run once. Add 5 lines, run again. This is how professionals avoid deep debugging traps.

When you format output, remember that users read labels, not variables. A line like `29.97` is technically right but context-poor. A line like `Subtotal: $29.97` is right and understandable. Communication is part of correctness.

If your output value seems strange, perform a plausibility check. Example: quantity 3 and price 9.99 should produce around 30. If you get 2997 or 9.999.999.99, you likely have either multiplication by wrong value or string repetition from missing conversion.

About `subtotal` and `total`: in many real systems, total includes tax, discounts, and fees. In our baseline task, we explicitly keep those out so fundamentals remain the focus. Therefore total equals subtotal. Do not invent extra math in the required version.

If you finish early, you may add optional features. But only after baseline is correct and tested. In engineering, delivering a complete baseline is better than delivering half-finished advanced features.

I also want you to notice your own debugging language. Instead of ‘it doesn’t work,’ say: ‘my script crashes on line 8 with ValueError when converting price.’ That precision speeds up help and builds professional communication skills.

As instructor, I will answer requirement clarifications and process questions. I won’t provide direct final code during assessment time, because the goal is independent synthesis. You are ready for this. Start with a clean file, use meaningful names, and run early and often.”

---

## 14) Guided Recovery Path (if class is struggling)

If many learners stall, use this scaffold publicly without giving complete final solution immediately.

### Step 1: just prompt and print

```python
item_name = input("Enter item name: ")
quantity_text = input("Enter quantity: ")
price_text = input("Enter price per item: ")

print(item_name, quantity_text, price_text)
```

### Step 2: convert types and print types

```python
quantity = int(quantity_text)
price_per_item = float(price_text)

print(type(quantity), type(price_per_item))
```

### Step 3: compute and print raw numbers

```python
subtotal = quantity * price_per_item
total = subtotal

print(subtotal, total)
```

### Step 4: format final receipt

```python
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
```

This keeps rigor while helping learners recover.

---

## 15) Optional Extension (post-baseline only)

### Tax extension example

```python
tax_rate = 0.08
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Total:    ${total:.2f}")
```

**Instructor reminder:** If extension is used, clearly label it as beyond baseline and not required for checkpoint grading.

---

## 16) Informal Grading Notes for Instructor

Fast-check list:
- [ ] Prompts are present and understandable.
- [ ] Quantity uses integer conversion.
- [ ] Price uses float conversion.
- [ ] Subtotal computed correctly.
- [ ] Total line present and baseline-consistent.
- [ ] Money formatting uses 2 decimals.
- [ ] Output is readable.

---

## 17) Scope Guardrails (Basics only)

In scope:
- plain script files
- input + conversion
- arithmetic + f-string formatting
- simple receipt output

Out of scope for this checkpoint:
- classes
- file persistence
- database writes
- complex validation loops

---

## 18) Final 60-second close

“Checkpoint complete. Whether your first attempt was smooth or messy, you did real programming work: read requirements, implemented logic, tested output, and debugged under time constraints. That is exactly how competence grows. Next session we continue with comparisons and booleans, then f-strings, then split/join, and then dedicated debugging habits.”

---

## 19) Additional drill prompts (for homework or extra support)

1. Modify receipt to support two items (still no loops).
2. Add an optional discount percent and recalculate total.
3. Add tax as extension and compare baseline vs taxed total.
4. Ask user to enter currency symbol and print with it.
5. Compare outputs with and without `:.2f`.
6. Print a warning if quantity is zero.
7. Write one sentence explaining difference between subtotal and total.
8. Create three test inputs and expected outputs before coding.
9. Perform peer review for variable naming and readability.
10. Reflect on one debugging habit to keep using.

These exercises preserve Basics scope while reinforcing checkpoint concepts.

---

## 20) Appendix A — Extended Minute-by-Minute Assessment Facilitation Script

### 00:00–00:03 Settling and emotional framing

“Take a breath. This is a checkpoint, not a trap. You are expected to think, test, and revise. Real programming looks like that.

Open a new script file named `checkpoint1_receipt.py` and keep your notes nearby.”

### 00:03–00:06 Rules and expectations

“Reminder: open-book, individual work, and timeboxed. I can clarify wording and requirements, but I won’t provide direct final code during build time.

Your goal is a correct baseline solution before optional extras.”

### 00:06–00:08 Rubric emphasis

“Scoring prioritizes: runs without crashing, correct math/types, readable formatted output, and clear variable names.”

### 00:08–00:12 Requirement parsing aloud

“Let’s parse the requirement line by line:
- one item name,
- one quantity,
- one unit price,
- subtotal calculation,
- total line present and equal to subtotal in baseline,
- receipt formatting with two-decimal money.

If you meet those points, you are in strong shape.”

### 00:12–00:18 Build phase checkpoint 1

“By this point, you should have prompts written. If not, stop adding features and get prompts done first.”

### 00:18–00:24 Build phase checkpoint 2

“Now convert quantity and price to numeric types. If your math result looks wrong, print `type(quantity)` and `type(price_per_item)`.”

### 00:24–00:30 Build phase checkpoint 3

“Compute subtotal and total. Re-read requirement: baseline total equals subtotal. Do not add hidden fees in required version.”

### 00:30–00:36 Build phase checkpoint 4

“Format receipt lines with labels and `:.2f` for currency. Output readability is graded.”

### 00:36–00:42 Build phase checkpoint 5

“Run with the sample data:
- item: Widget
- quantity: 3
- unit price: 9.99
Expected subtotal and total: 29.97.

If your result differs, verify multiplication and type conversion.”

### 00:42–00:48 Build phase checkpoint 6

“Final polish: spacing alignment, clear section separators, no debugging prints left in final output.”

### 00:48–00:50 Submission prep

“Save and run once more from start to finish. Confirm no syntax errors and no leftover temporary code.”

### 00:50–00:57 Debrief discussion

“Share one bug, one fix, and one testing strategy you used. We learn as much from repair process as from first-pass success.”

### 00:57–01:00 Session close and next-session preview

“Excellent effort. We now move to comparisons/booleans, f-strings, split/join, and debugging habits in Session 3.”

---

## 21) Appendix B — Clarification FAQ to Read During Checkpoint

**Q1: Do I need both subtotal and total lines?**  
A: Yes. Baseline requires both. In baseline, total equals subtotal.

**Q2: Should I include tax?**  
A: Not in baseline. Tax is optional extension after required version works.

**Q3: Can quantity be float?**  
A: Baseline expects integer quantity.

**Q4: Is exact spacing graded?**  
A: Perfect spacing is not required, but output must be clean and readable with clear labels.

**Q5: Can I use additional helper variables?**  
A: Yes, if they improve clarity.

---

## 22) Appendix C — Additional Valid Test Cases (Instructor Use)

Use these to quickly verify learner solutions:

1. `Pen`, quantity `2`, price `1.50`  
   subtotal/total = `3.00`

2. `Notebook`, quantity `1`, price `4.99`  
   subtotal/total = `4.99`

3. `Cable`, quantity `5`, price `2.25`  
   subtotal/total = `11.25`

4. `Sticker`, quantity `0`, price `0.99`  
   subtotal/total = `0.00` (technically valid baseline math)

5. `Keyboard`, quantity `3`, price `49.95`  
   subtotal/total = `149.85`

These cases reveal conversion or multiplication errors quickly.

---

## 23) Appendix D — Incremental Scaffold for Learners Needing Support

### Phase 1: Inputs only

```python
print("=== Receipt Generator ===")
item_name = input("Enter item name: ")
quantity_text = input("Enter quantity: ")
price_text = input("Enter price per item: ")
print(item_name, quantity_text, price_text)
```

### Phase 2: Convert + inspect

```python
quantity = int(quantity_text)
price_per_item = float(price_text)
print(type(quantity), type(price_per_item))
```

### Phase 3: Compute

```python
subtotal = quantity * price_per_item
total = subtotal
print(subtotal, total)
```

### Phase 4: Format final receipt

```python
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
```

This sequence helps without removing learner agency.

---

## 24) Appendix E — Instructor Debrief Prompts

Use these prompts to strengthen metacognition:

1. “Where did your first bug appear—input, conversion, math, or formatting?”
2. “How did you verify your fix?”
3. “What test input gave you the most confidence?”
4. “If you had five more minutes, what improvement would you add?”
5. “What will you do earlier next time to avoid late-stage errors?”

---

## 25) Appendix F — Session 2 Consolidation Notes

Reinforce skill chain explicitly:
- From Hour 5: positional text handling (`[0]`, slicing, `len`).
- From Hour 6: normalization and containment checks.
- From Hour 7: input conversion and numeric formulas.
- In Hour 8: synthesis into one coherent script.

This helps learners see continuity instead of isolated exercises.

---

## 26) Appendix G — Expanded Session 3 Preview Talk Track

“Session 3 starts with decision-making logic. In Hour 9, we use comparisons and boolean operators to make decisions based on user data. In Hour 10, we strengthen output quality with f-strings and formatting patterns. In Hour 11, we process text more deeply with split and join operations. In Hour 12, we formalize debugging habits so errors become manageable and informative.

That sequence is intentional: evaluate conditions, present information clearly, manipulate text structures, and debug effectively. Keep your Session 2 scripts—they become raw material for practicing Session 3 concepts.”

---

## 27) Appendix H — Instructor Reflection Checklist

After the hour, note:
- [ ] Did learners submit runnable scripts?
- [ ] Were subtotal and total lines both present and baseline-consistent?
- [ ] Were type conversions generally correct?
- [ ] Did output formatting meet two-decimal expectation?
- [ ] Which misconception should be revisited before Hour 9?

These notes improve instructional continuity.

---

## 28) Appendix I — Extended Troubleshooting Matrix for Checkpoint Facilitation

### Issue: Program crashes before receipt prints

Likely causes:
- syntax error,
- conversion error,
- variable name mismatch.

Facilitation script:
1. “Run again and read first error line.”
2. “Fix that first error only.”
3. “Run again; repeat cycle.”

### Issue: Output prints but subtotal is incorrect

Likely causes:
- wrong formula,
- quantity/price not converted,
- accidental string multiplication.

Facilitation script:
- “Print `quantity`, `price_per_item`, and their types.”
- “Manually compute one test expected value.”
- “Compare with script output.”

### Issue: subtotal and total differ unexpectedly

Likely causes:
- unintended extra arithmetic,
- leftover extension code.

Facilitation script:
- “For baseline, set `total = subtotal` exactly.”
- “Add tax/discount only after baseline passes.”

### Issue: formatting inconsistent

Likely causes:
- plain prints without f-strings,
- decimal formatting omitted.

Facilitation script:
- “Use `f"${value:.2f}"` for each money field.”

---

## 29) Appendix J — Extended Debrief Talk Track

“Let’s normalize what just happened. During a checkpoint, most learners encounter at least one bug. That is normal and expected. What matters is process.

A productive process usually looked like this:
1. run code,
2. read error,
3. isolate issue,
4. apply small fix,
5. re-run.

Notice this process mirrors professional software development more than ‘write once, run once’. If you practiced this cycle today, you are developing real engineering habits.

Now consider communication quality in your output. A receipt is not just math; it is a user-facing artifact. Labels, alignment, and decimals make your script useful to another person, not just to you.

Also notice requirement discipline. Some learners added tax or discount immediately and got stuck. Baseline-first strategy reduces risk and improves completion rates. Build required version first, then extend.

Finally, this checkpoint is cumulative evidence from Session 2. You successfully combined string handling, normalization awareness, type conversion, and basic arithmetic formatting into one coherent workflow.”

---

## 30) Appendix K — Additional Practice Checkpoint Variants

### Variant 1: Grocery item receipt

Same structure, different labels.

### Variant 2: Service invoice line

Input service name, hours, hourly rate; subtotal and total baseline equal.

### Variant 3: Ticket purchase receipt

Input event name, tickets, ticket price; subtotal and total baseline equal.

For each variant, maintain baseline consistency: `total = subtotal` unless extension clearly labeled.

---

## 31) Appendix L — Instructor Notes for Consistency Audits

Before distributing checkpoint instructions, verify internal consistency across:
- requirement text,
- sample output,
- rubric criteria,
- solution reference.

For this hour, consistency rule is explicit:
- subtotal calculated from quantity × unit price,
- total shown and equal to subtotal in baseline.

This avoids learner confusion and grading disputes.

---

## 32) Appendix M — Final Session 2 Closing Script (Long Form)

“Session 2 has focused on practical fundamentals that appear in nearly every beginner script. We started by reading text precisely through indexing and slicing. We then learned to normalize and search text using string methods. Next, we added interactive input and type conversion so scripts could work with user-provided values. Finally, we synthesized those pieces in this checkpoint.

If you felt moments of friction today, that is exactly where growth occurred. Programming confidence comes from repeated cycles of attempting, observing, and refining. You now have a concrete workflow for building small but complete programs: gather input, convert types, compute values, format outputs, and verify against sample expectations.

Session 3 extends this foundation in a structured order: comparisons and booleans first, then f-string formatting depth, then split/join text operations, then explicit debugging habits. Keep your scripts from today—they are valuable material for practicing those upcoming concepts.

Well done on finishing Checkpoint 1.”

---

## 33) Appendix N — Rapid-Fire Checkpoint Debrief Bank

Use these prompts right after submissions.

1. Which variable in your script was most important for readability?
2. Where did you perform numeric conversion, and why there?
3. How did you verify subtotal correctness?
4. Why does baseline total equal subtotal in this checkpoint?
5. What formatting choice improved receipt clarity most?

### Quick diagnostic prompts for common bugs

- “Print `type(quantity)` and `type(price_per_item)`.”
- “Show expected subtotal from manual math.”
- “Confirm `total = subtotal` in baseline.”
- “Check each money line uses `:.2f`.”

### Mini reflection script to read aloud

“Checkpoint outcomes are strongest when you can explain your choices, not just show your output. If you can describe your variable types, formula, and one debugging step, you are building durable coding competence.”

### Closing reinforcement

“Keep your final receipt script. In Session 3, we will reuse the same style of thinking—clear conditions, clean formatting, text operations, and explicit debugging habits.”

---

## 34) Appendix O — Final Reinforcement Notes

Instructor reminder script:
“Hour 8 is successful when learners can produce a complete, readable baseline solution and explain one debugging decision they made. Keep rubric language consistent with requirements: subtotal and total are both required, and baseline total equals subtotal.”

Mini verification snippet:

```python
quantity = 3
price_per_item = 9.99
subtotal = quantity * price_per_item
total = subtotal
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
```

Use this as a final clarity check before grading.

---

## 35) Appendix P — Grading Consistency Reminder Script

Use this exact language with co-instructors or TAs:

“Grade the baseline solution against baseline requirements. Confirm both subtotal and total lines are present. Confirm baseline total equals subtotal unless the student clearly labels an optional extension (tax/discount). Do not penalize minor spacing preferences if values and labels are clear and money formatting is correct.”

This closes the loop between instructions, sample output, rubric, and solution.

Additional recap script:
“Baseline completion is the goal. Fancy extras are optional after correctness. Clear requirements, consistent math, and readable output are professional habits you are already practicing.”

Instructor final reminder:
“During debrief, restate the consistency rule one more time: baseline subtotal and total should both appear, and baseline total equals subtotal. This prevents mixed interpretations and keeps grading fair. Invite learners to save their checkpoint script as a reference artifact for Session 3.”

Closing checklist for learners:
- My script runs end-to-end.
- My quantity and price conversions are correct.
- My subtotal and total are present and baseline-consistent.
- My receipt formatting is readable and uses two-decimal money output.
Final note: baseline-first execution is the expected professional workflow.
