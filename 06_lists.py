"""
06_lists.py
This file demonstrates list operations and common list methods.
"""

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# append()
numbers.append(60)
print("After append(60):", numbers)

# insert()
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

# remove()
numbers.remove(30)
print("After remove(30):", numbers)

# pop()
removed_item = numbers.pop()
print("After pop():", numbers)
print("Popped item:", removed_item)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

print("-" * 40)

# Iterating over list
print("Iterating over list:")
for n in numbers:
    print(n)

print("Program finished successfully.")

What This File Covers

✔ List creation

✔ append(), insert(), remove(), pop()

✔ sort(), reverse()

✔ Looping through list
