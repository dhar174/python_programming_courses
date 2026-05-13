# Day 10, Hour 3: Basic Encapsulation + Data Validation (Course Hour 39)

**Python Programming Basics – Session 10, Hour 3**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 39 – Basic encapsulation + data validation  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)  
**Prerequisites:** Contact class from Day 10 Hour 2; understanding of class methods and return statements  

---

## Learning Outcomes

By the end of this 60-minute session, learners will be able to:

1. **Write simple data validation rules directly inside class methods** — using conditional checks and return values to guard against invalid data.

2. **Differentiate between core business logic and User Interface (UI) logic** — recognizing that validation belongs in the class blueprint, not scattered across the menu loop.

3. **Manage invalid data gracefully** — preventing bad data from entering the system while providing clear feedback to users.

4. **Raise and preview ValueError** — introducing exception raising as an alternative to boolean returns (with the understanding that full error handling comes later in the course).

5. **Keep UI code clean and focused** — delegating validation responsibility to the class so the menu loop remains readable.

---

## Instructor Prep Notes

**Before class:**

- Open a blank file named `hour39_validation_demo.py` in your code editor, ready for live typing.
- Have the `Contact` class from Day 10 Hour 2 available for reference (or paste it at the top of your demo file).
- Test both the "return boolean" and "raise ValueError" patterns locally to ensure smooth live demo.
- Prepare a Contact object with a known valid phone number (e.g., "555-1234-5678") for live demonstration.
- Review common pitfalls section below so you can spot-check student code during lab circulation.

**Setup instruction (read aloud to class):**

"Please open your code editors and either create a new file called `validation_practice.py` or open your existing Contact Manager script. We're going to add smart validation to keep bad data out of our contact database. By the end of this hour, your program will reject invalid phone numbers automatically—no garbage data allowed!"

---

## Opening Script: Guardrails for Our Data (~5 minutes)

**Say (instructor narrative):**

"Right now, think about what happens when someone runs our Contact Manager. We ask for a name, a phone number, maybe an age or email. Our current `Contact` class accepts whatever the user types without question. What if someone types a negative age? What if they type letters where we expect numbers? What if they paste a phone number in an invalid format?

In real software development, one of your most important jobs is being a data gatekeeper. You are the guardian of data quality. We need guardrails—rules that prevent garbage from polluting our database.

Here's the key question I want you to think about: **Where should those guardrails live?** Should we put them in the `while` loop, right after we call `input()`? Or should we put them inside the `Contact` class itself?

Let me ask you to predict: what happens when a user manager imports contacts from a CSV file instead of typing them in a menu? If all our validation logic is buried in the menu loop, we'd have to copy-paste those same checks everywhere—once for keyboard entry, once for file import, once for API data. That's not maintainable. That's not professional.

The answer is **encapsulation**. We put the guardrails directly into the class. The class becomes a self-contained, intelligent unit that knows the rules of valid data. Anywhere that code wants to add or update a contact—whether through a menu, a file, an API, or anywhere else—it uses the class methods, and the class enforces the rules once, in one place."

---

## Concept Briefing: Encapsulation and Business Logic vs. UI

### Understanding Encapsulation

**Say:**

"Encapsulation is the practice of bundling data and the rules that protect that data into a single unit—the class. Think of it like a bank account. The bank doesn't let you just set your balance directly. You can't walk into the bank and say, 'I'd like my balance to be $1,000,000.' The bank has validation rules. You deposit or withdraw through specific methods, and those methods enforce the business rules.

Our `Contact` class should work the same way. Instead of:

```python
c = Contact("Alice", "555-1234")
c.phone = user_input  # No! Just stuffing data in!
```

We do:

```python
c = Contact("Alice", "555-1234")
success = c.update_phone(user_input)  # The method decides if it's valid
if success:
    print("Update successful!")
else:
    print("Invalid phone number.")
```

The key difference: the second approach keeps control inside the class. The class makes the decision."

### Separating UI from Core Logic

**Say:**

"This leads to our second core idea: **separation of concerns**. Your program has two different jobs:

1. **Core Logic (the class):** Understands what makes a Contact valid. Knows the business rules. Protects the data.

2. **User Interface (the menu loop):** Talks to the user. Prints prompts. Gets input. Calls the class methods. Responds to success or failure.

These two should not know too much about each other. The UI shouldn't know *why* a phone number is invalid—it should just know it *is* invalid. The class shouldn't need to know anything about `input()` or print statements—it just focuses on keeping data clean.

When you separate these concerns:
- **Code is reusable:** Any code that imports contacts uses the same validation.
- **Code is maintainable:** Change validation rules in one place.
- **Code is testable:** You can test the class without a running menu loop.
- **Code is readable:** The menu loop isn't cluttered with validation logic.

Let's look at how to actually build this."

### A Simple Validation Method: The Boolean Approach

**Say:**

"The simplest way to add validation is to have your method return `True` if the update succeeds and `False` if it fails."

**Type the following code and narrate as you type:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def update_phone(self, new_phone):
        """
        Update the phone number if it passes validation.
        Returns: True if valid and updated, False otherwise.
        """
        # Validation rule 1: Length check
        # Phone numbers should be at least 7 characters
        if len(new_phone) < 7:
            return False
        
        # If we got here, the phone number passed all checks
        self.phone = new_phone
        return True
```

**Say:**

"Notice the method signature: it takes one parameter, `new_phone`. It doesn't modify `self.phone` right away. Instead, it first validates. If validation passes, update and return `True`. If validation fails, don't touch the data, just return `False`.

This pattern is clean and simple. The caller knows exactly what the boolean means: success or failure. Let me show you a second approach that's more forceful."

---

## Concept: Defensive Programming with ValueError

**Say:**

"Returning `False` is polite. Sometimes we want to be more aggressive. In Python, when something is fundamentally wrong with a value—its format, its type, its content—we can **raise an exception**. Specifically, we raise a `ValueError` to say 'This value is invalid.'

The idea is: if someone passes bad data to the method, the method doesn't silently fail; it crashes with a clear message. Later in the course, we'll learn how to 'catch' these exceptions so the program doesn't crash, but for now, raising an error is a powerful way for the class to say 'No, I will not accept this.'

Here's the same `Contact` class, but using `ValueError`:"

**Type the following code:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def update_phone(self, new_phone):
        """
        Update the phone number if it passes validation.
        Raises ValueError if the phone number is invalid.
        """
        # Clean up the phone number: remove spaces and dashes
        # This helps us check if the remaining characters are all digits
        clean_phone = new_phone.replace(" ", "").replace("-", "")
        
        # Validation rule 1: Must contain only digits after cleanup
        if not clean_phone.isdigit():
            raise ValueError(
                f"Phone '{new_phone}' contains invalid characters. "
                f"Use only digits, spaces, and dashes."
            )
        
        # Validation rule 2: Must be at least 7 digits
        if len(clean_phone) < 7:
            raise ValueError(
                f"Phone '{new_phone}' is too short. "
                f"Must be at least 7 digits."
            )
        
        # If we get here, all validations passed
        self.phone = new_phone
        return True
```

**Say:**

"When we write `raise ValueError(...)`, we're telling Python 'Stop. Something is wrong. Here's the message explaining why.' The program stops right there, and the error message prints.

Notice how much more expressive the error messages are compared to returning `False`. We can tell the user exactly what's wrong: 'Use only digits,' or 'Too short.' The `f-string` lets us include the actual data the user entered, which is helpful for debugging.

For this hour, we're introducing ValueError as a preview. We're not catching it yet—the program will crash if it's raised. But that's okay for now. It's a powerful signal. Later, you'll learn `try`/`except` to catch these errors gracefully."

---

## Demo: Wiring Validation to the UI (~8 minutes)

**Say:**

"Now let's connect the class to a real menu loop. I'm going to show both approaches side by side, and you'll see how clean the menu becomes when the validation lives in the class."

**Demo 1: Using the Boolean Approach**

**Type and narrate:**

```python
# Approach 1: Boolean return value
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def update_phone(self, new_phone):
        # Validation: phone must be at least 7 characters
        if len(new_phone) < 7:
            return False  # Tell caller: invalid
        self.phone = new_phone  # Update only if valid
        return True  # Tell caller: success

# Instantiate a contact object
my_contact = Contact("Alice", "555-1234")

# Menu loop to update contact
while True:
    print(f"\nCurrent phone: {my_contact.phone}")
    user_input = input("Enter new phone (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    # Call method and capture the success/failure boolean
    success = my_contact.update_phone(user_input)
    
    # React to the result
    if success:
        print("✓ Phone updated successfully!")
    else:
        print("✗ Invalid phone number. Must be at least 7 characters.")
```

**Say as you narrate:**

"Look at how clean the `while` loop is. It only does two things: (1) present information to the user, (2) call the class method and respond to the result. The loop doesn't know anything about phone number validation rules. That responsibility lives in the class."

**Run the demo with valid and invalid inputs:**

```
Current phone: 555-1234
Enter new phone (or 'q' to quit): 123
✗ Invalid phone number. Must be at least 7 characters.

Current phone: 555-1234
Enter new phone (or 'q' to quit): 555-9999
✓ Phone updated successfully!

Current phone: 555-9999
Enter new phone (or 'q' to quit): q
```

**Say:**

"Notice: when I type '123', the class rejects it and returns False. When I type '555-9999', it's accepted. The loop doesn't need to understand why; it just follows the boolean result."

**Demo 2: Using ValueError (Quick Preview)**

**Type and narrate:**

```python
# Using the ValueError approach
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def update_phone(self, new_phone):
        clean_phone = new_phone.replace(" ", "").replace("-", "")
        if not clean_phone.isdigit():
            raise ValueError("Phone must contain only digits, spaces, and dashes.")
        if len(clean_phone) < 7:
            raise ValueError("Phone must be at least 7 digits.")
        self.phone = new_phone
        return True

# Create a contact
my_contact = Contact("Alice", "555-1234")

# UI loop
while True:
    print(f"\nCurrent phone: {my_contact.phone}")
    user_input = input("Enter new phone (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    # Try to update; if an error is raised, it will crash (for now)
    try:
        my_contact.update_phone(user_input)
        print("✓ Phone updated successfully!")
    except ValueError as e:
        print(f"✗ Error: {e}")
```

**Say:**

"This version uses `try`/`except`, which we'll cover in detail in the next module. The key idea: the class raises a `ValueError` with a specific message. The UI catches it and shows a friendly error. Either way—boolean or exception—the rule lives in the class, and the menu loop stays clean.

For the lab, I recommend the boolean approach since we haven't formally covered exceptions yet. But it's good to see both."

---

## Practice Exercise: Live Validation (~8 minutes)

**Say:**

"Let's work through a quick practice example together. I want you to think through the logic before I type."

**Present the scenario:**

"Imagine we have a `BankAccount` class. We want to write an `update_balance` method. Here's the rule: the new balance must be non-negative (you can't have negative money). Should we allow a balance of zero? Let's say yes—you can have zero balance."

**Ask the class:**

"What validation check should I write? Talk to your neighbor for 20 seconds. What's the condition?"

**Listen to answers. Then type:**

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def update_balance(self, new_balance):
        """Update balance if non-negative."""
        if new_balance < 0:
            return False
        self.balance = new_balance
        return True

# Test it
account = BankAccount("Bob", 100)

# Valid updates
print(account.update_balance(50))   # True, balance becomes 50
print(account.update_balance(0))    # True, balance becomes 0
print(account.balance)               # 0

# Invalid update
print(account.update_balance(-10))  # False, balance stays 0
print(account.balance)               # Still 0
```

**Say:**

"Notice: the invalid update doesn't change the balance. The method returns `False`, signaling failure. The data stays protected. This is encapsulation in action."

**Ask a follow-up:**

"What if the user enters the string '-10' instead of the number -10? Should we convert it? Should we reject it?"

**Discuss briefly:** For now, assume data comes in as the correct type. In real applications, you'd handle type conversion carefully.

---

## Hands-On Lab: Add Validation to Your Contact Manager (~28 minutes)

**Say:**

"Now it's your turn. You have about 28 minutes for this lab. Here's what I want you to do."

### Lab Overview and Specification

**Read aloud or display:**

**Objective:** Add a validation method to your `Contact` class and update your menu to use it.

**Task Steps:**

1. **Open your Contact Manager script** (or start fresh with a simple Contact class if you don't have one yet).

2. **Add a validation method to your `Contact` class** named `update_phone(new_phone)`:
   - The method takes one parameter: `new_phone` (a string).
   - It should implement **at least one** validation rule. Examples:
     - Check that the phone length is at least 7 characters: `len(new_phone) >= 7`
     - Check that it contains only digits, spaces, or dashes: `clean_phone.isdigit()` where `clean_phone = new_phone.replace(" ", "").replace("-", "")`
     - Check that it starts with a specific digit or country code
   - If the phone is valid, update `self.phone` and return `True`.
   - If invalid, do **not** modify `self.phone`, and return `False`.

3. **Update your menu loop** (specifically the "Update Contact" or "Search and Update" section):
   - When you ask the user for a new phone number, **do not** directly assign it to the contact's attribute.
   - **Do not** write: `contact.phone = user_input`
   - **Instead**, call your new method: `success = contact.update_phone(user_input)`
   - Check the `success` boolean:
     - If `True`, print a success message.
     - If `False`, print a helpful error message that explains what went wrong (e.g., "Phone number must be at least 7 characters").
     - Consider re-prompting the user or moving to the next menu item.

4. **Test your code** with both valid and invalid inputs:
   - Try a valid phone number and confirm it updates.
   - Try an invalid phone number and confirm it's rejected.
   - Verify that the contact's phone doesn't change when invalid input is given.

### Lab Checkpoints (Measurable Criteria)

**You must complete these checkpoints:**

- [ ] **Checkpoint 1:** The `update_phone` method exists and takes `new_phone` as a parameter.
- [ ] **Checkpoint 2:** The method contains at least one `if` statement that validates the phone.
- [ ] **Checkpoint 3:** The method returns `True` if valid, `False` if invalid.
- [ ] **Checkpoint 4:** The method updates `self.phone` only when the validation passes.
- [ ] **Checkpoint 5:** Your menu loop calls `update_phone` (not direct assignment) and handles the boolean result.
- [ ] **Checkpoint 6:** Invalid input is rejected without crashing; a helpful message is printed.
- [ ] **Checkpoint 7:** Your code runs without syntax errors when tested with valid and invalid inputs.

### Lab Walkthrough Solution (~Minute 20)

**After ~20 minutes of work, gather attention and show a solution sketch:**

**Say:**

"Let me show you a working example. Your code might look different, and that's fine—there are many valid ways to solve this. But watch for these key pieces."

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def display(self):
        return f"Contact: {self.name}, Phone: {self.phone}"
    
    def update_phone(self, new_phone):
        """
        Validate and update the phone number.
        Returns True if successful, False if invalid.
        """
        # Remove spaces and dashes for validation
        clean = new_phone.replace(" ", "").replace("-", "")
        
        # Rule 1: Must be all digits
        if not clean.isdigit():
            return False
        
        # Rule 2: Must be at least 7 digits
        if len(clean) < 7:
            return False
        
        # Rule 3 (optional): No more than 15 digits
        if len(clean) > 15:
            return False
        
        # All rules passed: update the attribute
        self.phone = new_phone
        return True

# Example menu snippet
if choice == "update":
    target_name = input("Enter contact name to update: ")
    # [Assume we search and find the contact; store in 'found']
    if found:
        new_phone = input("Enter new phone number: ")
        
        # Call the validation method
        if found.update_phone(new_phone):
            print("✓ Phone number updated!")
        else:
            print("✗ Invalid phone number.")
            print("   Phone must have 7-15 digits (spaces and dashes allowed).")
```

**Key teaching points to emphasize:**

- **Validation lives in the method:** The menu doesn't need to know the exact rules.
- **Boolean return:** Simple, clear contract: `True` means success, `False` means failure.
- **Message clarity:** If validation fails, tell the user exactly what went wrong.
- **No silent failures:** If the phone is invalid, `self.phone` is not modified.

**Say:**

"Did everyone get these pieces? The method, the boolean return, the UI handling? Spend the last few minutes finishing your code. I'll circulate and help anyone stuck."

### Circulation Notes for Instructor

**What to look for:**

- **Common mistake 1:** Validation logic in the menu, not in the class method.
  - **Fix:** "Move that `if` statement into the `update_phone` method. The class owns the rules."

- **Common mistake 2:** Not storing the boolean result; code like `contact.update_phone(new_phone)` with no `if` after.
  - **Fix:** "You need to capture the return value: `success = contact.update_phone(new_phone)`. Then use `if success:`."

- **Common mistake 3:** Validation rule too strict (e.g., rejecting valid phone formats).
  - **Fix:** "That rule is too strict. A phone like '555-1234' is valid. Remove the `.replace()` calls, or adjust your rule."

- **Common mistake 4:** Modifying `self.phone` before validation passes.
  - **Fix:** "Check first, then update. Do the `if` check, and only inside the `if True` block, update the attribute."

---

## Troubleshooting & Common Pitfalls

### Pitfall 1: Validation Logic Lives in the Wrong Place

**The trap:**

```python
# ❌ WRONG: Validation is in the menu loop, not the class
contact = Contact("Alice", "555-1234")

phone = input("Enter phone: ")
if len(phone) >= 7:  # Validation is HERE in the menu
    contact.phone = phone  # Direct assignment
else:
    print("Invalid")
```

**The fix:**

```python
# ✓ RIGHT: Validation is in the class method
contact = Contact("Alice", "555-1234")

phone = input("Enter phone: ")
if contact.update_phone(phone):  # Validation is in the method
    print("Updated!")
else:
    print("Invalid—try again")
```

**Why it matters:** If your validation logic is in the menu loop, other parts of your code (or other people's code, or future code) might bypass it. By putting validation inside the class, you protect the data *everywhere* the class is used.

---

### Pitfall 2: Forgetting to Return a Boolean

**The trap:**

```python
# ❌ WRONG: No return statement
def update_phone(self, new_phone):
    if len(new_phone) >= 7:
        self.phone = new_phone
        print("Phone updated!")  # Prints, but returns None implicitly
    # If invalid, returns None (implicitly)
```

**What happens:** The method returns `None`, not `True` or `False`. Your UI code might do this:

```python
result = contact.update_phone(phone)
if result:  # None is falsy, so this looks like False
    print("Success")
else:
    print("Failed")  # Always prints "Failed", even if it worked!
```

**The fix:**

```python
# ✓ RIGHT: Explicit return statements
def update_phone(self, new_phone):
    if len(new_phone) >= 7:
        self.phone = new_phone
        return True  # Explicit return
    else:
        return False  # Explicit return
```

**Student drill:** "Always ask: does my method return `True` or `False`? Say it out loud: 'If valid, return True. If invalid, return False.'"

---

### Pitfall 3: Modifying the Data Even When Validation Fails

**The trap:**

```python
# ❌ WRONG: Updates the data before checking validity
def update_phone(self, new_phone):
    self.phone = new_phone  # Oops, changed it!
    if len(new_phone) >= 7:
        return True
    else:
        self.phone = old_phone  # Try to undo—but we lost old_phone!
        return False
```

**What happens:** Either you corrupt the data or you get an error (`old_phone` is not defined).

**The fix:**

```python
# ✓ RIGHT: Validate first, update only if valid
def update_phone(self, new_phone):
    # Check the validation BEFORE modifying anything
    if len(new_phone) >= 7:
        self.phone = new_phone  # Now it's safe to update
        return True
    else:
        # Don't modify self.phone if invalid
        return False
```

**Teaching point:** "Always validate first. Think of it like checking the weather before you leave the house. You don't put on your coat and then check—you check first, then decide."

---

### Pitfall 4: Writing Overly Strict Validation Rules

**The trap:**

```python
# ❌ TOO STRICT: Rejects valid phone numbers
def update_phone(self, new_phone):
    # Rule: must be exactly 10 characters
    if len(new_phone) == 10:  # What about "(555) 123-4567"? That's 14 chars!
        self.phone = new_phone
        return True
    return False
```

**What happens:** Students with formatted phone numbers (with spaces, parentheses, dashes) get rejected. This is frustrating.

**The fix:**

```python
# ✓ BETTER: Account for formatting
def update_phone(self, new_phone):
    # Extract only digits
    digits_only = new_phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # Rule: must have at least 7 digits
    if len(digits_only) >= 7:
        self.phone = new_phone  # Store as user entered it (or normalize if you want)
        return True
    return False
```

**For the lab:** "Start simple: just check the length. If students want to add more rules, great! Show them how. But don't make it so complicated that valid data gets rejected."

---

### Pitfall 5: Exception Handling Overkill (ValueError Confusion)

**The trap:**

Students might try to use exceptions in ways that complicate their code:

```python
# ❌ OVERLY COMPLEX: Raising exceptions for normal failures
def update_phone(self, new_phone):
    if len(new_phone) < 7:
        raise ValueError("Phone too short")  # OK for critical failures, not for normal validation
    self.phone = new_phone
    return True
```

**Then in the menu:**

```python
# ❌ MESSY: Have to catch and handle
try:
    success = contact.update_phone(phone)  # But now it might raise an exception, confusing!
except ValueError:
    print("Invalid")
```

**For the lab:** Remind students: "We're doing boolean returns this hour. ValueError is a preview for the next module. If your method works, stick with the boolean pattern. Don't mix—keep it simple."

---

### Pitfall 6: Infinite Loops in the Menu

**The trap:**

```python
# ❌ WRONG: Menu loop that doesn't exit cleanly
while True:
    phone = input("Enter phone: ")
    if not contact.update_phone(phone):
        print("Invalid. Try again.")
        # Falls through to next iteration... infinite loop if user can't get it right
```

**What happens:** If the user keeps entering invalid data, they have no way out. They have to hit Ctrl+C.

**The fix:**

```python
# ✓ RIGHT: Offer a way out
while True:
    phone = input("Enter phone (or 'q' to skip): ")
    if phone.lower() == 'q':
        break
    if contact.update_phone(phone):
        print("Updated!")
        break  # Exit after success
    else:
        print("Invalid. Try again or press 'q' to skip.")
```

**Teaching point:** "Always give users a way out. Even if validation fails, don't trap them."

---

### Pitfall 7: Not Testing Edge Cases

**The trap:**

Students write a validation rule and test only the happy path:

```python
# ✓ Tested:
contact.update_phone("555-1234567")  # Valid, 12 chars with dashes

# ❌ NOT TESTED:
contact.update_phone("")  # Empty string? Crashes or passes?
contact.update_phone("   ")  # Spaces only? What happens?
contact.update_phone(None)  # What if someone passes None?
contact.update_phone(5551234567)  # What if it's a number, not a string?
```

**The fix:**

"During the lab, walk students through a test checklist:

1. Test a **valid input**. Does it update?
2. Test an **invalid input**. Does it reject?
3. Test **edge cases**: empty string, None, numbers, very long strings, special characters.
4. After each test, check: did the data change when it shouldn't? Is the error message helpful?"

**Demo checklist on the board:**

```
[ ] Valid input updates
[ ] Invalid input rejected
[ ] Empty string handled
[ ] None handled
[ ] Edge cases pass
[ ] No crashes
```

---

### Pitfall 8: Confusing `return False` with "Method Failed"

**The trap:**

Students sometimes think a `return False` means the method crashed:

```python
# ❌ WRONG THINKING: "If it returns False, the program is broken"
result = contact.update_phone(phone)
if not result:
    print("ERROR: Method failed!")  # Not an error—just invalid input
```

**The fix:**

"Return False just means 'validation didn't pass.' It's not an error—it's expected behavior for invalid input. Errors are when the method crashes (exception) or does something unexpected."

**Teach the difference:**

- **`return False`**: Normal response to invalid input. The method worked fine; it's just saying "no."
- **Exception**: Unexpected problem. Something is seriously wrong.
- **Silent failure**: Method doesn't return anything (returns `None`). Bad—the caller doesn't know what happened.

---

## Quick-Check Questions (3–5 Probes for Understanding)

**Ask these questions throughout or at the end to gauge understanding:**

**Question 1 (Encapsulation):**
"Why should validation rules live inside the class method instead of in the menu loop?"

**Expected answer:** Centralized, reusable, maintainable, keeps UI clean.

**Question 2 (Boolean returns):**
"What does `True` mean when a method returns it? What does `False` mean?"

**Expected answer:** `True` = operation succeeded, `False` = operation failed / input was invalid.

**Question 3 (UI separation):**
"If I add validation to my `Contact` class, what does the menu loop NOT have to worry about?"

**Expected answer:** The menu loop doesn't need to know the specific validation rules; it just uses the boolean result.

**Question 4 (State protection):**
"If I call `contact.update_phone('123')` (which is too short) and the method returns `False`, what happens to `contact.phone`?"

**Expected answer:** It doesn't change. The old value stays. The method doesn't modify it if validation fails.

**Question 5 (ValueError preview):**
"We saw `raise ValueError(...)` in the demo. What does raising an error do?"

**Expected answer:** It stops the program with an error message, signaling that something is wrong. Later, we'll learn to catch these errors so the program doesn't stop.

---

## Wrap-Up Notes (Summary + Reflection Prompts)

### Summary

**Say (instructor recap):**

"Today we learned **encapsulation**: putting data and the rules that protect it into the same unit—the class. We showed two patterns for validation:

1. **Boolean returns:** Method returns `True` if valid, `False` if not. Simple and clear for the UI to handle.

2. **Raising exceptions:** Method raises `ValueError` if invalid. More forceful. (We'll catch these formally next module.)

The big takeaway: **the class owns its data**. The class decides what data is acceptable. The UI's job is to talk to the user and call the class methods. This separation keeps code clean, reusable, and maintainable.

You added validation to at least one method. Your Contact Manager now rejects bad data instead of blindly accepting it. That's professionalism. That's software engineering."

### Reflection Prompts (Optional, 2–3 min)

**Ask learners to think or discuss:**

1. **"Think of a class you might write in a project. What's one validation rule it should have? Where would you put that rule?"**

2. **"If you were working on a team, why might your teammates thank you for putting validation inside the class instead of in the menu?"**

3. **"We rejected invalid data with a `return False`. Can you imagine a situation where you'd want to raise an exception instead? (Hint: think about a critical failure vs. a user input error.)"**

---

## Facilitation Notes (Instructor Tips, Timing, Extensions)

### Timing Guidance

- **0:00–0:05** Opening Script (~5 min): Set the context. Pose the "where should guardrails live?" question.
- **0:05–0:15** Concept Briefing (~10 min): Encapsulation, UI vs. core logic, boolean returns, then ValueError.
- **0:15–0:23** Demo (~8 min): Show both patterns (boolean and exception) wired to a menu loop. Run live examples.
- **0:23–0:31** Practice Exercise (~8 min): Simple BankAccount example, guided together.
- **0:31–1:00** Lab (~29 min): Students implement validation on their Contact or simple class. Circulate. (~20 min solo work, ~5–7 min walkthrough, ~2 min final checks).
- **1:00** Wrap-up (~1 min): Quick recap.

**If running short:** Skip the ValueError section; focus on boolean returns. Raise ValueError is a preview; students can learn full exception handling later.

**If running long:** Reduce demo time or shorten practice exercise. The lab is the core; ensure students get hands-on time.

### Common Facilitation Moves

1. **Spot-check during lab:** Ask a student: "Show me where your validation rule is. Is it in the class or the menu?" Guide if needed.

2. **Use a "pair walk":** Have students briefly pair-program. "Turn to your neighbor. One of you share your `update_phone` method. Is it correct?"

3. **Celebrate small wins:** "I see someone's validation is working! Silently give them a thumbs up."

4. **Redirect without criticizing:** "That's a start. Let me show you a tweak..." (Avoid saying "wrong").

5. **Model the thinking:** When a student asks "How should I write the validation?", don't just give the answer. Ask back: "What condition would make a phone number invalid? Tell me the rule in English first."

6. **Build confidence:** For students struggling: "This is hard because you're learning real professional patterns. You're doing great. Here's a small hint..."

### Extension Ideas (Stay in Basics Scope)

1. **Multiple validation rules:** Add a length check *and* an "only digits/dashes/spaces" check. Create a method that returns a detailed error message about which rule failed.

2. **Normalize on storage:** Store the phone as digits-only (`"5551234567"`), but display with formatting (`"(555) 123-4567"`). This teaches the difference between storage format and display format.

3. **Add a `validate_name` method:** Similar pattern—check that name is not empty, is longer than 1 character, etc. Apply the same principle to other attributes.

4. **Soft vs. hard fails:** One method returns False for "nice" failures (user input error); another raises ValueError for "hard" failures (corrupted data). Discuss the difference with students.

5. **Compare two patterns:** Have students implement the same validation using boolean returns and another using raising ValueError. Discuss when to use each in a larger team project.

6. **Bonus: Separate validation from update:** Add a method like `is_valid_phone(phone_str)` that returns boolean without modifying anything. Use it to validate *before* calling `update_phone()`. This teaches the single-responsibility principle.

7. **Real-world validation:** Discuss formats like E.164 (international phone standard). Show how a real phone validator works (they can peek at a library like `phonenumbers`). Emphasize: "Real validation is complex; for this course, we keep it simple."

### Technology Notes

- **Live coding:** Type slowly. Narrate as you type so learners can follow. Pause for questions.
- **Error tolerance:** If you mistype, fix it live. This is modeling real debugging. Say: "Oops, I made a typo. Let me fix that. Notice the error message? That's how Python tells us what went wrong."
- **Save/share code:** Consider sharing your demo file with the class afterward (via LMS, Slack, email, or repo link). Label it `hour39_demo.py` so they can reference it later.
- **Breakpoints/print debugging:** If code isn't working during demo, add `print()` statements to show what's happening. This models debugging technique.

### Addressing Common Struggles

**Student says: "My validation code works, but it's really long. Is that okay?"**  
Answer: "Great question! Yes, it's okay if it's clear and correct. As you learn more, you'll find ways to make it more concise. For now, clear and correct is more important than short."

**Student says: "Why do we need to return True/False? Why not just update or not?"**  
Answer: "Excellent question! The boolean return lets the UI know what happened. Did it work or not? The UI needs to know so it can tell the user. If we just silently update or don't, the user is confused."

**Student says: "Can I use an `if`/`else` without `return`?"**  
Answer: "Definitely. Here's an alternative..." (Show both patterns.) "Either way, the key is: validate first, then update."

**Student says: "What if someone edits the file and changes the validation rules?"**  
Answer: "Good thought! This is why we put validation *inside the class*. All the code that creates or updates contacts goes through the class. The validation is protected in one place. Later, you'll learn about access control (private attributes) to prevent direct edits."

### Instructor Reflection Questions (For You, After Class)

1. Did students understand that validation belongs in the class, not the menu?
2. Did anyone successfully use the boolean return pattern to guard their data?
3. Which students struggled with the boolean logic? Do they need a 1-on-1 check-in?
4. Did the BankAccount practice example help, or would a different example have been clearer?
5. Are students ready to move to exception handling and file I/O, or do they need more practice with validation patterns?

---

## Session Wrap-Up Checklist

Before you dismiss the class:

- [ ] Did learners get their `update_phone` method working?
- [ ] Did at least 3–4 learners verbally confirm they understand the boolean return or exception pattern?
- [ ] Did you circulate and spot-check for the common pitfalls above?
- [ ] Did you reinforce the key message: "Validation lives in the class, not the menu"?
- [ ] Do learners know what's coming next (checkpoint + file I/O)?

---

**End of Hour 39 Lecture Script**
