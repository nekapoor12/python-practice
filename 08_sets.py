"""
08_sets.py
This file demonstrates set operations in Python.
"""

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

print("-" * 40)

# add()
set1.add(10)
print("After adding 10 to set1:", set1)

# remove()
set1.remove(2)
print("After removing 2 from set1:", set1)

# discard()
set1.discard(100)  # No error even if element not present
print("After discard(100):", set1)

print("-" * 40)

# Set operations
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

print("-" * 40)

# Iterating over a set
print("Iterating over set1:")
for item in set1:
    print(item)

print("Program finished successfully.")

What This File Covers

✔ Set creation

✔ add(), remove(), discard()

✔ union(), intersection(), difference(), symmetric_difference()

✔ Looping through set
