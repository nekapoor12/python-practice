"""
16_comprehension.py
This file demonstrates comprehension in Python:
- List comprehension
- Dictionary comprehension
- Set comprehension
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", numbers)

print("-" * 40)

# List comprehension: get even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers (list comprehension):", even_numbers)

# List comprehension: square of numbers
squares = [x * x for x in numbers]
print("Squares:", squares)

print("-" * 40)

# Dictionary comprehension
square_dict = {x: x * x for x in numbers}
print("Dictionary of squares:", square_dict)

print("-" * 40)

# Set comprehension
odd_set = {x for x in numbers if x % 2 != 0}
print("Odd numbers set:", odd_set)

print("Program finished successfully.")

What This File Covers

✔ List comprehension

✔ Dictionary comprehension

✔ Set comprehension
