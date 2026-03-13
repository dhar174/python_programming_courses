# Day 2, Hour 1: Pattern: Factory (practical creation + validation)

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 2 (Hour 5 of 48)
- **Focus**: The Factory Pattern for object creation and validation
- **Prerequisites**: Comfort with basic classes and initialization
- **Goal**: Teach students how to extract complex creation and validation logic out of `__init__` into dedicated factory methods.

---

## 1. Instructor Talk Points (10–20 minutes)

**Instructor Talk Points:**

- **The Problem with `__init__`**: "When we build objects, especially from external data like JSON or user input, we often need to validate fields, supply defaults, or transform data types. If we put all of that logic inside `__init__`, our initialization method becomes huge, hard to test, and violates the Single Responsibility Principle. `__init__` should just initialize an object."
- **Why Factories**: "The Factory Pattern solves this. A factory is a function or class method whose single job is to assemble and return a new object. By centralizing creation logic, we enforce consistent creation rules and reduce duplicated code across our app."
- **Factory Responsibilities**: "A good factory ensures that any object it returns is fully valid. It normalizes inputs and raises clear exceptions (like our custom `ValidationError` from yesterday) if it can't build the object. This guarantees that once an object exists in memory, it is safe to use."
- **Implementation in Python**: "In Python, we don't always need complex 'Factory Classes' like in Java. Often, a simple `@classmethod` like `Record.from_dict()` or a standalone function like `create_record()` works perfectly and is highly Pythonic."

## 2. Live Demo: Factory Implementation (5–10 minutes)

**Live Demo Steps:**

1. **Setup the Baseline**:
   *(Action: Create a simple `User` class with a basic `__init__`.)*
   "Let's say we have a simple model and we're getting raw, unvalidated JSON-like dictionaries."
   ```python
   # Demo: models.py
   class User:
       def __init__(self, full_name, role):
           self.full_name = full_name
           self.role = role
   ```

2. **Build the Factory**:
   *(Action: Add a `@classmethod` acting as our factory.)*
   "Instead of cluttering `__init__`, let's build `UserFactory.from_dict()`"
   ```python
   class UserFactory:
       @classmethod
       def from_dict(cls, data):
           # 1. Validation
           if "name" not in data:
               raise ValueError("Missing required field: 'name'")
           
           # 2. Normalization / Defaults
           name = data["name"].strip().title()
           role = data.get("role", "member").lower()
           
           # 3. Validation of values
           if role not in ["admin", "member", "guest"]:
               raise ValueError(f"Invalid role: {role}")
               
           # 4. Creation
           return User(full_name=name, role=role)
   ```

3. **Demonstrate Usage**:
   *(Action: Show valid and invalid input handling.)*
   ```python
   # Valid input
   good_data = {"name": "  alice smith  ", "role": "ADMIN"}
   user = UserFactory.from_dict(good_data)
   print(f"Created: {user.full_name}, {user.role}")

   # Invalid input - missing field
   try:
       bad_data_1 = {"role": "member"}
       UserFactory.from_dict(bad_data_1)
   except ValueError as e:
       print(f"Caught error: {e}")
       
   # Invalid input - bad role
   try:
       bad_data_2 = {"name": "Bob", "role": "superadmin"}
       UserFactory.from_dict(bad_data_2)
   except ValueError as e:
       print(f"Caught error: {e}")
   ```
   "Notice how all the messy parsing rules are hidden away in the factory?"

## 3. Hands-on Lab: Factory Implementation (25–35 minutes)

**Lab Prompt for Students:**
"Now, implement a factory for your Tracker capstone model."

1. **Implement the Factory**: Create a factory method (e.g., a `@classmethod` named `from_dict`) that creates your primary model class from a dictionary (simulating JSON input).
2. **Add Validation**: Ensure it checks for required fields. If fields are missing, raise the custom exception you built yesterday (e.g., `ValidationError`).
3. **Add Defaults**: Use `.get(key, default)` to supply default values for optional fields (like setting 'status' to 'pending').
4. **Test It**: Write a small block of code to load two sample records from hard-coded dictionaries—one valid, one invalid. Print the successful object and capture the exception for the invalid one.

*Optional Extensions for fast finishers:*
- Add a second factory method `from_user_input()` that takes separate string arguments, strips whitespace, and enforces capitalization rules.

**Instructor: Circulate and check:**
- **Common Pitfall**: Are they trying to serialize custom objects directly without conversion?
- **Common Pitfall**: Are they using silent defaults (e.g., returning `None` for a name) that hide mistakes instead of failing fast?
- Make sure they are raising exceptions to block invalid data.

## 4. Quick Check / Exit Ticket (5 minutes)

- **Quick Check Question:** "What's the main benefit of centralizing creation logic into a factory rather than putting it in `__init__` or spreading it across your application?"
  - *Answer:* It enforces consistent creation and validation rules in one place, keeping `__init__` clean and adhering to the Single Responsibility Principle. All objects created are guaranteed to be in a valid state.
- **Wrap-up:** "Excellent. Now that we can reliably create valid objects, next hour we'll look at the Strategy Pattern to dynamically swap how we process or filter those objects."
