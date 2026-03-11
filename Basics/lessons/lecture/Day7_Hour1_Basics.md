# Day 7, Hour 1: Conditionals: if/elif/else and Boundaries (Course Hour 25)
**Python Programming Basics – Session 7**

**Course:** Python Programming (Basics)
**Runbook alignment:** Session 7, Course Hour 25 – Conditionals: if/elif/else and boundaries
**Duration:** 60 minutes
**Mode:** Instructor-led + live coding + guided lab
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on conditional logic: writing clear if/elif/else statements, handling boundary values correctly, ordering conditions properly, and choosing between nested and flat branching. Stay within Basics scope — do not introduce match/case statements (Python 3.10+), ternary operators, or advanced pattern matching. The key outcomes are writing readable boolean expressions, handling edge cases at boundaries, and debugging common condition-ordering mistakes. The lab reinforces all of this in a shipping calculator with tiered pricing rules.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Write clear if/elif/else statements that handle multiple distinct cases.
2. Explain why the order of elif branches matters and demonstrate what happens when conditions overlap.
3. Handle boundary values correctly using appropriate comparison operators (>=, >, <=, <).
4. Choose between nested conditionals and flat if/elif chains based on readability.
5. Build a shipping calculator that computes cost using tiered weight rules and correctly handles all boundary weights."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to boolean logic from Day 3; introduce branching decision flow
- **0:05–0:18** Core concept: if/elif/else structure, execution order, the "first match wins" rule
- **0:18–0:28** Boundary handling: inclusive vs exclusive, off-by-one errors, testing edge cases
- **0:28–0:35** Nested vs flat conditionals: readability tradeoffs
- **0:35–0:45** Live demo: shipping tiers with correct boundary handling
- **0:45–0:57** Guided lab: Shipping Calculator
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour25_conditionals_demo.py` before class begins.
- Have a second file called `hour25_lab_shipping.py` ready with empty comments as a starter for learners who fall behind.
- Have the Python REPL ready in a terminal (type `python` or `python3`) for quick interactive experiments.
- Plan to show at least one example where incorrect condition ordering causes a bug.
- Plan to demonstrate testing boundary values: if tiers are 0–5, 5–10, 10+, test with weights 5, 5.01, 10, 10.01.
- Review Day 3, Hour 1 (Course Hour 9) material on boolean comparisons (==, !=, <, >, <=, >=, and, or, not) — learners should already know these operators but may need a quick refresher.

**Say:** "Please have your editor open and an empty file ready. Today we are building decision trees in code. You will type alongside me, then build your own shipping calculator in the lab."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Day 3

**Say:**
"Welcome to Session 7. Today we start a two-day deep dive into control flow: the mechanisms that let your program make decisions and repeat actions.

Back in Day 3, Hour 1, we introduced boolean comparisons and logical operators: `==`, `!=`, `<`, `>`, `<=`, `>=`, and the keywords `and`, `or`, `not`. We used them to write simple eligibility checks and guards.

But we did not yet build full branching logic where your program chooses between multiple possible paths. That is what we do today.

The tool we use for branching is the if statement, and its extensions elif and else. If you have written any code before, you have probably seen these. But even experienced programmers make subtle mistakes with conditionals, especially around boundary values and condition ordering.

Today we will learn how to write conditionals that are correct, readable, and maintainable."

### 3.2 Motivating the need

**Say:**
"Let me give you a few real-world situations where you need branching logic:

- A shipping company charges different rates based on package weight: under 5 pounds, 5 to 10 pounds, over 10 pounds. Your program must decide which rate applies.
- A grading system assigns letter grades based on numeric scores: A for 90–100, B for 80–89, C for 70–79, and so on.
- An authentication system allows access only if the user is logged in AND has the required permission level.
- A form validator checks that an email contains an `@` symbol AND that the password is at least 8 characters long.

In each case, the program must evaluate conditions and choose which block of code to execute. That is the job of if/elif/else statements."

### 3.3 Set expectations for the hour

**Say:**
"In this hour, we will learn:
- how to structure if/elif/else statements clearly
- why the order of conditions matters and what happens when they overlap
- how to handle boundary values without off-by-one errors
- when to use nested conditionals versus flat if/elif chains
- and how to build a tiered shipping calculator that handles all edge cases correctly

The concepts are straightforward. The challenge is in the details: getting boundaries right, ordering conditions logically, and testing thoroughly."

---

## 4) Concept: if/elif/else Structure

### 4.1 Beginner-friendly definition

**Say:**
"A conditional statement lets your program choose between different blocks of code based on whether conditions are true or false.

The simplest form is the if statement:

```python
if condition:
    # code that runs only if condition is True
```

Python evaluates the condition. If it is `True`, the indented block runs. If it is `False`, Python skips that block entirely.

You can add an else clause to handle the False case:

```python
if condition:
    # runs if True
else:
    # runs if False
```

And you can add elif clauses to check multiple conditions in sequence:

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False and condition_2 is True
elif condition_3:
    # runs if condition_1 and condition_2 are False, and condition_3 is True
else:
    # runs if all conditions are False
```

The key rule: Python evaluates conditions from top to bottom and executes the first block whose condition is True. Once it finds a match, it skips all remaining elif and else blocks. This is called 'first match wins' behavior."

### 4.2 Why this matters

**Say:**
"The 'first match wins' rule has a critical consequence: the order of your conditions matters.

If you write:

```python
if weight > 0:
    print('Standard rate')
elif weight > 10:
    print('Heavy rate')
```

The second condition will never execute, because every weight greater than 10 is also greater than 0, so the first block always matches first.

You must order conditions from most specific to most general, or use non-overlapping ranges."

---

## 5) Concept: Boundary Handling

### 5.1 The boundary problem

**Say:**
"Consider a shipping company with these rules:

- 0 to 5 pounds: $5 flat rate
- 5 to 10 pounds: $10 flat rate
- Over 10 pounds: $15 flat rate

Question: if a package weighs exactly 5 pounds, which rate applies? What about exactly 10 pounds?

The business rule might say 'up to and including 5 pounds' or 'more than 5 pounds.' The difference is one pound, but it changes which code block executes.

In code, you express this using comparison operators:

- `weight <= 5` means 'up to and including 5'
- `weight < 5` means 'less than 5, so 4.99 and below'
- `weight > 5` means 'more than 5, so 5.01 and above'
- `weight >= 5` means '5 and above'

Getting this wrong is called an off-by-one error. It is one of the most common bugs in programming."

### 5.2 How to handle boundaries correctly

**Say:**
"Here is a safe pattern for handling ranges with clear boundaries. Let's say the tiers are:

- 0 up to 5 (inclusive): tier 1
- more than 5 up to 10 (inclusive): tier 2
- more than 10: tier 3

You write:

```python
if weight <= 5:
    rate = 5
elif weight <= 10:
    rate = 10
else:
    rate = 15
```

Notice that I do not need to write `elif weight > 5 and weight <= 10`. Why? Because if we reach the elif, we already know weight is greater than 5 — the first condition failed. The elif inherits that knowledge.

This is called an implicit range check. It makes the code simpler and easier to read."

### 5.3 Testing boundary values

**Say:**
"Once you write a conditional with ranges, you must test it at the boundaries. For the tiers above, test with these weights:

- 0 (minimum)
- 5 (boundary)
- 5.01 (just over boundary)
- 10 (boundary)
- 10.01 (just over boundary)
- 100 (well over)

If your code gives the correct rate for all six values, your boundaries are correct. If any fails, you have an off-by-one error."

---

## 6) Concept: Nested vs Flat Conditionals

### 6.1 Nested conditionals

**Say:**
"Sometimes you need to check a second condition only if the first condition is true. You can nest if statements:

```python
if is_member:
    if purchase_amount > 100:
        discount = 0.20
    else:
        discount = 0.10
else:
    discount = 0
```

This works, but notice how the indentation grows. If you nest three or four levels, the code becomes hard to read."

### 6.2 Flat conditionals with combined conditions

**Say:**
"You can often flatten nested conditionals by combining conditions with `and`:

```python
if is_member and purchase_amount > 100:
    discount = 0.20
elif is_member:
    discount = 0.10
else:
    discount = 0
```

This is easier to scan because all branches are at the same indentation level.

General guideline: prefer flat if/elif chains when possible. Use nesting only when the second condition truly depends on the first being true."

---

## 7) Live Coding Demo: Shipping Calculator (~10 minutes)

### 7.1 Announce the demo

**Say:**
"Now I am going to build a shipping calculator. The rules are:

- 0 to 5 pounds: $5
- more than 5, up to 10 pounds: $10
- more than 10 pounds: $15

I will write the code, test it at the boundaries, deliberately introduce a bug by ordering conditions incorrectly, and then fix it. Watch how I test and think aloud."

### 7.2 Code the correct version

**Type aloud:**

```python
# Shipping calculator - correct version

weight = float(input("Enter package weight in pounds: "))

if weight <= 0:
    print("Error: weight must be positive.")
elif weight <= 5:
    cost = 5
    category = "Light"
elif weight <= 10:
    cost = 10
    category = "Medium"
else:
    cost = 15
    category = "Heavy"

if weight > 0:
    print(f"Category: {category}")
    print(f"Shipping cost: ${cost}")
```

**Say:**
"Notice a few things:

1. I check for invalid input first: weight must be positive. This is called a guard clause.
2. I use `<=` for the boundaries because the problem says 'up to and including.'
3. I do not repeat the lower bound in each elif. If we reach `elif weight <= 10`, we already know weight is greater than 5.
4. I use an else for the final tier, because if weight is greater than 10, there are no more conditions to check."

### 7.3 Test at boundaries

**Say:**
"Let me test this. I will run it five times with different weights."

**Run the program and test:**
- Input: 5 → Output: "Category: Light, Shipping cost: $5" ✓
- Input: 5.01 → Output: "Category: Medium, Shipping cost: $10" ✓
- Input: 10 → Output: "Category: Medium, Shipping cost: $10" ✓
- Input: 10.01 → Output: "Category: Heavy, Shipping cost: $15" ✓
- Input: 0 → Output: "Error: weight must be positive." ✓

**Say:**
"All boundaries work correctly. Now let me show you what happens if I order conditions incorrectly."

### 7.4 Demonstrate incorrect ordering

**Type aloud:**

```python
# Shipping calculator - WRONG: overlapping conditions

weight = float(input("Enter package weight in pounds: "))

if weight > 0:
    cost = 5
    category = "Light"
elif weight > 5:
    cost = 10
    category = "Medium"
elif weight > 10:
    cost = 15
    category = "Heavy"
```

**Say:**
"What is wrong here? The first condition is `weight > 0`. That matches almost every valid weight. So the first block always runs, and the other two never execute.

Let me test with weight 12. It should be Heavy and $15."

**Run and show:**
- Input: 12 → Output: "Category: Light, Shipping cost: $5" ✗

**Say:**
"The program says Light, which is wrong. This is a condition-ordering bug. The fix is to reorder from most specific to most general, or use non-overlapping ranges."

### 7.5 Fix and retest

**Say:**
"The correct approach is to either check most restrictive first, or use non-overlapping boundaries. We already saw the non-overlapping version. Let me show the restrictive-first version:

```python
if weight <= 0:
    print("Error: weight must be positive.")
elif weight > 10:
    cost = 15
    category = "Heavy"
elif weight > 5:
    cost = 10
    category = "Medium"
else:
    cost = 5
    category = "Light"
```

Now the heaviest tier is checked first. If it does not match, we check the medium tier. If that does not match, we know it must be light.

Both approaches work. Choose the one that matches how you think about the problem."

---

## 8) Guided Lab: Shipping Calculator (~25 minutes)

### 8.1 Announce the lab

**Say:**
"Now it is your turn. You will build a shipping calculator with slightly more complex rules. Here is the specification:

**Lab: Shipping Calculator**

**Goal:** Create a program that asks for package weight and computes the shipping cost using tiered rules.

**Rules:**

- Weight must be positive (validate and show error if not)
- 0 to 5 pounds: $5 base rate
- More than 5, up to 10 pounds: $10 base rate
- More than 10 pounds: $15 base rate

**Optional extensions (if you finish early):**

1. Add a free shipping threshold: if weight is greater than 0 and cost would be $15, but the user has a membership flag, make shipping free.
2. Add a fragile surcharge: ask if the package is fragile (yes/no). If yes, add $3 to the cost.

**Completion criteria:**

- Program runs without errors for all test weights
- Correct cost for boundary values: 5, 5.01, 10, 10.01
- Readable branching logic
- Clear output showing weight, category, and cost

You have 25 minutes. I will circulate and help. Start with the basic version first."

### 8.2 Circulate and provide feedback

Walk around the room. Look for:

- **Off-by-one errors:** Students using `<` when they should use `<=`, or vice versa.
- **Condition ordering bugs:** First condition too broad, later conditions never reached.
- **No validation:** Not checking for negative or zero weight.
- **Printing without checking validity:** Printing cost even when weight is invalid.

**Common mistake to watch for:**

```python
if weight < 5:
    cost = 5
elif weight < 10:
    cost = 10
else:
    cost = 15
```

This treats exactly 5 pounds as medium, and exactly 10 as heavy. Is that what the problem asked for? Check the spec.

**Coaching language:**

- "Walk me through what happens when weight is exactly 5. Which block runs?"
- "If the first condition is True, do the other conditions get checked?"
- "How could you test whether your boundaries are correct?"

### 8.3 Debugging support

If a student is stuck:

1. Ask them to add `print(weight)` right after input to confirm the value.
2. Ask them to test with one specific weight that fails, and trace through each condition by hand.
3. If their conditions overlap, draw a number line on paper showing the ranges and where they overlap.

---

## 9) Debrief and Knowledge Check (~12 minutes)

### 9.1 Share-out

**Say:**
"Let us hear from a few people. Who wants to show their solution and explain how they handled the boundaries?"

**Call on 2–3 learners. Ask:**

- "What comparison operator did you use for each boundary?"
- "How did you test your solution?"
- "Did you try any of the optional extensions?"

### 9.2 Common mistakes review

**Say:**
"Here are the most common mistakes I saw today:

1. **Overlapping conditions:** Checking `weight > 0` before checking `weight > 10` means the first condition always wins.

2. **Wrong comparison operator:** Using `<` when you mean `<=`. One is exclusive, the other is inclusive. Read the problem carefully.

3. **Not validating input:** Forgetting to check that weight is positive. Always validate user input.

4. **Inconsistent boundaries:** Saying '5 to 10 pounds' without specifying whether 5 and 10 are included. Be precise.

The fix for all of these: write the conditions carefully, test at boundaries, and trace through your logic by hand before running the code."

### 9.3 Conceptual recap

**Say:**
"Let me summarize today's key ideas:

1. **if/elif/else structure:** Python checks conditions from top to bottom and executes the first block whose condition is True. Once a block runs, the rest are skipped.

2. **Condition ordering:** Put the most specific or restrictive conditions first, or use non-overlapping ranges. If conditions overlap, only the first match will execute.

3. **Boundary handling:** Use `<=` and `>=` for inclusive boundaries, `<` and `>` for exclusive. Test at boundary values to catch off-by-one errors.

4. **Nested vs flat:** Prefer flat if/elif chains for readability. Use nesting only when the second condition truly depends on the first.

These are not advanced concepts, but they require precision. The difference between `<` and `<=` is one character in your code, but it can mean a 10% price difference for your customer."

---

## 10) Exit Ticket (~3 minutes)

**Say:**
"Before we finish, write down your answer to this question. You do not need to submit it, but think it through:

**Question:** Suppose you have three conditions:

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

What grade does a score of 85 receive? Why?

What would happen if you reversed the order of the conditions?"

**Pause for 1 minute, then reveal the answer:**

**Say:**
"A score of 85 receives a 'B'. Here is why:

- The first condition, `score >= 90`, is False, so we skip that block.
- The second condition, `score >= 80`, is True, so we execute that block and assign `grade = 'B'`.
- We skip the remaining conditions because we already found a match.

If you reversed the order:

```python
if score >= 70:
    grade = 'C'
elif score >= 80:
    grade = 'B'
elif score >= 90:
    grade = 'A'
```

A score of 85 would receive a 'C', because `score >= 70` is True, so that block runs first. The later conditions never get checked. This is a bug.

Lesson: condition order matters. Always write conditions from most restrictive to least restrictive, or use non-overlapping ranges."

---

## 11) Transition to Next Hour

**Say:**
"Excellent work today. You now know how to write clear branching logic and handle boundaries correctly.

In Hour 2, we will learn about while loops and sentinel patterns: how to repeat an action until the user tells you to stop. We will use conditionals inside loops to control when the loop should exit.

Take a 5-minute break. When you return, have your editor ready."

---

## 12) Appendix: Quick Reference for Instructors

### Condition ordering rules

- **Most restrictive first:** Check narrow ranges before broad ranges.
- **Non-overlapping ranges:** Use boundaries that do not overlap, and document which end is inclusive.
- **Guard clauses first:** Validate inputs before processing them.

### Testing checklist

- Minimum value (often 0)
- Each boundary value (e.g., 5, 10)
- Just above each boundary (e.g., 5.01, 10.01)
- Maximum or very large value (e.g., 1000)
- Invalid values (negative, zero if not allowed, non-numeric if applicable)

### Troubleshooting common student issues

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "My cost is always $5 even for heavy packages" | First condition too broad | Check condition order; most restrictive first |
| "Weight 5 gives $10 but it should give $5" | Wrong comparison operator | Change `<` to `<=` or vice versa based on spec |
| "My code crashes with ValueError" | Input is not numeric | Add try/except around `float(input(...))` (optional; covered in Hour 44) |
| "I don't know what inclusive means" | Boundary ambiguity | Explain: inclusive means the boundary value is included in that range |

---

## 13) Optional Extensions for Advanced Learners

If a student finishes early and wants a challenge:

1. **Add a second dimension:** Create a calculator that considers both weight and distance, with a base rate plus per-mile charge.

2. **Volume-based pricing:** Ask for package dimensions (length, width, height) and compute volumetric weight. Use the greater of actual weight and volumetric weight for pricing.

3. **Multi-tier discounts:** Add a loyalty tier (bronze, silver, gold) and apply different discount percentages to the base rate.

All extensions should stay within Basics scope: use only if/elif/else, basic arithmetic, and clear variable names. Do not introduce functions or classes yet (those are covered in Session 9).

---

## 14) Deep Dive: Common Pitfalls in Detail

### 14.1 The "always true" trap

**Teaching point:**
"One of the most frustrating bugs for beginners is writing a condition that is always true or always false. Here are examples:

**Always true:**
```python
if age or age >= 18:
    print("Access granted")
```

Why is this wrong? The expression `age or age >= 18` uses the `or` operator. If age is any non-zero value, it is truthy, so the condition is True regardless of whether age is 18 or not. A 5-year-old would get access.

The correct code is:
```python
if age >= 18:
    print("Access granted")
```

**Always false:**
```python
if weight > 10 and weight < 5:
    print("Invalid range")
```

This checks whether weight is both greater than 10 AND less than 5 at the same time. That is impossible, so this condition can never be True. If you meant 'outside the range 5 to 10', you need `or`:
```python
if weight < 5 or weight > 10:
    print("Outside normal range")
```

When debugging conditionals, trace through the logic step by step and ask: is there any input that makes this True? Is there any input that makes this False? If the answer to either question is no, you have a logic error."

### 14.2 Comparing strings and numbers

**Teaching point:**
"Python will let you write `if '5' < 10`, but it raises a `TypeError` at runtime because you cannot compare a string to an integer.

This happens when you forget to convert user input:

```python
age = input("Enter your age: ")  # age is a string
if age >= 18:  # TypeError: '>=' not supported between str and int
    print("Adult")
```

The fix:
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
```

Always convert user input to the appropriate type before using it in comparisons."

### 14.3 Empty elif blocks

**Teaching point:**
"Sometimes students write:

```python
if weight <= 5:
    cost = 5
elif weight <= 10:
    # TODO: calculate cost
else:
    cost = 15
```

If you leave an elif or else block empty, Python raises an `IndentationError` because it expects at least one statement. If you genuinely need a placeholder, use `pass`:

```python
if weight <= 5:
    cost = 5
elif weight <= 10:
    pass  # temporary placeholder
else:
    cost = 15
```

But in real code, do not ship placeholders. Either complete the logic or remove the branch."

### 14.4 Accidental assignment in conditions

**Teaching point:**
"In some languages, you can accidentally write `if x = 5` when you mean `if x == 5`. Python protects you from this: assignment in a condition causes a `SyntaxError`.

But you can still make a related mistake with the walrus operator `:=` (Python 3.8+):

```python
if (score := 85) > 80:
    print("Pass")
```

This assigns 85 to score and then checks if 85 > 80. Unless you specifically intend to assign and test in one expression, avoid `:=` in conditionals. It is an advanced feature not covered in Basics."

---

## 15) Conceptual Check: When NOT to Use if/elif/else

**Teaching point:**
"Not every decision requires a conditional. Sometimes a calculation or a data structure is clearer.

**Example: Tier-based pricing**

Instead of:
```python
if tier == 'bronze':
    discount = 0.05
elif tier == 'silver':
    discount = 0.10
elif tier == 'gold':
    discount = 0.15
else:
    discount = 0
```

You could use a dictionary:
```python
discount_rates = {
    'bronze': 0.05,
    'silver': 0.10,
    'gold': 0.15
}
discount = discount_rates.get(tier, 0)
```

This is not always better, but when you have many tiers and the logic is a simple lookup, a dictionary is more maintainable. You will learn more about this pattern in Session 6.

For now, use if/elif/else when you need it. Just be aware that as your code grows, you will learn alternative patterns that reduce repetition."

---

## 16) Accessibility Note: Writing Error Messages

**Teaching point:**
"When your conditionals detect invalid input, write clear, actionable error messages.

**Bad:**
```python
if weight <= 0:
    print("Error")
```

What error? What should the user do?

**Better:**
```python
if weight <= 0:
    print("Error: Weight must be a positive number.")
```

**Even better:**
```python
if weight <= 0:
    print("Error: Weight must be a positive number. Please enter a value greater than 0.")
```

Good error messages explain:
1. What went wrong
2. What is expected
3. How to fix it

This is especially important in CLI programs where the user cannot see visual cues like red text boxes."

---

## 17) Real-World Context: Why Boundaries Matter

**Teaching point:**
"In professional software, boundary errors cost money. Here are real examples:

1. **Banking:** A bank's overdraft fee logic had a boundary error. If your balance was exactly $0.00, the system treated it as overdrawn and charged a fee. Customers noticed and complained. The fix cost the bank millions in refunds.

2. **Shipping:** An e-commerce company's shipping calculator used `<` instead of `<=` for a weight tier. Packages weighing exactly 10 pounds were charged the next tier up. Thousands of customers were overcharged by $5 each before the bug was caught.

3. **Gaming:** A game's level-up system had a condition that checked `if xp > 1000`. But the designer meant `if xp >= 1000`. Players who earned exactly 1000 XP did not level up, causing confusion.

These are not theoretical problems. Boundary errors are common, expensive, and completely preventable if you test carefully."

---

## 18) Summary: Key Takeaways

**Say:**
"Before we move to Hour 2, let me emphasize the four most important points:

1. **Condition order matters.** Python evaluates from top to bottom and stops at the first True condition. If your conditions overlap, only the first one that matches will execute.

2. **Test at boundaries.** If your tiers are 0–5, 5–10, 10+, test with weights 5, 5.01, 10, 10.01. If any fails, you have a boundary bug.

3. **Use the right operator.** `<=` means 'up to and including.' `<` means 'up to but not including.' Read the problem carefully and choose correctly.

4. **Validate input first.** Check that data is valid before processing it. Use guard clauses at the top of your logic.

These principles apply to every program you will ever write, not just this shipping calculator."

---

**End of Hour 1 Script**
