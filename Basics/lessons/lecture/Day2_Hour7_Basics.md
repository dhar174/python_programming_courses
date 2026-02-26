# Hour 7: Input/Output + Type Conversion
Python Programming (Basic) • Day 2, Session 2

---

## Learning Outcomes
- Collect user input and convert types safely (happy path)
- Explain why input() returns a string
- Apply int() and float() for numeric conversions

---

## The input() Function

### Always Returns a String
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(type(name))  # <class 'str'>

age = input("Enter your age: ")
print(type(age))   # <class 'str'> - NOT int!
```

### Why This Matters
```python
age = input("Enter your age: ")  # User types 25
# age is "25", not 25
next_year = age + 1  # TypeError!
```

---

## Type Conversion Functions

### Converting to Numbers
```python
# String to integer
age_str = "25"
age = int(age_str)
print(age + 1)  # 26

# String to float
price_str = "19.99"
price = float(price_str)
print(price * 2)  # 39.98
```

### Converting Input Directly
```python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

---

## Common Conversion Patterns

### Safe Patterns for Numeric Input
```python
# Integer input
quantity = int(input("How many? "))

# Float input
temperature = float(input("Temperature: "))

# Combine operations
print(f"Double: {quantity * 2}")
```

### When Conversion Fails
```python
# If user types "abc" instead of a number:
# ValueError: invalid literal for int()
```

---

## ValueError Preview

### What Happens with Bad Input
```python
# User enters "hello" when asked for a number
number = int("hello")  # ValueError!
```

### For Now: Assume Valid Input
- In this hour, we practice the "happy path"
- Full error handling comes later (exceptions)
- Mention: "We'll learn to handle bad input later"

---

## Demo: Simple Converter

### Show Type Conversion in Action
```python
# Temperature converter (F to C)
fahrenheit = input("Enter temperature in °F: ")
print(f"Input type: {type(fahrenheit)}")

# Convert to float for math
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9

print(f"Fahrenheit type: {type(fahrenheit)}")
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

---

## Demo: Show ValueError

### What Happens with Non-Numeric Input
```python
# This will crash if user enters text
number = int("3.5")  # ValueError!
# Can't convert "3.5" directly to int

# Correct approach:
number = int(float("3.5"))  # 3
# Or just use float if decimals expected
```

---

## Lab: Unit Converter

**Time: 25-35 minutes**

### Tasks
- Choose: miles→km OR °F→°C
- Ask user for a number
- Convert and print formatted output

### Conversion Formulas
- Miles to km: `km = miles * 1.60934`
- °F to °C: `celsius = (fahrenheit - 32) * 5 / 9`

---

## Lab: Example Interaction

### Miles to Kilometers
```
=== Miles to Kilometers Converter ===
Enter distance in miles: 10
10.0 miles = 16.09 kilometers
```

### Fahrenheit to Celsius
```
=== Temperature Converter ===
Enter temperature in °F: 98.6
98.6°F = 37.0°C
```

---

## Lab: Sample Solution Structure

```python
# Miles to Kilometers
print("=== Miles to Kilometers Converter ===")
miles = float(input("Enter distance in miles: "))

# Convert
km = miles * 1.60934

# Display with formatting
print(f"{miles} miles = {km:.2f} kilometers")
```

---

## Lab: Alternative Solution (Temperature)

```python
# Fahrenheit to Celsius
print("=== Temperature Converter ===")
fahrenheit = float(input("Enter temperature in °F: "))

# Convert
celsius = (fahrenheit - 32) * 5 / 9

# Display with formatting
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

---

## Completion Criteria (Hour 7)

✓ Correct conversion on sample input  
✓ Readable output with units  
✓ Uses proper type conversion

---

## Common Pitfalls (Hour 7)

⚠️ **ValueError when user types text**
```python
# Remind learners: for now, assume valid input
# We'll handle errors properly later
```

⚠️ **Hard-coded constants wrong**
```python
# Double-check your conversion factors!
# Miles to km: 1.60934
# F to C: (f - 32) * 5/9
```

---

## Optional Extensions

- Add a menu to choose conversion type (no loops yet)

```python
print("1. Miles to Kilometers")
print("2. Fahrenheit to Celsius")
choice = input("Choose (1 or 2): ")

if choice == "1":
    # miles conversion
    pass
elif choice == "2":
    # temperature conversion
    pass
```

---

## Quick Check

**Question**: What happens if you call `int()` on `'3.5'`?

**Answer**: `ValueError` — Python cannot convert a string with a decimal point directly to int. Use `int(float('3.5'))` if you need the integer value (3).

---
