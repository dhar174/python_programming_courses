# Loop Patterns: Searching, Filtering, and Aggregating (Course Hour 31)

**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 31 – Loop Patterns: Searching, Filtering, and Aggregating  
**Duration:** 90 minutes  
**Mode:** Instructor-led + live demo + hands-on lab  
**Audience:** Beginners in Python

---

## 1) Learning Outcomes

**By the end of this hour, students will be able to:**

1. Implement linear search to find the first matching element in a list using a `for` loop and conditional logic
2. Implement search-all patterns to collect multiple matching elements using a result list and append operations
3. Apply filter patterns to create new lists containing only elements that satisfy specific conditions
4. Implement aggregation patterns using accumulators to compute totals, counts, and other derived values
5. Combine search, filter, and aggregation patterns to solve complex real-world data processing problems

---

## 2) Instructor Prep and Delivery Note

**Setup checklist:**
- Open Python 3.x in your editor with a fresh file: `demo_loop_patterns.py`
- Have two sample datasets ready to paste (student list, sales data)
- Set a timer for each demo phase (5-min search, 5-min search-all, 8-min filter, 8-min aggregate, 8-min combined, 6-min lab intro)
- Pre-test all code examples to ensure they run without errors
- Have a whiteboard or shared editor ready to show student questions and iterate together

**Core message:** Loop patterns are the foundation of data processing. Mastery of search, filter, and aggregation translates directly to data analysis, database queries, and real-world automation tasks. These five patterns appear in nearly every professional software system, from databases that retrieve records matching criteria (search/filter) to analytics dashboards that calculate summaries (aggregation). Learning them deeply today means you'll recognize them instantly in job interviews, code reviews, and real-world applications.

**Why this matters:** Historically, students who master these five patterns can solve complex data problems with confidence. They move faster, write cleaner code, and understand system APIs (like SQL queries, API filters, pandas operations) more intuitively because they see the same patterns recurring. This hour is an investment in your intuition as a programmer.

---

## 3) Opening Script

> **Say:** "Today we shift from 'Can I write a loop?' to 'What can I do WITH a loop?' We'll explore five core patterns that professional programmers use every single day: searching lists, filtering data, and aggregating values. By the end of this hour, you'll be able to manipulate any dataset, answer 'what', 'how many', and 'which ones' questions using nothing but loops and conditionals. Let's begin."

---

## 4) Conceptual Briefing

### The Five Loop Patterns (Overview and Why Each Exists)

Loop patterns are fundamental because they address five distinct questions programmers ask constantly when working with data:

**Pattern 1: Linear Search**  
*Question: "Is there an item matching this condition, and what is it?"*  
Find the first element matching a condition; return when found or report 'not found'. Use this when you only need ONE matching item and can stop searching once you find it. Real-world uses: finding a user by ID in a user database, locating the first error in a log file, checking if a password is correct (stop on first match).

**Pattern 2: Search-All**  
*Question: "What are ALL the items that match this condition?"*  
Find ALL elements matching a condition; collect them in a result list. Differs from linear search in that you never return early—you iterate through the ENTIRE collection. Use this when you need a complete inventory of matching items. Real-world uses: retrieve all orders for a customer, find all files matching a pattern, list all students in a class above a certain GPA.

**Pattern 3: Filter**  
*Question: "How do I remove items that DON'T match, keeping only the matching ones?"*  
Create a new list containing only elements that satisfy a condition (removes non-matching items). Conceptually similar to search-all but focused on the idea of "creating a subset". Use this when you want to clean, narrow, or reduce data. Real-world uses: filter spam emails, show only completed tasks in a to-do list, keep only profitable products in a catalog.

**Pattern 4: Aggregation**  
*Question: "What is the combined summary of all these items? (sum, count, average, max, etc.)"*  
Use an accumulator to combine or summarize values (sum, count, maximum, average, product, etc.). Does NOT return a collection; returns a single combined value. Use this to extract insights from data. Real-world uses: calculate total revenue, count how many users are active, find the best test score, compute an average price.

**Pattern 5: Combined Patterns**  
*Question: "How do I combine multiple operations to solve a complex problem?"*  
Chain search, filter, and aggregation to solve complex problems in a single pass or multiple passes. For example: "Find all grades above 85, then calculate their average" combines filtering + aggregation. Real-world uses: find the average salary of employees in a specific department, list all products that are both in stock AND below a price threshold, calculate the median score of passing students.

**Key insight:** Each pattern uses a loop + conditional. Mastering these five fundamentals unlocks the ability to solve 80% of real-world programming problems. When you encounter a new programming language, library, or tool, look for these patterns first—they're universal.

---

## 5) Live Demo (40 minutes total)

### Demo Phase 1: Linear Search (5 minutes)

**Say:** "Let's search for the first student with a name starting with 'A'."

```python
students = ["Alice", "Bob", "Andrew", "Carol", "Amy"]

def linear_search(lst, target):
    for item in lst:
        if item[0].lower() == target.lower():
            return item  # Return immediately when found
    return None  # Return None if not found

result = linear_search(students, "a")
print(f"Found: {result}")
```

**Run and explain:**
- The loop checks each item's first character
- When found, we `return` immediately—no unnecessary iterations
- If the loop completes without finding, we return `None`
- Linear search is O(n) but simple and reliable

**Student takeaway:** Use linear search when you need ONE item and can stop as soon as you find it.

### Demo Phase 2: Search-All (5 minutes)

**Say:** "Now find ALL students whose names start with 'A'."

```python
def search_all(lst, target):
    results = []  # Accumulator for matches
    for item in lst:
        if item[0].lower() == target.lower():
            results.append(item)  # Collect all matches
    return results

all_a_names = search_all(students, "a")
print(f"All A-names: {all_a_names}")
```

**Run and explain:**
- Key difference: we never `return` early; we iterate through the ENTIRE list
- We collect matches in a results list using `append()`
- After the loop ends, we return the complete list
- Works even if zero, one, or many matches exist

**Student takeaway:** Use search-all when you need ALL matching items, not just the first.

### Demo Phase 3: Filter (8 minutes)

**Say:** "Let's filter to keep only names with more than 4 characters."

```python
def filter_long_names(lst, min_length):
    filtered = []
    for name in lst:
        if len(name) > min_length:
            filtered.append(name)
    return filtered

long_names = filter_long_names(students, 4)
print(f"Names longer than 4 chars: {long_names}")
```

**Run and explain:**
- Filter is similar to search-all but with a different condition
- We're removing elements that don't match (keeping only matches)
- The result is a NEW list (original is unchanged)
- Filtering is safe—no side effects, no data loss

**Extend the demo:**

```python
# Example: filter sales over $100
sales = [50, 150, 30, 200, 75, 110]

def filter_high_sales(sales_list, threshold):
    high_sales = []
    for sale in sales_list:
        if sale > threshold:
            high_sales.append(sale)
    return high_sales

high = filter_high_sales(sales, 100)
print(f"Sales over $100: {high}")
```

**Student takeaway:** Filter creates a subset; use it to answer "which elements satisfy this condition?"

### Demo Phase 4: Aggregation (8 minutes)

**Say:** "Let's aggregate: what is the total revenue? Count of transactions? Average sale?"

```python
def sum_sales(sales_list):
    total = 0  # Accumulator initialized to identity (0 for sum)
    for sale in sales_list:
        total += sale  # Accumulate
    return total

total_revenue = sum_sales(sales)
print(f"Total revenue: ${total_revenue}")

def count_sales(sales_list):
    count = 0  # Accumulator initialized to 0
    for sale in sales_list:
        count += 1  # Or use len() after the loop
    return count

num_transactions = count_sales(sales)
print(f"Number of transactions: {num_transactions}")

def average_sale(sales_list):
    if not sales_list:
        return 0
    total = sum_sales(sales_list)
    return total / len(sales_list)

avg = average_sale(sales)
print(f"Average sale: ${avg:.2f}")
```

**Run and explain:**
- Aggregation REQUIRES an accumulator (initialized before the loop)
- Common accumulators: sum (start at 0), count (start at 0), max (start at first item), min (start at first item)
- The accumulator is UPDATED inside the loop
- The loop does not collect items; it combines them into a single value

**Student takeaway:** Use aggregation to answer "What is the total/average/max/count?"

### Demo Phase 5: Combined Patterns (8 minutes)

**Say:** "Now let's combine: find the average of ONLY the high-value sales."

```python
def avg_high_sales(sales_list, threshold):
    high_sales = []
    # Step 1: Filter
    for sale in sales_list:
        if sale > threshold:
            high_sales.append(sale)
    
    # Step 2: Aggregate
    if not high_sales:
        return 0
    total = sum(high_sales)
    return total / len(high_sales)

avg_high = avg_high_sales(sales, 100)
print(f"Average of sales over $100: ${avg_high:.2f}")
```

**Alternative (single pass):**

```python
def avg_high_sales_onepass(sales_list, threshold):
    high_total = 0
    high_count = 0
    for sale in sales_list:
        if sale > threshold:
            high_total += sale
            high_count += 1
    
    if high_count == 0:
        return 0
    return high_total / high_count

avg_high_v2 = avg_high_sales_onepass(sales, 100)
print(f"Average (single pass): ${avg_high_v2:.2f}")
```

**Explain both approaches:**
- Two-pass: clear, easy to understand, slightly less efficient
- One-pass: uses two accumulators, more efficient on large datasets
- Both are correct; choose clarity first, optimize later

**Student takeaway:** Combine patterns by filtering first, then aggregating—or do both in one pass with conditional accumulation.

### Demo Phase 6: Lab Preview (6 minutes)

**Say:** "In the lab, you'll apply all five patterns to a real dataset of student grades. You'll search for a specific student, find all students above a threshold, filter the grades, calculate the class average, and combine everything to answer: 'Who qualifies for the honor roll?'"

---

## 6) Practice Walkthrough

**Guided mini-exercise (5 minutes):**

```python
# Sample data:
grades = [85, 92, 78, 88, 95, 70, 91]

# Find the highest grade (aggregation with max)
highest = grades[0]
for grade in grades:
    if grade > highest:
        highest = grade
print(f"Highest grade: {highest}")

# Find all grades above 85 (filter)
good_grades = []
for grade in grades:
    if grade >= 85:
        good_grades.append(grade)
print(f"Grades >= 85: {good_grades}")

# Count how many students passed (count >= 70, aggregation)
pass_count = 0
for grade in grades:
    if grade >= 70:
        pass_count += 1
print(f"Students who passed: {pass_count}")
```

**Check for understanding:** Ask students to identify which pattern each code segment uses. Debrief any confusion.

---

## 7) Lab with Full Checkpoints (~30 minutes)

**Checkpoint 1: Linear Search (~ 4 minutes)**
Write a function `find_student(roster, target_name)` that searches a list of student names and returns the first match or "Not found".

```python
def find_student(roster, target_name):
    for name in roster:
        if name.lower() == target_name.lower():
            return name
    return "Not found"

roster = ["Alice", "Bob", "Carol", "Dave", "Eve"]
print(find_student(roster, "carol"))
```

**Checkpoint 2: Search-All (~ 4 minutes)**
Write `find_all_by_grade(students_grades_dict, min_grade)` that returns a list of all students with grades >= min_grade.

```python
def find_all_by_grade(students, min_grade):
    matching = []
    for student, grade in students.items():
        if grade >= min_grade:
            matching.append(student)
    return matching

students = {"Alice": 92, "Bob": 78, "Carol": 85, "Dave": 88}
print(find_all_by_grade(students, 85))
```

**Checkpoint 3: Filter (~ 4 minutes)**
Write `filter_positive(numbers)` that returns a new list containing only positive numbers.

```python
def filter_positive(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives

data = [5, -3, 8, -1, 0, 12]
print(filter_positive(data))
```

**Checkpoint 4: Count Aggregation (~ 4 minutes)**
Write `count_high_grades(grades, threshold)` that returns the number of grades above threshold.

```python
def count_high_grades(grades, threshold):
    count = 0
    for grade in grades:
        if grade > threshold:
            count += 1
    return count

grades = [85, 92, 78, 88, 95, 70, 91]
print(count_high_grades(grades, 85))
```

**Checkpoint 5: Sum Aggregation (~ 4 minutes)**
Write `sum_high_sales(sales, threshold)` that returns the total revenue from sales above threshold.

```python
def sum_high_sales(sales, threshold):
    total = 0
    for sale in sales:
        if sale >= threshold:
            total += sale
    return total

sales = [50, 150, 30, 200, 75, 110]
print(sum_high_sales(sales, 100))
```

**Checkpoint 6: Average Aggregation (~ 4 minutes)**
Write `average_grade(grades)` that calculates the mean of all grades.

```python
def average_grade(grades):
    if not grades:
        return 0
    total = sum(grades)
    return total / len(grades)

grades = [85, 92, 78, 88, 95]
print(f"Average: {average_grade(grades):.2f}")
```

**Checkpoint 7: Combined Pattern (~ 6 minutes)**
Write `honor_roll_average(students, threshold)` that returns the average grade of only students above the threshold. Students is a dictionary: `{"name": grade}`.

```python
def honor_roll_average(students, threshold):
    high_grades = []
    for name, grade in students.items():
        if grade >= threshold:
            high_grades.append(grade)
    
    if not high_grades:
        return 0
    return sum(high_grades) / len(high_grades)

students = {"Alice": 92, "Bob": 78, "Carol": 85, "Dave": 88, "Eve": 95}
print(f"Honor roll average (>= 85): {honor_roll_average(students, 85):.2f}")
```

**Instructor circulation focus:**
- Checkpoint 1–3: Ensure students understand when to use `return` (search) vs. `append` (filter/search-all)
- Checkpoint 4–6: Check that accumulators are initialized BEFORE the loop and updated inside
- Checkpoint 7: Monitor for correct combining of filter logic + aggregation

---

## 8) Troubleshooting Pitfalls

**Pitfall 1: Initializing accumulator inside the loop**  
Wrong: `total = 0; for x in lst: total = 0; total += x`  
Right: `total = 0; for x in lst: total += x`  
**Fix:** Initialize accumulators BEFORE entering any loop.

**Pitfall 2: Returning early in search-all**  
Wrong: `for x in lst: if condition: return x` (returns first match, not all)  
Right: `results = []; for x in lst: if condition: results.append(x); return results`  
**Fix:** Use `append` to collect, then return the full list after the loop.

**Pitfall 3: Modifying original list when you mean to filter**  
Wrong: `for x in lst: if not condition: lst.remove(x)` (modifies while iterating—unstable)  
Right: `filtered = [x for x in lst if condition]` or build a new list with append  
**Fix:** Build a NEW list with `append`; don't modify during iteration.

**Pitfall 4: Forgetting the condition in aggregation**  
Wrong: `total = 0; for x in lst: total += x` (sums ALL, not filtered)  
Right: `total = 0; for x in lst: if condition: total += x`  
**Fix:** Add the `if condition:` check before updating the accumulator.

**Pitfall 5: Not handling empty lists in division**  
Wrong: `total / len(lst)` (crashes if len(lst) == 0)  
Right: `if len(lst) == 0: return 0; else: return total / len(lst)`  
**Fix:** Check for empty before dividing to avoid `ZeroDivisionError`.

**Pitfall 6: Case sensitivity in search/filter**  
Wrong: `if name == "Alice"` (fails if user enters "alice" or "ALICE")  
Right: `if name.lower() == "alice"`  
**Fix:** Normalize strings with `.lower()` or `.upper()` before comparing.

---

## 9) Quick-Check Questions

**Q1:** What is the key difference between linear search and search-all?  
**A1:** Linear search returns on the first match (using `return`); search-all collects all matches in a list (using `append` and returning after the loop).

**Q2:** When would you use filter instead of search-all?  
**A2:** Filter and search-all are very similar. Use "filter" conceptually when you want to remove non-matching elements (create a subset). Use "search-all" when finding all items meeting a condition. They're often the same code pattern.

**Q3:** Why must an accumulator be initialized BEFORE the loop?  
**A3:** The loop updates the accumulator. If initialized inside, it resets on every iteration, losing the previous value.

**Q4:** What happens if you don't check for empty lists before dividing in an average calculation?  
**A4:** You get a `ZeroDivisionError` crash. Always check `if len(lst) > 0` or `if lst:` before dividing.

**Q5:** How do you combine filter and aggregation?  
**A5:** Two approaches: (1) Filter to a new list, then aggregate that list, or (2) Aggregate with a conditional inside the loop.

**Q6:** What does `.lower()` do and why is it useful in search?  
**A6:** `.lower()` converts a string to lowercase. It's useful in search to make comparisons case-insensitive so "Alice", "alice", and "ALICE" all match.

**Q7:** Can you search while also aggregating in the same loop?  
**A7:** Yes! Use an `if condition:` to filter which items to aggregate, while keeping the accumulator active for all loop iterations.

---

## 10) Wrap-Up Narrative

> **Say:** "Today you learned five patterns that professional programmers use constantly. Search finds items. Search-all collects all matches. Filter creates subsets. Aggregation combines values. And combined patterns solve real-world problems. These patterns form the backbone of data processing. In your next jobs, interviews, and projects, you'll recognize these patterns everywhere—in databases, in APIs, in analytics. Master these five, and you unlock 80% of practical programming."

---

## 11) Facilitation Notes

**Pacing strategy:**
- Demo: 40 min total (6 phases, strictly timed). If students ask questions DURING a demo, pause the timer and answer, then resume.
- Lab: 30 min (7 checkpoints, ~4 min each; Checkpoint 7 is 6 min). Circulate constantly. Stop anyone stuck for more than 2 minutes and prompt with leading questions.
- Q&A / Wrap: 10 min. Use this time to review common mistakes and celebrate successes.

**Preparation during lab:**
- Checkpoint 1–3: Students should move quickly. If you see someone stuck, ask: "What pattern are we using here?" and "Where should we put the return statement?"
- Checkpoint 4–6: Accumulators are the sticking point. Watch for students initializing inside the loop. Common fix: "Where did you put `count = 0`? Should it be inside or outside the loop?"
- Checkpoint 7: The integration point. Some students will write it in two passes; others in one. Both are correct. Ask them to explain their approach.

**Differentiation strategies:**

**For advanced students:** After Checkpoint 7, challenge them:
1. "Write a two-pass version of honor-roll-average (first pass: filter; second pass: aggregate) and compare it to the one-pass version. Which is more efficient? Why?"
2. "Modify Checkpoint 7 to also return the COUNT of honor-roll students, not just the average. What accumulator would you add?"
3. "If the students dictionary had 1 million entries, which approach (one-pass or two-pass) would you choose and why?"

**For struggling students:** Provide a structured template:
```python
def template_pattern(data, condition):
    result = []  # or: accumulator = 0
    for item in data:
        if condition:  # Check condition here
            result.append(item)  # or: accumulator += item
    return result  # or: return accumulator
```
Have them fill in the blanks for each checkpoint. Emphasize: "Three lines are always the same: create container, loop, check condition. Only the action inside `if` changes."

**Common questions to anticipate and answer:**
- "Can I use `sum()` instead of a loop?" → Yes, for sum; also `max()`, `min()`, `len()`. But learn loops first; they're the foundation. Built-in functions are optimized for after you understand the pattern.
- "Is this what pandas does?" → Yes, very similar operations! Pandas is faster on huge datasets (100k+ rows) because it's written in C, but pandas DataFrames use these exact patterns under the hood.
- "Do I always need a new list for filter?" → Best practice: yes, use a new list. Modifying the original while iterating can cause bugs (items get skipped or duplicated). New lists are safer.
- "What if I want to search for the maximum instead of a first match?" → That's aggregation, not search! Use an accumulator: `max_val = data[0]; for item in data: if item > max_val: max_val = item`

**Instructor mindset:** These patterns are deceptively simple but profoundly important. Students who internalize them move from "Can I write a loop?" to "What should I do with a loop?" This is the threshold moment where programming becomes a skill rather than a syntax exercise. Invest time here—it pays dividends in every future module and project.

---

## 12) Assessment and Differentiation Rubric

| Criterion | Proficient | Developing | Needs Support |
|-----------|-----------|-----------|-----------|
| **Linear Search** | Correctly returns first match or "not found"; uses early `return` | Finds first match but doesn't return cleanly | Doesn't return early; loops unnecessarily |
| **Search-All** | Collects all matches in list; returns after loop completes | Collects most matches but misses edge cases | Returns early; only finds first item |
| **Filter** | Creates new list with matching items; original unchanged | Filters correctly but modifies original | Doesn't build new list; loses data |
| **Aggregation** | Initializes accumulator before loop; updates inside; handles empty list | Initializes correctly but forgets empty check | Initializes inside loop; loses values |
| **Combined** | Filters correctly, then aggregates; handles all edge cases | Combines patterns but misses one edge case (e.g., division by zero) | Doesn't combine; solves only one pattern |
| **Code Quality** | Clear variable names; comments on key lines; deterministic | Functional but sparse comments; unclear names | Hard to follow; no comments; hard-coded values |

**Exit criteria:** Students should demonstrate proficiency in at least Checkpoints 1–5 and partial proficiency in 6–7 before moving to Hour 4.