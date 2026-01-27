"""
12_file_handling.py
This file demonstrates file handling in Python:
- Writing to a file
- Reading from a file
"""

# Writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("This file is created using Python.\n")
file.close()

print("Data written to file successfully.")

print("-" * 40)

# Reading from the file
file = open("sample.txt", "r")
content = file.read()
file.close()

print("Reading data from file:")
print(content)

print("-" * 40)

# Appending to the file
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()

print("Data appended to file successfully.")

print("-" * 40)

# Reading again
file = open("sample.txt", "r")
content = file.read()
file.close()

print("Final file content:")
print(content)

print("Program finished successfully.")

What This File Covers

✔ open()

✔ write()

✔ read()

✔ append mode

✔ close()
