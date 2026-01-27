"""
09_dictionary.py
This file demonstrates dictionary operations in Python.
"""

# Creating a dictionary
student = {
    "name": "Neha",
    "age": 26,
    "course": "Python"
}

print("Original dictionary:", student)

print("-" * 40)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

print("-" * 40)

# Adding a new key-value pair
student["city"] = "Bangalore"
print("After adding city:", student)

# Updating a value
student["age"] = 27
print("After updating age:", student)

# Removing a key
student.pop("course")
print("After removing course:", student)

print("-" * 40)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("-" * 40)

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

print("Program finished successfully.")

What This File Covers

✔ Dictionary creation

✔ Add, update, delete elements

✔ keys(), values(), items()

✔ Looping through dictionary
