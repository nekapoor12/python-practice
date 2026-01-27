"""
19_os_module.py
This file demonstrates usage of the os module for basic system operations.
"""

import os

# Get current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

print("-" * 40)

# List files and folders in current directory
print("Files and folders in current directory:")
items = os.listdir(current_dir)
for item in items:
    print(item)

print("-" * 40)

# Create a new directory
new_dir = "test_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("Created directory:", new_dir)
else:
    print("Directory already exists:", new_dir)

print("-" * 40)

# Check if path exists
print("Does test_folder exist?", os.path.exists(new_dir))

print("Program finished successfully.")

What This File Covers

✔ os.getcwd()

✔ os.listdir()

✔ os.mkdir()

✔ os.path.exists()
