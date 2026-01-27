"""
11_functions.py
This file demonstrates functions in Python:
- Simple function
- Function with arguments
- Function with return value
"""

# Simple function
def greet():
    print("Hello, welcome to Python!")

# Function with arguments
def greet_person(name):
    print("Hello", name)

# Function with return value
def add(a, b):
    return a + b

# Calling functions
greet()

greet_person("Neha")

result = add(10, 20)
print("Result of add(10, 20):", result)

print("-" * 40)

# Function with default argument
def power(base, exp=2):
    return base ** exp

print("power(5):", power(5))
print("power(5, 3):", power(5, 3))

print("Program finished successfully.")


What This File Covers

✔ Defining functions

✔ Arguments

✔ Return values

✔ Default arguments
