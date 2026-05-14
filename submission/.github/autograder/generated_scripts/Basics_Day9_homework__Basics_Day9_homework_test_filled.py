#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 9 Homework (Filled Test Submission)
# 
# This sample submission is used for local and CI autograder validation.
# 

# In[ ]:


import math
from math import sqrt

GLOBAL_DISCOUNT_RATE = 0.10
GLOBAL_SCORE = 0

def greet_user(name: str) -> str:
    return f"Hello, {name}!"

def compute_order_total(unit_price: int, quantity: int) -> int:
    return unit_price * quantity

def format_receipt_line(item_name: str, total: int) -> str:
    return f"{item_name} -> {total}"

def apply_discount(price: float, discount_rate: float = 0.10) -> float:
    return price - (price * discount_rate)

def build_greeting(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

def explain_shadowing(local_score: int) -> str:
    return f"local score = {local_score}, global score = {GLOBAL_SCORE}"

def add_name_in_place(names: list[str], new_name: str) -> None:
    names.append(new_name)

def uppercase_copy(names: list[str]) -> list[str]:
    return [name.upper() for name in names]

def add_contact(contacts: dict[str, str], name: str, phone: str) -> dict[str, str]:
    updated = dict(contacts)
    updated[name] = phone
    return updated

def format_username(name: str) -> str:
    return name.strip().lower()

def main() -> None:
    learner_name = "Ava"
    item_name = "notebooks"
    total = compute_order_total(7, 3)
    print("Function defined: greet_user(name)")
    print(f"Greeting return: {greet_user(learner_name)}")
    print(f"Order total return: {total}")
    print(f"Receipt line: {format_receipt_line(item_name, total)}")
    print("Return beats print: saved result for later use")

    print(f"Global rate stays: {GLOBAL_DISCOUNT_RATE}")
    print(f"Scoped discount on 50.0 -> {apply_discount(50.0)}")
    print(f"Shadowing demo: {explain_shadowing(5)}")
    print(f"Default greeting: {build_greeting('Mia')}")
    print(f"Custom greeting: {build_greeting('Mia', 'Welcome back')}")

    roster = ["ava", "ben"]
    add_name_in_place(roster, "cora")
    uppercase_version = uppercase_copy(roster)
    contacts = add_contact({"Ava": "555-0101", "Ben": "555-0102"}, "Cora", "555-0103")
    print(f"Mutated roster: {roster}")
    print(f"Returned uppercase copy: {uppercase_version}")
    print(f"Original roster preserved after copy: {roster}")
    print("Updated contacts: Ava=555-0101, Ben=555-0102, Cora=555-0103")
    print("Docstring note: say whether your function mutates or returns new data")

    print(f"math.sqrt(81) -> {math.sqrt(81)}")
    print("Module import style: math.sqrt keeps the module namespace clear")
    print(f"Specific import style: sqrt(49) -> {sqrt(49)}")
    print(f"Custom helper preview: format_username('Charles') -> {format_username('Charles')}")
    print("Naming warning: do not name your file random.py")

if __name__ == "__main__":
    main()

