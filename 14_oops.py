"""
14_oops.py
This file demonstrates Object-Oriented Programming concepts:
- Class
- Object
- Constructor
- Methods
- Inheritance
"""

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Derived class (Inheritance)
class Employee(Person):
    def __init__(self, name, age, emp_id):
        # Call parent class constructor
        super().__init__(name, age)
        self.emp_id = emp_id

    def display_employee(self):
        self.display()
        print("Employee ID:", self.emp_id)


# Creating objects
p1 = Person("Neha", 26)
print("Person details:")
p1.display()

print("-" * 40)

e1 = Employee("Neha", 26, "EMP101")
print("Employee details:")
e1.display_employee()

print("Program finished successfully.")

What This File Covers

✔ Class

✔ Object

✔ Constructor (__init__)

✔ Methods

✔ Inheritance

✔ super()
