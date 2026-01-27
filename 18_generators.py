"""
18_generators.py
This file demonstrates generators and the use of yield in Python.
"""

# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
print("Numbers generated using generator:")

for num in count_up_to(5):
    print(num)

print("-" * 40)

# Another generator example: even numbers
def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

print("Even numbers up to 10:")

for num in even_numbers(10):
    print(num)

print("Program finished successfully.")


What This File Covers

✔ Generator function

✔ yield keyword

✔ Iterating over generator
