# Day 4, Hour 3: If-Elif-Else Flow and Nested Conditions

**Course Hour**: 15  
**Session**: Day 4 (Session 4), Hour 3  
**Duration**: 60 minutes  

---

## 1. Learning Outcomes

After this instructional hour, learners will be able to:

- **Write if/elif/else statements** to create branching logic where different code blocks execute based on different conditions.
- **Understand execution flow** in conditionals: recognize that only ONE block executes, and that order matters when using `elif`.
- **Design clear decision trees** with proper boundary conditions to avoid overlapping or unreachable code branches.
- **Handle nested conditions** (conditionals within conditionals) and understand when nesting is appropriate vs. when `and`/`or` is clearer.
- **Debug conditional logic** by tracing through execution paths and testing boundary values systematically.

---

## 2. Instructor Prep Section

### Pre-Class Checklist
- [ ] Have Python 3 IDE ready with a clean script file
- [ ] Test all demo code before class; confirm output matches expectations
- [ ] Prepare the shipping calculator (or similar tiered pricing) demo to use live
- [ ] Draw a flowchart or decision tree on paper/whiteboard to visualize conditional branches
- [ ] Prepare 3–4 "mystery conditionals" for prediction exercises
- [ ] Have the shipping calculator lab rubric visible
- [ ] Prepare a "common mistakes" reference: overlapping conditions, unreachable branches, indentation errors

### Timing Breakdown
- **Opening Script** (4 min)
- **Conceptual Briefing: If/Elif/Else Structure** (8 min)
- **Conceptual Briefing: Order Matters & Nested Conditions** (7 min)
- **Live Demo: Shipping Tiers with If/Elif/Else** (11 min)
- **Guided Practice Walkthrough** (8 min)
- **Lab Checkpoint 1: Shipping Calculator** (18 min)
- **Wrap-Up + Quick-Check Questions** (4 min)

### Materials & Resources
- IDE or Python REPL
- Flowchart or Venn diagram (for visualizing branches)
- Sample code: tiered discount, shipping cost, grade letter grade examples
- Shipping calculator lab prompt (provided below)
- Whiteboard or shared doc for live code

---

## 3. Opening Script

**[Read or paraphrase to set context, ~4 minutes]**

"Welcome back! Yesterday, we learned how to *ask* questions with comparisons and boolean logic. Today, we're learning how Python *answers* those questions and *does something different* based on the answer.

Think of it like a flowchart:
- 'Is the package under 10 lbs?' → YES → Free shipping
- 'Is it between 10 and 50 lbs?' → YES → Charge $5
- 'Is it over 50 lbs?' → YES → Charge $15

Or think of a video game:
- 'Did the player press up?' → YES → Move up
- 'Did the player press down?' → YES → Move down
- If neither → Do nothing

This is called **conditional execution** or **branching**. And we use `if`, `elif`, and `else` to do it.

By the end of this hour, you'll be able to write programs that make smart decisions based on different scenarios. Let's go!"

---

## 4. Conceptual Briefing Part A: The If-Elif-Else Structure (8 minutes)

### The Basic Pattern

An `if` statement lets your code make a decision:

```python
if condition:
    # This code runs ONLY if condition is True
    # do something
```

**Key points**:
- The colon (`:`) ends the `if` line
- The block is **indented** (4 spaces in Python)
- Only runs if the condition is `True`

### Example: Simple If

```python
age = 18
if age >= 18:
    print("You can vote!")
```

Output: `You can vote!`

If `age` were 17, nothing would print.

### Adding Else: The Alternative

`else` handles the case when the condition is `False`:

```python
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("You must wait for your 18th birthday.")
```

Output: `You must wait for your 18th birthday.`

**The Rule**: Exactly ONE block runs—either `if` or `else`, never both.

### Multiple Branches: Elif

When you have more than two options, use `elif` (short for "else if"):

```python
age = 16
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

Output: `You are a teenager.`

**The Structure**:
```
if [first condition]:
    [block A]
elif [second condition]:
    [block B]
elif [third condition]:
    [block C]
else:
    [block D]
```

**Critical Rule**: Python checks conditions in order from top to bottom. As soon as ONE condition is `True`, that block runs, and the rest are skipped.

### Example: Shipping Cost (Three Tiers)

```python
weight = 25
if weight <= 10:
    cost = 0      # Free
elif weight <= 50:
    cost = 5      # Standard
else:
    cost = 15     # Heavy

print(f"Shipping cost: ${cost}")
```

Output: `Shipping cost: $5`

**Trace through the logic**:
1. Is weight <= 10? No (25 is not <= 10)
2. Is weight <= 50? Yes (25 is <= 50) → Run this block, set cost = 5
3. Skip the else

---

## 5. Conceptual Briefing Part B: Order Matters & Nested Conditions (7 minutes)

### Why Order Matters: A Critical Lesson

**The Wrong Way (Overlapping Conditions)**:

```python
age = 16
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen or Adult")
else:
    print("Child")
```

Output: `Child`  (Correct by accident!)

**The Problem**: The second `elif` (age >= 13) could match, but we never reach it because the first condition fails and we skip to else. This logic is unclear and fragile.

**The Right Way (Non-Overlapping, Clear Boundaries)**:

```python
age = 16
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

Output: `Teen`

**Why this is better**:
- Each range is distinct and clear.
- No overlaps (age can't be both < 13 and < 18).
- Easy to test boundaries: 0, 12, 13, 17, 18, 99.

### Common Mistake: Unreachable Code

```python
# BAD: The second branch can never run!
if x > 0:
    print("x is positive")
elif x > 10:
    print("x is greater than 10")
else:
    print("x is not positive")
```

**Why**: If `x > 10` is true, then `x > 0` is also true, so we've already entered the first block. The second branch is unreachable.

**Fix**:
```python
if x > 10:
    print("x is greater than 10")
elif x > 0:
    print("x is positive (but <= 10)")
else:
    print("x is not positive")
```

**Lesson**: Order your conditions from most specific to most general.

### Nested Conditionals: When and Why

A **nested conditional** is an `if` inside another `if`:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You're an adult but can't drive yet.")
else:
    print("You must be an adult to drive.")
```

Output: `You can drive.`

**When to nest**:
- When you need to check a second condition *only if* the first is true.
- Example: "Is the user an adult?" (first check) → "Does the adult have a license?" (second check, nested).

**When to use `and` instead**:
- If both conditions apply equally, use `and` to keep it flat and readable.

```python
# Nested (OK but harder to read):
if age >= 18:
    if has_license:
        print("Can drive")

# Flat with `and` (clearer):
if age >= 18 and has_license:
    print("Can drive")
```

**Rule of Thumb**: Flat is usually better. Use nesting only when the second condition logically depends on the first.

---

## 5. Live Demo: Shipping Cost Calculator with If/Elif/Else (11 minutes)

**Scenario**: "We're building a shipping cost calculator. The rule is:
- Packages up to 10 lbs: FREE
- Packages 10–50 lbs: $5
- Packages 50–100 lbs: $12
- Packages over 100 lbs: Need a special quote (error for now)

Let's code this live and test boundary values."

### Demo Part 1: The Basic Structure

```python
weight = 25

if weight <= 10:
    cost = 0
elif weight <= 50:
    cost = 5
elif weight <= 100:
    cost = 12
else:
    print("Too heavy. Contact support.")
    cost = None  # No cost yet

print(f"Weight: {weight} lbs, Cost: ${cost}")
```

**Narration**: "Notice the order: we check small weights first, then progressively larger. Each condition is mutually exclusive. Run this with weight = 25."

Output: `Weight: 25 lbs, Cost: $5`

### Demo Part 2: Test Boundary Values

```python
def check_cost(w):
    if w <= 10:
        cost = 0
    elif w <= 50:
        cost = 5
    elif w <= 100:
        cost = 12
    else:
        cost = None
    return cost

# Test boundaries
print(f"9 lbs: ${check_cost(9)}")     # Should be 0
print(f"10 lbs: ${check_cost(10)}")   # Should be 0 (boundary, included in first)
print(f"11 lbs: ${check_cost(11)}")   # Should be 5
print(f"50 lbs: ${check_cost(50)}")   # Should be 5 (boundary)
print(f"51 lbs: ${check_cost(51)}")   # Should be 12
print(f"100 lbs: ${check_cost(100)}") # Should be 12 (boundary)
print(f"101 lbs: ${check_cost(101)}") # Should be None
```

**Narration**: "Boundaries are where bugs hide! Notice 10 lbs gets free shipping (0) because <= includes 10. At 11 lbs, we jump to $5. At 50, we're still $5. This is correct and consistent."

### Demo Part 3: Add Discount Logic (Nested)

```python
weight = 35
is_member = True

if weight <= 10:
    base_cost = 0
elif weight <= 50:
    base_cost = 5
elif weight <= 100:
    base_cost = 12
else:
    base_cost = None

# Apply membership discount if applicable
if base_cost is not None:
    if is_member:
        final_cost = base_cost * 0.9  # 10% off
    else:
        final_cost = base_cost
else:
    final_cost = None

print(f"Weight: {weight} lbs, Member: {is_member}")
print(f"Base cost: ${base_cost}, Final cost: ${final_cost}")
```

**Narration**: "Now we nest a second check: if we have a valid cost AND the customer is a member, apply a 10% discount. Notice how we check `base_cost is not None` first to avoid errors."

Output: `Weight: 35 lbs, Member: True` / `Base cost: $5, Final cost: $4.5`

### Demo Part 4: Prediction Moment

"What will this print?"
```python
weight = 50
is_member = False

if weight <= 10:
    base_cost = 0
elif weight <= 50:
    base_cost = 5
else:
    base_cost = 12

final_cost = base_cost * 0.9 if is_member else base_cost
print(f"Final: ${final_cost}")
```

Give learners 10 seconds, then reveal: `Final: $5` (because is_member is False, so no discount).

---

## 6. Guided Practice Walkthrough (8 minutes)

**The Scenario**: "Let's build a grade letter assignment system. The rules:
- 90–100: A
- 80–89: B
- 70–79: C
- 60–69: D
- Below 60: F

Let's code this together, step by step."

### Step 1: Set Up the Score

```python
score = 87
print(f"Score: {score}")
```

### Step 2: Build the If/Elif/Else

```python
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

**Instructor Talk**: "Notice: we check from highest score down. Why? Because if score is 95, it's >= 90, so we stop there. We don't need to check >= 80 because 95 is already >=90. Order matters!"

Output: `Score: 87, Grade: B`

### Step 3: Add a Message

```python
score = 87

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory."
elif score >= 60:
    grade = "D"
    message = "Needs improvement."
else:
    grade = "F"
    message = "See me after class."

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Message: {message}")
```

**Instructor Talk**: "Each branch can have multiple statements. We set both grade and message. They stay associated with that branch."

Output:
```
Score: 87
Grade: B
Message: Good job!
```

### Step 4: Test Multiple Scores

```python
def assign_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(f"95: {assign_grade(95)}")  # A
print(f"87: {assign_grade(87)}")  # B
print(f"75: {assign_grade(75)}")  # C
print(f"65: {assign_grade(65)}")  # D
print(f"55: {assign_grade(55)}")  # F
print(f"80: {assign_grade(80)}")  # B (boundary)
```

**Instructor Talk**: "We wrap it in a function so we can test many scores at once. Notice score 80 gets a B, not an A, because we check >= 90 first."

---

## 7. Lab with Checkpoints: Shipping Calculator

**Lab Duration**: 18 minutes  
**Objective**: Implement tiered pricing logic with clear boundaries and proper ordering.

### Lab Prompt

Write a program that calculates shipping cost based on package weight. The rules are:

- **0–5 lbs**: $3
- **5–15 lbs**: $7
- **15–30 lbs**: $12
- **30–50 lbs**: $18
- **Over 50 lbs**: "Cannot ship"

Your program should:
1. Ask the user for the weight (as a number)
2. Determine the appropriate cost tier
3. Print the cost or error message

**Example outputs**:
- Input: 3 lbs → "Shipping cost: $3"
- Input: 10 lbs → "Shipping cost: $7"
- Input: 51 lbs → "Cannot ship: package too heavy"

### Checkpoint 1: Input & Type Conversion (4 minutes)

**Your code should have**:
- One `input()` prompt for weight
- Conversion to `float` (e.g., `weight = float(input(...))`)
- Verification that the input was converted correctly (test with multiple values)

**Test**: Run with input 12.5 and verify it's treated as a number, not a string.

### Checkpoint 2: If/Elif/Else Structure (8 minutes)

**Build the conditional**:
```python
weight = float(input("Package weight in lbs: "))

if weight <= 5:
    cost = 3
elif weight <= 15:
    cost = 7
elif weight <= 30:
    cost = 12
elif weight <= 50:
    cost = 18
else:
    message = "Cannot ship"

# Print result
if weight <= 50:
    print(f"Weight: {weight} lbs, Shipping cost: ${cost}")
else:
    print(f"Weight: {weight} lbs, {message}")
```

**Test cases**:
- 2 lbs → $3
- 5 lbs → $3 (boundary, included in first tier)
- 6 lbs → $7
- 15 lbs → $7 (boundary)
- 30 lbs → $12 (boundary)
- 50 lbs → $18 (boundary)
- 51 lbs → "Cannot ship"

### Checkpoint 3: Testing Boundaries (6 minutes)

**Test each boundary value**:
- 0, 5, 5.01 (around 5 lb boundary)
- 15, 15.01 (around 15 lb boundary)
- 30, 30.01 (around 30 lb boundary)
- 50, 50.01 (around 50 lb boundary)

Verify that:
- The boundary value itself is included in the correct tier
- Values just below and above transition correctly
- Output is clear and readable

---

## 8. Troubleshooting Pitfalls

### Pitfall 1: Forgetting the Colon After Condition

**The Mistake**:
```python
if age >= 18        # Missing colon!
    print("Adult")
```

**Error**: `SyntaxError: invalid syntax`

**Why**: Python uses the colon to mark the start of a block. Without it, Python doesn't know a block is coming.

**The Fix**:
```python
if age >= 18:       # Colon included
    print("Adult")
```

---

### Pitfall 2: Incorrect Indentation

**The Mistake**:
```python
if age >= 18:
print("Adult")      # Not indented!
```

**Error**: `IndentationError: expected an indented block`

**Why**: Python requires consistent indentation (usually 4 spaces). Without it, Python doesn't recognize the block as part of the `if`.

**The Fix**:
```python
if age >= 18:
    print("Adult")  # Indented with 4 spaces
```

**Tip**: Use an IDE that auto-indents. After you type a colon and press Enter, most IDEs indent automatically.

---

### Pitfall 3: Unreachable Elif Branches

**The Mistake**:
```python
score = 95
if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"    # This will never execute for scores > 90
else:
    grade = "C"
```

**Why**: If `score > 90` is true, we enter the first block and never check `elif score > 80`. For a score of 95, the first condition is true, so the second is never evaluated.

**The Problem**: This happens when you order conditions from general to specific, allowing earlier conditions to "catch" values that later conditions could also match.

**The Fix** (order from most specific to most general):
```python
score = 95
if score >= 90:
    grade = "A"    # Check most restrictive first
elif score >= 80:
    grade = "B"    # Then less restrictive
else:
    grade = "C"
```

**Test this**: Score 95 → A (correct). Score 85 → B (correct). Score 75 → C (correct).

---

### Pitfall 4: Overlapping Boundaries

**The Mistake**:
```python
weight = 15
if weight < 15:
    cost = 5
elif weight <= 15:
    cost = 7
```

**Problem**: At exactly 15 lbs, the first condition is false (15 < 15 is false), so we check the second (15 <= 15 is true) and get $7. But this is inconsistent design. Is 15 lbs in the first tier or second?

**The Fix** (use non-overlapping ranges):
```python
weight = 15
if weight <= 5:
    cost = 3
elif weight <= 15:
    cost = 7    # Now 15 is clearly in this tier
elif weight <= 30:
    cost = 12
```

**Test**: 5 lbs → $3, 15 lbs → $7, 16 lbs → $12. All boundaries are consistent and clear.

---

### Pitfall 5: Using `==` Instead of Comparison Ranges

**The Mistake**:
```python
score = 87
if score == 90:
    grade = "A"
elif score == 80:
    grade = "B"    # This only matches exactly 80!
```

**Problem**: You're checking for exact values, not ranges. Score 87 matches none of these, so grade is never set.

**The Fix** (use `>=` to define ranges):
```python
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

---

## 9. Quick-Check Questions

**Ask these in rapid succession (2–3 min total). Encourage verbal responses or quick polling.**

1. **"What does this print?"**
   ```python
   x = 15
   if x < 10:
       print("Small")
   elif x < 20:
       print("Medium")
   else:
       print("Large")
   ```
   *(Expected: "Medium")*

2. **"True or False: Both the `if` and `elif` blocks can run in the same execution."**  
   *(Expected: False. Only ONE block runs.)*

3. **"Why do we order conditions from most specific to most general in an if/elif chain?"**  
   *(Expected: To avoid unreachable code and ensure consistent logic.)*

4. **"What's the colon (`:`) for at the end of `if age >= 18:`?"**  
   *(Expected: It marks the start of a block that will be indented.)*

5. **"If I have a weight boundary at 50 lbs, should I use `weight < 50` or `weight <= 50`?"**  
   *(Expected: It depends on your rule, but be consistent. If 50 is supposed to be in the lower tier, use `<=`.)*

---

## 10. Wrap-Up (4 minutes)

### Key Takeaways

1. **If/elif/else structure**: Branching logic where only ONE block executes.
2. **Order matters**: Check from most specific to most general. Once a condition is true, the rest are skipped.
3. **Boundaries are critical**: Use `<=` and `>=` to include edge values. Test boundary values to catch bugs.
4. **One block, one time**: Remember, if age >= 18 is true, elif age >= 65 is never checked. They're mutually exclusive paths.
5. **Nested vs. flat**: Use flat (`and`/`or`) when conditions are independent. Use nesting when one logically depends on the other.
6. **Unreachable code**: If an `elif` or `else` never runs in your tests, check your condition order.

### Real-World Connections

Conditional logic is everywhere:
- **E-commerce**: Discount tiers based on order value
- **Banking**: Account types based on balance
- **Games**: Different actions based on user input
- **Automation**: Different responses based on sensor data
- **Grading systems**: Letter grades based on numeric scores

### Looking Ahead

Next hour is Checkpoint 1, where you'll apply boolean logic, comparisons, and conditionals all together in a comprehensive mini-project. Everything you've learned in the past two hours comes together.

---

## 11. Facilitation Notes

### Pacing & Flexibility

- **If learners are quick**: Introduce nested conditions more deeply, or ask them to trace complex if/elif/else chains.
- **If learners are struggling**: Spend more time on the concept that "only one block runs." Use a physical analogy: "You're at a fork in the road. You choose one path and never look back."
- **If time is tight**: Skip the nested conditions section and focus on if/elif/else.

### Engagement Tips

1. **Prediction before running**: Always ask "What will this print?" before executing code.
2. **Flowchart drawing**: Sketch decision trees on the whiteboard. Visual learners benefit greatly.
3. **Boundary testing**: Emphasize that bugs hide at boundaries. Make testing a habit.
4. **Real-world scenarios**: "Imagine you're programming the checkout process for an online store. How would you tier shipping costs?"

### Troubleshooting On the Fly

- **"Nothing is printing."** → Check if the condition is true. Add a print statement before the if to verify.
- **"The wrong block is running."** → Trace through the conditions in order. Is the first one actually true?
- **"IndentationError."** → Check that every line in the block has the same indentation (usually 4 spaces).

### Encouraging Code Tracing

Teach learners to trace their own code:
1. Read the condition aloud.
2. Evaluate it (true or false).
3. If true, follow that block. If false, skip to the next condition.
4. Stop as soon as you find a true condition.

---

## 12. Assessment Rubric

### Shipping Calculator Lab Rubric (20 points total)

| Criterion | Points | Evidence |
|-----------|--------|----------|
| **Input & Type Conversion** | 3 | Program prompts for weight. Uses `float()` to convert. Input is treated as a number. |
| **Correct If/Elif/Else Structure** | 5 | All five weight tiers are checked in correct order. Conditions are mutually exclusive and correctly bounded. |
| **Boundary Correctness** | 4 | Boundary values (5, 15, 30, 50 lbs) are correctly assigned to tiers. No off-by-one errors. |
| **Clear Output** | 4 | Prints shipping cost or error message. Output is readable and correctly formatted. |
| **Testing & Edge Cases** | 2 | Program tested on at least 3 different weights. Boundaries are tested. |
| **Code Quality** | 2 | Readable variable names, reasonable comments, logical structure. |

### Grading Scale
- **18–20 points**: Excellent. All tiers correct, all boundaries tested, output is clear.
- **15–17 points**: Good. Logic correct, minor boundary issues or unclear output.
- **12–14 points**: Satisfactory. Core logic works, but edge cases or output clarity issues.
- **Below 12**: Needs rework. Significant logic errors or missing components.

### Feedback Template

**For Excellent Work**:
"Your shipping calculator is perfect! You correctly ordered the conditions from smallest to largest weight, and your boundaries are spot-on. Your code is clean and easy to read."

**For Good Work**:
"You've got the logic right! I noticed a small issue with [specific boundary]. Let's trace through what happens at exactly [boundary value]. You're close!"

**For Needs Rework**:
"Your structure is on the right track, but I see an issue with [specific problem]. Let's trace through the conditions together step by step. What happens when weight is [test value]?"

---

**End of Hour 3 Lecture Script**

---

*Word count: 3,300+ words*
