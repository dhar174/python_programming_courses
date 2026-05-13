# Day 4, Hour 4: Session Wrap-Up and Checkpoint 1 Assessment

**Course Hour**: 16  
**Session**: Day 4 (Session 4), Hour 4  
**Duration**: 60 minutes  

---

## 1. Learning Outcomes

After this instructional hour, learners will be able to:

- **Integrate boolean logic, comparisons, and conditionals** into a single coherent program that makes decisions based on user input.
- **Demonstrate mastery of Fundamentals Checkpoint 1** by building a receipt generator that uses input validation, type conversion, arithmetic, and formatted output.
- **Test and debug programs systematically**, using print statements and logical reasoning to identify and fix errors.
- **Explain their code decisions** to an instructor, showing understanding of why specific operators or structures were chosen.
- **Reflect on the first session** and identify strengths and areas for continued growth in Python fundamentals.

---

## 2. Instructor Prep Section

### Pre-Class Checklist
- [ ] Have the checkpoint rubric printed or shared with learners
- [ ] Review the sample receipt generator solution (but don't show full code)
- [ ] Prepare a breakdown of grading criteria (correctness, formatting, code quality)
- [ ] Ensure learners know the time limit (45–60 min for the checkpoint)
- [ ] Set up a way to collect submissions (file upload, screenshare, email, etc.)
- [ ] Have a timer visible for learners (helps manage time)
- [ ] Prepare 2–3 debugging examples in case learners get stuck

### Timing Breakdown
- **Opening Script & Tone Setting** (5 min)
- **Recap of Key Concepts** (8 min)
- **Grading Rubric Walkthrough** (6 min)
- **High-Level Solution Walkthrough** (7 min) *(no full code)*
- **Checkpoint Lab Work Time** (30 min) *(45–60 min total for checkpoint)*
- **Wrap-Up & Debrief** (4 min)

### Materials & Resources
- Checkpoint 1 rubric (detailed scoring)
- Sample input/output for receipt generator
- Debugging reference guide (common errors)
- Timer (visible to learners)
- Optional: Simple receipt template to guide structure

---

## 3. Opening Script

**[Read or paraphrase to set tone, ~5 minutes]**

"Welcome to the final hour of Day 4! Today, we've built something powerful: you've learned to ask questions (comparisons), combine answers (logical operators), and make decisions (if/elif/else). Now it's time to put it all together.

This hour is **Checkpoint 1**. Think of it as a celebration of what you've learned so far—not a test to make you anxious, but a chance to show that you can integrate everything: variables, types, input, arithmetic, and output into a real program.

Here's what's happening:

1. I'll explain what we're grading and how.
2. I'll walk you through the problem without giving away the code.
3. You'll have 45–60 minutes to build a **Receipt Generator**.
4. The program asks for item info, calculates totals, and prints a formatted receipt.

This is open-book. You can reference your notes, ask for hints, and use what you've learned. But the code has to be yours.

Let's dive in. You've got this."

---

## 4. Conceptual Briefing: What Checkpoint 1 Measures (8 minutes)

### The Big Picture

**Checkpoint 1 is NOT** about memorizing syntax or being perfect.

**Checkpoint 1 IS** about:
- Taking requirements and turning them into code
- Using correct operators and data types
- Creating readable output
- Catching and fixing your own mistakes

### The Problem You'll Solve

You're building a **Receipt Generator** for a simple online store.

**Input**:
- Item name (string)
- Quantity (integer or float)
- Price per item (float)

**Processing**:
- Calculate subtotal: quantity × price
- Add a fixed $2.50 service fee
- Add 8% sales tax
- Calculate final total

**Output**:
Print a nicely formatted receipt like this:

```
========== RECEIPT ==========
Item: Widget
Quantity: 3
Price per item: $10.00
Subtotal: $30.00
Service fee: $2.50
Subtotal with fee: $32.50
Sales tax (8%): $2.60
Total: $35.10
=============================
```

### Key Skills Tested

1. **Input handling**: Ask for item, quantity, price. Handle user input.
2. **Type conversion**: Convert string input to numbers where needed.
3. **Arithmetic**: Multiply, add, calculate percentages.
4. **String formatting**: Use f-strings to display values with proper decimal places.
5. **Code organization**: Clear variable names, logical flow, readable output.

### What "Correct" Means

- Program runs without crashing on valid inputs
- Calculations are mathematically correct
- Output is formatted clearly (money shown to 2 decimals)
- Code is readable and not overly complex

### What "Incorrect" Means

- Program crashes or throws errors
- Calculations are wrong (wrong formula, wrong order of operations)
- Output is unclear or unformatted
- Code is so tangled it's hard to read

---

## 5. High-Level Solution Walkthrough (7 minutes)

**[Walk through structure WITHOUT giving full code. Describe the steps, ask learners to predict what happens.]**

### Step 1: Get Input

```
Ask: "What item?"
Ask: "How many?"
Ask: "Price per item?"
```

**Instructor question**: "What type should quantity be? Integer or float? Both are fine, but you need to think about it."

### Step 2: Convert to Numbers

"You got three pieces of input as strings (because `input()` returns strings). Convert the quantity and price to numbers. The item name stays a string."

**Instructor question**: "What does `float("10.50")` give you? A string that looks like a number, or an actual number you can use in math?"

### Step 3: Calculate Subtotal

"Multiply quantity by price per item."

```python
subtotal = quantity * price_per_item
```

**Instructor question**: "If quantity is 3 and price is 10.00, what's the subtotal?"

### Step 4: Add Service Fee

"Add $2.50 to the subtotal."

```python
subtotal_with_fee = subtotal + 2.50
```

### Step 5: Calculate Tax

"Compute 8% of the subtotal_with_fee. That's the tax amount."

```python
tax = subtotal_with_fee * 0.08
```

**Instructor question**: "Why do we tax the subtotal_with_fee, not just the subtotal? Because the service fee is part of what we're taxing."

### Step 6: Calculate Final Total

"Add the tax to the subtotal_with_fee."

```python
total = subtotal_with_fee + tax
```

### Step 7: Print the Receipt

"Print all values in a nicely formatted way. Use f-strings and format money to 2 decimals."

```python
print("Item:", item)
print(f"Quantity: {quantity}")
print(f"Price per item: ${price_per_item:.2f}")
# ... more lines ...
print(f"Total: ${total:.2f}")
```

**Instructor talk**: "Notice `.2f` in the f-string. That means 'format as a float with 2 decimal places.' So 10 becomes 10.00, and 35.1 becomes 35.10."

### Step 8: Test with Sample Input

"Test your code with this example:
- Item: Widget
- Quantity: 3
- Price per item: 10.00

Expected output shows:
- Subtotal: $30.00
- Service fee: $2.50
- Subtotal with fee: $32.50
- Tax (8%): $2.60
- Total: $35.10"

---

## 6. Practice Walkthrough: Building a Step (5 minutes) *(adapted from live building time)*

**Together, let's build ONE piece to show the pattern.**

"Let's start with input and conversion. Here's the structure:"

```python
# Step 1: Get input
item = input("Item name: ")
quantity_str = input("Quantity: ")
price_str = input("Price per item: ")

# Step 2: Convert to numbers
quantity = float(quantity_str)
price_per_item = float(price_str)

# Step 3: Show what we got
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price: ${price_per_item}")
```

**Instructor talk**: "Notice we convert the strings to floats. Now quantity and price are actual numbers we can do math with. Test this with input: Widget, 3, 10.00"

Then ask: "What comes next? Subtotal. How do you calculate it?"

**Expected answer**: "Multiply quantity by price_per_item."

Let a learner provide the code, then confirm it's correct.

---

## 7. Lab with Checkpoints: Receipt Generator (Checkpoint 1)

**Lab Duration**: 45–60 minutes total *(30 min active lab time)*  
**Objective**: Build a complete receipt generator that integrates input, calculations, and formatted output.

### Lab Prompt: Receipt Generator

You're building a receipt generator for a store. Write a Python program that:

1. **Asks for**:
   - Item name
   - Quantity (number)
   - Price per item (in dollars)

2. **Calculates**:
   - Subtotal: quantity × price per item
   - Subtotal with service fee: subtotal + $2.50
   - Sales tax (8%): 0.08 × subtotal with fee
   - Total: subtotal with fee + sales tax

3. **Prints** a formatted receipt showing:
   - Item name
   - Quantity
   - Price per item (formatted to 2 decimals)
   - Subtotal (formatted to 2 decimals)
   - Service fee ($2.50)
   - Subtotal with service fee
   - Sales tax amount
   - Final total

**Example output** (with input: Widget, 3, 10.00):
```
========== RECEIPT ==========
Item: Widget
Quantity: 3
Price per item: $10.00
Subtotal: $30.00
Service fee: $2.50
Subtotal with fee: $32.50
Sales tax (8%): $2.60
Total: $35.10
=============================
```

### Checkpoint 1: Input & Type Conversion (10 minutes)

**Your code should have**:
- Three `input()` prompts (item, quantity, price)
- Correct type conversion: `quantity = float(...)`, `price = float(...)`
- No crashes when running with sample data

**Test**: Run with input "Widget", "3", "10.00". No errors.

### Checkpoint 2: Arithmetic Calculations (15 minutes)

**Your code should have**:
- `subtotal = quantity * price_per_item`
- `subtotal_with_fee = subtotal + 2.50`
- `tax = subtotal_with_fee * 0.08`
- `total = subtotal_with_fee + tax`

**Verify**: For input 3 × $10.00:
- Subtotal: $30.00 ✓
- With fee: $32.50 ✓
- Tax: $2.60 ✓
- Total: $35.10 ✓

### Checkpoint 3: Formatted Output (15 minutes)

**Your code should have**:
- Labels for each line (e.g., "Item:", "Quantity:", etc.)
- Money values formatted with `:.2f` (e.g., `${total:.2f}`)
- Clear, readable layout (decorative borders are optional but nice)

**Test case**:
```
Input: Apple, 5, 1.50
Expected output:
Item: Apple
Quantity: 5
Price per item: $1.50
Subtotal: $7.50
Service fee: $2.50
Subtotal with fee: $10.00
Sales tax (8%): $0.80
Total: $10.80
```

---

## 8. Troubleshooting Pitfalls

### Pitfall 1: Forgetting to Convert Input

**The Mistake**:
```python
quantity = input("Quantity: ")
subtotal = quantity * 10   # TypeError!
```

**Why It Breaks**: `input()` returns a string. You can't multiply a string by a number.

**The Fix**:
```python
quantity = float(input("Quantity: "))  # Convert first
subtotal = quantity * 10
```

---

### Pitfall 2: Wrong Order of Calculations

**The Mistake**:
```python
tax = subtotal * 0.08          # Tax on subtotal
total = subtotal + fee + tax   # But forgot to tax the fee!
```

**Why It's wrong**: The service fee should be taxed too. The tax should be on `subtotal + fee`, not just `subtotal`.

**The Fix**:
```python
subtotal_with_fee = subtotal + 2.50
tax = subtotal_with_fee * 0.08  # Tax the full amount
total = subtotal_with_fee + tax
```

---

### Pitfall 3: Rounding Too Early

**The Mistake**:
```python
subtotal = round(quantity * price, 2)
tax = subtotal * 0.08              # Tax calculated on rounded value
# ...later...
total = subtotal + fee + tax       # Total might be off by a penny
```

**Why It's wrong**: Rounding early can introduce small errors that compound. Calculate first, round only for display.

**The Fix**:
```python
subtotal = quantity * price        # Don't round yet
tax = subtotal * 0.08
total = subtotal + fee + tax

# Only round when printing
print(f"Total: ${total:.2f}")   # .2f rounds for display
```

---

### Pitfall 4: Unclear or Missing Output

**The Mistake**:
```python
print(quantity)
print(subtotal)
print(tax)
print(total)
```

**Why It's wrong**: Learners don't know what each number represents. Is 3 the quantity or the tax?

**The Fix**:
```python
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

---

### Pitfall 5: Not Testing with Different Inputs

**The Mistake**: Writing code that works for one example but fails on others.

**Why It's a problem**: You might have hardcoded values or made assumptions that break with different inputs.

**The Fix**: Test with multiple examples:
- Example 1: 3 widgets @ $10.00
- Example 2: 1 apple @ $1.50
- Example 3: 10 items @ $0.99
- Edge case: Fractional quantity like 2.5

---

## 9. Quick-Check Questions

**These are diagnostic. Use them to gauge understanding and redirect if needed.**

1. **"How many times should you run your code before submitting?"**  
   *(Expected: At least 2–3 times with different inputs. Tests aren't just for developers; they're for programmers.)*

2. **"If your output shows `$10` instead of `$10.00`, what's the issue?"**  
   *(Expected: The formatting isn't using `.2f`. Use `f"{value:.2f}"` to force 2 decimal places.)*

3. **"You calculated tax on just the subtotal, not the subtotal-with-fee. Is that correct?"**  
   *(Expected: No. Tax should be on the full amount including the service fee.)*

4. **"How do you convert a string to a number in Python?"**  
   *(Expected: `int()`, `float()`, or `int(input(...))`.)*

5. **"What's one mistake you found and fixed while writing your code?"**  
   *(This is a reflection question. Any answer shows self-awareness.)*

---

## 10. Wrap-Up (4 minutes)

### What We Accomplished This Session

In the last 4 hours (Day 4), we built the foundation for decision-making in Python:

- **Hour 1 (Day 4, Hour 2)**: Learned comparisons and boolean logic.
- **Hour 2 (Day 4, Hour 3)**: Built conditional branching with if/elif/else.
- **Hour 3 (Day 4, Hour 4)**: Integrated everything into a real program (today).

### From Today's Checkpoint

The receipt generator is more than a homework assignment. It's proof that you can:
- Take a real-world requirement
- Break it into steps
- Write code that does the math correctly
- Format output for humans to read

That's professional programming.

### Looking Ahead

Next week, we'll learn more data structures (lists, dictionaries, loops) and ways to organize our code better (functions, modules). But today, you've shown you can handle the fundamentals.

### One Final Thought

Programming is problem-solving. Every error you encounter and fix makes you a better programmer. If your code doesn't work the first time, that's not failure—that's data. Use it to improve.

Great job today. You should be proud.

---

## 11. Facilitation Notes

### Before the Checkpoint Starts

1. **Clarify the rules**:
   - This is individual work (no copying).
   - You can ask for hints, but I won't give you the code.
   - Use your notes and the IDE's help features.
   - You have 45–60 minutes.

2. **Set expectations**:
   - Correctness first, then formatting.
   - A program that works is better than perfect formatting that's wrong.
   - If you get stuck, ask for help. Don't sit in silence.

3. **Provide a template (optional)**:
   - Some learners benefit from a skeleton to fill in:
     ```python
     # Input
     item = input(...)
     
     # Conversion
     quantity = float(...)
     
     # Calculations
     subtotal = ...
     
     # Output
     print(...)
     ```

### During the Checkpoint

**Circulate and watch for**:
- Learners who start typing without a plan (gently redirect: "What's step 1?")
- Type errors (string instead of number)—ask them to trace the error
- Calculation errors (wrong formula)—ask them to write it on paper first
- Output issues (missing labels)—ask them to compare to the example

**Respond to questions**:
- "How do I convert a string to a number?" → Remind them of `float()` and `int()`.
- "Is my tax calculation right?" → Ask them to walk you through it. Do they tax the fee?
- "How do I format money?" → Show them `.2f` again if needed, but don't code it for them.

### After the Checkpoint

1. **Collect submissions** in your chosen method (email, upload, screenshare, etc.)
2. **Give verbal feedback** if time allows: "Your logic is solid. Nice work."
3. **Debrief briefly**: "Raise your hand if you found a bug and fixed it." (Building culture of debugging as normal)

### Grading Quickly

Use the rubric provided. Focus on:
1. Does it run? (If not, why not?)
2. Are the calculations correct?
3. Is the output readable?

Don't be harsh on minor formatting differences. The core skills matter most.

---

## 12. Assessment Rubric

### Checkpoint 1: Receipt Generator Rubric (30 points total)

| Criterion | Points | Evidence |
|-----------|--------|----------|
| **Input Handling** | 4 | Three `input()` prompts. Collects item (string), quantity, and price. No crashes on valid input. |
| **Type Conversion** | 3 | Quantity and price converted to `float`. Item remains a string. No `TypeError` when calculating. |
| **Calculations (Subtotal)** | 4 | Correct subtotal: `quantity × price_per_item`. Tested and verified. |
| **Calculations (Service Fee)** | 3 | Correctly adds $2.50 to subtotal. Subtotal_with_fee is accurate. |
| **Calculations (Tax)** | 4 | Correctly calculates 8% tax on subtotal_with_fee (not just subtotal). Tax amount is accurate. |
| **Calculations (Total)** | 3 | Correctly adds all components: subtotal + fee + tax. Final total matches expected value. |
| **Output Formatting** | 3 | Money values display with 2 decimals (e.g., $10.00). Each value is labeled. Layout is clear and readable. |
| **Code Quality** | 3 | Variable names are descriptive. Logic is straightforward. No unnecessary complexity. |

### Grading Scale
- **28–30 points**: Excellent. All calculations correct, output perfectly formatted, code is clean.
- **24–27 points**: Good. All calculations correct, minor formatting issues, code is readable.
- **20–23 points**: Satisfactory. Core logic works, but one calculation or formatting issue, or output could be clearer.
- **15–19 points**: Needs work. Multiple calculation errors or significant output issues.
- **Below 15**: Requires rework. Major errors in logic or conversions; program doesn't run correctly.

### Sample Feedback

**Excellent**:
"Outstanding work! Your receipt generator is perfect. You correctly handled all conversions, calculated each component in the right order, and formatted the output beautifully. You're ready for more complex challenges."

**Good**:
"Great job overall! Your logic is solid and your program runs. I noticed the tax could be calculated on the subtotal_with_fee rather than just the subtotal—let's talk about that. You're very close to perfect."

**Satisfactory**:
"You've got the right idea and most of the program works. There's an issue with [specific area, e.g., tax calculation]. Let's trace through it together. Once you fix that, you'll be good."

**Needs Work**:
"Your approach is on the right track, but there are a few issues that need fixing. Let's debug together. Start by testing with the sample input and see where the output diverges from the expected receipt."

---

## Checkpoint 1 Sample Test Cases

### Test Case 1: Standard Order
**Input**: Widget, 3, 10.00
- Subtotal: $30.00
- Service fee: $2.50
- With fee: $32.50
- Tax (8%): $2.60
- **Total: $35.10** ✓

### Test Case 2: Small Order
**Input**: Apple, 1, 1.50
- Subtotal: $1.50
- Service fee: $2.50
- With fee: $4.00
- Tax (8%): $0.32
- **Total: $4.32** ✓

### Test Case 3: Fractional Quantity
**Input**: Notebook, 2.5, 5.00
- Subtotal: $12.50
- Service fee: $2.50
- With fee: $15.00
- Tax (8%): $1.20
- **Total: $16.20** ✓

---

**End of Hour 4 Lecture Script (Checkpoint 1)**

---

*Word count: 3,150+ words*
