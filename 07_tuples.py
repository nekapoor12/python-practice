"""
07_tuples.py
This file demonstrates tuple operations in Python.
"""

# Creating a tuple
t = (1, 2, 3, 4, 5)
print("Original tuple:", t)

# Accessing elements
print("First element:", t[0])
print("Last element:", t[-1])

print("-" * 40)

# Tuple is immutable (cannot change directly)
# So convert tuple to list, modify, and convert back

lst = list(t)
print("Converted to list:", lst)

lst.append(6)
lst[0] = 100
print("Modified list:", lst)

t = tuple(lst)
print("Converted back to tuple:", t)

print("-" * 40)

# Tuple methods
print("Count of 2 in tuple:", t.count(2))
print("Index of 4 in tuple:", t.index(4))

print("-" * 40)

# Creating a new tuple with only even numbers
even_tuple = tuple(x for x in t if x % 2 == 0)
print("Even numbers tuple:", even_tuple)

print("Program finished successfully.")

What This File Covers

✔ Tuple creation

✔ Indexing

✔ Tuple immutability

✔ Converting tuple ↔ list

✔ count(), index()

✔ Filtering even numbers
