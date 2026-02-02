# Day 1, Hour 4: Numbers and Operators
## Python Programming (Basics) – Lecture Script

**Course:** Python Programming (Basics) – 48 Hours  
**Session:** Day 1 (Session 1)  
**Hour:** 4 of 4  
**Duration:** 60 minutes (instructional time)  
**Topic:** Numbers and Arithmetic Operators  

---

## Learning Outcomes

By the end of this hour, learners will be able to:
- Use Python's arithmetic operators (+, -, *, /, //, %, **)
- Apply order of operations (PEMDAS) in expressions
- Explain the difference between integer division (//) and float division (/)
- Use the modulo operator (%) for practical tasks like even/odd checks
- Convert user input to numeric types for calculations
- Use round() appropriately for display formatting
- Build a practical calculator program from scratch

---

## Hour Overview and Timing

| Segment | Duration | Activity |
|---------|----------|----------|
| Recap & Hook | 5 min | Review Hours 1-3, preview Hour 4 |
| Instruction | 10-15 min | Operators, precedence, int vs float |
| Live Demo | 5-10 min | Mini calculator walkthrough |
| Hands-On Lab | 25-35 min | Tip Calculator project |
| Debrief & Wrap | 5-10 min | Solutions share, Day 1 celebration |

**Break reminder:** If you haven't taken your mid-session break yet, consider offering a 3-5 minute micro-break before the lab.

---

## Part 1: Recap and Context (5 minutes)

### Opening (Welcome Back)

**[Speaking cue: Enthusiastic, acknowledging progress]**

"Alright everyone, welcome to Hour 4—the final hour of Day 1! Let's take just a moment to appreciate how far we've come today. If this is your first time programming in Python—or your first time programming at all—you should feel really good about what you've accomplished."

**[Pause briefly for effect]**

"In Hour 1, we got our environment set up, learned how to save files, run scripts, and navigate the LogicalLabs workspace. That's not trivial—many people struggle with just getting Python running."

"In Hour 2, we learned how to use `print()`, write comments, and most importantly, how to **read error messages**. That skill alone will save you hours of frustration as you continue learning."

"In Hour 3, we learned about variables and data types—strings, numbers, booleans—and we used the `type()` function to peek inside our data. We learned that `'5'` and `5` are very different things in Python."

**[Transition tone: Building momentum]**

"Now in Hour 4, we're going to put numbers to work. We're going to do **math**—but not math class math. This is **practical math**: the kind you need to split a restaurant bill, calculate a tip, figure out per-person costs, or build any program that deals with money, measurements, or counts."

### Quick Recap Question (Interactive)

**[Instructor cue: Ask for a volunteer or call on someone]**

"Before we dive in, let's do a quick check. Who can remind us: what's the difference between `'5'` and `5`?"

**[Expected answer:]**
- `'5'` is a string (text)—you can't do math with it directly
- `5` is an integer (a number)—you can add, subtract, multiply it

**[If no one answers, provide it yourself with energy]**

"Right! `'5'` is a string—it's text, it has quotes around it. Python treats it like the letter 'A' or the word 'hello'. You can't add it to another number. But `5` is an **integer**—an actual number—and Python knows how to do math with it."

**[Transition: Set the stage]**

"That distinction is going to be **super important** in about 30 minutes when you build your first calculator program. Let's get started!"

---

## Part 2: Instruction – Numbers and Operators (10-15 minutes)

### The Seven Arithmetic Operators

**[Speaking cue: Clear, methodical delivery]**

"Python gives us seven main arithmetic operators. You already know most of them from regular math, but a couple might be new. I'm going to walk through all seven, and then we'll see them in action."

**[Write on screen or show slide—speak as you display each operator]**

#### **1. Addition: `+`**

"First up: **addition**. The plus sign does exactly what you'd expect."

```python
result = 10 + 5
print(result)  # Output: 15
```

"Ten plus five equals fifteen. No surprises here."

---

#### **2. Subtraction: `-`**

"Next: **subtraction**. The minus sign."

```python
result = 10 - 5
print(result)  # Output: 5
```

"Ten minus five equals five. Still straightforward."

---

#### **3. Multiplication: `*`**

"Now **multiplication**. In Python, we use the **asterisk** or star symbol."

```python
result = 10 * 5
print(result)  # Output: 50
```

"Ten times five equals fifty. Notice we use `*`, not the × symbol you might see in a math textbook. That's because × isn't on your keyboard, and computers prefer symbols we can actually type."

---

#### **4. Division: `/`**

"Okay, here's where things get interesting. **Division** uses a single forward slash."

```python
result = 10 / 5
print(result)  # Output: 2.0
```

**[Pause—this is important]**

"Notice the result: `2.0`, not `2`. Even though 10 divided by 5 equals exactly 2, Python gives us `2.0`—a **float**, which is a decimal number."

**[Emphasize this point]**

"This is by design. In Python 3, the `/` operator **always** gives you a float, even when the division is exact. That's actually helpful because it means you never lose precision by accident."

**[Give another example]**

```python
result = 10 / 3
print(result)  # Output: 3.3333333333333335
```

"Ten divided by three gives us a long decimal. Python keeps many digits of precision. In a few minutes, we'll talk about how to round this for display."

---

#### **5. Integer Division (Floor Division): `//`**

**[Speaking cue: Slow down—this is a common confusion point]**

"Now here's operator number five, and this one trips people up: **integer division**, also called **floor division**. It uses **two forward slashes**."

```python
result = 10 // 3
print(result)  # Output: 3
```

"Notice: the result is `3`, not `3.333...`. The `//` operator **throws away the decimal part** and gives you just the whole number."

**[Make this concrete with a real-world analogy]**

"Think about it like this: If you have 10 cookies and 3 people, how many **whole cookies** does each person get? Three. That's what `//` tells you. It doesn't round—it just cuts off everything after the decimal point. This is called 'floor division' because it rounds **down** to the nearest integer."

**[Another example]**

```python
result = 10 // 5
print(result)  # Output: 2
```

"Ten divided by five with `//` gives us `2`—an integer, not `2.0`. So when you want a whole number result and you don't care about the remainder, use `//`."

**[Check for understanding]**

"Quick prediction question: What will `7 // 2` give us?"

**[Pause for answers—expected: 3]**

"Right! Seven divided by two is 3.5, but `7 // 2` gives us **3**—it chops off the `.5`."

---

#### **6. Modulo: `%`**

**[Speaking cue: This is unfamiliar to many—go slow]**

"Operator number six is called **modulo**, and it uses the percent sign: `%`."

**[Important: Define clearly]**

"The modulo operator gives you the **remainder** after division. Not the quotient—the **remainder**."

```python
result = 10 % 3
print(result)  # Output: 1
```

**[Explain step-by-step]**

"Ten divided by three is 3 with a remainder of 1. The `%` operator gives us that remainder: `1`."

**[More examples to solidify]**

```python
print(10 % 5)  # Output: 0  (no remainder—divides evenly)
print(7 % 2)   # Output: 1  (7 ÷ 2 = 3 remainder 1)
print(8 % 2)   # Output: 0  (8 ÷ 2 = 4 remainder 0)
```

**[Real-world application—this makes it click]**

"Here's why modulo is incredibly useful: checking if a number is **even or odd**."

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

"If a number divided by 2 has a remainder of 0, it's even. If the remainder is 1, it's odd. We haven't covered `if` statements yet—that's coming in Session 7—but just know that `%` is the tool you use for this kind of check."

**[Another real-world use case]**

"You'll also see modulo used for things like: 'Every 10th customer gets a discount,' or 'Wrap around after reaching a limit,' or 'Check if a year is a leap year.' The remainder operation shows up **everywhere** in real programs."

---

#### **7. Exponentiation: `**`**

**[Final operator—quick and clear]**

"Last one: **exponentiation**, which means 'raising to a power.' Python uses **two asterisks**."

```python
result = 2 ** 3
print(result)  # Output: 8
```

"Two to the power of three equals eight. Two times two times two."

```python
result = 5 ** 2
print(result)  # Output: 25
```

"Five squared equals twenty-five."

**[Note for context]**

"You won't use this one as often in basic programs, but it's there when you need it—for area calculations, scientific formulas, or compound interest."

---

### Order of Operations (PEMDAS)

**[Speaking cue: Connect to prior knowledge]**

"Okay, now that we know all seven operators, let's talk about **order of operations**. If you've taken algebra, you might remember **PEMDAS**—Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."

**[Reassure the audience]**

"If that sounds like a flashback to math class, don't worry—we're not doing algebra here. We just need to understand how Python decides what to calculate first."

**[Show an example]**

```python
result = 10 + 5 * 2
print(result)  # Output: 20, not 30
```

**[Ask the audience to predict]**

"Quick prediction: is the result `30` or `20`?"

**[Pause for answers]**

"The answer is **20**. Here's why: Python does **multiplication before addition**. So it calculates `5 * 2` first, which gives `10`, and then adds `10 + 10` to get `20`."

**[Show what happens if you want 30]**

```python
result = (10 + 5) * 2
print(result)  # Output: 30
```

"If you want to force the addition to happen first, you use **parentheses**. Python always does what's inside parentheses first. So `(10 + 5)` becomes `15`, and then `15 * 2` gives us `30`."

**[Practical takeaway]**

"When in doubt, **use parentheses**. They make your code clearer, and they guarantee the calculation happens in the order you intend."

---

### Integer Results vs. Float Results

**[Speaking cue: Reinforce the earlier point]**

"Let's revisit something we touched on earlier: **integers vs. floats**."

**[Clear definitions]**

"An **integer** is a whole number—no decimal point. Examples: `5`, `-3`, `1000`."

"A **float** is a number with a decimal point. Examples: `5.0`, `3.14`, `-0.5`."

**[Key rules in Python]**

```python
print(10 / 5)   # 2.0 (float)—regular division always gives a float
print(10 // 5)  # 2 (int)—floor division gives an integer
print(10 * 2)   # 20 (int)—both operands are ints
print(10 * 2.0) # 20.0 (float)—one operand is a float, so result is a float
```

**[Explain the last one]**

"Notice that last one: `10 * 2.0` gives us `20.0`, not `20`. Why? Because when you mix an integer and a float in an operation, Python 'promotes' the result to a float. That's called **type coercion**, and it happens automatically."

**[Practical implication]**

"For most of your programs, this won't matter. But if you're doing something like counting items or working with array indices, you'll want integers. If you're doing money calculations or scientific measurements, you'll usually want floats."

---

### Using `round()` for Display (Not Storage)

**[Speaking cue: Practical guidance—this prevents a common mistake]**

"Alright, last concept before we get to the demo: rounding."

**[Show a messy result]**

```python
result = 10 / 3
print(result)  # Output: 3.3333333333333335
```

"That's ugly. If you're displaying a price or a measurement, you don't want 15 decimal places. You want something clean like `3.33`."

**[Introduce round()]**

"Python has a built-in function called `round()` that lets you control how many decimal places to show."

```python
result = 10 / 3
print(round(result, 2))  # Output: 3.33
```

"The first argument is the number you want to round. The second argument is how many decimal places to keep. So `round(result, 2)` gives us two decimal places: `3.33`."

**[Important warning]**

"Here's the key thing: use `round()` when you're **displaying** a result—when you're printing it to the screen or showing it to a user. **Do not** round intermediate values that you're going to use in further calculations."

**[Show why]**

```python
# Bad: rounding too early
price = 19.99
tax = round(price * 0.07, 2)  # 1.40
total = price + tax  # 21.39

# Good: round only at the end
price = 19.99
tax = price * 0.07  # 1.3993
total = price + tax  # 21.3893
print(f"Total: ${round(total, 2)}")  # Display: $21.39
```

"If you round too early, you can introduce tiny errors that compound. So as a rule of thumb: **calculate with full precision, round only for display**."

**[Quick formatting note]**

"Later in the course, we'll learn about **f-strings** with formatting options, which give you even more control over how numbers look. For now, `round()` will get the job done."

---

**[Transition to demo]**

"Alright! That's the theory. Let's see this stuff in action with a live demo."

---

## Part 3: Live Demo – Mini Calculator (5-10 minutes)

**[Instructor cue: Share your screen and open VS Code or the Python environment]**

### Demo Overview

"I'm going to build a tiny calculator program right in front of you. This will show you how to use the operators, how to handle user input, and how to format the output. I'll also show you a common mistake and how to fix it."

**[Narrate as you type—this is live coding, so go slow]**

---

### Step 1: Basic Arithmetic

**[Start with a new file: `calculator_demo.py`]**

```python
# calculator_demo.py
# Simple calculator demonstrating Python operators

print("=== Basic Arithmetic ===")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

**[Run the program]**

"Let's run this and see what we get."

**[Expected output:]**

```
=== Basic Arithmetic ===
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000
```

**[Point out key results]**

"Look at the division results. Regular division gives us that long decimal: `3.333...`. Floor division gives us `3`—just the whole number. And modulo gives us `1`—the remainder."

---

### Step 2: Division Comparison

**[Add to the file]**

```python
print("\n=== Division: / vs // ===")
print(f"10 / 4 = {10 / 4}")    # 2.5
print(f"10 // 4 = {10 // 4}")  # 2
print(f"10 / 5 = {10 / 5}")    # 2.0
print(f"10 // 5 = {10 // 5}")  # 2
```

**[Run again and narrate]**

"Even when the division is exact—like 10 divided by 5—the single slash gives us `2.0` (a float), and the double slash gives us `2` (an integer)."

---

### Step 3: Even/Odd Check with Modulo

**[Add to the file]**

```python
print("\n=== Even/Odd Check with % ===")
number = 7
remainder = number % 2
print(f"{number} % 2 = {remainder}")
if remainder == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

**[Run and explain]**

"Seven mod two equals one, so we know seven is odd."

**[Change the number and re-run]**

```python
number = 8
remainder = number % 2
print(f"{number} % 2 = {remainder}")
if remainder == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

"Eight mod two equals zero, so eight is even. This is a super common pattern—you'll use it all the time."

---

### Step 4: Getting User Input (The Gotcha)

**[Speaking cue: Slow down—this is where the common mistake happens]**

"Now let's make this interactive. Let's ask the user for two numbers and do some math."

**[Add to the file—intentionally make the mistake first]**

```python
print("\n=== User Input Calculator ===")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = num1 + num2
print(f"Result: {result}")
```

**[Run the program and enter values]**

```
Enter first number: 10
Enter second number: 5
Result: 105
```

**[React with surprise]**

"Whoa! I entered 10 and 5, and instead of getting 15, I got `105`! What happened?"

**[Pause for effect, then explain]**

"Remember what we said at the start: `input()` **always returns a string**. So when I typed `10`, Python stored `'10'`—the text version. And when you use `+` with strings, Python **concatenates** them—it glues them together. So `'10' + '5'` becomes `'105'`."

**[Fix it by converting to float]**

```python
print("\n=== User Input Calculator (Fixed) ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print(f"Result: {result}")
```

**[Run again]**

```
Enter first number: 10
Enter second number: 5
Result: 15.0
```

"There we go! By wrapping `input()` with `float()`, we convert the string to a number **before** we do the math. Now it works correctly."

---

### Step 5: Formatting the Output

**[Add rounding for clean display]**

```python
print(f"Result: {round(result, 2)}")
```

**[Run again]**

"Now if we do a division that gives us a messy decimal, we can round it for display."

**[Demo with division]**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 / num2
print(f"Result: {round(result, 2)}")
```

**[Enter 10 and 3]**

```
Enter first number: 10
Enter second number: 3
Result: 3.33
```

"Much cleaner."

---

**[Wrap the demo]**

"Alright, so that's your mini calculator. You've seen all seven operators, you've seen the difference between `/` and `//`, you've seen how to use `%` to check for even or odd, and you've seen the **critical** step of converting `input()` to a number before doing math."

**[Transition to lab]**

"Now it's your turn. You're going to build a **Tip Calculator**—a real, practical program that you could actually use at a restaurant. Let's walk through what you'll be building."

---

## Part 4: Hands-On Lab – Tip Calculator (25-35 minutes)

**[Instructor cue: Display the lab instructions on screen]**

### Lab Overview

"Here's what you're going to build: a program that asks for a restaurant bill total and a tip percentage, then calculates the tip amount and the final total. And we want the output to look clean—two decimal places, like real money."

---

### Lab Instructions

**[Read through these clearly and slowly]**

**Your task:**

1. Create a new file called `tip_calculator.py`
2. Ask the user for the bill total (before tip)
3. Ask the user for the tip percentage (e.g., 15, 18, 20)
4. Calculate the tip amount in dollars
5. Calculate the final total (bill + tip)
6. Display both the tip amount and final total, formatted to 2 decimal places

**Example run:**

```
Enter the bill total: 45.50
Enter the tip percentage: 18
Tip amount: $8.19
Final total: $53.69
```

---

### Completion Criteria

**[Explain what "done" looks like]**

Your program is complete when:
- It correctly calculates the tip for **any** bill amount and percentage
- It handles decimal inputs (e.g., 45.50, not just whole numbers)
- The output is formatted to exactly 2 decimal places
- You've tested it with at least two different inputs

**[Encourage testing]**

"Don't just run it once and call it done. Try a few different values. Try $100 with a 20% tip—does it give you $20.00 and $120.00? Try $47.82 with 15%—does it give you $7.17 and $54.99? Testing is part of building."

---

### Hints and Reminders

**[Provide scaffolding without giving away the solution]**

1. **Use `float()` to convert input:** Remember, `input()` gives you a string. You need `float(input(...))` to get a number you can do math with.

2. **Tip percentage is out of 100:** If someone types `18`, they mean 18%, which is `0.18` as a decimal. So you'll need to divide by 100.

3. **Use `round()` for display:** To show exactly 2 decimal places, use `round(amount, 2)`.

4. **Formula reminder:**
   - `tip_amount = bill * (tip_percent / 100)`
   - `final_total = bill + tip_amount`

---

### Common Pitfalls to Watch For

**[Warn about the traps]**

- **Forgetting `float()` conversion:** If your program prints weird results or crashes, check if you're converting input to a number.

- **Using integer division by accident:** If you use `//` instead of `/`, your tip will be wrong.

- **Rounding too early:** Don't round the tip amount before adding it to the bill. Do all the math first, then round for display.

- **Type mismatches:** If you see an error like `can't multiply sequence by non-int`, it means you're trying to do math with a string.

---

### Optional Extensions (If You Finish Early)

**[For advanced learners or those who finish quickly]**

1. **Split the bill among friends:** Ask how many people are splitting the bill, then calculate the per-person cost.

2. **Add sales tax:** Ask for a sales tax percentage and apply it **before** calculating the tip (because you tip on the pre-tax total, or post-tax—dealer's choice!).

3. **Offer tip suggestions:** Before asking for a tip percentage, display three options—15%, 18%, and 20%—with the dollar amounts for each.

---

### Lab Time: Get Started!

**[Instructor cue: Set expectations]**

"You've got about 25 to 35 minutes for this lab. I'll be walking around to help if you get stuck. Remember: **errors are feedback**. If you see a red error message, read it carefully. It's usually telling you exactly what's wrong and where."

**[Encourage collaboration but not copy/paste]**

"Feel free to talk to the person next to you if you're stuck, but make sure you understand every line of **your own** code. Copying someone else's solution doesn't teach you anything."

**[Final encouragement]**

"You've got this! You already know everything you need to build this program. Go ahead and get started."

---

**[Instructor: Circulate during lab time]**

### While Students Work: Circulating Tips

**Look for these common issues:**

1. **Missing `float()` conversion:**
   - Symptom: Program prints `105` instead of `15`, or crashes with "can't multiply..."
   - Fix: Show them how to wrap `input()` with `float()`

2. **Forgetting to divide tip_percent by 100:**
   - Symptom: Tip amount is 18 times the bill instead of 18% of the bill
   - Fix: Point out that 18% means `18 / 100`, which is `0.18`

3. **Using `//` instead of `/`:**
   - Symptom: Tip amount is way too low or zero
   - Fix: Explain the difference and ask which one they want

4. **Rounding issues:**
   - Symptom: Output shows too many decimals or weird rounding
   - Fix: Show correct usage of `round(value, 2)`

5. **Syntax errors (missing parentheses, quotes, etc.):**
   - Response: Ask them to read the error message out loud, then ask where the line is

**[Encourage debugging mindset]**

When a student says "It's not working," ask:
- "What did you expect to happen?"
- "What actually happened?"
- "What does the error message say?"
- "Can you print out the intermediate values to see where it goes wrong?"

---

## Part 5: Debrief and Wrap-Up (5-10 minutes)

**[Instructor cue: Call everyone back together]**

"Alright everyone, let's come back together and talk through what we built."

---

### Solution Walkthrough

**[Show a complete working solution on screen]**

"Here's one way to solve the Tip Calculator. Yours might look a little different, and that's fine—there are many correct ways to write this."

```python
# tip_calculator.py
# Calculates tip and total for a restaurant bill

print("=== Tip Calculator ===")

# Get input from user
bill = float(input("Enter the bill total: "))
tip_percent = float(input("Enter the tip percentage: "))

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
final_total = bill + tip_amount

# Display results with 2 decimal places
print(f"Tip amount: ${round(tip_amount, 2)}")
print(f"Final total: ${round(final_total, 2)}")
```

**[Walk through key parts]**

"Let's break this down:"

1. **Line 5-6:** We use `float(input(...))` to get numeric input. This converts the string to a float so we can do math with it.

2. **Line 9:** We calculate the tip by multiplying the bill by the percentage divided by 100. So if the bill is $50 and the tip is 20%, we do `50 * (20 / 100)`, which gives us `50 * 0.2`, which is $10.

3. **Line 10:** We add the tip to the bill to get the final total.

4. **Line 13-14:** We use `round()` with 2 decimal places to make the output look like real money.

**[Test it together]**

"Let's test this with an example. If the bill is $45.50 and we tip 18%, what should we get?"

**[Calculate on screen or ask students]**

- Tip: $45.50 × 0.18 = $8.19
- Total: $45.50 + $8.19 = $53.69

"Perfect. That matches what the program prints."

---

### Common Issues and Fixes

**[Share the most common mistakes you saw during lab time]**

"As I was walking around, I saw a few common mistakes. Let's talk about them so everyone can learn."

**1. Forgetting `float()` conversion**

```python
# Wrong:
bill = input("Enter the bill total: ")
tip_amount = bill * 0.18  # ERROR! Can't multiply string by float
```

```python
# Right:
bill = float(input("Enter the bill total: "))
tip_amount = bill * 0.18  # Works!
```

"If you forget `float()`, Python treats the input as text, and you can't do math with text."

---

**2. Not dividing tip percentage by 100**

```python
# Wrong:
tip_amount = bill * tip_percent  # If tip_percent is 18, this multiplies bill by 18!
```

```python
# Right:
tip_amount = bill * (tip_percent / 100)  # Converts 18 to 0.18
```

"Remember: when someone says '18%', they mean 18 out of 100, which is 0.18 as a decimal."

---

**3. Rounding too early**

```python
# Less precise:
tip_amount = round(bill * (tip_percent / 100), 2)
final_total = round(bill + tip_amount, 2)
```

```python
# Better:
tip_amount = bill * (tip_percent / 100)
final_total = bill + tip_amount
print(f"Tip: ${round(tip_amount, 2)}")
print(f"Total: ${round(final_total, 2)}")
```

"Do all your math with full precision, then round only when you display. This avoids tiny errors."

---

### Student Solutions Share-Out

**[Ask for volunteers]**

"Who wants to share their solution? Did anyone do something different, or add one of the optional extensions?"

**[Call on 1-2 students to share their screen or read their code]**

**[Provide positive, specific feedback]**

- "I like how you added helpful comments at the top."
- "Nice job using descriptive variable names—`bill_total` is clearer than just `b`."
- "Cool! You added the split feature. How did that work?"

---

### Quick Check / Exit Ticket

**[Speaking cue: Final knowledge check]**

"Before we wrap up Day 1, one last quick check question:"

**Question:** "What does the modulo operator (`%`) return, and when is it useful?"

**[Pause for answers]**

**Expected answer:**
- It returns the **remainder** after division
- Useful for checking if a number is even/odd, or for repeating patterns, or "every Nth item" logic

**[If no one answers, give it yourself]**

"`%` gives you the remainder. So `10 % 3` is `1` because 10 divided by 3 is 3 with a remainder of 1. You use it all the time to check if a number is even or odd—if `number % 2` equals zero, it's even."

---

### Day 1 Wrap-Up and Celebration

**[Speaking cue: Celebratory and encouraging tone]**

"Alright everyone, let's talk about what you just accomplished today—because it's actually a **big deal**."

**[Recap the day]**

"In **four hours**, you went from 'I don't know Python' to 'I can build a working calculator program.'"

**[List the wins]**

"You learned how to:
- Set up and run Python scripts
- Print output and read error messages
- Create variables and work with different data types
- Use seven different arithmetic operators
- Handle user input and convert it to the right type
- Format numbers for clean output
- Build a complete, functioning program from scratch"

**[Make it real]**

"That Tip Calculator you just built? That's a **real program**. You could literally use it the next time you go out to eat. You could send it to a friend. You could put it in a portfolio. It's small, but it's **real**."

---

### What's Next: Preview of Day 2 (Session 2)

**[Speaking cue: Build anticipation]**

"Tomorrow, we're going to level up. We're going to talk about **strings**—how to slice them, search them, clean them up, and format them. Strings are everywhere in real programs: user input, file names, email addresses, URLs, messages. So we'll spend a whole session making you really comfortable with text."

**[Quick preview of topics]**

"Here's what's coming in Session 2:
- **Hour 5:** String indexing and slicing—how to grab parts of a string
- **Hour 6:** String methods—cleaning, searching, replacing
- **Hour 7:** More input/output patterns and type conversions
- **Hour 8:** Checkpoint 1—a mini-assessment so you can test your fundamentals and see how far you've come"

**[Set expectations]**

"So make sure you save your work from today. If you haven't already, click **Save All** in your editor and make sure your files are in the right folder. When you come back tomorrow, we'll hit the ground running."

---

### Closing Encouragement

**[Speaking cue: Warm, genuine, motivating]**

"I just want to say: if you've never programmed before, today might have felt challenging. And that's **normal**. Learning to code is like learning a new language—it takes time, it takes practice, and it takes patience with yourself."

**[Acknowledge the effort]**

"But you showed up. You typed the code. You ran into errors and you fixed them. You built something. That's what matters."

**[Set the tone for the rest of the course]**

"Over the next 11 sessions, we're going to keep building on what you learned today. Each day, you'll add a new skill. And by the end of this course, you'll look back at today and think, 'Wow, I've come a long way.'"

**[Final practical reminders]**

"Before you leave:
- Make sure your files are saved in the lab workspace
- If you had any login issues or technical problems, let me know before next session
- If you want extra practice tonight, try building a different kind of calculator—maybe one that converts Fahrenheit to Celsius, or calculates the area of a rectangle"

**[Dismiss with energy]**

"Great work today, everyone. I'll see you tomorrow for Session 2. Have a great rest of your day!"

---

## Appendix: Troubleshooting Reference

### Error Messages and Fixes

**Error:** `TypeError: can't multiply sequence by non-int of type 'float'`

**Cause:** Trying to do math with a string (usually forgot to convert `input()`)

**Fix:** 
```python
# Wrong:
bill = input("Enter bill: ")
tip = bill * 0.18

# Right:
bill = float(input("Enter bill: "))
tip = bill * 0.18
```

---

**Error:** `ValueError: could not convert string to float: 'hello'`

**Cause:** User typed non-numeric input when program expected a number

**Fix:** Add input validation (covered in Session 8) or give clearer instructions

---

**Error:** `ZeroDivisionError: division by zero`

**Cause:** Dividing by zero

**Fix:** Check the value before dividing, or give a better error message

---

**Issue:** Output shows too many decimal places (e.g., `8.190000000001`)

**Cause:** Float precision quirks

**Fix:** Use `round(value, 2)` for display

---

**Issue:** Program prints `'105'` instead of `15` when adding two inputs

**Cause:** Forgot to convert `input()` to `float()` or `int()`

**Fix:** Wrap `input()` with `float()`

---

## Additional Practice Problems (Optional Homework)

### Problem 1: Temperature Converter
Write a program that converts Fahrenheit to Celsius using the formula:
```
C = (F - 32) × 5 / 9
```

### Problem 2: Area Calculator
Calculate the area of a rectangle given length and width. Display the result with 2 decimal places.

### Problem 3: Split the Bill
Extend the tip calculator to split the total among a group of people. Ask how many people, then show the per-person cost.

### Problem 4: Compound Interest
Calculate compound interest given principal, rate (as a percentage), and years. Formula:
```
A = P × (1 + r/100) ** t
```

---

## Instructor Notes

### Timing Adjustments

- If running behind: Skip the optional extensions discussion, shorten the demo
- If running ahead: Do a second demo showing one of the extensions, or do more interactive prediction questions
- The lab is the most important part—protect that time

### Common Question: "When do I use `/` vs `//`?"

**Answer:** Use `/` (regular division) for almost everything—money, measurements, averages. Use `//` (floor division) when you specifically need a whole number and you want to ignore the remainder—like "how many full boxes do I need?" or "how many complete weeks?"

### Common Question: "Why doesn't Python just use × and ÷?"

**Answer:** Because those symbols aren't on a standard keyboard! Python uses symbols that every keyboard has: `*` for multiply, `/` for divide. It's the same reason we use `==` for "equals" instead of a single `=` (which is already taken for assignment).

### Common Question: "Do I need to memorize PEMDAS?"

**Answer:** Not really. Just remember: when in doubt, use parentheses. They make your code clearer and guarantee the order you want. Python will follow standard math order, but explicit is better than implicit.

---

## Key Takeaways (Summary for Students)

1. **Seven arithmetic operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
2. **Division always gives a float:** `/` → float, `//` → integer
3. **Modulo gives the remainder:** Useful for even/odd checks and repeating patterns
4. **Use parentheses to control order:** They make your intent clear
5. **Always convert `input()` before math:** Use `float()` or `int()`
6. **Round for display, not storage:** Do math with full precision, round only at the end

---

**End of Day 1, Hour 4**

---

**Total Word Count: ~5,200 words**

This script is designed to be read nearly verbatim by an instructor, with natural pauses for interaction, demonstrations, and student work time. The tone is conversational and encouraging, appropriate for beginners with no prior programming experience.
