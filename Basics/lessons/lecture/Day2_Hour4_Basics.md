# Day 2, Hour 4: Checkpoint 1 — Fundamentals Mini-Assessment (Course Hour 8)

**Python Programming Basics – Session 2**  
**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 2, Course Hour 8  
**Duration:** 60 minutes (assessment-centric)  
**Mode:** Instructor framing + timeboxed individual checkpoint + debrief  
**Instructor Deliverable Script:** Designed for direct delivery, aligned with the runbook assessment model for Hour 8.

---

## Learning Outcomes

By the end of this hour, learners will:

1. **Consolidate learning from Day 1 and Day 2 (Hours 1–7):** Synthesize all fundamentals covered in the previous 7 hours into a cohesive mini-project.
2. **Apply fundamentals (variables, data types, operators, strings, input/output) in combination:** Demonstrate practical use of variables, numbers, strings, input, and numeric conversion in a single working script.
3. **Debug multi-step programs:** Build a small complete program from requirements, test incrementally, and show clear, readable output formatting.
4. **Explain design decisions and best practices:** Reflect on variable naming, type choices, and one debugging step they used during implementation.
5. **Prepare for Day 3 (conditional logic):** Establish a solid foundation in fundamentals that will support conditional structures and loops in the next session.

This checkpoint is **open-book and individual**. You can use your notes, your previous scripts, and class materials. The purpose is not memorization; the purpose is demonstration of basic competence with independent synthesis.

---

## Instructor Prep & Setup Checklist

### Before the hour begins

- [ ] Print or display the **Simple Receipt Generator** problem statement (provided below).
- [ ] Have the **Reference Solution** open in an editor for quick access during debrief or recovery.
- [ ] Review the **Rubric** (4 categories: correctness 35%, math/types 35%, formatting 20%, code clarity 10%).
- [ ] Prepare timer or clock for 50-minute checkpoint window (0:08–0:50).
- [ ] Test that `input()`, `int()`, `float()`, f-strings with `:.2f`, and `print()` work in your environment.
- [ ] Have submission portal ready (GitHub Classroom, file upload, or local folder).
- [ ] Brief any TAs or co-instructors on monitoring milestones (10-min, 20-min, 30-min, 38-min, 45-min checks).
- [ ] Optional: Print the **Guided Recovery Path** to display if class stalls.

### Materials needed

- Student machines with Python 3.x and a code editor.
- Blank script template or empty file for each learner named `checkpoint1_receipt.py`.
- Internet access for documentation (if allowed per checkpoint rules).

---

## Opening Script

"Welcome to Checkpoint 1. This is an open-book, individual assessment. You can use your notes, your previous scripts, and class materials. The purpose is not memorization; the purpose is demonstration of basic competence.

This checkpoint is timeboxed: you have 50 minutes to build and test a complete program. Focus on correctness first, then formatting. If you get stuck, simplify your approach and make sure the core requirements are working before adding extras.

I can clarify requirements, but I will not provide direct solutions. Think of this as a low-pressure simulation of real coding work: read requirements, build incrementally, test, and submit.

Here's what we'll do:
1. I'll walk through the problem and rubric (8 minutes).
2. You'll work on your receipt generator (50 minutes).
3. We'll debrief and share insights (7 minutes).
4. Final wrap and preview of Day 3 (3 minutes).

Let's start. Open a new file called `checkpoint1_receipt.py` and keep your notes nearby. You are ready for this."

---

## Core Concepts

### Checkpoint purpose

This assessment combines all fundamentals from Day 1 and Day 2 (Hours 1–7) into a single working program. It tests:
- **Input and conversion:** Reading user input as text and converting to appropriate types.
- **Variable naming:** Choosing clear, descriptive names that reflect purpose.
- **Arithmetic:** Computing subtotal as quantity × price per item.
- **String formatting:** Displaying money values to 2 decimal places using f-strings.
- **Output design:** Creating a readable receipt structure with clear labels.

### Assessment model

- **Timeboxed:** 50 minutes to plan, code, test, and submit.
- **Incremental:** Encouraged to build and test frequently (not write 30 lines then run once).
- **Open-book:** Class materials, notes, and previous scripts are available.
- **Individual:** Each learner submits their own work.

### Design principles for this hour

1. **Requirements first:** Translate the written problem into variable names and logic before coding.
2. **Types matter:** Choosing the right type (`int` vs `float`) clarifies intent and prevents bugs.
3. **Readable output:** Users read labels and formatted values; output is not just data, it's communication.
4. **Baseline sufficiency:** A correct, simple solution is better than a half-finished advanced one.
5. **Debugging as learning:** Errors during implementation are normal and reveal understanding.

---

## Live Coding Demo

### Demo: Walk through the Simple Receipt Generator solution step-by-step

"I'll show you one way to approach this. This is not the only way, but it demonstrates the concepts clearly.

#### Step 1: Outline your variables

Before touching code, think about what you need:
- Item name (text)
- Quantity (a count, so integer)
- Price per item (decimal, so float)
- Subtotal (quantity × price)
- Total (subtotal, no tax yet)

#### Step 2: Write prompts and collect input

```python
# Checkpoint 1: Simple Receipt Generator
print("=== Receipt Generator ===")

item_name = input("Enter item name: ").strip()
quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price per item: "))
```

Notice: I call `.strip()` on the name to remove accidental spaces. I convert quantity to `int` and price to `float` immediately.

#### Step 3: Compute subtotal and total

```python
subtotal = quantity * price_per_item
# Baseline requirement: no tax/discount yet
total = subtotal
```

At this point, if something is wrong, print these values to debug: `print(quantity, price_per_item, subtotal)`.

#### Step 4: Format and print the receipt

```python
print()
print("========== RECEIPT ==========")
print(f"Item:     {item_name}")
print(f"Quantity: {quantity}")
print(f"Price:    ${price_per_item:.2f} each")
print("-----------------------------")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
print("=============================")
```

The f-string `:.2f` ensures all money values display with exactly 2 decimal places. The labels make the receipt readable.

#### Step 5: Test with sample data

```
Sample input:
  Item: Widget
  Quantity: 3
  Price per item: 9.99

Expected output:
  Subtotal: $29.97
  Total: $29.97
```

Test it yourself. If you get 29.97, you're correct. If you get something else (2997, 9.999.999.99, etc.), there's a type mismatch or missing conversion.

That's the full solution. The key moves are: plan variables → collect input with conversion → compute → format output."

---

## Guided Lab with Checkpoints

### Problem statement (read aloud slowly)

"Build a Python script that generates a simple receipt for one item purchase.

**Requirements:**
- Input: item name, quantity, price per item.
- Compute subtotal as quantity × price per item.
- Compute total. In this baseline version, there is no tax or discount, so total equals subtotal.
- Print a neat receipt with aligned lines; money values rounded to 2 decimals using f-strings with `:.2f`.

Your script must:
1. Ask for item name.
2. Ask for quantity.
3. Ask for price per item.
4. Compute **subtotal** as quantity × price per item.
5. Compute **total**. In the baseline version, total equals subtotal.
6. Print a receipt that includes item, quantity, unit price, subtotal, and total.
7. Format money values to exactly two decimal places.

**Accuracy consistency note:** In the required version, `total` must be present and must equal `subtotal`. If tax/discount is added, that is extension only, not baseline."

### Required output format (example)

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

"Both subtotal and total are required output lines. In the baseline, they match."

### Three checkpoints with timing

Use these milestones to monitor progress and offer guidance. Announce each checkpoint aloud.

#### **Checkpoint 1: Input collection and variable setup (~10 minutes into lab)**

"Checkpoint: everyone should have prompts and variable assignments complete."

At this point, students should have:
- Print title statement.
- Three `input()` calls with clear prompts.
- Variables assigned from input (with conversion for quantity and price).

**Example code to look for:**
```python
item_name = input("Enter item name: ").strip()
quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price per item: "))
```

**Quick check:** Ask a learner: "What type is `quantity` and why did you choose that?"

#### **Checkpoint 2: Type conversion and computation (~20 minutes into lab)**

"Checkpoint: make sure `quantity` and `price_per_item` are numeric types before multiplication. Compute subtotal and set total equal to subtotal."

At this point, students should have:
- Correct type conversions (quantity as `int`, price as `float`).
- Subtotal computed as `subtotal = quantity * price_per_item`.
- Total assigned as `total = subtotal`.

**Example code to look for:**
```python
subtotal = quantity * price_per_item
total = subtotal
```

**Quick check:** Have students print subtotal with a sample input and verify with a calculator. Example: quantity 3, price 9.99 → expected subtotal 29.97.

#### **Checkpoint 3: Output formatting and verification (~40 minutes into lab)**

"Checkpoint: add total line and confirm total equals subtotal in baseline version. Polish output formatting to two decimals and clear labels."

At this point, students should have:
- Receipt header and body text.
- All required output lines (item, quantity, price, subtotal, total).
- Money values formatted with `:.2f` inside f-strings.
- Readable layout with separators and alignment.

**Example code to look for:**
```python
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
```

**Quick check:** Print the receipt and visually inspect for clarity, alignment, and two-decimal money formatting.

---

## Assessment Rubric

### Rubric walkthrough (5–8 minutes at start of checkpoint)

"I will grade for correctness, readability, and basic code quality—not for advanced features. If your script is simple but correct, that is excellent for this stage."

### Rubric categories and scoring

| Category | Points | Criteria |
|----------|--------|----------|
| **Program runs end-to-end (35%)** | 35 | Starts and finishes without crash on valid input. Prompts and output appear in logical order. |
| **Correct math and types (35%)** | 35 | Quantity converted to integer. Price converted to float. Subtotal computed correctly as quantity × price. Total equals subtotal in baseline. |
| **Readable output formatting (20%)** | 20 | Money shown to exactly 2 decimals using `:.2f`. Labels are clear and helpful. Receipt structure is easy to read with proper separators. |
| **Code clarity (10%)** | 10 | Meaningful variable names (e.g., `subtotal`, not `c`). Logical flow with minimal, helpful comments. |
| **Total** | **100** | |

### Rubric script to read aloud

"I will grade for correctness, readability, and basic code quality—not for advanced features. If your script is simple but correct, that is excellent for this stage.

**Program runs end-to-end:** Does it start without error and produce output? 35 points.

**Correct math and types:** Are the type conversions right? Is subtotal computed correctly? Is total equal to subtotal in the baseline? 35 points.

**Readable output formatting:** Are all money values shown to 2 decimals? Are labels clear? Is the layout easy to read? 20 points.

**Code clarity:** Are your variable names meaningful? Is your logic easy to follow? 10 points.

If all four are solid, you have a full 100-point submission. If one area is weak, that reflects in that category's score. Make sure baseline correctness is your priority."

---

## Troubleshooting Pitfalls

### Pitfall 1: Forgetting numeric conversion

**Issue:** Student reads price as text and tries arithmetic, resulting in string repetition instead of math.

**Example bug:**
```python
price = input("Enter price: ")
subtotal = price * 3  # Results in "9.999.999.99" (string repetition)
```

**Root cause:** `input()` always returns a string. Arithmetic on strings repeats, not adds.

**Prevention:** Convert immediately: `price = float(input("Enter price: "))`.

**Instructor response script:** "Check your variable types with `print(type(variable))`. If you see `<class 'str'>`, convert it with `float()` or `int()` before multiplication."

### Pitfall 2: Quantity read as float unnecessarily

**Issue:** Not a fatal error, but using `float` for quantity (a count) obscures intent.

**Example:** `quantity = float(input("Enter quantity: "))` (results in 3.0 instead of 3).

**Prevention:** Use `int` for counts and whole numbers. `int` communicates that quantity is discrete, not continuous.

**Instructor response:** "For a quantity (a count), use `int`. It makes your code's intent clearer. Counts are whole numbers, and `int` says that."

### Pitfall 3: Subtotal and total inconsistency

**Issue:** Student adds unintended math to total, breaking the baseline requirement that total equals subtotal.

**Example bug:**
```python
subtotal = quantity * price
total = subtotal + price  # Unintended extra item added!
```

**Root cause:** Misunderstanding of the baseline requirement or copy-paste error.

**Prevention:** Re-read the requirement: "baseline has no tax/discount. Total should equal subtotal exactly."

**Instructor response script:** "Re-read the requirement: in this baseline, total should equal subtotal. No tax, no discount, no extra math. If you are adding tax or discount, save that as an optional extension after baseline works."

### Pitfall 4: Formatting omitted or incorrect

**Issue:** Student prints money values without the `:.2f` format specifier, resulting in inconsistent decimal places.

**Example bug:**
```python
print("Subtotal:", subtotal)  # Outputs "Subtotal: 29.97" or "Subtotal: 29.970000001"
```

**Prevention:** Use f-strings with `:.2f`: `print(f"Subtotal: ${subtotal:.2f}")`.

**Instructor response:** "Use f-strings with `:.2f` for all money. It improves clarity and ensures consistent formatting. Example: `f'${price:.2f}'`."

### Pitfall 5: Unhelpful variable names

**Issue:** Using single-letter or vague names like `a`, `b`, `c`, or `x`, `y`, `z` obscures code intent.

**Example bug:**
```python
a = int(input())
b = float(input())
c = a * b
print(c)
```

**Root cause:** Rush or lack of familiarity with naming conventions.

**Prevention:** Choose names that explain purpose: `quantity`, `price_per_item`, `subtotal`.

**Instructor response:** "Choose names that explain what each variable holds. Instead of `a`, `b`, `c`, use `quantity`, `price_per_item`, `subtotal`. Naming is not cosmetic; naming is thinking."

### Pitfall 6: Logic errors in multi-step calculations

**Issue:** Correct types but incorrect formula or wrong order of operations.

**Example bug:**
```python
subtotal = quantity + price_per_item  # Should be multiplication!
total = subtotal
```

**Prevention:** Manually verify the formula before coding. Example: "3 items at $9.99 each should be $29.97, not $12.99."

**Instructor response:** "Verify your math with a calculator for one sample. If input is quantity 3 and price 9.99, subtotal should be 29.97. If you get 12.99, you're adding instead of multiplying."

---

## Exit Ticket & Quick-Check Questions

### Immediate debrief (7 minutes after submissions close)

"Let's debrief quickly. This checkpoint tested real fundamentals: input, types, arithmetic, and output formatting.

Raise your hand if your first run worked end-to-end. Great. If it didn't, that is normal. Debugging is part of coding, not a sign of failure.

Now, pair-share for one minute: what error did you hit first, and how did you fix it?"

After pair-share, ask **2 learners**:
1. "What was the issue?"
2. "How did you diagnose it?"
3. "What exact code change fixed it?"

This reinforces debugging as a skill, not a failure.

### Quick-check questions (1–2 minutes each)

Ask these to verify understanding and guide reflection:

1. **"What is the type of `input()` return value?"**  
   **Expected answer:** `str` (string). All input is text until converted.

2. **"Why did you use `int` for quantity and `float` for price?"**  
   **Expected answer:** Quantity is a count (whole number), price includes decimals. Types clarify intent.

3. **"How did you format money to 2 decimals?"**  
   **Expected answer:** Used f-string with `:.2f`, e.g., `f"${subtotal:.2f}"`.

4. **"What happens if you multiply a string by a number?"**  
   **Expected answer:** String repetition, not arithmetic. Example: `"abc" * 3` gives `"abcabcabc"`, not 3 × abc.

5. **"Why is total equal to subtotal in this checkpoint?"**  
   **Expected answer:** No tax or discount in baseline version. Total and subtotal are the same by design.

---

## Wrap-Up & Recap

### Session 2 summary script (verbatim)

"In Session 2, we built a strong fundamentals stack:
- **Hour 5:** String indexing, slicing, and `len()`.
- **Hour 6:** Method-based text normalization and search.
- **Hour 7:** Interactive input and numeric conversion.
- **Hour 8:** A mini-assessment that combines all of the above.

If today felt challenging, that is expected. You are building real programming habits, not memorizing isolated commands. Every error you debugged today is an investment in your coding intuition."

### Key takeaways to reinforce

1. **Plan before you code:** Translate requirements into variable names and logic.
2. **Types matter:** Choose the right type to prevent bugs and clarify intent.
3. **Build incrementally:** Write 5 lines, run, test. Don't write 30 lines then debug.
4. **Output is communication:** Users read labels and formatted values, not raw variables.
5. **Debugging is learning:** Errors are information, not failure.

### Connection to Day 3

"Next session follows this exact sequence:
- **Hour 9:** Comparisons and boolean logic (decisions in code).
- **Hour 10:** String formatting with f-strings (you've seen this; we'll go deeper).
- **Hour 11:** Text operations with `split()` and `join()` (breaking text apart and rebuilding).
- **Hour 12:** Debugging habits at Basics level (systematic approaches to finding and fixing bugs).

That progression will help you write clearer decisions, cleaner output, and stronger troubleshooting workflows. Keep your receipt script—it is valuable material for practicing those upcoming concepts."

---

## Facilitation Notes & Pacing Checkpoints

### Minute-by-minute facilitation guide

#### **0:00–0:03 Settling and emotional framing**

"Take a breath. This is a checkpoint, not a trap. You are expected to think, test, and revise. Real programming looks like that.

Open a new script file named `checkpoint1_receipt.py` and keep your notes nearby."

#### **0:03–0:08 Rules and expectations**

"Welcome to Checkpoint 1. This is open-book and individual. You can use your notes, your previous scripts, and class materials. The purpose is not memorization; the purpose is demonstration of basic competence.

This checkpoint is timeboxed. Focus on correctness first, then formatting. If you get stuck, simplify your approach and make sure the core requirements are working before adding extras.

I can clarify requirements, but I will not provide direct solutions. Think of this as a low-pressure simulation of real coding work: read requirements, build incrementally, test, and submit."

#### **0:08–0:10 Rubric walkthrough**

"Here's how I'll grade:
- 35% for correctness (runs, no crashes, prompts in order).
- 35% for correct math and types (right conversions, right formula).
- 20% for readable output (2-decimal money, clear labels).
- 10% for code clarity (good variable names, logical flow).

If all four are solid, you have 100 points."

#### **0:10–0:50 Checkpoint lab (monitor milestones)**

Before starting: "Build in this order and run after each step. Frequent small runs prevent large debugging sessions."

**At 0:10 (minute 10):** "Checkpoint: everyone should have prompts and variable assignments complete."

**At 0:20 (minute 20):** "Checkpoint: make sure quantity and price_per_item are numeric types before multiplication."

**At 0:30 (minute 30):** "Checkpoint: verify your subtotal with a calculator for one sample input."

**At 0:38 (minute 38):** "Checkpoint: add total line and confirm total equals subtotal in baseline version."

**At 0:45 (minute 45):** "Checkpoint: polish output formatting to two decimals and clear labels. You're in the home stretch."

**At 0:50:** "Time is up. Wrap up and submit your script."

#### **0:50–0:57 Debrief**

"Let's debrief quickly. Raise your hand if your first run worked end-to-end. If it didn't, that is normal. Debugging is part of coding.

Pair-share for one minute: what error did you hit first, and how did you fix it?"

Ask 2–3 learners their debugging stories.

#### **0:57–1:00 Final wrap and Day 3 preview**

"Checkpoint complete. Whether your first attempt was smooth or messy, you did real programming work: read requirements, implemented logic, tested output, and debugged under time constraints. That is exactly how competence grows.

Next session we continue with comparisons and booleans, then f-strings, then split/join, and then dedicated debugging habits.

Keep your checkpoint script—it is a reference artifact for Day 3."

### Pacing checkpoints for instructor awareness

| Time | Milestone | Action |
|------|-----------|--------|
| 0:00–0:03 | Settling | Emotional framing, students open editor |
| 0:03–0:08 | Rules | Explain checkpoint mode and expectations |
| 0:08–0:10 | Rubric | Walk through 4 categories and scoring |
| 0:10–0:50 | Lab | Monitor 5 milestones (10, 20, 30, 38, 45 min) |
| 0:50–0:57 | Debrief | Pair-share, ask 2–3 debugging stories |
| 0:57–1:00 | Wrap | Recap and Day 3 preview |

### Guided recovery path (if class is struggling)

If many learners stall, use this scaffold publicly without giving complete final solution immediately.

**Step 1: Just prompt and print**
```python
item_name = input("Enter item name: ")
quantity_text = input("Enter quantity: ")
price_text = input("Enter price per item: ")

print(item_name, quantity_text, price_text)
```

**Step 2: Convert types and print types**
```python
quantity = int(quantity_text)
price_per_item = float(price_text)

print(type(quantity), type(price_per_item))
```

**Step 3: Compute and print raw numbers**
```python
subtotal = quantity * price_per_item
total = subtotal

print(subtotal, total)
```

**Step 4: Format final receipt**
```python
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
```

This keeps rigor while helping learners recover.

---

## Real-World Context & Applications

### Industry relevance

Receipt generation is one of the most common beginner tasks in retail, POS (Point of Sale) systems, e-commerce, and financial software:

- **Retail:** Every cash register generates receipts. This checkpoint mirrors that logic.
- **E-commerce:** Online stores print order summaries with item totals.
- **Invoicing:** Business software calculates line items, subtotals, and totals.
- **Financial apps:** Banking and budgeting apps track purchases and balances.

The skills you practiced today—input, types, arithmetic, formatting—are foundational to all of these domains.

### Career connection

Competence with this checkpoint demonstrates:
1. **Requirement translation:** Reading specs and breaking them into code.
2. **Type discipline:** Choosing appropriate data types to prevent bugs.
3. **Output design:** Making output readable for end users, not just developers.
4. **Testing mindset:** Validating output and debugging incrementally.

These are skills valued across software roles: QA, development, data engineering, and system administration.

### Problem-solving applications

This checkpoint pattern appears in many real scenarios:

1. **Discount calculator:** Add a discount percent and recalculate total.
2. **Multi-item order:** Support two or three items (no loops yet).
3. **Tax calculator:** Add tax rate and compute total = subtotal + tax.
4. **Currency conversion:** Input USD amount, convert to EUR, GBP, etc.
5. **Inventory tracker:** Track quantity on hand, quantity sold, and remaining.

All of these follow the same pattern: **input → type conversion → computation → formatted output**.

---

## Advanced Topics & Summary

### Optional extensions (post-baseline only)

After your baseline solution is correct and tested, you may explore these extensions:

#### Tax extension example

```python
tax_rate = 0.08
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Total:    ${total:.2f}")
```

**Instructor reminder:** If extension is used, clearly label it as beyond baseline and not required for checkpoint grading.

#### Discount extension example

```python
discount_percent = 10  # 10% discount
discount_amount = subtotal * (discount_percent / 100)
total = subtotal - discount_amount

print(f"Subtotal:  ${subtotal:.2f}")
print(f"Discount:  ${discount_amount:.2f}")
print(f"Total:     ${total:.2f}")
```

#### Multi-item extension (advanced, requires thinking about structure)

```python
# Collect two items
item1_name = input("Item 1 name: ")
item1_qty = int(input("Item 1 quantity: "))
item1_price = float(input("Item 1 price: "))

item2_name = input("Item 2 name: ")
item2_qty = int(input("Item 2 quantity: "))
item2_price = float(input("Item 2 price: "))

# Compute
subtotal1 = item1_qty * item1_price
subtotal2 = item2_qty * item2_price
total = subtotal1 + subtotal2

# Print
print(f"{item1_name}: ${subtotal1:.2f}")
print(f"{item2_name}: ${subtotal2:.2f}")
print(f"Total:        ${total:.2f}")
```

**Note:** This works but is repetitive. In Session 3+ (with loops and lists), you'll learn a cleaner approach.

### Connection to Day 3 and beyond

The skills you practiced today are **prerequisites** for everything ahead:

- **Hour 9 (Comparisons and booleans):** "If subtotal exceeds $100, apply discount." Requires comparing numbers.
- **Hour 10 (String formatting):** Deeper f-string skills; you used `:.2f` today, and you'll use more format codes.
- **Hour 11 (split/join):** Parsing CSV data (comma-separated values) like "Item, Quantity, Price" and reconstructing output.
- **Hour 12 (Debugging habits):** Systematic approaches to finding and fixing bugs learned through exercises like this one.

### Final grading notes for instructor

**Fast-check list:**
- [ ] Prompts are present and understandable.
- [ ] Quantity uses integer conversion.
- [ ] Price uses float conversion.
- [ ] Subtotal computed correctly (quantity × price).
- [ ] Total line present and baseline-consistent (equals subtotal).
- [ ] Money formatting uses exactly 2 decimals (`:.2f`).
- [ ] Output is readable with clear labels and separators.
- [ ] Variable names are meaningful (not `a`, `b`, `c`).

**Consistency reminder:**
Grade the baseline solution against baseline requirements. Confirm both subtotal and total lines are present. Confirm baseline total equals subtotal unless the student clearly labels an optional extension (tax/discount). Do not penalize minor spacing preferences if values and labels are clear and money formatting is correct.

**Closing reinforcement for learners:**
"Checkpoint complete. Whether your first attempt was smooth or messy, you did real programming work: read requirements, implemented logic, tested output, and debugged under time constraints. That is exactly how competence grows. Session 3 extends this foundation: comparisons, deeper formatting, text operations, and debugging habits. Keep your scripts from today—they are valuable material for those upcoming concepts."

---

**End of Day 2, Hour 4 Instructor Script**

*Word count: 3,847 | Structure: 13 H2 sections | Learning outcomes: 5 explicit | Lab checkpoints: 3 with timing | Pitfalls: 6 H3 subsections | Runbook alignment: Hour 8 / Session 2 / Course Hour 8*
