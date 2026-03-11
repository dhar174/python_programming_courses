# Day 10, Hour 3: Basic encapsulation + data validation (Course Hour 39)
**Python Programming Basics – Session 10**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 39 – Basic encapsulation + data validation  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Emphasize the core concept of keeping "business rules" (validation) attached to the data model (the class), separated from the user interface (the menu `input()` logic).

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Write simple data validation rules directly inside class methods.
2. Differentiate between core business logic and User Interface (UI) logic.
3. Manage invalid data gracefully to prevent bad data from entering the system."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Guardrails for our data
- **0:05–0:15** Core concept: Encapsulation and business logic vs UI
- **0:15–0:25** Core concept: Defensive programming with `ValueError`
- **0:25–0:35** Live demo: `update_phone` method with validation
- **0:35–0:55** Guided lab: Add validation rules
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour39_validation_demo.py` ready for live coding.
- Keep the `Contact` class from the previous hour available.
- **Say:** "Please open your code editors and start a new file called `validation.py`. Paste your `Contact` class at the top. We are going to make it much smarter."

---

## 3) Opening Script: Guardrails for our data (~5 minutes)

**Say:**
"Right now, our `Contact` class allows us to put absolutely anything into the `name` and `phone` attributes. What happens if a user types a negative number for an age, or types letters instead of numbers for a phone number? Our program blindly accepts it. 

When you build real software, one of your main jobs is keeping garbage data out of your data model. We need guardrails.

The question is, *where* do we put those guardrails? Do we put them in the `while` loop menu, right after we ask the user for input? Or do we put them inside the `Contact` class itself?"

---

## 4) Concept: Encapsulation and business logic vs UI

### 4.1 Encapsulating the rules

**Say:**
"The best practice is to put the validation rules inside the class. This is called **encapsulation**. The class is a self-contained unit that 'knows' how a valid contact should look. The loop—the User Interface—shouldn't care *why* a phone number is invalid; it should just try to update the class, and the class should say 'Yes' or 'No'.

If we put the rules in the UI, and later we write another script to import contacts from a file, we would have to copy and paste all those rules again. Instead, we bundle the rules into the blueprint."

### 4.2 A naive `update_phone` method

**Type and narrate:**

```python
# hour39_validation_demo.py

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def update_phone(self, new_phone):
        # A simple check: phone numbers should be at least 7 characters
        if len(new_phone) >= 7:
            self.phone = new_phone
            return True # Tell the caller it worked
        else:
            return False # Tell the caller it failed!
```

**Say:**
"Here, the class method `update_phone` takes a new phone number. It checks the length. If it's valid, it updates the internal attribute and returns `True`. If not, it politely refuses and returns `False`."

---

## 5) Concept: Defensive programming with ValueError

**Say:**
"Returning `False` is one way to handle it. A more forceful way is to throw an error. In Python, when something goes wrong with a value's format, we can manually **raise a ValueError**.

**Type and narrate:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        # We can even use our validation upon creation!
        if not self.update_phone(phone):
             print(f"Warning: {phone} is not a valid format!")

    def update_phone(self, new_phone):
        # Removing spaces and dashes to check if it's all digits
        clean_phone = new_phone.replace("-", "").replace(" ", "")
        
        if not clean_phone.isdigit():
            # A forceful stop!
            raise ValueError(f"Phone number '{new_phone}' contains invalid characters.")
            
        if len(clean_phone) < 7:
             raise ValueError("Phone number is too short.")
             
        # If we pass all checks:
        self.phone = new_phone
        return True
```

**Say:**
"When we say `raise ValueError("message")`, we are causing the script to loudly complain and crash with our specific message. Later in this course, we'll learn how to 'catch' these errors so the program doesn't actually crash, but for now, raising an error is how the core logic clearly signals that a rule has been violated."

---

## 6) Live Demo: Wiring it to the UI

**Say:**
"Let's assume our class doesn't crash, but just returns `True` or `False`. Let's wire it up to our `while` loop menu."

**Type and narrate:**

```python
# Assuming Contact is defined above (using the True/False method)
my_contact = Contact("Alice", "555-1234")

# UI Logic
while True:
    print(f"\nCurrent phone is {my_contact.phone}")
    new_num = input("Enter new number (or 'q' to quit): ")
    
    if new_num == 'q':
        break
        
    # We call the method, and the boolean tells us what to print
    success = my_contact.update_phone(new_num)
    
    if success:
        print("Success! Number updated.")
    else:
        print("Error: The number you entered is too short. Try again.")
```

**Run it and demonstrate.**

**Say:**
"Notice how clean the `while` loop is. The loop only worries about printing strings and taking `input()`. All the heavy business rules are tucked safely away inside the `Contact` class. This separation of UI and Core Logic is a key tenet of modern software architecture."

---

## 7) Hands-on Lab: Add Validation Rules

### 7.1 Lab overview

**Say:**
"Now you're going to add validation guardrails to your Contact Manager project."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Add validation**

**Task:**
1. Open your Contact Manager script.
2. In your `Contact` class, write a method called `update_phone(new_phone)`. 
3. Inside this method, write a validation rule. For example: the phone number must be all digits (using `.isdigit()`), or it must be at least 10 characters long.
4. If it's valid, update `self.phone` and return `True`. If invalid, return `False`.
5. In your `while` loop menu, under the "Search/Update" branch, when you ask the user for a new phone number, do not set the attribute directly (e.g., *do not* write `c.phone = new_number`). Instead, call your new method (e.g., `success = c.update_phone(new_number)`).
6. If `success` is False, `print` a helpful error message to the user and prompt them again.

---

**Instructor Note for Circulation:**
Look closely at where students are writing their `if` statements. If they are writing `if new_number.isdigit():` down in the `elif choice == '3':` menu block, gently correct them. Remind them to move that logic up into the `def update_phone` block inside the class. Ensure they are using the boolean result of `update_phone` to trigger their UI `print()` statements.

### 7.3 Walkthrough solution

**After 20 minutes, show a brief snippet of the solution:**

```python
# The Class (Business Logic)
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def update_phone(self, new_phone):
        # Validation rule: must be longer than 5 chars
        if len(new_phone) >= 5:
            self.phone = new_phone
            return True
        return False

# The Menu (UI Logic snippet)
    elif choice == '3':
        target = input("Enter name to search: ")
        # ... search logic ...
        if found_obj:
            new_p = input("New phone: ")
            
            # Using the method instead of direct attribute assignment
            is_valid = found_obj.update_phone(new_p)
            
            if is_valid:
                print("Update successful.")
            else:
                print("Update failed: Phone number must be at least 5 characters.")
```

**Say:**
"Did everyone manage to keep the UI clean? The `if is_valid:` check is much easier to read than cluttering the menu with complicated validation checks."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"We explored Encapsulation. We moved data validation directly into the class blueprints so that objects can protect their own data. This is far better than relying on the UI menu loop to know the exact rules."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: Where is the best place to enforce data validation: in the user interface (the menu loop), or inside the class method?"

**Expected answer:** Let them answer. "Inside the class method! Because it keeps the rules centralized (encapsulated) in the blueprint, and keeps the UI code clean and focused only on talking to the user."
