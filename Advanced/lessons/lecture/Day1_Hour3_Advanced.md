# Day 1, Hour 3: Properties, Invariants, and Custom Exceptions

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 1 (Hour 3 of 48)
- **Focus**: Object validation with `@property`, enforcing invariants, and custom exceptions.
- **Goal**: Teach students how to bulletproof their class models and communicate domain errors cleanly.

---

## 1. Properties, Invariants, and Custom Exceptions (10-20 minutes)

**Instructor Talk Points:**

- **Invariants:** "An 'invariant' is a rule about your object that must always be true. For example: A bank account balance cannot be 'banana'. A task cannot have a negative priority. If an invariant is violated, the object is mathematically invalid."
- **Properties as Controlled Access:** "How do we enforce these rules? In basic Python, you might just do `person.age = -5`. In Advanced Python, we enforce invariants by using the `@property` decorator to turn attribute access into a controlled method call. We validate the data before it gets stored."
- **Custom Exceptions:** "When validation fails, what do we do? We don't just return `None` or `False`. Returning `False` is silent failure—the developer calling your code might ignore it. We raise an Exception. Even better, we define our own domain-specific Exceptions like `ValidationError` rather than using a generic `ValueError`."

## 2. Live Demo: Validated Properties and Custom Exceptions (5-10 minutes)

**Live Demo Steps:**

1. **Defining a Custom Exception:**
   "First, let's create a custom exception so we can specifically catch validation issues."
   ```python
   class ValidationError(Exception):
       """Raised when domain rules are violated."""
       pass
   ```

2. **Using `@property`:**
   "Now, let's look at a basic `Task` class and add validation to its `priority` attribute. We don't want any priority lower than 1."
   ```python
   class Task:
       def __init__(self, title, description, priority=1):
           self.title = title
           self.description = description
           # Look carefully! We use the property setter here implicitly:
           self.priority = priority 

       @property
       def priority(self):
           return self._priority

       @priority.setter
       def priority(self, value):
           if not isinstance(value, int) or value < 1:
               raise ValidationError(f"Priority must be an integer >= 1. Got: {value}")
           self._priority = value
   ```
   "Notice the underscore in `self._priority`. This indicates it's a 'private' backing store. The property acts as the front door, validating anyone who tries to enter."

3. **Raising and Catching:**
   ```python
   try:
       # Let's try to break it
       t = Task("Clean Desk", "Tidy up workspace", priority=-1)
   except ValidationError as e:
       print(f"Failed to create task: {e}")
   ```
   "See how clean that is? The model protects itself. The UI (this `try/except` block) catches our specific `ValidationError` and decides what to print."

## 3. Hands-on Lab: Validation + Exceptions (25-35 minutes)

**Lab Prompt for Students:**

"Let's bulletproof the models you created in Hour 2."

1. **Add Validation:** Choose an attribute on your primary capstone model. Turn it into a property (`@property` getter and setter). Add at least one validation rule to it (e.g., non-empty name, positive amount, valid email format).
2. **Define Custom Exceptions:** Define at least two custom exceptions for your domain errors: `ValidationError` and `NotFoundError`. 
3. **Raise Exceptions:** Update a service function or your model constructor to raise these exceptions when bad inputs are provided or an item cannot be found.
4. **Catch Execution:** Write a short script simulating the UI that tries to assign bad data, catches your specific `ValidationError`, and prints a user-friendly error message.

**Instructor: Circulate and check:**
- **Pitfall Warning:** Ensure they aren't catching `Exception` broadly (`except Exception:`). By catching the broad base `Exception`, they hide typos, syntax errors, and unexpected issues. Enforce catching the specific `ValidationError`.
- Ensure they are using the underscore (`_`) for the backing variable in their property. Without the underscore inside the setter, `self.attr = value` will call the setter again recursively, causing a recursion error!

*Optional Extensions for fast finishers:*
- Add an `error_message` attribute to your custom exception class so it can store a structured dictionary of field errors (e.g., `{"age": "Must be > 0", "name": "Required"}`).
- Add a helper method to normalize user input before validation (e.g., stripping whitespace and capitalizing names).

## 4. Debrief and Quick Check (5 minutes)

- **Debrief:** Have someone share their custom exception logic and a specific rule they enforced.
- **Quick Check Question:** "Why is raising and catching a specific `ValueError` or a custom `ValidationError` better than catching everything with a bare `except Exception:` block?"
  - *Answer:* Because catching all exceptions will silently hide completely unrelated bugs, like missing variables, typos, or fundamental system errors. You should only catch the errors you expect to handle.
- **Wrap-up:** "Your models are now secure from bad data. In the final hour of today, we are going to look at architectural design principles: determining when to inherit from a class, and when to compose a class alongside others."
