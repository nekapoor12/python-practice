1. Convert a tuple into a list, modify the list, and convert it back to a tuple.

t = (1, 2, 3, 4, 5, 6)
print("original tuple", t)

lst = list(t)
print("original list", lst)

lst.append(7)
lst[0] = 100

print("modified list",lst)

lst = tuple(lst)
print("modified tuple",lst)

output:
original tuple (1, 2, 3, 4, 5, 6)
original list [1, 2, 3, 4, 5, 6]
modified list [100, 2, 3, 4, 5, 6, 7]
modified tuple (100, 2, 3, 4, 5, 6, 7)


2. Given a tuple (1,2,3,4,5), create a new tuple containing only even numbers.

t = (1,2,3,4,5)
even_tuple = tuple(i for i in t if i%2==0)
Print(even_tuple)

Output:
(2, 4)

3. Write a program to find the index of an element in a tuple without using index().

name = ("neha", "rani", "kapoor")
x = "rani"

idx=0
while idx < len(name):
  if (name[idx] == x):
    print("found", x, "at index", idx)
  idx += 1

output:
found rani at index 1


nums = (1,2,3,4,5,6,7,8,9)
x = 4

idx=0
while idx < len(nums):
  if (nums[idx] == x):
    print("found x at index", idx)
  idx += 1

output:
found x at index 3


4. Check if two tuples have any common elements.

t1 = ("neha", "rani")
t2 = ("rani", "kapoor")


found = False

for i in t1:
  if i in t2:
    print("found the common name", i)
    found = True
    break
if not found:
  print("not found")

output: 
found the common name rani


 5. Create a tuple of 5 user inputs and calculate their sum.

nums = []

for i in range(5):
  nums.append(int(input("enter the number: ")))

nums = tuple(nums)

print("tuple:", nums)
print("sum:", sum(nums))

output:
enter the number: 1
enter the number: 3
enter the number: 4
enter the number: 6
enter the number: 11
tuple: (1, 3, 4, 6, 11)
sum: 25

6.Input a tuple of numbers and print only the even numbers.
nums = []
n = int(input("enter the number:"))

for i in range(4):  #n can be changes to number of inputs you want to give
  nums.append(int(input("enter the number:")))

nums = tuple(nums)
print("tuple:", nums)

for i in nums:
  if i%2==0:
    print("even numbers:",  i)

Output:
enter the number:12
enter the number:12
enter the number:13
enter the number:14
enter the number:15
tuple: (12, 13, 14, 15)
even numbers: 12
even numbers: 14
