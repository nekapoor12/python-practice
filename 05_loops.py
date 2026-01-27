"""
05_loops.py
This file demonstrates loops in Python:
- for loop
- while loop
- break
- continue
"""

# for loop example
print("For loop example:")
for i in range(1, 6):
    print("i =", i)

print("-" * 40)

# while loop example
print("While loop example:")
count = 1
while count <= 5:
    print("count =", count)
    count += 1

print("-" * 40)

# break example
print("Break example:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("-" * 40)

# continue example
print("Continue example:")
for i in range(1, 10):
    if i == 5:
        print("Skipping i =", i)
        continue
    print("i =", i)

print("Program finished successfully.")


What This File Covers

✔ for loop

✔ while loop

✔ break

✔ continue
