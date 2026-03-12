# Day 10, Hour 1: Intro classes: objects, attributes, methods (Course Hour 37)
**Python Programming Basics – Session 10**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 37 – Intro classes: objects, attributes, methods  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Emphasize the concepts of wrapping data (attributes) and behavior (methods) together into a single "blueprint" (class) before making actual "things" (objects). Keep it strictly to one simple class—do not introduce inheritance or complex class attributes.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain the difference between a class and an object.
2. Create a basic class using the `class` keyword and the `__init__` method.
3. Define instance attributes to store data inside objects.
4. Instantiate objects from a class and call their methods."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: The shift to Object-Oriented Programming (OOP)
- **0:05–0:15** Core concept: Class vs. Object, `__init__`, and attributes
- **0:15–0:25** Core concept: Methods and the `self` parameter
- **0:25–0:35** Live demo: Building a Contact class
- **0:35–0:55** Guided lab: Create and store Contact objects
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour37_classes_demo.py` ready for live coding.
- **Say:** "Please open your code editors and start a new file called `intro_to_classes.py` to type along with our examples today."

---

## 3) Opening Script: The Shift to OOP (~5 minutes)

**Say:**
"So far, we have been writing code that largely keeps data and behavior separate. We kept data in lists or dictionaries, and we wrote separate functions to process that data. For example, passing a nested dictionary of contacts into a `print_contact()` function.

While that works well for small scripts, it can become hard to manage as our programs grow. What if we could wrap the raw data and the functions that manipulate that data into one neat, bundled package?

Welcome to Object-Oriented Programming, or OOP. In OOP, we bundle data and behavior together. Today, we are going to learn how to create your own custom data structures using entirely your own rules."

---

## 4) Concept: Class vs. Object, `__init__`, and Attributes

### 4.1 Class vs. Object

**Say:**
"A **class** is a blueprint. Think of it like a factory template or an architectural blueprint for a house. It dictates what properties and actions the house should have, but you can't live in a blueprint.

An **object** is the actual house built from that blueprint. It's the physical (or in this case, digital) realization of the blueprint in the computer's memory. You can build multiple houses—multiple objects—from one blueprint."

### 4.2 The `__init__` Method and Attributes

**Type and narrate:**

```python
# hour37_classes_demo.py

class Contact:
    # __init__ sets up the object exactly when it is created
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Creating two distinct Contact objects from our blueprint
person1 = Contact("Alice", "555-0101")
person2 = Contact("Bob", "555-0202")

print(person1.name)
print(person2.phone)
```

**Say:**
"We define a class using the `class` keyword, followed by the name, usually capitalized. 

Inside the class, we have a special function called `__init__` (with two underscores on each side). This is the initializer function. It runs automatically the very second a new object is created.

Notice the word `self`. `self` refers to the *specific object* currently being created or used. When we say `self.name = name`, we are attaching the `name` argument to this specific object as an **attribute**—a piece of data stored inside the object."

---

## 5) Concept: Methods

**Say:**
"Objects don't just hold data; they can have behaviors. Functions inside a class are called **methods**. Let's add a method to our `Contact` class to display its information."

**Type and narrate:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def display(self):
        return f"Contact: {self.name} | Phone: {self.phone}"

# Testing out our method
person3 = Contact("Charlie", "555-0303")
print(person3.display())
```

**Say:**
"We added `display()`. Look at its parameter list: just `self`. When we call `person3.display()`, Python automatically passes the `person3` object in as `self` behind the scenes. This is why you must include `self` as the first parameter of any regular method! We return a formatted string that we can then easily print."

---

## 6) Live Demo: A Complete Contact Example

**Say:**
"Let's put it all together. Let's create our class and test it out by making a couple of objects."

**Type and narrate:**

```python
# A complete class demonstration

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        return f"{self.name} can be reached at {self.phone}"

# Main program demonstration
print("--- Creating Contacts ---")
my_friend = Contact("David", "555-1234")
my_coworker = Contact("Eve", "555-9876")

print("Let's look at the raw objects:")
print(my_friend) # Output will be a memory address, not very readable!

print("\nLet's use our display method instead:")
print(my_friend.display())
print(my_coworker.display())
```

**Run it and demonstrate.**

**Say:**
"Notice what happens if we print the object directly. We just get a memory location, like `<__main__.Contact object at 0x1034...>`. That's why having a `display()` method that returns a readable formatted string is so useful."

---

## 7) Hands-on Lab: Contact Class

### 7.1 Lab overview

**Say:**
"Now it's time for you to build your own `Contact` class. We are taking the first step to upgrading our old dictionary-based contact manager to use objects instead."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Contact class**

**Task:**
1. Create a `Contact` class. It should have an `__init__` method that takes `name` and `phone` and stores them as instance attributes (`self.name`, `self.phone`).
2. Add a `display()` method to the class that returns a nicely formatted string showing the contact's name and phone number.
3. In your main program space (outside the class), create at least three different `Contact` objects.
4. Store these three objects in a standard Python list, for example `my_contacts = [c1, c2, c3]`.
5. Loop through the list using a `for` loop, and call the `.display()` method on each object, printing the result.

---

**Instructor Note for Circulation:**
Look out for students forgetting the `self` parameter in `__init__` or `display`, which causes runtime errors. Point out when they accidentally declare a class attribute (outside of `__init__`) instead of an instance attribute (inside `__init__` using `self`). Ensure they are storing object instances inside the list, not strings or dictionaries.

### 7.3 Walkthrough solution

**After 20 minutes, show a brief solution:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        return f"[{self.name}] - {self.phone}"

# Main Program
contact1 = Contact("Alice Smith", "555-1111")
contact2 = Contact("Bob Jones", "555-2222")
contact3 = Contact("Carol Danvers", "555-3333")

directory = [contact1, contact2, contact3]

print("My Directory:")
for c in directory:
    print(c.display())
```

**Say:**
"Did you successfully store the objects in a list? This sets us up perfectly for the next hour, where we will build out search and update features that iterate through these lists of objects."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"We just took our first step into Object-Oriented Programming. We created a blueprint using `class`, stored data using `__init__` and instance attributes, and defined behavior using methods. Then, we brought that blueprint to life by creating object instances."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: When writing methods inside a class, what does the `self` parameter represent?"

**Expected answer:** Let them answer. "It represents the specific, current object instance being created or acted upon. It's how the object refers to its own internal data."
