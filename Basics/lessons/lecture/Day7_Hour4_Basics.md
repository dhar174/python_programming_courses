# Day 7, Hour 4: Loop Patterns: Counters, Accumulators, Min/Max (Course Hour 28)
**Python Programming Basics – Session 7**

**Course:** Python Programming (Basics)
**Runbook alignment:** Session 7, Course Hour 28 – Loop patterns: counters, accumulators, min/max
**Duration:** 60 minutes
**Mode:** Instructor-led + live coding + guided lab
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on three essential loop patterns: counters (counting items that meet a condition), accumulators (summing or building values), and min/max tracking (finding extremes). Stay within Basics scope — do not introduce functional programming concepts like map/filter/reduce, lambda functions, or comprehensions. The key outcomes are recognizing these patterns, initializing variables correctly, and applying them to compute statistics from user input. The lab reinforces all of this in a number statistics calculator.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Use a counter pattern to count items that meet a specific condition.
2. Use an accumulator pattern to compute sums, products, or concatenate strings.
3. Find the minimum and maximum values in a collection, initializing trackers safely.
4. Compute an average by combining an accumulator and a counter.
5. Build a number statistics program that reads 5 numbers and computes min, max, sum, and average."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 3 for loops; introduce common patterns
- **0:05–0:15** Counter pattern: counting items that meet a condition
- **0:15–0:25** Accumulator pattern: building up a result
- **0:25–0:38** Min/max pattern: tracking extremes
- **0:38–0:48** Live demo: number statistics calculator
- **0:48–0:57** Guided lab: Number Stats
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour28_patterns_demo.py` before class begins.
- Have a second file called `hour28_lab_stats.py` ready with empty comments as a starter.
- Have the Python REPL ready for quick experiments.
- Plan to show common initialization mistakes (like initializing min to 0).
- Plan to demonstrate the difference between counting all items versus counting items that meet a condition.
- Have examples ready for sum, product, and string concatenation accumulators.

**Say:** "Please have your editor open and an empty file ready. Today we learn three fundamental loop patterns that you will use in almost every program: counting, accumulating, and finding min/max. You will build a statistics calculator."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 3

**Say:**
"Welcome back. In Hour 3, we learned for loops: iterating over lists and using range() to repeat code a specific number of times. We built a multiplication table using nested loops.

Today we focus on three patterns that come up constantly in programming: counting, accumulating, and finding extremes. These are not new Python features. They are problem-solving strategies that use the loops you already know.

Every time you need to process a collection of data and compute a result — whether it is summing numbers, finding the largest value, or counting how many items meet a condition — you will use one of these patterns."

### 3.2 Motivating the need

**Say:**
"Let me give you a few real-world situations where you need these patterns:

- A teacher needs to compute the average grade from a list of scores (accumulator + counter).
- A store manager needs to count how many products are out of stock (counter).
- A sports app needs to find the highest score in a game (min/max).
- A financial app needs to sum all transactions for the month (accumulator).

In each case, you loop through data and build up a result. The pattern you choose depends on what result you need."

### 3.3 Set expectations for the hour

**Say:**
"In this hour, we will learn:
- how to count items that meet a condition
- how to accumulate values (sum, product, concatenation)
- how to track minimum and maximum values safely
- how to combine these patterns to compute statistics
- and how to build a number statistics calculator that does all three

By the end, you will recognize these patterns in code and know how to apply them to new problems."

---

## 4) Pattern 1: Counter

### 4.1 What is a counter?

**Say:**
"A counter is a variable that starts at zero and increases by one every time a condition is met. The structure is:

```python
count = 0

for item in items:
    if condition:
        count = count + 1

print(f'Found {count} items matching condition')
```

The key steps:

1. Initialize count to 0 before the loop.
2. Inside the loop, check if the item meets your condition.
3. If yes, increment count by 1.
4. After the loop, count holds the total number of matching items."

### 4.2 Example: Counting even numbers

**Say:**
"Let me show you a concrete example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1

print(f'There are {even_count} even numbers')
```

Output:
```
There are 5 even numbers
```

We loop through the list. For each number, we check if it is even (divisible by 2). If yes, we increment even_count. After the loop, even_count is 5, because there are five even numbers: 2, 4, 6, 8, 10."

### 4.3 Common mistakes

**Say:**
"Two common mistakes with counters:

**1. Not initializing to 0:**

```python
# WRONG: count not initialized
for num in numbers:
    if num % 2 == 0:
        count = count + 1  # NameError: count not defined
```

You must initialize count before the loop.

**2. Incrementing unconditionally:**

```python
# WRONG: increments every iteration, not just when condition is true
count = 0
for num in numbers:
    count = count + 1
    if num % 2 == 0:
        # nothing here
```

The increment must be inside the if block, so it only runs when the condition is true."

---

## 5) Pattern 2: Accumulator

### 5.1 What is an accumulator?

**Say:**
"An accumulator is a variable that starts at an initial value and grows by adding (or multiplying, or appending) each item. The structure is:

```python
total = 0

for item in items:
    total = total + item

print(f'Total: {total}')
```

The key steps:

1. Initialize the accumulator to an appropriate starting value (0 for sums, 1 for products, empty string for concatenation).
2. Inside the loop, update the accumulator by adding/multiplying/appending the current item.
3. After the loop, the accumulator holds the final result."

### 5.2 Example: Sum of numbers

**Say:**
"Let me show you the most common accumulator: summing numbers.

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print(f'Total: {total}')
```

Output:
```
Total: 150
```

We start with total = 0. Then we add each number: 0 + 10 = 10, then 10 + 20 = 30, then 30 + 30 = 60, then 60 + 40 = 100, then 100 + 50 = 150."

### 5.3 Other accumulator types

**Say:**
"Accumulators are not just for sums. Here are other common uses:

**Product (multiply):**
```python
numbers = [2, 3, 4]

product = 1  # start at 1, not 0!

for num in numbers:
    product = product * num

print(product)  # Output: 24 (2 * 3 * 4)
```

**String concatenation:**
```python
words = ['Hello', 'world', '!']

sentence = ''

for word in words:
    sentence = sentence + word + ' '

print(sentence)  # Output: 'Hello world ! '
```

**Building a list:**
```python
numbers = [1, 2, 3, 4, 5]

evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # Output: [2, 4]
```

The pattern is the same: start with an appropriate initial value, then update it in each iteration."

### 5.4 Common mistakes

**Say:**
"Two common mistakes with accumulators:

**1. Wrong initial value:**

```python
# WRONG: sum starts at 1 instead of 0
total = 1
for num in numbers:
    total = total + num
```

Your sum is now 1 too high. For sums, always start at 0. For products, start at 1.

**2. Initializing inside the loop:**

```python
# WRONG: total resets to 0 every iteration
for num in numbers:
    total = 0
    total = total + num
```

The accumulator must be initialized before the loop, not inside it."

---

## 6) Pattern 3: Min/Max Tracking

### 6.1 What is min/max tracking?

**Say:**
"To find the minimum or maximum value in a collection, you keep track of the best value seen so far. The structure is:

```python
min_value = first_item

for item in items:
    if item < min_value:
        min_value = item

print(f'Minimum: {min_value}')
```

The key steps:

1. Initialize min_value to the first item in the collection.
2. Loop through the rest of the items.
3. If the current item is smaller than min_value, update min_value.
4. After the loop, min_value holds the smallest value."

### 6.2 Example: Finding minimum

**Say:**
"Let me show you how to find the minimum value:

```python
numbers = [45, 12, 67, 23, 89, 5, 34]

min_value = numbers[0]  # start with the first number

for num in numbers:
    if num < min_value:
        min_value = num

print(f'Minimum: {min_value}')
```

Output:
```
Minimum: 5
```

We start with min_value = 45 (the first number). Then we compare each number:

- 12 < 45? Yes, so min_value = 12.
- 67 < 12? No, so min_value stays 12.
- 23 < 12? No, so min_value stays 12.
- 89 < 12? No, so min_value stays 12.
- 5 < 12? Yes, so min_value = 5.
- 34 < 5? No, so min_value stays 5.

Final min_value is 5."

### 6.3 Finding maximum

**Say:**
"Finding the maximum is the same pattern, but with a greater-than comparison:

```python
numbers = [45, 12, 67, 23, 89, 5, 34]

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print(f'Maximum: {max_value}')
```

Output:
```
Maximum: 89
```

Same logic, but we update max_value only when the current number is larger."

### 6.4 Common mistakes

**Say:**
"The most common mistake with min/max is initializing to 0:

```python
# WRONG: min initialized to 0
min_value = 0

for num in numbers:
    if num < min_value:
        min_value = num
```

If all numbers are positive, min_value stays 0, which is wrong. If all numbers are negative, min_value stays 0, which is also wrong.

The safe approach: initialize to the first item in the collection. That way, you are guaranteed to find the true minimum."

### 6.5 Using built-in functions

**Say:**
"Python provides built-in min() and max() functions:

```python
numbers = [45, 12, 67, 23, 89, 5, 34]

print(f'Minimum: {min(numbers)}')
print(f'Maximum: {max(numbers)}')
```

These do the same thing as our loops, but are more concise. However, it is important to understand the pattern, because sometimes you need to track min/max based on a more complex condition, and the built-in functions are not enough."

---

## 7) Combining Patterns: Computing Average

### 7.1 Average requires two patterns

**Say:**
"To compute an average, you need both an accumulator (to sum the values) and a counter (to count how many values there are). Then divide the sum by the count.

```python
numbers = [10, 20, 30, 40, 50]

total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

average = total / count

print(f'Average: {average}')
```

Output:
```
Average: 30.0
```

We accumulate the sum (150) and count the items (5), then divide: 150 / 5 = 30."

### 7.2 Simplification

**Say:**
"In this case, we know the count in advance (it is len(numbers)), so we could simplify:

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print(f'Average: {average}')
```

But if you are reading numbers from user input and do not know the count in advance, you must count them inside the loop."

---

## 8) Live Coding Demo: Number Statistics (~10 minutes)

### 8.1 Announce the demo

**Say:**
"Now I am going to build a number statistics calculator. The program will:

1. Ask the user to enter 5 numbers.
2. Compute and display:
   - Minimum
   - Maximum
   - Sum
   - Average

I will use all three patterns: accumulator (for sum), min/max tracking, and a counter (for average). Watch how I initialize each variable and update it in the loop."

### 8.2 Code the solution

**Type aloud:**

```python
# Number statistics calculator

print("Enter 5 numbers:")

numbers = []

for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

# Initialize trackers
total = 0
min_value = numbers[0]
max_value = numbers[0]

# Loop through numbers and update trackers
for num in numbers:
    total = total + num
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

# Compute average
average = total / len(numbers)

# Display results
print()
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
```

**Say:**
"Let me explain the key parts:

1. **Collect numbers:** We ask the user for 5 numbers and store them in a list.

2. **Initialize trackers:** We set total to 0, and min_value and max_value to the first number in the list.

3. **Loop through numbers:** For each number, we:
   - Add it to total (accumulator)
   - Check if it is smaller than min_value (update if yes)
   - Check if it is larger than max_value (update if yes)

4. **Compute average:** Divide total by the count of numbers.

5. **Display results:** Print all statistics with formatting."

### 8.3 Test the code

**Say:**
"Let me test this with some numbers."

**Test input:**
- 10
- 5
- 20
- 15
- 30

**Output:**
```
Minimum: 5.0
Maximum: 30.0
Sum: 80.0
Average: 16.00
```

**Say:**
"All statistics are correct. The program uses three patterns: accumulator (sum), min/max tracking, and count (for average)."

### 8.4 Common mistake: Initializing min to 0

**Say:**
"A common bug is initializing min_value to 0:

```python
min_value = 0  # WRONG

for num in numbers:
    if num < min_value:
        min_value = num
```

If I enter numbers like 10, 20, 30, the minimum should be 10. But because min_value starts at 0, and no number is less than 0, min_value stays 0. This is wrong.

The fix: initialize to the first number in the list, not to 0."

---

## 9) Guided Lab: Number Stats (~25 minutes)

### 9.1 Announce the lab

**Say:**
"Now it is your turn. You will build a number statistics calculator. Here is the specification:

**Lab: Number Stats**

**Goal:** Ask the user to enter 5 numbers, then compute and display min, max, sum, and average.

**Rules:**

- Prompt for 5 numbers (use float() to allow decimals)
- Store numbers in a list
- Compute min, max, sum, and average using loop patterns (not built-in functions like min() or sum())
- Display results with clear labels
- Format average to 2 decimal places

**Optional extensions (if you finish early):**

1. Allow the user to choose how many numbers to enter.
2. Add validation: if the user enters invalid input, re-prompt.

**Completion criteria:**

- Program computes correct statistics for any set of 5 numbers
- Uses loop patterns (accumulator, min/max)
- Clean, formatted output

You have 25 minutes. I will circulate and help."

### 9.2 Circulate and provide feedback

Walk around the room. Look for:

- **Wrong initialization:** Min/max initialized to 0 instead of first number.
- **Accumulator mistakes:** Total not initialized, or initialized inside the loop.
- **Average calculation:** Dividing by wrong count, or forgetting to divide.
- **Using built-in functions:** Students using min() or sum() instead of implementing the pattern.

**Common mistake to watch for:**

```python
min_value = 0
max_value = 0

for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
```

This produces wrong results if all numbers are positive (min stays 0) or all numbers are negative (max stays 0).

**Coaching language:**

- "If all your numbers are positive, what happens if min_value starts at 0?"
- "Where should you initialize your accumulator variables? Before or inside the loop?"
- "How do you compute an average? What two values do you need?"

### 9.3 Debugging support

If a student is stuck:

1. Ask them to print their tracker variables at the end of each loop iteration to see how they change.
2. Ask them to test with simple numbers like 1, 2, 3, 4, 5 first.
3. If their min/max is wrong, ask them to trace through the loop by hand with the numbers they entered.

---

## 10) Debrief and Knowledge Check (~12 minutes)

### 10.1 Share-out

**Say:**
"Let us hear from a few people. Who wants to show their solution and explain how they tracked min and max?"

**Call on 2–3 learners. Ask:**

- "How did you initialize min_value? Why?"
- "What happens in your loop on each iteration?"
- "Did you try any of the optional extensions?"

### 10.2 Common mistakes review

**Say:**
"Here are the most common mistakes I saw today:

1. **Initializing min/max to 0:** This breaks if all numbers are positive or negative. Always initialize to the first item in the list.

2. **Initializing inside the loop:** If you initialize total = 0 inside the loop, it resets every iteration and never accumulates. Initialize before the loop.

3. **Wrong average formula:** Average is sum divided by count, not sum divided by the last number.

4. **Using built-in functions:** While min() and sum() work, the point of this lab is to practice the loop patterns. In real code, use built-ins when appropriate, but understand the pattern first.

The fix for all of these: plan your initialization carefully, test with small inputs, and trace through the loop by hand."

### 10.3 Conceptual recap

**Say:**
"Let me summarize today's key ideas:

1. **Counter pattern:** Start at 0, increment by 1 when a condition is true. Use for counting items that match criteria.

2. **Accumulator pattern:** Start at an appropriate initial value (0 for sums, 1 for products), then add/multiply/append each item. Use for building up results.

3. **Min/max pattern:** Start with the first item, then update if you find a smaller/larger value. Use for finding extremes.

4. **Combining patterns:** Many problems require multiple patterns. For example, computing an average uses both an accumulator (sum) and a counter (count).

These three patterns are fundamental. You will use them in almost every program you write."

---

## 11) Exit Ticket (~3 minutes)

**Say:**
"Before we finish, write down your answer to this question:

**Question:** If you want to find the minimum value in a list of 100 negative numbers, what should you initialize min_value to? Why?

**Pause for 1 minute, then reveal the answer:**

**Say:**
"Initialize min_value to the first number in the list: min_value = numbers[0].

Why? If you initialize to 0, and all numbers are negative (like -5, -10, -20), then every comparison num < min_value will be true (because negative numbers are less than 0). But you will never update min_value correctly, and your final answer will be 0, which is wrong.

By initializing to the first number, you are guaranteed to start with a value that is actually in the list. Then the comparisons work correctly regardless of whether the numbers are positive, negative, or mixed."

---

## 12) Transition to Next Session

**Say:**
"Excellent work today. You now know the three most important loop patterns: counting, accumulating, and tracking extremes.

Next session (Session 8, starting on Day 8), we will build on these patterns to create menu-driven programs and handle input validation. You will combine loops, conditionals, and data structures into a functional CLI contact manager.

That concludes Session 7. Take a well-deserved break before the next session."

---

## 13) Appendix: Quick Reference for Instructors

### Pattern summary

**Counter:**
```python
count = 0
for item in items:
    if condition:
        count += 1
```

**Accumulator (sum):**
```python
total = 0
for item in items:
    total += item
```

**Accumulator (product):**
```python
product = 1
for item in items:
    product *= item
```

**Min/Max:**
```python
min_value = items[0]
for item in items:
    if item < min_value:
        min_value = item
```

### Testing checklist

- Is the accumulator/counter initialized before the loop?
- Is the initial value correct (0 for sum, 1 for product, first item for min/max)?
- Does the loop update the variable correctly?
- Is the final result computed after the loop (like average = total / count)?

### Troubleshooting common student issues

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "My sum is always 0" | Not updating total inside loop, or initializing inside loop | Check that total += num is inside the loop |
| "My min is always 0" | Initialized to 0 instead of first item | Initialize to numbers[0] or first item |
| "My average is wrong" | Dividing by wrong count, or not dividing at all | Average = total / count, computed after loop |
| "My product is 0" | Initialized to 0 instead of 1 | For products, initialize to 1, not 0 |
| "My counter never increases" | Increment not inside if block | count += 1 must be inside the if condition |

---

## 14) Real-World Context: Why These Patterns Matter

**Teaching point:**
"These three patterns are not just academic exercises. They are the building blocks of data processing:

1. **Finance:** Banks sum transactions, find maximum withdrawal, count overdrafts.
2. **Analytics:** Data scientists compute averages, find outliers (min/max), count events.
3. **Gaming:** Games track high scores (max), total points (sum), number of wins (counter).
4. **E-commerce:** Stores sum cart totals, find most expensive item (max), count items in stock (counter).

Every time you see aggregated data — like 'Average rating: 4.5 stars' or 'Total views: 1.2 million' — these patterns are running behind the scenes."

---

## 15) Advanced Topic: Running Min/Max

**Teaching point (optional, for advanced learners):**
"Sometimes you need to track both the value and the index where min/max occurred:

```python
numbers = [45, 12, 67, 23, 89, 5, 34]

min_value = numbers[0]
min_index = 0

for i in range(len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_index = i

print(f'Minimum: {min_value} at index {min_index}')
```

Output:
```
Minimum: 5 at index 5
```

This pattern is useful when you need to know where the extreme value is, not just what it is. For example, finding the day of the month with the highest sales."

---

## 16) Style Guide: Naming Variables

**Teaching point:**
"Choose clear names for accumulator and tracker variables:

Good:
```python
total = 0
count = 0
min_value = items[0]
even_count = 0
```

Bad:
```python
x = 0
n = 0
m = items[0]
c = 0
```

Use descriptive names that explain what the variable tracks. Your code is read more often than it is written."

---

## 17) Conceptual Check: When NOT to Loop

**Teaching point:**
"Not every problem requires a loop. Python provides built-in functions for common operations:

- **sum(numbers)**: Computes the sum of a list.
- **min(numbers)**: Finds the minimum value.
- **max(numbers)**: Finds the maximum value.
- **len(numbers)**: Counts the number of items.

Use these when appropriate. But understand the loop patterns first, because:

1. Built-ins only work for simple cases. If you need to sum only even numbers, or find the maximum based on a complex condition, you need a loop.

2. Understanding the pattern helps you debug when built-ins do not do what you expect.

3. Not all languages have these built-ins. The loop patterns are universal."

---

## 18) Summary: Key Takeaways

**Say:**
"Before we finish, let me emphasize the four most important points:

1. **Initialize before the loop.** All accumulators, counters, and trackers must be set up before the loop starts.

2. **Choose the right initial value.** 0 for sums, 1 for products, first item for min/max. Wrong initialization causes wrong results.

3. **Update inside the loop.** The loop body must change the accumulator/counter/tracker based on each item.

4. **Combine patterns when needed.** Many problems require multiple patterns. Understand each one individually, then combine them.

These patterns are not Python-specific. They apply to every programming language. Master them, and you can solve a huge range of problems."

---

**End of Hour 4 Script**
**End of Session 7**
