"""
04_conditions.py
This file demonstrates conditional statements in Python:
- if
- elif
- else
"""

# Example 1: Check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("-" * 40)

# Example 2: Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

print("Program finished successfully.")


What This File Covers

✔ if

✔ elif

✔ else

✔ Logical conditions
