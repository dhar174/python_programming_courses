# Day 1, Hour 4: Composition vs Inheritance + Polymorphism

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 1 (Hour 4 of 48)
- **Focus**: Architectural composition, limiting inheritance, and leveraging polymorphism.
- **Goal**: Teach students how to organize complex class relationships without creating rigid and brittle inheritance trees.

---

## 1. Composition vs Inheritance (10-20 minutes)

**Instructor Talk Points:**

- **The Problem with Inheritance:** "When we first learn Object-Oriented Programming, inheritance seems like the ultimate tool. Everything becomes a sub-class: `Dog(Animal)`, `Car(Vehicle)`. But in big systems, deep inheritance trees become rigid blockades. Change the base class, and you break dozens of subclasses. This is brittle design."
- **The Golden Rule:** "Inheritance is for 'is-a' relationships. Composition is for 'has-a' relationships. If an Employee *is a* Person, inheritance might work. But if an Employee *has an* Address, it shouldn't inherit from Address. It should hold an `Address` object as an attribute."
- **Polymorphism via Duck Typing:** "Python allows us to simplify branching logic using 'Polymorphism'. Polymorphism means 'many forms'. It allows different classes to share identical method signatures. Because Python uses Duck Typing ('If it walks like a duck and quacks like a duck, it is a duck'), we don't even need strict inheritance interfaces to achieve it."

## 2. Live Demo: Polymorphism and Composition (5-10 minutes)

**Live Demo Steps:**

1. **The Messy `if/elif` Branching:**
   "Let's look at an exporter script. It's a mess of if/elif statements. Every time we add a format, we have to rewrite this messy function."
   ```python
   def export_data(data, format_type):
       if format_type == "json":
           print(f"Exporting to JSON: {{'data': '{data}'}}")
       elif format_type == "csv":
           print(f"Exporting to CSV: {data}")
       elif format_type == "xml":
           print(f"Exporting to XML: <data>{data}</data>")
       else:
           raise ValueError("Unknown format")
           
   export_data("ReportData", "json")
   ```

2. **Refactoring with Polymorphism:**
   "Let's fix this heavily branched approach. We'll create separate classes that share the same action method: `export()`."
   ```python
   class JSONExporter:
       def export(self, data):
           print(f"Exporting to JSON: {{'data': '{data}'}}")

   class CSVExporter:
       def export(self, data):
           print(f"Exporting to CSV: {data}")

   # The caller doesn't care which object it gets, as long as it has an export() method.
   def generate_report(data, exporter):
       print("Preparing report...")
       exporter.export(data)  # This is polymorphism!

   json_exp = JSONExporter()
   generate_report("ReportData", json_exp)
   
   csv_exp = CSVExporter()
   generate_report("ReportData", csv_exp)
   ```
   "We just removed branching. If we want XML tomorrow, we just write an `XMLExporter` class and pass it in. We don't have to touch the `generate_report` function at all."

3. **Demonstrating Composition:**
   "Now notice `generate_report`. The report generation process *has-an* exporter. We are composing behavior here."

## 3. Hands-on Lab: Refactoring Exercise (25-35 minutes)

**Lab Prompt for Students:**

"We are going to refactor a messy script using classes and polymorphism."

1. **The Starter Code:** Start with this branching code snippet (or write your own feature with a big `if/elif` chain).
   ```python
   def process_payment(amount, method):
       if method == "credit_card":
           print(f"Processing ${amount} via Credit Card API")
       elif method == "paypal":
           print(f"Redirecting to PayPal for ${amount}")
       else:
           raise ValueError("Unknown gateway")
   ```
2. **Refactor:** Break this up into two separate strategy classes (e.g., `CreditCardProcessor` and `PayPalProcessor`). Both classes should share exactly the same method name (e.g., `pay(amount)`).
3. **Execution Interface:** Write a `Checkout` class showing *composition*. It should be initialized with the total amount and an instance of payment processor. Write a `complete_checkout()` method that calls the chosen processor.
4. **Demonstrate:** Run your `Checkout` by passing in the credit card processor, then swap it to the PayPal processor.

**Instructor: Circulate and check:**
- **Pitfall Warning:** Are students putting the `if/elif` inside the new classes? Remind them that the purpose is to eliminate the conditionals entirely by injecting the right object.
- Are they confusing Inheritance and Composition? Make sure they are instantiating the classes and associating them.

*Optional Extensions for fast finishers:*
- Add a third implementation (e.g., a Crypto/Bitcoin or Bank Transfer payment processor) and run it without changing the `Checkout` class.
- Pass the method type as a string and use a dictionary to fetch the corresponding processor instance.

## 4. Debrief and Quick Check (5 minutes)

- **Debrief:** Invite a student to display their polymorphic setup and explain why it's better than massive `if/else` statements.
- **Quick Check Question:** "Name one specific scenario where object composition is safer or more flexible than deep inheritance."
  - *Answer:* When behaviors change dynamically at runtime (like swapping payment processors), or when you want an object to have behaviors from multiple completely unrelated families (e.g., a GUI Window *has-a* Logger, but shouldn't inherit from Logger).
- **Wrap-up:** "That concludes Day 1! Great job crossing the gap between basic Python scripts and advanced object-oriented architecture. We'll start tomorrow by looking at standard creation and architectural patterns."
