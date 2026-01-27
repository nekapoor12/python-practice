"""
20_unittest_demo.py
This file demonstrates basic unit testing using Python's unittest module.
"""

import unittest

# Function to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

    def test_add_negative(self):
        result = add(-10, -5)
        self.assertEqual(result, -15)

    def test_subtract_zero(self):
        result = subtract(10, 0)
        self.assertEqual(result, 10)


# This allows the test to be run directly
if __name__ == "__main__":
    unittest.main()


What This File Covers

✔ What is unittest

✔ How to write test cases

✔ How to use assertEqual

✔ How to run tests



How to Run This File
In terminal:

python 20_unittest_demo.py


You should see something like:

....
----------------------------------------------------------------------
Ran 4 tests in 0.00s

OK
