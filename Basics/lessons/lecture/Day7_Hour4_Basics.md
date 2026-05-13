# Day 7, Hour 4: Loop Patterns - Counters, Accumulators, Min/Max

**Instructor:** Charles Niswander  
**Course:** Python Programming (Basic) - PCEP Aligned  
**Duration:** 60 minutes  
**Target:** 25+ students, beginner level

## Learning Outcomes

By the end of this hour, students will be able to:

1. **Implement counter patterns** – Create variables that increment inside conditionals to count specific items in a loop.
2. **Build accumulators** – Initialize and update variables that collect values (sum, product, concatenation) across iterations.
3. **Develop min/max tracking** – Write code to find minimum and maximum values while iterating through data.
4. **Calculate averages programmatically** – Combine counters and accumulators to compute the average of a dataset.
5. **Build a real number statistics program** – Integrate all four patterns into a single, cohesive application.

---

## 1. Instructor Prep & Setup Checklist

### Preparation (15 minutes before class)

**Setup Checklist:**

- [ ] **IDE open and ready** – Python interpreter running, VS Code with Markdown preview enabled
- [ ] **Sample files prepared:**
  - `counter_demo.py` – Counter pattern walkthrough (no student intervention)
  - `accumulator_demo.py` – Accumulator pattern walkthrough
  - `minmax_demo.py` – Min/Max pattern walkthrough
  - `stats_program.py` – Complete number statistics program (result demo, not editable)
- [ ] **Terminal clear** – Previous commands hidden for clean demo
- [ ] **Breakout rooms configured** – 4-5 students per room for guided lab
- [ ] **Timing plan visible** – Instructor notes with checkpoint schedule
- [ ] **Backup plan ready** – Static code snippets in case IDE fails; printed runbook in hand

### Room Setup

- **Projection**: Live Python IDE visible to all students
- **Audio/Chat**: Enabled; monitor for "I'm stuck" or hand-raise signals
- **Learner resources**: Lab worksheet printed/shared in chat

**Contingency**: If live demo fails, paste pre-prepared code blocks from `counter_demo.py` into interpreter.

---

## 2. Opening Script

### Hook (2 minutes)

**Say:**

"Imagine you're a teacher grading 100 papers. You need to count how many pass, find the highest and lowest scores, and compute the class average. You can't do that with a single print statement—you need *patterns*. Today, you'll learn four loop patterns that professional programmers use every day to solve problems like this."

### Learning Objectives Recap (1 minute)

**Say:**

"In this hour, you'll master loop patterns: counters, accumulators, min/max tracking, and average calculations. By the end, you'll write a complete program that processes a list of numbers and reports statistics—the same logic used in data analysis, game development, and finance."

### Real-World Connection (1 minute)

**Say:**

"Your stock portfolio app needs to track gains/losses (accumulator), your fitness app counts workouts (counter), your grade tracker finds your highest and lowest scores (min/max), and your banking app computes average monthly spending (average). All use loop patterns."

---

## 3. Core Concepts: Counter, Accumulator, Min/Max, Average

### 3.1 Counter Pattern

**Concept:**

A counter is a variable that increments when a specific condition is met inside a loop. Use it to count how many items satisfy a condition.

**Structure:**

```python
count = 0

for item in items:
    if condition:
        count = count + 1

print(f'Total matches: {count}')
```

**Example: Count even numbers**

```python
numbers = [10, 5, 20, 15, 30]
even_count = 0

for num in numbers:
    if num % 2 == 0:  # Check if even
        even_count = even_count + 1

print(f'Even numbers: {even_count}')  # Output: 3
```

**Key Points:**

- Initialize counter to 0 (or appropriate starting value).
- Increment *inside* the `if` block so it only counts when the condition is true.
- Increment *after* the loop is complete to get the final count.

**Common Mistake:**

```python
# WRONG: increments every iteration, not just when condition is true
count = 0
for num in numbers:
    count = count + 1
    if num % 2 == 0:
        # nothing here
```

### 3.2 Accumulator Pattern

**Concept:**

An accumulator is a variable that starts at an initial value and grows by adding (or multiplying, or appending) each item. Use it to collect or combine values across iterations.

**Structure:**

```python
total = 0

for item in items:
    total = total + item

print(f'Total: {total}')
```

**Example: Sum a list**

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num

print(f'Sum: {total}')  # Output: 150
```

**Initialization Rules:**

- **For addition**: Initialize to 0
- **For multiplication**: Initialize to 1
- **For string concatenation**: Initialize to empty string `""`
- **For lists**: Initialize to empty list `[]`

**Key Points:**

- Choose the correct initial value based on the operation.
- Update the accumulator inside the loop.
- The final result is ready after the loop completes.

### 3.3 Min/Max Pattern

**Concept:**

Track the minimum and maximum values as you iterate. Initialize with the first item, then update only if a new extreme is found.

**Structure:**

```python
minimum = numbers[0]
maximum = numbers[0]

for num in numbers[1:]:  # Skip first item (already assigned)
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(f'Min: {minimum}, Max: {maximum}')
```

**Example:**

```python
numbers = [10, 5, 20, 15, 30]
minimum = numbers[0]  # Start with first value
maximum = numbers[0]

for num in numbers[1:]:  # Loop from second item onward
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(f'Min: {minimum}, Max: {maximum}')  # Output: Min: 5, Max: 30
```

**Key Points:**

- Initialize min and max with the first list item (not 0 or infinity).
- Iterate through the remaining items.
- Update min/max only when a new extreme is found.
- Works for any comparable data (numbers, strings, dates).

### 3.4 Average Pattern

**Concept:**

Combine a counter and accumulator to compute the average: `average = total / count`.

**Structure:**

```python
total = 0
count = 0

for item in items:
    total = total + item
    count = count + 1

average = total / count
print(f'Average: {average}')
```

**Example:**

```python
numbers = [10, 5, 20, 15, 30]
total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

average = total / count
print(f'Average: {average}')  # Output: 16.0
```

**Formatting the average:**

```python
average = total / count
print(f'Average: {average:.2f}')  # Output: 16.00 (two decimal places)
```

**Key Points:**

- Use accumulator for the sum, counter for the number of items.
- Divide only *after* the loop completes.
- Format to two decimal places for clarity: `{average:.2f}`.
- Watch for division by zero if the list is empty.

---

## 4. Live Coding Demo

### Setup (1 minute)

**Say:**

"I'm going to write a program that processes a list of numbers and computes statistics using all four patterns. Watch how I build it step by step, then you'll do the same in the lab."

### Demo Code: Number Statistics Program

**Say:**

"Here's the program:"

```python
# Number Statistics Program
# Demonstrates: counter, accumulator, min/max, average

numbers = [10, 5, 20, 15, 30]

# Initialize variables
total = 0
count = 0
minimum = numbers[0]
maximum = numbers[0]

# Process the numbers
for num in numbers[1:]:
    total = total + num
    count = count + 1
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Don't forget the first number in calculations!
total = total + numbers[0]
count = count + 1

# Compute average
average = total / count

# Display results
print(f'Min: {minimum:.1f}')
print(f'Max: {maximum:.1f}')
print(f'Sum: {total:.1f}')
print(f'Average: {average:.2f}')
```

**Expected Output:**

```
Min: 5.0
Max: 30.0
Sum: 80.0
Average: 16.00
```

### Demo Walkthrough (5 minutes)

**Say:**

"Line by line:
- We start with `numbers = [10, 5, 20, 15, 30]`.
- We initialize: `total = 0` (accumulator), `count = 0` (counter), and min/max to the first value.
- In the loop, we add each remaining number to the total, count it, and check for new min/max.
- After the loop, we handle the first number (which we skipped in the loop).
- We compute `average = total / count = 80 / 5 = 16.00`.
- Finally, we print the results with proper formatting."

**Interactive Question:**

"Why do we start the loop at `numbers[1:]` instead of `numbers[0]`?"

*Pause for student input. Expected answer: "Because we already used `numbers[0]` for min/max initialization."*

---

## 5. Guided Lab with 3 Explicit Checkpoints

### Lab Instructions

**Activity:** Build a number statistics program from scratch using counter, accumulator, and min/max patterns.

**Starter Code:**

```python
# Student Lab: Number Statistics Program
# Your task: Complete this program to process a list of numbers

numbers = [12, 8, 25, 9, 18, 14, 22]

# TODO: Initialize variables for total, count, minimum, maximum
# Hint: Initialize minimum and maximum to the first number


# TODO: Write a for loop to process the numbers
# Hint: Update total and count for every number
# Hint: Check if the current number is less than minimum or greater than maximum


# TODO: Calculate average after the loop


# TODO: Print results in this format:
# Minimum: X.X
# Maximum: X.X
# Sum: X.X
# Average: X.XX
```

### Checkpoint 1 (Minute 5)

**Objective:** Students initialize variables correctly.

**Success Criteria:**
- [ ] `total`, `count`, `minimum`, `maximum` are declared and initialized
- [ ] `minimum` and `maximum` are set to `numbers[0]`
- [ ] Loop structure begins (for loop created)

**Instructor Action:**
- Walk around and check student screens for correct initialization.
- Say: "Show me your initialized variables. Do they match the hints?"
- Stop and clarify common mistakes: forgetting `numbers[0]` for min/max, or initializing min to 0.

### Checkpoint 2 (Minute 20)

**Objective:** Students complete the loop with all four patterns.

**Success Criteria:**
- [ ] Loop iterates through all numbers
- [ ] `total = total + num` and `count = count + 1` inside loop
- [ ] Min/max comparisons implemented (`if num < minimum` and `if num > maximum`)
- [ ] Loop completes without syntax errors

**Instructor Action:**
- Check if loops are running without errors (run each student's code).
- Say: "Run your code. Do you see any errors? If yes, read the error message and tell me what line has the problem."
- Pause demo at 22 minutes for quick check-in.

### Checkpoint 3 (Minute 25)

**Objective:** Students compute average and format output.

**Success Criteria:**
- [ ] `average = total / count` calculated after loop
- [ ] Print statements formatted with correct decimal places
- [ ] Program produces expected output:
  ```
  Minimum: 8.0
  Maximum: 25.0
  Sum: 108.0
  Average: 15.43
  ```

**Instructor Action:**
- Run each student's program and verify output matches expected result.
- Say: "Compare your output to the expected result. Do they match?"
- Celebrate completion: "Excellent! You've built a complete statistics program using all four loop patterns."

### Troubleshooting Hints

| Problem | Cause | Fix |
|---------|-------|-----|
| `NameError: name 'total' is not defined` | Variable not initialized | Add `total = 0` before the loop |
| Wrong min/max values | Forgot to include first number or didn't initialize correctly | Set `minimum = numbers[0]` before loop |
| Average is wrong | Forgot to count the first number | Make sure `count` includes all numbers |
| Syntax error in loop | Missing colon or incorrect indentation | Check `:` at end of `for` line; indent loop body |

---

## 6. Assessment Rubric

**Total Points: 10**

| Criterion | Points | Rubric |
|-----------|--------|--------|
| **Input/Storage** | 2 | Variables initialized correctly; data stored in list (2 pts). Missing initialization (1 pt). No initialization (0 pts). |
| **Loop Patterns** | 4 | All four patterns implemented correctly—counter, accumulator, min/max, average (4 pts). Three patterns correct (3 pts). Two patterns correct (2 pts). One or fewer correct (0 pts). |
| **Average Calculation** | 2 | Average computed correctly after loop; formatted to 2 decimal places (2 pts). Computed but wrong format (1 pt). Not computed or wrong result (0 pts). |
| **Code Quality** | 2 | Clear variable names, proper indentation, readable output (2 pts). Minor issues (1 pt). Major issues or unrunnable code (0 pts). |

---

## 7. Troubleshooting Pitfalls

### Common Student Errors and Intervention Strategies

**Error 1: Counter increments every iteration**

**Student Code:**
```python
count = 0
for num in numbers:
    count = count + 1
    if num % 2 == 0:
        pass  # doesn't do anything
```

**Problem:** Counter is outside the `if` block, so it counts all numbers, not just even ones.

**Intervention:** Say, "If the increment is outside the `if` block, it runs on every iteration. Where should it go?" Guide the student to move `count = count + 1` inside the `if` block.

**Error 2: Min/Max initialized to 0 or a static value**

**Student Code:**
```python
numbers = [10, 5, 20, 15, 30]
minimum = 0
maximum = 0
```

**Problem:** If all numbers are positive and 0 is not in the list, minimum stays 0 (wrong). If a number is negative, maximum might be negative (also wrong).

**Intervention:** Say, "What's the minimum of [10, 5, 20, 15, 30]? It's 5, not 0. How do we start with the correct initial value?" Guide the student to use `numbers[0]`.

**Error 3: Average calculated inside the loop**

**Student Code:**
```python
total = 0
count = 0
for num in numbers:
    total = total + num
    count = count + 1
    average = total / count  # Inside the loop!
    print(f'Average so far: {average}')
```

**Problem:** Average changes on every iteration and is computed prematurely. The final average is correct by chance, but the logic is wrong.

**Intervention:** Say, "When should we calculate the average? We need the final total and count. Where does that calculation belong?" Guide the student to move the average calculation outside the loop, *after* it completes.

**Error 4: Forgetting the first number in calculations**

**Student Code:**
```python
numbers = [10, 5, 20, 15, 30]
minimum = numbers[0]
maximum = numbers[0]
total = 0
count = 0

for num in numbers[1:]:  # Skips numbers[0]!
    total = total + num
    count = count + 1
    # min/max logic...

average = total / count  # Doesn't include first number!
```

**Problem:** The first number is used for min/max initialization but not added to the total or counted.

**Intervention:** Say, "Your min/max are correct, but the sum is 70 instead of 80. Why?" Guide the student to either:
  - Add `total = total + numbers[0]` after the loop, *or*
  - Start the loop at `numbers[0]` instead of `numbers[1:]`

---

## 8. Exit Ticket & Quick-Check Questions

### Individual Reflection (3 minutes)

**Say:**

"Before we wrap up, answer these questions individually. You don't need to write code—just think about the logic."

**Question 1:** "In a counter pattern, where does the increment go: inside or outside the `if` block?"

*Expected answer:* Inside the `if` block.

**Question 2:** "You have a list of test scores. To find the lowest score, would you initialize `minimum` to 0, or to the first score in the list?"

*Expected answer:* To the first score (because 0 might not be a valid score, or a score could be negative).

**Question 3:** "Why do we compute the average after the loop, not inside it?"

*Expected answer:* Because we need the final total and count, which aren't complete until the loop is done.

### Spot-Check Responses

- **Strong:** Student explains the "why" behind each pattern (e.g., "min/max start with the first item because that's a real value").
- **Developing:** Student identifies the pattern but struggles to explain the reasoning.
- **Intervention:** Student is confused; flag for one-on-one follow-up after this hour.

---

## 9. Wrap-Up & Recap

### Debrief (2 minutes)

**Say:**

"Excellent work! You've built a complete statistics program using four professional loop patterns. Let's recap:

- **Counter:** Increments inside an `if` to count matches.
- **Accumulator:** Updates to collect values (sum, product, concatenation).
- **Min/Max:** Tracks extremes by comparing each new value.
- **Average:** Combines counter and accumulator to compute the mean.

These patterns are the foundation of data processing. Every time you filter data, aggregate results, or analyze a dataset, you're using one or more of these patterns."

### Connection to Next Hour

**Say:**

"In the next hour, we'll continue with more complex patterns and loops. But everything we do builds on these four patterns. Master them now, and everything else becomes easier."

### Celebration

**Say:**

"Give yourselves a round of applause. You've completed Day 7, Hour 4. You're now 28 hours into the Python Basics course—you're more than halfway through the first week!"

---

## 10. Facilitation Notes & Pacing Checkpoints

### Timing Plan (60 minutes total)

| Segment | Duration | Notes |
|---------|----------|-------|
| **Opening Script** | 4 min | Hook + objectives + real-world connection |
| **Core Concepts** | 12 min | Counter, Accumulator, Min/Max, Average (3 min each) |
| **Live Coding Demo** | 6 min | Demo code + walkthrough + interactive question |
| **Guided Lab – Checkpoint 1** | 5 min | Variable initialization check |
| **Guided Lab – Checkpoint 2** | 15 min | Loop + patterns check (run code at 22 min) |
| **Guided Lab – Checkpoint 3** | 5 min | Average + formatting check |
| **Exit Ticket** | 3 min | Quick-check questions |
| **Wrap-Up & Recap** | 5 min | Debrief + celebration |
| **Buffer** | 5 min | Overflow time for struggling students |

### Intervention Triggers

- **Minute 5:** If a student hasn't initialized variables, pause and show an example on screen.
- **Minute 22:** Run one volunteer's code live. If it fails, use it as a teaching moment: "Let's read the error together."
- **Minute 25:** Any student without correct output gets a one-on-one walkthrough after class.

### Facilitation Strategies

1. **Normalize mistakes:** "I deliberately put a bug in the demo code earlier—did you catch it? That's good debugging practice."
2. **Celebrate progress:** Use check-ins to praise specific behaviors: "I like how you tested your code after each change."
3. **Peer teaching:** "Can someone explain the counter pattern to the person next to you?"
4. **Differentiation:**
   - **Advanced students:** "Try modifying the program to also count how many numbers are above the average."
   - **Struggling students:** Provide the starter code with only one TODO at a time.

---

## 11. Real-World Context & Applications

### Professional Use Cases

**Data Analysis:**
"A data analyst uses accumulators to sum monthly sales, counters to count transactions by category, and min/max to find peak and valley prices."

**Gaming:**
"A game developer uses accumulators for player score, counters for kill count or lives lost, min/max for high score and low health threshold, and averages for AI difficulty calibration."

**Finance:**
"A financial system uses accumulators for portfolio value, counters for transaction count, min/max for largest gain/loss, and averages for daily trading volume."

**Scientific Research:**
"A researcher uses these patterns to process sensor data: accumulate readings, count samples, track extremes, and compute mean values for statistical analysis."

### Bridging to Advanced Topics

These patterns scale to complex data structures and real-world scenarios:

- **With dictionaries:** Track separate accumulators for each category. For example, a retailer might have a dictionary `sales_by_region` and accumulate totals separately for each region, then compute regional averages and find the region with the highest sales (min/max on dictionary values).
- **With nested loops:** Apply patterns independently to each subset of data. For instance, a data scientist might process multiple datasets in a list, computing statistics for each one independently by using nested counters, accumulators, and min/max trackers.
- **With functions:** Extract pattern logic into reusable functions for cleaner code. Instead of writing the entire statistics computation inline, you can create functions like `compute_average(numbers)`, `find_min_max(numbers)`, or `count_matches(items, condition)` and reuse them across your program.
- **With files:** Read and process data from files using these same patterns. A data analyst might read a CSV file line by line, accumulating quarterly totals, counting valid records, and tracking highest and lowest values from the file data.

---

## 12. Advanced Topics & Summary

### Extension Challenges

**For students who finish early:**

1. **Median calculation:** "Can you modify the program to find the median (middle value)? Hint: You'll need to sort the list first, then check if the count is odd or even to find the middle element."
2. **Variance and standard deviation:** "Research how to calculate variance—it's the average of squared differences from the mean. Standard deviation is the square root of variance. These are used to measure how spread out your data is."
3. **Filtering with counter:** "Count how many numbers are above the average. This combines multiple patterns: first calculate the average, then loop through again with a conditional counter."
4. **Multiple data types:** "Adapt the program to work with user input instead of a hardcoded list. Use a loop to repeatedly ask for numbers until the user enters 'done', then process the collected data using your statistics program."
5. **Range calculation:** "Add a line that calculates the range (the difference between max and min). This tells you how spread out your data is."
6. **Mode calculation:** "Find the most frequent number in the list. This requires a counter pattern inside a nested loop—for each unique value, count how many times it appears, then track which count is highest."

### Summary & Key Takeaways

**Four Essential Loop Patterns:**

1. **Counter** – Counts occurrences; initialize to 0, increment inside conditional.
2. **Accumulator** – Collects values; initialize to appropriate base value, update inside loop.
3. **Min/Max** – Tracks extremes; initialize to first item, compare and update inside loop.
4. **Average** – Combines counter and accumulator; compute after loop completes.

**Success Indicators:**

- Students can identify which pattern is needed for a given problem.
- Students can write code that implements all four patterns without syntax errors.
- Students understand why each pattern is structured the way it is (not just memorizing code).

**Homework Reminder:**

"Tonight's assignment (Day 7 homework) will give you more practice with these patterns. You'll build a program that processes real-world data—maybe grades, temperatures, or stock prices. The logic is identical to what you've learned today."

---

**End of Instructor Notes – Day 7, Hour 4**
