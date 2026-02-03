# Day 2, Hour 2: String Formatting with F-Strings
**Python Programming Basics – Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Hour 9: 3 minutes
- Introduction to F-Strings: 10-12 minutes
- Formatting Numbers (Decimals, Width, Alignment): 8-10 minutes
- Why F-Strings Beat Concatenation: 3-5 minutes
- Live Demo (Tip Calculator Upgrade): 5-10 minutes
- Hands-On Lab (Upgrade Tip Calculator): 25-35 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Use f-strings to create formatted string output with variables
2. Format floating-point numbers to a fixed number of decimal places
3. Apply width and alignment specifiers for columnar output
4. Explain why f-strings are more readable than string concatenation
5. Upgrade existing code to use f-string formatting
6. Create professional-looking program output with consistent formatting

---

## Section 1: Recap & Transition from Hour 9 (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome back! In Hour 9, we learned how to make decisions using comparison operators and boolean logic. You built an eligibility checker that combined multiple conditions with `and` and `or`.

Quick check: **Who successfully got their eligibility checker working with all the boundary values correct?**

[Wait for responses]

Great! Those comparison skills are going to show up in almost every program you write from now on.

### The Output Problem

**[Instructor speaks:]**

Now, let me show you something. Here's output from a typical beginner program:

```python
bill = 87.5
tip_percent = 18
tip = bill * tip_percent / 100
total = bill + tip

print("Bill: $" + str(bill))
print("Tip (" + str(tip_percent) + "%): $" + str(tip))
print("Total: $" + str(total))
```

**Output:**
```
Bill: $87.5
Tip (18%): $15.75
Total: $103.25
```

This works, but look at the code. It's **clunky**:
- We have to convert numbers to strings manually with `str()`
- We have to remember where to put spaces and punctuation
- It's hard to read and easy to make mistakes
- The dollar amounts aren't consistently formatted (87.5 vs 15.75)

**There's a better way.** It's called **f-strings** (formatted string literals), and it's going to make your output beautiful and your code readable.

Let's learn it!

---

## Section 2: Introduction to F-Strings (10-12 minutes)

### What Is an F-String?

**[Instructor speaks:]**

An **f-string** is a string literal that lets you **embed expressions directly inside** the string using curly braces `{}`. 

Here's the basic syntax:

```python
name = "Alice"
age = 25

# Old way (concatenation)
print("My name is " + name + " and I am " + str(age) + " years old")

# New way (f-string)
print(f"My name is {name} and I am {age} years old")
```

**Both produce the same output:**
```
My name is Alice and I am 25 years old
```

**Notice the `f` before the quote?** That tells Python: "This is an f-string. Evaluate anything inside `{}`."

### Why F-Strings Are Better

**[Instructor speaks:]**

Let's break down the advantages:

1. **No manual type conversion needed**
   ```python
   age = 25
   
   # Old way - must convert to string
   print("Age: " + str(age))
   
   # F-string - Python handles it
   print(f"Age: {age}")
   ```

2. **Variables go right where they belong in the sentence**
   ```python
   name = "Bob"
   score = 95
   
   # Old way - hard to see the final sentence structure
   print(name + " scored " + str(score) + " points")
   
   # F-string - reads like the output
   print(f"{name} scored {score} points")
   ```

3. **You can put expressions inside the curly braces**
   ```python
   width = 10
   height = 5
   
   # Calculate inside the f-string!
   print(f"The area is {width * height} square meters")
   ```
   
   **Output:**
   ```
   The area is 50 square meters
   ```

### F-String Basics: The Anatomy

**[Instructor speaks:]**

Let's look at the parts of an f-string:

```python
name = "Charlie"
age = 30

message = f"Hello, {name}! You are {age} years old."
```

Breaking it down:
- **`f`** before the opening quote: marks this as an f-string
- **`"Hello, ..."`**: regular string content
- **`{name}`**: placeholder that gets replaced with the value of `name`
- **`{age}`**: placeholder that gets replaced with the value of `age`

**The curly braces are signals:** "Insert this variable's value here."

### Quick Check #1

**[Instructor asks:]**

What will this code print?

```python
city = "New York"
temperature = 72

print(f"The temperature in {city} is {temperature}°F")
```

[Pause for student predictions]

**Answer:**
```
The temperature in New York is 72°F
```

The variables `city` and `temperature` get inserted exactly where they appear in the curly braces.

### Using Expressions in F-Strings

**[Instructor speaks:]**

You're not limited to just variable names. You can put **any valid Python expression** inside the curly braces:

```python
price = 19.99
quantity = 3

print(f"Total: ${price * quantity}")
```

**Output:**
```
Total: $59.97
```

You can even call methods:

```python
name = "alice"

print(f"Hello, {name.upper()}!")
```

**Output:**
```
Hello, ALICE!
```

**[Key insight]:** Python evaluates the expression inside `{}`, converts the result to a string, and inserts it.

---

## Section 3: Formatting Numbers – Decimals, Width, Alignment (8-10 minutes)

### The Problem: Ugly Number Output

**[Instructor speaks:]**

Let's say we're working with money:

```python
price = 19.5
tax = 1.625
total = price + tax

print(f"Price: ${price}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")
```

**Output:**
```
Price: $19.5
Tax: $1.625
Total: $21.125
```

This looks unprofessional:
- Currency should always show 2 decimal places ($19.50, not $19.5)
- We can't actually charge $21.125—that's not a valid amount
- The numbers don't align nicely

**F-strings have a solution:** format specifiers.

### Format Specifier Syntax: {value:format}

**[Instructor speaks:]**

Inside the curly braces, you can add a colon `:` followed by a format specifier:

```python
{variable:format_spec}
```

The most common format specs for numbers:

**1. Fixed decimal places: `.Nf`**

```python
price = 19.5

print(f"Price: ${price:.2f}")
```

**Output:**
```
Price: $19.50
```

**Breaking down `.2f`:**
- **`.2`**: show exactly 2 digits after the decimal point
- **`f`**: format as a floating-point number

**More examples:**

```python
pi = 3.14159265

print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")
print(f"Pi to 0 decimals: {pi:.0f}")
```

**Output:**
```
Pi to 2 decimals: 3.14
Pi to 4 decimals: 3.1416
Pi to 0 decimals: 3
```

**[Important note]:** The `.2f` format rounds, it doesn't truncate:

```python
value = 1.625

print(f"{value:.2f}")    # 1.62 (rounds down)

value = 1.626
print(f"{value:.2f}")    # 1.63 (rounds up)
```

### Format Specifier: Width and Alignment

**[Instructor speaks:]**

Sometimes you want to create columnar output—like a receipt where the dollar amounts line up on the right.

**Width specifier: `N` (where N is the total width)**

```python
print(f"{"Item":<20} {"Price":>10}")
print(f"{"Coffee":<20} {"$3.50":>10}")
print(f"{"Sandwich":<20} {"$8.75":>10}")
```

**Output:**
```
Item                      Price
Coffee                    $3.50
Sandwich                  $8.75
```

**Breaking down the format spec:**
- **`<`**: left-align
- **`>`**: right-align
- **`^`**: center-align
- **Number**: total width in characters

**Combined with decimal formatting:**

```python
item = "Latte"
price = 4.5

print(f"{item:<15} ${price:>6.2f}")
```

**Output:**
```
Latte           $  4.50
```

**Breaking this down:**
- **`{item:<15}`**: left-align `item` in a 15-character field
- **`{price:>6.2f}`**: right-align `price` in a 6-character field, with 2 decimal places

### Quick Check #2

**[Instructor asks:]**

What will this code print?

```python
name = "Alice"
score = 87.6789

print(f"{name} scored {score:.1f} points")
```

[Pause for student predictions]

**Answer:**
```
Alice scored 87.7 points
```

The format spec `.1f` rounds the score to 1 decimal place.

### Common Format Specifiers Reference

**[Instructor speaks:]**

Here's a quick reference you'll want to bookmark:

```python
value = 1234.5678

# Fixed decimals
print(f"{value:.2f}")        # 1234.57

# Width and alignment
print(f"{value:>10.2f}")     # "   1234.57" (right-aligned, 10 chars wide)
print(f"{value:<10.2f}")     # "1234.57   " (left-aligned)

# Thousands separator
print(f"{value:,.2f}")       # 1,234.57

# Percentage
percentage = 0.875
print(f"{percentage:.1%}")   # 87.5%
```

**For now, focus on `.2f` for money.** That's the one you'll use most often.

---

## Section 4: Why F-Strings Beat Concatenation (3-5 minutes)

### The Concatenation Mess

**[Instructor speaks:]**

Let me show you the same output three different ways:

**Method 1: Concatenation (the old way)**

```python
name = "Alice"
age = 25
balance = 1234.56

print("Customer: " + name + ", Age: " + str(age) + ", Balance: $" + str(balance))
```

**Problems:**
- You have to call `str()` on every non-string
- Hard to see where spaces and punctuation go
- Easy to make mistakes

**Method 2: str.format() (also old)**

```python
print("Customer: {}, Age: {}, Balance: ${}".format(name, age, balance))
```

**Better, but:**
- Variables are separated from where they appear
- Still hard to read for complex strings

**Method 3: F-strings (the modern way)**

```python
print(f"Customer: {name}, Age: {age}, Balance: ${balance:.2f}")
```

**Advantages:**
- Variables are right where they belong
- No manual type conversion
- Format specifiers inline
- Reads like the output you'll see

**[Key teaching moment]:** F-strings were added in Python 3.6 (2016) because developers were so tired of concatenation and `.format()`. This is now the **preferred way** to format strings in Python.

### When NOT to Use F-Strings

**[Instructor speaks:]**

F-strings are great, but there are times to avoid them:

1. **When the string is used multiple times with different values:**
   ```python
   # Use str.format() for templates
   template = "Hello, {name}! Your score is {score}."
   print(template.format(name="Alice", score=95))
   print(template.format(name="Bob", score=87))
   ```

2. **When you're building strings from user input that might contain `{}`:**
   ```python
   # User input might break the f-string
   user_message = input("Enter a message: ")  # User types: "My code: {name}"
   # print(f"{user_message}")  # This might cause errors
   ```

**For this course, use f-strings for output. They're simpler and more readable.**

---

## Section 5: Live Demo – Tip Calculator Upgrade (5-10 minutes)

### Demo Script: Making Output Professional

**[Instructor speaks:]**

Remember the Tip Calculator from yesterday? Let's take it and upgrade the output using f-strings.

**[Open editor and create `tip_calculator_formatted.py`]**

**[Instructor types and speaks:]**

```python
# tip_calculator_formatted.py
# Purpose: Calculate tip and total, with professional formatting

print("=== Tip Calculator ===\n")

# Get user input
bill_input = input("Enter the bill amount: $")
tip_percent_input = input("Enter tip percentage (e.g., 18): ")

# Convert to numbers
bill = float(bill_input)
tip_percent = float(tip_percent_input)

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

# Display results with formatting
print("\n--- Receipt ---")
print(f"Bill:        ${bill:.2f}")
print(f"Tip ({tip_percent:.0f}%):   ${tip_amount:.2f}")
print(f"-" * 25)
print(f"Total:       ${total:.2f}")
print("\nThank you!")
```

**[Run the program]**

```
=== Tip Calculator ===

Enter the bill amount: $87.50
Enter tip percentage (e.g., 18): 20

--- Receipt ---
Bill:        $87.50
Tip (20%):   $17.50
-------------------------
Total:       $105.00

Thank you!
```

**[Instructor explains the formatting:]**

Let's look at what makes this output professional:

1. **Line 19:** `${bill:.2f}` ensures bill always shows 2 decimals
2. **Line 20:** `{tip_percent:.0f}` shows percentage without decimals (20, not 20.0)
3. **Line 20:** `${tip_amount:.2f}` formats tip amount as currency
4. **Line 22:** `${total:.2f}` formats total consistently
5. **Line 21:** `"-" * 25` creates a separator line (not f-string related, but nice!)

**Notice how readable the code is?** You can see exactly what the output will look like just by reading the f-strings.

### Adding Alignment

**[Instructor speaks:]**

Now let's make it even better with alignment:

```python
# Display results with better alignment
print("\n--- Receipt ---")
print(f"{'Bill:':<15} ${bill:>8.2f}")
print(f"{'Tip (' + str(int(tip_percent)) + '%):':<15} ${tip_amount:>8.2f}")
print("-" * 26)
print(f"{'Total:':<15} ${total:>8.2f}")
print("\nThank you!")
```

**Output:**
```
--- Receipt ---
Bill:           $   87.50
Tip (20%):      $   17.50
--------------------------
Total:          $  105.00

Thank you!
```

**[Key points]:**
- **`:<15`**: left-align labels in a 15-character field
- **`:>8.2f`**: right-align dollar amounts in an 8-character field with 2 decimals
- The dollar amounts now line up beautifully

**[Instructor speaks:]**

The aligned version is more complex, so **don't worry if you don't use alignment in your lab today**. Just getting comfortable with `.2f` for money is the main goal.

---

## Section 6: Hands-On Lab – Upgrade Tip Calculator (25-35 minutes)

### Lab Overview

**[Instructor speaks:]**

Now it's your turn! You're going to take the Tip Calculator and upgrade it with f-string formatting.

**Lab Goal:** Rewrite output using f-strings with proper decimal formatting.

### Lab Instructions: Upgrade Tip Calculator

**Scenario:** You have a working Tip Calculator, but the output looks unprofessional. Your job is to format it beautifully using f-strings.

**Requirements:**

Create a Python script called `tip_calculator_pro.py` that:

1. **Prompts the user for:**
   - Bill amount (as a float)
   - Tip percentage (as a float)

2. **Calculates:**
   - Tip amount (bill × tip percentage / 100)
   - Total amount (bill + tip)

3. **Displays a formatted receipt with:**
   - All dollar amounts showing exactly 2 decimal places
   - Clear labels for each line
   - A separator line between the calculations and the total
   - A thank you message

4. **Uses f-strings exclusively** (no string concatenation with `+`)

### Starter Template

```python
# tip_calculator_pro.py
# Purpose: Calculate tip with professional formatting

print("=== Professional Tip Calculator ===\n")

# Get user input
bill_input = input("Enter the bill amount: $")
tip_percent_input = input("Enter tip percentage (e.g., 15, 18, 20): ")

# Convert to numbers
bill = float(bill_input)
tip_percent = float(tip_percent_input)

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

# TODO: Display formatted receipt using f-strings
print("\n--- Your Receipt ---")

# Your formatted output goes here
```

### Example Output

**Test Case 1:**
```
=== Professional Tip Calculator ===

Enter the bill amount: $45.50
Enter tip percentage (e.g., 15, 18, 20): 18

--- Your Receipt ---
Bill:        $45.50
Tip (18%):   $8.19
-------------------------
Total:       $53.69

Thank you for dining with us!
```

**Test Case 2:**
```
=== Professional Tip Calculator ===

Enter the bill amount: $123
Enter tip percentage (e.g., 15, 18, 20): 20

--- Your Receipt ---
Bill:        $123.00
Tip (20%):   $24.60
-------------------------
Total:       $147.60

Thank you for dining with us!
```

**Notice:**
- Even though the input was `123` (no decimals), the output shows `$123.00`
- All dollar amounts consistently show 2 decimal places
- The percentage in the tip line matches what the user entered

### Completion Criteria

Your solution must:
- ✅ Use f-strings for all output (no `+` concatenation)
- ✅ Format all dollar amounts with exactly 2 decimal places using `.2f`
- ✅ Display the tip percentage in the output
- ✅ Include a separator line (e.g., dashes)
- ✅ Run without errors
- ✅ Handle both integer and decimal inputs correctly

### Common Pitfalls to Watch For

**[Instructor speaks:]**

As you work, watch out for these common mistakes:

1. **Forgetting the `f` before the string:**
   ```python
   # WRONG - This is just a regular string
   print("Total: {total:.2f}")
   
   # RIGHT - The f makes it work
   print(f"Total: {total:.2f}")
   ```

2. **Using concatenation inside f-strings unnecessarily:**
   ```python
   # AWKWARD - mixing styles
   print(f"Bill: $" + str(bill))
   
   # BETTER - pure f-string
   print(f"Bill: ${bill:.2f}")
   ```

3. **Wrong format specifier:**
   ```python
   # WRONG - .2 without the f
   print(f"${total:.2}")     # This won't work
   
   # RIGHT
   print(f"${total:.2f}")
   ```

4. **Forgetting curly braces:**
   ```python
   # WRONG - variable name appears literally
   print(f"Total: $total")
   
   # RIGHT
   print(f"Total: ${total}")
   ```

### Optional Extensions

If you finish early, try these:

1. **Split Bill Calculator:** Add a third input asking how many people are splitting the bill, then show the per-person amount

2. **Alignment:** Use width and alignment specifiers to make labels and amounts line up in columns

3. **Multiple Tip Options:** Calculate and display three different tip amounts (15%, 18%, 20%) so the user can choose

**Example of Optional Extension #3:**

```
--- Tip Options ---
15%:  $45.50 + $6.83 = $52.33
18%:  $45.50 + $8.19 = $53.69
20%:  $45.50 + $9.10 = $54.60
```

**[Instructor speaks:]**

Alright, you have 25-35 minutes. Remember:
- The key pattern is `{variable:.2f}` for money
- Test with different amounts to verify your formatting works
- Read error messages—they'll tell you if you forgot the `f` or have a syntax error

Let's make some beautiful output!

---

## Section 7: Debrief & Exit Ticket (5 minutes)

### Solution Walkthrough

**[Instructor shares solution:]**

```python
# tip_calculator_pro.py
# Purpose: Calculate tip with professional formatting

print("=== Professional Tip Calculator ===\n")

# Get user input
bill_input = input("Enter the bill amount: $")
tip_percent_input = input("Enter tip percentage (e.g., 15, 18, 20): ")

# Convert to numbers
bill = float(bill_input)
tip_percent = float(tip_percent_input)

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

# Display formatted receipt
print("\n--- Your Receipt ---")
print(f"Bill:        ${bill:.2f}")
print(f"Tip ({tip_percent:.0f}%):   ${tip_amount:.2f}")
print("-" * 25)
print(f"Total:       ${total:.2f}")
print("\nThank you for dining with us!")
```

**[Key points to highlight:]**

1. **Line 19:** `.2f` ensures the bill always displays as currency
2. **Line 20:** `.0f` shows tip_percent as a whole number (18, not 18.0)
3. **Line 20:** `.2f` formats the tip amount with 2 decimals
4. **Line 22:** `.2f` formats the total consistently
5. **No `str()` conversions needed**—f-strings handle it automatically

### Common Issues Students Encountered

**[Instructor speaks:]**

Let me address a few things I saw as I walked around:

[Adjust based on actual student work, but common issues include:]

1. **Forgetting the leading `f`:** Most common mistake—the string needs that `f` prefix
2. **Using `.2` instead of `.2f`:** You need the `f` at the end for floating-point format
3. **Mixing concatenation and f-strings:** Pick one style and stick with it—f-strings are cleaner

### Extensions Showcase

**[Instructor speaks:]**

If anyone completed the extensions, let's see what you built!

[Call on 1-2 students who finished extensions to share their screen briefly]

Great creativity! The split-bill calculator is especially practical.

### Exit Ticket

**[Instructor asks:]**

Before we wrap up Hour 10, answer this in your notes or in the chat:

**Question:** Why is f-string formatting usually better than `+` concatenation for building output strings?

**Expected answer:** F-strings are more readable (variables go where they appear in output), don't require manual `str()` conversions, allow inline formatting (like `.2f`), and are less error-prone.

---

## Recap: What We Accomplished

In this hour, you:
✅ Learned f-string syntax with the `f""` prefix and `{}` placeholders  
✅ Used `.2f` format specifier to display numbers with 2 decimal places  
✅ Applied f-strings to make program output clean and professional  
✅ Understood why f-strings are better than concatenation  
✅ Upgraded the Tip Calculator with proper currency formatting  
✅ Explored width and alignment specifiers (optional)  

**This is a game-changer for your code.** From now on, every program you write can have clean, professional output. No more messy concatenation with `+` and `str()` everywhere.

In Hour 11, we'll learn how to work with text data—splitting sentences into words and joining words back together.

**Great work! Take a quick 5-minute break.**

---

## Quick Reference Card (for students)

**F-String Basics:**
```python
# Basic syntax
name = "Alice"
print(f"Hello, {name}!")

# With expressions
width = 5
height = 3
print(f"Area: {width * height}")
```

**Number Formatting:**
```python
price = 19.5

# Fixed decimals (most common for money)
print(f"${price:.2f}")          # $19.50

# Different decimal places
print(f"{pi:.4f}")              # 3.1416

# No decimals
print(f"{age:.0f}")             # 25
```

**Alignment (Optional):**
```python
# Left, right, center
print(f"{'Left':<10}")          # 'Left      '
print(f"{'Right':>10}")         # '     Right'
print(f"{'Center':^10}")        # '  Center  '

# Combined with decimals
print(f"${price:>8.2f}")        # '   19.50'
```

**Common Format Specifiers:**
- `.2f` — 2 decimal places (money)
- `.0f` — no decimal places (whole numbers)
- `:>10` — right-align in 10-character field
- `:<10` — left-align in 10-character field
- `:,` — thousands separator (1,234.56)

**Remember:**
- Put `f` before the opening quote: `f"text {var}"`
- Variables go in curly braces: `{variable}`
- Format with colon: `{variable:.2f}`
- No `str()` conversion needed!

---

**End of Hour 10 Script**
