"""
10_strings.py
This file demonstrates string operations and common string methods.
"""

text = "Hello Python World"

print("Original string:", text)

print("-" * 40)

# Length of string
print("Length of string:", len(text))

# Convert to upper and lower case
print("Upper case:", text.upper())
print("Lower case:", text.lower())

# Capitalize and title
print("Capitalize:", text.capitalize())
print("Title:", text.title())

print("-" * 40)

# Replace
new_text = text.replace("Python", "Programming")
print("After replace:", new_text)

# Check start and end
print("Starts with 'Hello':", text.startswith("Hello"))
print("Ends with 'World':", text.endswith("World"))

print("-" * 40)

# Split and join
words = text.split(" ")
print("Split into words:", words)

joined = "-".join(words)
print("Joined with '-':", joined)

print("-" * 40)

# Find and count
print("Index of 'Python':", text.find("Python"))
print("Count of 'o':", text.count("o"))

print("-" * 40)

# Reverse string
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

print("Program finished successfully.")

What This File Covers

✔ len()

✔ upper(), lower(), capitalize(), title()

✔ replace()

✔ startswith(), endswith()

✔ split(), join()

✔ find(), count()

✔ Reverse string
