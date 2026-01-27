"""
17_lambda.py
This file demonstrates lambda (anonymous) functions in Python.
"""

# Normal function
def add(a, b):
    return a + b

print("Normal function add(10, 20):", add(10, 20))

# Lambda function
add_lambda = lambda a, b: a + b
print("Lambda function add(10, 20):", add_lambda(10, 20))

print("-" * 40)

# Lambda with map()
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print("Squares using lambda + map:", squares)

print("-" * 40)

# Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda + filter:", even_numbers)

print("Program finished successfully.")

What This File Covers

✔ Lambda functions

✔ map()

✔ filter()
