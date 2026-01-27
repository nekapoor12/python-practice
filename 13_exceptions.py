"""
13_exceptions.py
This file demonstrates exception handling in Python:
- try
- except
- else
- finally
"""

# Example 1: Handling division by zero
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integers!")

else:
    print("Division successful.")

finally:
    print("This block always executes.")

print("-" * 40)

# Example 2: Manually raising an exception
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above!")

print("You are eligible.")

print("Program finished successfully.")


What This File Covers

✔ try

✔ except

✔ else

✔ finally

✔ raise
