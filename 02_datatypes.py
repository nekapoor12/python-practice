"""
02_datatypes.py
This file demonstrates different built-in data types in Python.
"""

# Integer
a = 10
print("a =", a, "Type:", type(a))

# Float
b = 3.14
print("b =", b, "Type:", type(b))

# String
c = "Hello Python"
print("c =", c, "Type:", type(c))

# Boolean
d = True
print("d =", d, "Type:", type(d))

print("-" * 40)

# List (mutable)
e = [1, 2, 3, 4]
print("e =", e, "Type:", type(e))

# Tuple (immutable)
f = (1, 2, 3, 4)
print("f =", f, "Type:", type(f))

# Set (unique elements)
g = {1, 2, 3, 3, 4}
print("g =", g, "Type:", type(g))

# Dictionary (key-value pairs)
h = {"name": "Neha", "age": 26}
print("h =", h, "Type:", type(h))

print("-" * 40)

# Type conversion
x = "100"
print("Before conversion:", x, "Type:", type(x))

y = int(x)
print("After conversion:", y, "Type:", type(y))

z = float(y)
print("Float conversion:", z, "Type:", type(z))

print("Program finished successfully.")


What This File Covers

✔ int, float, str, bool

✔ list, tuple, set, dict

✔ type()

✔ Type conversion
