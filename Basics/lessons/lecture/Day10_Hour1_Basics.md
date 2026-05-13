# Day 10, Hour 1: Introduction to Object-Oriented Programming – Classes, Objects, and the `self` Parameter

## 1. Learning Outcomes

By the end of this hour, students will be able to:

1. **Create a basic class using the `class` keyword with an `__init__` method** – Students will understand the syntax and structure of Python class definitions, including the constructor method that initializes new objects.

2. **Instantiate objects from a class and call methods on those objects** – Students will practice creating instances and invoking methods with proper object dot notation.

3. **Distinguish between a class (blueprint) and an object (instance)** – Students will articulate how classes serve as templates and objects represent concrete instances with their own state and behavior.

4. **Use instance attributes with the `self` parameter to store object-specific data** – Students will understand how `self` enables each object to maintain unique attribute values independent of other instances.

5. **Understand the role of methods and the `self` parameter in class behavior** – Students will recognize that `self` is a reference to the current object and that methods operate on that object's data.

---

## 2. Instructor Prep

### Learning Context & Prerequisites
Before teaching this hour, ensure students are comfortable with:
- **Function definitions and calls** – They should know how to write `def func():` and call `func()`.
- **Dictionaries and key-value pairs** – Objects use attributes similar to dictionary key-value storage.
- **Conditional logic and loops** – Essential for practice exercises and lab work.
- **Variable scope** – Helps explain why `self` is necessary to distinguish instance attributes.

### Setup & Materials Needed

**Code Examples Prepared Ahead:**
1. A simple `Contact` class with `__init__`, attributes, and a display method (provided in Live Demo).
2. A `Book` class for the guided practice walkthrough.
3. A partially completed `BankAccount` class for the lab exercise.

**Code Environment:**
- Python 3.x (3.8+) installed and verified.
- Interactive Python terminal (REPL) or Jupyter Notebook for live demonstrations.
- All code examples saved in plain `.py` files in your instructor directory for quick copy-paste.

**Student Materials:**
- Access to Python IDE (VS Code, PyCharm, or Thonny) or cloud-based Python (Replit, Google Colab).
- Blank starter files for the practice walkthrough and lab exercise provided in advance.

### Common Pitfalls to Watch For
1. **Forgetting the `self` parameter** – Students often write `def __init__(name):` instead of `def __init__(self, name):`.
2. **Confusing class attributes with instance attributes** – Emphasize that each object has its own copy of attributes.
3. **Not calling methods correctly** – Students may try `Contact.display()` instead of `contact.display()` (forgetting the instance).
4. **Treating `__init__` as optional** – Reinforce that `__init__` is the standard way to initialize objects (though not strictly mandatory).
5. **Misunderstanding `self`** – Students sometimes think `self` is a keyword like `def`; clarify it is just a variable name by convention.

### Timing Breakdown (25–35 minutes for lab)
- **Opening & Context** (2 min)
- **Concept Briefing** (6–7 min)
- **Live Demo with Contact Class** (4–5 min)
- **Guided Practice Walkthrough** (5–6 min)
- **Lab Exercise with Checkpoints** (8–10 min)
- **Wrap-Up & Quick Questions** (2 min)

---

## 3. Opening Script

**[Read verbatim or closely paraphrase the following to open the hour]**

"Welcome to Hour 37! Today we're crossing into one of the most powerful and widely used features of Python: Object-Oriented Programming, or OOP. 

So far, we've built programs using functions and data structures like lists and dictionaries. But what if we could bundle data and the functions that operate on that data into a single, reusable package? That's exactly what OOP lets us do.

Think about a real-world scenario. A bank might manage thousands of accounts. Each account has properties—like a balance and an account holder's name—and actions that you can perform on it—like depositing or withdrawing money. In procedural programming, we'd write separate functions and pass data to them. But in OOP, we can model a 'BankAccount' as a class that bundles everything together: the account properties and the operations specific to accounts.

Today, we'll introduce the fundamentals: **what classes are, how to define them, how to create objects (called 'instantiating'), and how the special `self` parameter works.** We'll start simple and build up to a practical lab where you'll create your own class. By the end of this hour, you'll have the mental model and hands-on experience to build real-world object-oriented solutions."

---

## 4. Concept Briefing

### 4.1 What Is a Class?

A **class** is a blueprint or template for creating objects. Just as a cookie cutter defines the shape of cookies you make, a class defines the structure and behavior of objects you create. Think of a class as a factory—you design the factory once, and then it produces many products (objects) all following the same design.

**Key Points:**
- A class is defined using the `class` keyword.
- It describes what attributes (data) an object will have and what methods (actions) it can perform.
- No object exists yet—the class is just a definition.
- A class is abstract until you create an instance from it.
- Multiple classes can coexist in the same program, each with different purposes.

**Example analogy:**
```
Cookie Cutter (class) → 🍪 Cookie 1, 🍪 Cookie 2, 🍪 Cookie 3 (objects/instances)
```

**Why classes matter:**
In procedural programming (the style you've used so far), you might write a function like `display_contact(name, phone)` and another like `update_contact_phone(name, phone)`. But these functions are disconnected—you have to pass all the data separately each time. With a class, all the data (name, phone) and all the operations (display, update) are bundled together into a single cohesive unit. This is especially powerful when you have many related pieces of data and many operations on that data.

### 4.2 What Is an Object (Instance)?

An **object** is a concrete realization of a class. When you use a class to create an object, that object is called an **instance** of the class.

**Key Points:**
- Each object is independent; changes to one object do not affect another.
- Each object has its own state (attribute values).
- Multiple objects can be created from the same class.

**Example:**
```python
class Contact:
    pass

# Create three objects (instances) of the Contact class
alice = Contact()
bob = Contact()
charlie = Contact()

# Each is a separate object
print(alice)     # <__main__.Contact object at 0x...>
print(bob)       # <__main__.Contact object at 0x...> (different address)
print(charlie)   # <__main__.Contact object at 0x...> (different address)
```

### 4.3 Attributes and the `self` Parameter

**Attributes** are variables that belong to an object. They store the object's state or data. Think of attributes as the "properties" or "characteristics" of an object.

The **`self` parameter** is a reference to the current object. It allows methods to access and modify the object's own attributes. Without `self`, there would be no way for a method to know which object it's operating on.

**How `self` works (detailed explanation):**
- When you call a method on an object, Python automatically passes the object as the first argument to the method.
- That argument is received as `self` inside the method.
- Inside the method, `self.attribute_name` refers to that specific object's attribute.
- `self` is not a keyword—it's just a variable name by convention. You could technically call it something else (like `this` or `obj`), but the Python community uses `self` consistently.

**Concrete `self` example with annotations:**
```python
class Contact:
    def __init__(self, name):
        self.name = name       # self refers to THIS object
        self.phone = None      # Each Contact object gets its own name and phone

# When we create an object:
alice = Contact("Alice")
# Internally, Python does: Contact.__init__(alice, "Alice")
# Inside __init__, self IS alice, so self.name IS alice.name

bob = Contact("Bob")
# Internally, Python does: Contact.__init__(bob, "Bob")
# Inside __init__, self IS bob, so self.name IS bob.name

# Now verify the independence:
print(alice.name)  # "Alice" (alice's version of name)
print(bob.name)    # "Bob" (bob's version of name)

# Each object has its own separate attributes
print(id(alice))   # Some memory address like 140234678...
print(id(bob))     # A different memory address like 140234679...
# They're completely separate objects in memory
```

**Why `self` is necessary:**
Without `self`, there would be no way for methods to distinguish between different objects:
```python
# HYPOTHETICAL (doesn't work this way):
class Contact:
    def __init__(name):  # No self!
        name = name  # Which name? The parameter? A global?
    
    def display():  # No self!
        print(name)  # Which contact's name? Impossible to know!

# The language wouldn't know which object to operate on!
```

**Instance attributes vs. local variables:**
```python
class Contact:
    def __init__(self, name):
        self.name = name  # Instance attribute—belongs to the object
        phone = "555-0000"  # Local variable—only exists in __init__
    
    def display(self):
        print(self.name)  # This works (instance attribute)
        print(phone)  # ERROR! phone only existed in __init__
```

**The `self` pattern in methods:**
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount  # Modify this object's balance
    
    def get_balance(self):
        return self.balance  # Return this object's balance

# Each method operates on the specific object it was called on:
acc1 = BankAccount(1000)
acc2 = BankAccount(500)

acc1.deposit(100)  # self is acc1; acc1.balance becomes 1100
acc2.deposit(50)   # self is acc2; acc2.balance becomes 550

print(acc1.get_balance())  # 1100 (acc1's balance)
print(acc2.get_balance())  # 550 (acc2's balance)
```

### 4.4 The `__init__` Method (Constructor)

The `__init__` method is a special method called a **constructor**. It runs automatically when you create a new object and sets up the object's initial state.

**Syntax:**
```python
class ClassName:
    def __init__(self, param1, param2):
        self.attr1 = param1
        self.attr2 = param2
```

**Key Points:**
- `__init__` has two leading and two trailing underscores (double underscore).
- It always has `self` as the first parameter.
- It runs once when the object is created: `obj = ClassName(val1, val2)`.
- It is not required (a class works without it), but it is the standard way to initialize objects.

**Why `__init__` is useful:**
Without `__init__`:
```python
class Contact:
    pass

c = Contact()
c.name = "Alice"  # Manually set attribute after creation (error-prone)
```

With `__init__`:
```python
class Contact:
    def __init__(self, name):
        self.name = name  # Attribute set up automatically, consistently

c = Contact("Alice")  # Clean and clear
```

### 4.5 Methods

A **method** is a function that belongs to a class. Methods define the actions or behaviors that objects can perform. Methods are how you interact with objects and modify their state.

**Syntax:**
```python
class ClassName:
    def __init__(self, param):
        self.param = param
    
    def method_name(self):
        # Use self to access the object's attributes
        return self.param
    
    def another_method(self, arg):
        # Methods can perform actions, modify attributes, or return values
        self.param = self.param + arg
        return self.param
    
    def action_method(self):
        # Methods don't have to return anything
        print(f"Object has param: {self.param}")
```

**Calling methods:**
```python
obj = ClassName("value")
result = obj.method_name()           # Calls method, may return a value
result2 = obj.another_method(5)      # Methods can take additional arguments
obj.action_method()                  # Call a method that doesn't return anything
```

**Method types and patterns:**

**1. Getter methods** – Return information about the object's state:
```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return self.gpa
```

**2. Setter methods** – Modify the object's state:
```python
    def set_gpa(self, new_gpa):
        self.gpa = new_gpa  # Update this object's gpa
    
    def set_name(self, new_name):
        self.name = new_name  # Update this object's name
```

**3. Action methods** – Perform an action without returning a value:
```python
    def display_info(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")
    
    def increment_year(self):
        self.year = self.year + 1
```

**4. Query methods** – Ask questions about the object's state:
```python
    def has_high_gpa(self):
        return self.gpa >= 3.5
    
    def is_passing(self):
        return self.gpa >= 2.0
```

**Why `self` in methods:**
Inside a method, `self` refers to the specific object the method was called on. This allows different objects to maintain independent state:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # self refers to the specific Circle object
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        # Again, self refers to the specific Circle object
        return 2 * 3.14159 * self.radius
    
    def scale_up(self, factor):
        # Modify this specific object's radius
        self.radius = self.radius * factor

# Create and use different circles:
circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.area())  # Uses circle1's radius (5)
print(circle2.area())  # Uses circle2's radius (10)

circle1.scale_up(2)    # Doubles circle1's radius to 10
print(circle1.radius)  # 10
print(circle2.radius)  # 10 (circle2 is unchanged)

# Both circles can call the same methods, but each operates on its own data
```

**Method interactions:**
Methods can call other methods on the same object:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def info(self):
        # One method calling another method
        area = self.area()
        perim = self.perimeter()
        print(f"Area: {area}, Perimeter: {perim}")

rect = Rectangle(4, 5)
rect.info()  # Calls area() and perimeter() internally
# Output: Area: 20, Perimeter: 18
```

---

## 5. Live Demo with Contact Class

**[Demonstrate this live in an interactive Python terminal. Type code line by line and show output.]**

### 5.1 Define and Instantiate a Contact Class

```python
class Contact:
    """A simple contact record."""
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
    
    def call_info(self):
        return f"Calling {self.name} at {self.phone}"

# Create two Contact objects
alice = Contact("Alice Johnson", "555-0001")
bob = Contact("Bob Smith", "555-0002")

print(alice.name)      # Output: Alice Johnson
print(bob.name)        # Output: Bob Smith
print(alice.call_info())  # Output: Calling Alice Johnson at 555-0001
```

### 5.2 Show Attribute Independence

```python
# Verify each object has its own attributes
print(f"Alice's phone: {alice.phone}")  # 555-0001
print(f"Bob's phone: {bob.phone}")      # 555-0002

# Modify one object's attributes—does not affect the other
alice.phone = "555-9999"
print(f"Alice's phone now: {alice.phone}")  # 555-9999
print(f"Bob's phone still: {bob.phone}")    # 555-0002 (unchanged)
```

### 5.3 Call Methods on Different Objects

```python
# Each object calls its own method with its own data
alice.display()
# Output:
# Name: Alice Johnson
# Phone: 555-9999

bob.display()
# Output:
# Name: Bob Smith
# Phone: 555-0002
```

### 5.4 Emphasize the `self` Connection

```python
# When we call alice.display(), Python passes alice as self
# Inside the method, self.name is alice.name
# Similarly, when we call bob.display(), self is bob

# You can verify this by looking at the object's memory address
print(id(alice))        # Some address like 140234678...
print(type(alice))      # <class '__main__.Contact'>
```

**Talking Point:** "Notice how `alice.display()` uses alice's data, and `bob.display()` uses bob's data. That's the magic of `self`—it always refers to the object the method was called on."

---

## 6. Guided Practice Walkthrough: Building a Book Class

**[Lead students through this step-by-step. Have them type along or follow along in their notebooks.]**

### 6.1 Outline the Book Class

"We're going to build a `Book` class that represents a book with a title, author, and number of pages. Let's start with the structure."

```python
class Book:
    """Represents a book with basic information."""
    
    def __init__(self, title, author, pages):
        # Set up the book's initial state
        self.title = title
        self.author = author
        self.pages = pages
```

**Talking Point:** "Notice we have three instance attributes: `title`, `author`, and `pages`. Each `Book` object will have its own copies of these."

### 6.2 Add a Display Method

```python
    def display_info(self):
        """Display the book's information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
```

**Talking Point:** "This method uses `self` to access the current book's attributes. When we call `book1.display_info()`, Python passes `book1` as `self` inside the method."

### 6.3 Add a Summary Method

```python
    def summary(self):
        """Return a brief summary of the book."""
        return f"{self.title} by {self.author} ({self.pages} pages)"
```

### 6.4 Create and Use Book Objects

```python
# Create book objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Use the methods
book1.display_info()
# Output:
# Title: 1984
# Author: George Orwell
# Pages: 328

print(book2.summary())  
# Output: To Kill a Mockingbird by Harper Lee (281 pages)

# Access attributes directly
print(f"Book 1 has {book1.pages} pages.")  # Book 1 has 328 pages.
print(f"Book 2 has {book2.pages} pages.")  # Book 2 has 281 pages.
```

**Talking Point:** "Each book object is independent. `book1` and `book2` are completely separate objects in memory, each with their own attribute values."

### 6.5 Demonstrate Independence

```python
# Modify one book's attributes
book1.pages = 350  # Extended edition!

print(book1.summary())  # "1984 by George Orwell (350 pages)"
print(book2.summary())  # "To Kill a Mockingbird by Harper Lee (281 pages)"
# book2 is unaffected
```

---

## 7. Lab Exercise: BankAccount Class with 7 Checkpoints

Students now build a `BankAccount` class with progressive checkpoints. Time: 8–10 minutes.

### Checkpoint 1: Define the Class and `__init__` Method

Create a `BankAccount` class with `__init__` that accepts `account_holder` and `initial_balance`:

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
```

**Verification:** Create two accounts and verify they have independent balances:
```python
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)
print(acc1.balance)  # Should print 1000
print(acc2.balance)  # Should print 500
```

### Checkpoint 2: Add a Display Method

Add a method to display the account details:

```python
    def display_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")
```

**Verification:**
```python
acc1.display_account()
# Should output:
# Account Holder: Alice
# Current Balance: $1000
```

### Checkpoint 3: Add a Deposit Method

Add a method to deposit money:

```python
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
```

**Verification:**
```python
acc1.deposit(200)  # Should print "Deposited $200. New balance: $1200"
print(acc1.balance)  # Should be 1200
```

### Checkpoint 4: Add a Withdrawal Method

Add a method to withdraw money (with a simple safety check):

```python
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"Insufficient funds. Your balance is ${self.balance}")
```

**Verification:**
```python
acc1.withdraw(300)  # Should succeed
acc1.withdraw(5000)  # Should print "Insufficient funds..."
```

### Checkpoint 5: Add a Get Balance Method

Add a simple method that returns the current balance (useful for other code to use):

```python
    def get_balance(self):
        return self.balance
```

**Verification:**
```python
current = acc1.get_balance()
print(f"Balance: ${current}")  # Should print current balance
```

### Checkpoint 6: Add a Transfer Method

Add a method to transfer funds from one account to another:

```python
    def transfer_to(self, recipient_account, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            recipient_account.balance = recipient_account.balance + amount
            print(f"Transferred ${amount} from {self.account_holder} to {recipient_account.account_holder}")
        else:
            print(f"Cannot transfer. {self.account_holder} has insufficient funds.")
```

**Verification:**
```python
acc1.transfer_to(acc2, 100)
# Should print transfer message and update both accounts
print(acc1.balance)  # Should be reduced
print(acc2.balance)  # Should be increased
```

### Checkpoint 7: Full Account Summary and Independence Check

Verify the complete class works correctly and that both accounts operate independently:

```python
print("=== Final Account Status ===")
acc1.display_account()
acc2.display_account()

# Verify independence—changing one doesn't affect the other
acc1.deposit(50)
print(f"After acc1 deposit, acc1 balance: {acc1.balance}")
print(f"After acc1 deposit, acc2 balance: {acc2.balance}")
# acc2 balance should remain unchanged
```

---

## 8. Troubleshooting Common Issues

### Issue 1: "NameError: name 'self' is not defined"
**Cause:** Student used `self` outside of a method, or forgot to pass `self` in the method definition.
```python
# WRONG:
class Contact:
    def __init__(name):  # Missing self
        self.name = name  # NameError: self is not defined

# RIGHT:
class Contact:
    def __init__(self, name):  # Include self as first parameter
        self.name = name
```
**Fix:** Remind students that `self` is required as the first parameter in every method. It is not optional. Every method needs it, even if the method doesn't use it:
```python
class Timer:
    def start(self):  # Even if this method doesn't use self, it still needs to be there
        print("Timer started")
```

### Issue 2: "TypeError: __init__() missing 1 required positional argument"
**Cause:** Student created an object without providing the required arguments, or the method signature expects different arguments.
```python
# WRONG:
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

alice = Contact("Alice")  # Missing phone argument
# TypeError: __init__() missing 1 required positional argument: 'phone'

# RIGHT:
alice = Contact("Alice", "555-1234")  # Provide all required arguments
```
**Fix:** Check the method signature and ensure all required arguments are provided when creating the object. If an argument is optional, use a default value:
```python
class Contact:
    def __init__(self, name, phone=None):  # phone has a default
        self.name = name
        self.phone = phone

alice = Contact("Alice")  # Now works; phone defaults to None
bob = Contact("Bob", "555-0002")  # Can also provide phone
```

### Issue 3: Modifying one object affects another
**Cause:** Students often accidentally share attribute definitions by using class-level attributes instead of instance attributes, or by assigning mutable objects (lists, dicts) that get shared.
```python
# WRONG (all instances share the same list):
class Container:
    items = []  # Class attribute—shared by ALL instances!
    
    def add_item(self, item):
        self.items.append(item)

c1 = Container()
c2 = Container()
c1.add_item("A")
print(c2.items)  # ["A"] — WRONG! c2's items should be empty

# RIGHT (each instance has its own list):
class Container:
    def __init__(self):
        self.items = []  # Instance attribute—unique per object
    
    def add_item(self, item):
        self.items.append(item)

c1 = Container()
c2 = Container()
c1.add_item("A")
print(c2.items)  # [] — CORRECT! c2's items is independent
```
**Fix:** Use `__init__` to set up instance attributes so each object gets its own copy. If you need to share data across all instances, be explicit about it:
```python
class User:
    total_users = 0  # Class attribute—shared intentionally
    
    def __init__(self, name):
        self.name = name  # Instance attribute—unique per object
        User.total_users += 1  # Explicitly access class attribute

u1 = User("Alice")
u2 = User("Bob")
print(User.total_users)  # 2 (all users share this count)
```

### Issue 4: Forgetting parentheses when calling a method
**Cause:** Student accesses the method object itself instead of calling it.
```python
# WRONG:
result = alice.display  # Returns the method object, does not call it
# <bound method Contact.display of ...>

# RIGHT:
alice.display()  # Calls the method with parentheses
```
**Fix:** Remind students that methods are functions and must be called with `()`. Without parentheses, you get the method object itself, not the result of calling it.

### Issue 5: Trying to call a method on the class instead of an instance
**Cause:** Student calls a method on the class directly, bypassing the object.
```python
# WRONG:
Contact.display()  # TypeError: display() missing 1 required positional argument: 'self'

# RIGHT:
alice = Contact("Alice")
alice.display()  # Call on the instance
```
**Fix:** Explain that methods are called on objects (instances), not on the class itself. The class is the blueprint; instances are what you call methods on:
```python
class Dog:
    def bark(self):
        print("Woof!")

# Dog is a class (blueprint)
# dog1 is an instance of the class
dog1 = Dog()
dog1.bark()  # Correct—call method on instance

# Dog.bark() doesn't work because there's no "dog" to bark
# Methods need an object to operate on
```

### Issue 6: Mixing up `self.attribute` and local variables
**Cause:** Student creates local variables instead of instance attributes, or tries to use instance attributes after they've gone out of scope.
```python
# WRONG:
class Contact:
    def __init__(self, name):
        name = name  # This creates a local variable, not an instance attribute!
    
    def display(self):
        print(self.name)  # Error: self doesn't have 'name'

# RIGHT:
class Contact:
    def __init__(self, name):
        self.name = name  # This creates an instance attribute

alice = Contact("Alice")
alice.display()  # Works correctly
```
**Fix:** Always use `self.attribute_name` to create and access instance attributes. Local variables (without `self.`) are only available within that specific method.

### Issue 7: Incorrect understanding of what `__init__` returns
**Cause:** Student tries to capture a return value from `__init__` or expects `__init__` to return the object.
```python
# WRONG:
alice = Contact.__init__("Alice")  # Incorrect usage
# OR expecting __init__ to return something

# RIGHT:
alice = Contact("Alice")  # Calling the constructor, which implicitly returns the object
```
**Fix:** Clarify that `__init__` doesn't return anything (or returns `None`). The constructor call `ClassName(...)` automatically creates and returns the new object. You don't call `__init__` directly.

---

## 9. Quick-Check Questions

Ask these questions to gauge comprehension:

1. **What is the difference between a class and an object?**
   - Expected: A class is a blueprint or template; an object is a specific instance created from that blueprint.

2. **Why do we use `self` as the first parameter in methods?**
   - Expected: `self` refers to the current object, allowing methods to access and modify that object's attributes.

3. **What does `__init__` do?**
   - Expected: `__init__` is a constructor method that runs automatically when an object is created and initializes the object's attributes.

4. **If I create two `Contact` objects and modify one's `name` attribute, does it affect the other?**
   - Expected: No, each object is independent with its own set of attributes.

5. **How do you call a method on an object?**
   - Expected: Using dot notation: `object.method()` or `object.method(arguments)`.

---

## 10. Wrap-Up & Transition

**[Summarize the hour with the following talking points]**

"Excellent work! Today you've learned the fundamentals of Object-Oriented Programming. You now understand:

- **Classes as blueprints**: A class defines the structure and behavior of objects.
- **Objects as instances**: Each object is independent with its own state.
- **The `self` parameter**: It refers to the current object, enabling each object to manage its own data.
- **Methods as actions**: Methods define what objects can do, and they operate on the object's own attributes.

These concepts form the foundation of OOP. In the next session, we'll build on this by introducing **inheritance**, where one class can extend another. But the mental model you've developed today—classes, objects, attributes, and methods—will carry forward into all advanced OOP topics.

For now, practice building small classes. The more you build, the more natural the syntax and thinking will become. In your next hour, we'll explore inheritance and see how classes can build upon each other. Great effort today!"

---

## 11. Facilitation Notes

### Pacing Strategy
- **If students are struggling:** Spend more time on Concept Briefing and Live Demo. Simplify the Book class walkthrough and reduce the number of lab checkpoints (focus on 1–3). Use simpler examples like a `Light` class (on/off, brightness) before moving to more complex ones.
- **If students are confident:** Extend the lab with additional methods (like `__str__` for better display) or challenge them to add attribute validation in `__init__`. Ask them to think about what other methods would be useful for a BankAccount.
- **Monitor comprehension throughout:** Ask students to explain concepts in their own words rather than just writing code. This reveals deeper understanding.

### Engagement Tips
- **Use real-world analogies consistently:** Compare classes to blueprints, templates, or recipes throughout the hour. Return to these analogies when students seem confused.
- **Live coding matters—type in real time:** Don't use pre-prepared slides for code. Type in the interactive terminal, not just slides. Show errors and fix them live. This models debugging and shows that errors are normal.
- **Encourage questions as learning opportunities:** OOP is conceptually new for many students. Frame questions as opportunities to deepen understanding, not as interruptions.
- **Peer explanation:** Have students explain the Contact or Book class to each other in their own words. Teaching others reinforces learning.
- **Use physical analogies:** Draw diagrams of the object, its attributes, and methods on a whiteboard. Visual representation helps abstract concepts become concrete.

### Demo Troubleshooting
- **If code fails:** Show the error message, read it aloud, explain what it means. This models debugging behavior that students should emulate.
- **If a student's code doesn't work:** Celebrate the error as a learning opportunity and work through it together with the class. Don't just fix it silently.
- **If stuck:** Step back and draw a diagram of the object, its attributes, and methods to visualize the structure. Sometimes students just need a different perspective.
- **Avoid "just works" magic:** When something works, explain why. When something fails, explain why it failed. Never gloss over the "why."

### Timing Recovery Strategies
- **Running over?** Prioritize Concept Briefing and Live Demo. The lab checkpoints can be assigned as practice homework or completed in the next session's opening minutes.
- **Ahead of schedule?** Use the extra time for deeper exploration: ask "What if we added this method?" or "How would we modify the BankAccount to track transaction history?" Have students build additional methods collaboratively.
- **Lab checkpoint overflow?** Designate some checkpoints as "homework" or "extension" tasks that students complete after class.

### Support Materials & Resources
- **Starter code availability:** Have starter code for the lab available so students can copy-paste and focus on the logic rather than syntax.
- **Reference card:** Provide a reference card with the class syntax template for students to keep as a quick reference.
- **Recorded demo:** Offer a recorded demo video for students who want to review after class.
- **Office hours cheat sheet:** Have a list of common mistakes and fixes available for students seeking help.
- **Peer review prompts:** Prepare simple prompts like "Does the method use `self` correctly?" to guide peer reviews during lab time.

### Classroom Dynamics
- **Mix up activities:** Alternate between teacher talk, live demo, guided walkthrough, and independent lab work to maintain engagement.
- **Monitor participation:** Notice who's struggling and who's comfortable. Adjust support accordingly.
- **Celebrate success:** When a student gets their first class working, acknowledge it. These small wins build confidence.
- **Normalize confusion:** Remind students that confusion is part of learning. "If you're confused, you're probably learning something new—that's exactly where we want to be."

### Post-Class Follow-Up
- **Collect completed labs:** Review a few lab implementations to identify common misconceptions for the next session.
- **Send a recap email:** Summarize key concepts and point students to resources for practice.
- **Offer practice problems:** Provide 2–3 simple class-building challenges for homework.

### Technical Setup Check (Before Class)
- ✅ Python 3.x (3.8+) installed and tested on your demo machine
- ✅ Code examples copied to your working directory and tested
- ✅ Interactive terminal (REPL) or Jupyter Notebook working
- ✅ Slides or talking points organized
- ✅ Starter code prepared and tested
- ✅ Student machines have Python available

---

## 12. Assessment & Differentiation

### Formative Assessment (During the Hour)

1. **Observation during lab work:** Are students correctly using `self`? Are they creating independent objects? Watch for: forgetting `self`, calling methods on the class instead of instances, accidentally sharing attributes between objects.

2. **Quick-check questions:** Use the 5 questions in Section 9 to gauge understanding at the end. Listen for accurate language (students should say "instance" not "copy," should understand `self` refers to the current object).

3. **Code review:** Review a few students' `BankAccount` implementations during the lab to identify misconceptions. Look for patterns (e.g., if multiple students forget `self`, spend extra time reinforcing it).

4. **Pair monitoring:** If students are working in pairs, observe their interactions. Do they explain concepts to each other? Can they debug together?

5. **Checkpoint verification:** As students complete each checkpoint, quickly verify correctness. This gives them immediate feedback and prevents errors from compounding.

### Differentiation Strategies

**For students who are struggling:**
- Reduce the scope: Focus on 2–3 lab checkpoints (e.g., just `__init__`, `display_account`, and `deposit`).
- Provide more scaffolding: Offer pseudocode or skeleton code with blanks to fill in.
- Pair them with a confident peer for the lab work.
- Use simpler examples: Use a `Lamp` class (on/off, brightness) instead of `BankAccount`. Fewer methods, fewer attributes.
- Pre-teach key concepts: Before the hour, meet with struggling students and go through a simple class example one-on-one.
- Extend examples they understand: Start with `Contact`, then extend it by adding one method at a time.

**For students who are advanced:**
- Extend the challenge: Ask them to add input validation (e.g., reject negative deposits).
- Introduce new concepts early: Show them `__str__` method to customize how objects are printed.
- Challenge them to add a `transaction_log` attribute that records all deposits and withdrawals as a list.
- Have them explain OOP concepts to the class or write a summary blog post.
- Assign a "deep dive" extension: "What other methods would a BankAccount need in real life? Build 2–3 more."
- Introduce class-level thinking: Ask them to think about what attributes and methods a `Bank` class would need (meta-thinking about class design).

**For students at grade level:**
- Standard lab with all 7 checkpoints (as designed).
- Encourage them to extend one checkpoint with additional functionality (e.g., add a fee calculation).
- Have them review and provide feedback to peers' code.

### Assessment Criteria for the Lab

A successful lab implementation should:
- ✅ Have a correctly defined `__init__` method with `self` and appropriate attributes.
- ✅ Include methods that use `self` to access and modify attributes.
- ✅ Demonstrate that two different account objects maintain independent balances.
- ✅ Show correct method calls with object dot notation (`account.method()`).
- ✅ Handle edge cases (like insufficient funds for withdrawal).
- ✅ Use appropriate variable names and consistent code style.
- ✅ Include comments explaining key sections (optional but encouraged).

**Grading rubric** (if applicable):
| Criterion | Points | Exemplary | Proficient | Developing | Beginning |
|-----------|--------|-----------|-----------|-----------|-----------|
| Class Definition & `__init__` | 20 | Correct use of `__init__`, all attributes set | Minor issues with structure | Missing attributes or incorrect `self` | No `__init__` or fundamentally broken |
| Methods & `self` | 20 | All methods use `self` correctly | Most methods correct, minor issues | Several methods missing or incorrect `self` | Methods not using `self` or missing |
| Object Independence | 20 | Two objects clearly maintain separate state | Objects mostly independent | Some attribute mixing | No evidence of independence |
| Method Calls | 20 | All calls use correct dot notation | Most calls correct | Some incorrect call syntax | Incorrect or missing calls |
| Edge Cases & Logic | 20 | Handles errors (insufficient funds, etc.) | Basic logic correct | Partial logic implementation | Logic not implemented |
| **Total** | **100** | 90–100 | 80–89 | 70–79 | <70 |

### Common Misconceptions to Address

| Misconception | Reality | How to Address |
|---|---|---|
| "`self` is a keyword like `def`" | `self` is just a variable name by convention. You could name it `this` or `obj`, but don't. | Show that `self` is just a parameter name. You could rename it, but no one does. |
| "Objects all share the same attributes" | Each object instance has its own set of attribute values. | Show two objects modifying one attribute; demonstrate the other is unaffected. |
| "`__init__` is optional" | It's not strictly mandatory, but it's the standard way to set up objects consistently. | Show the problem of manual attribute assignment vs. using `__init__`. |
| "I can call `ClassName.method()`" | Methods are called on objects: `obj.method()`. Calling on the class won't work (missing `self`). | Demonstrate the error and show why `self` is needed. |
| "Using `self.name = name` is redundant" | It's not. It distinguishes the local `name` parameter from the instance attribute `self.name`. | Show the difference: with and without `self.` |
| "Methods are like functions I've used before" | Methods are similar but tied to objects. They automatically receive `self` as the first argument. | Show the function vs. method syntax side-by-side. |

### Homework / Practice Extension

Assign one of the following to reinforce the hour's learning:

1. **Build a `Person` class** with attributes (name, age, email) and methods (greet, update_email, get_info). Example:
   ```python
   class Person:
       def __init__(self, name, age, email):
           self.name = name
           self.age = age
           self.email = email
       
       def greet(self):
           print(f"Hello, I'm {self.name}")
       
       def have_birthday(self):
           self.age += 1
   ```

2. **Expand the `BankAccount`** class by adding a `transaction_history` attribute that records each deposit/withdrawal as a list of strings. Example:
   ```python
   self.transaction_history = []
   # Then in each method, append to the list:
   self.transaction_history.append(f"Deposited ${amount}")
   ```

3. **Create a `Student` class** with (name, student_id, gpa) and methods to update_gpa, display_info, and check_standing (pass/fail based on GPA).

4. **Reflection writing:** "Explain to someone who has never programmed what a class is and why it's useful. Use the Contact or Book class as an example." (Encourage them to use their own words and analogies.)

5. **Design a class from scratch:** Pick something from your own life (Playlist, Game, Pet, Car, etc.) and design what attributes and methods it should have. Write 2–3 attributes and 2–3 methods (pseudocode is fine).

6. **Debug someone else's code:** Provide a broken BankAccount implementation with common errors and have students identify and fix them.

### Follow-Up Resources for Students

- **Python.org documentation:** https://docs.python.org/3/tutorial/classes.html
- **W3Schools OOP tutorial:** https://www.w3schools.com/python/python_oops.asp
- **Visualizer tool:** Use Python Tutor (https://pythontutor.com/) to visualize object creation and method calls step-by-step.
- **Practice problems:** Provide links to coding challenge sites (LeetCode, HackerRank, CodeWars) with beginner-level class challenges.
- **Office hours:** Make yourself available for follow-up questions on class design and `self`.

---

**End of Day 10, Hour 1 Lecture Script**
