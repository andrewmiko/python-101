"""
Task 6: Partials

Objective: Demonstrate proficiency in using partial functions in Python.

Problem:
Write a Python program that uses the functools.partial to create a partial function from the pow function (exponentiation). The partial function should always raise numbers to the power of 3. Use this partial function to calculate and print the cube of numbers from 1 to 5.

Expected Output:

    •	The cube of each number from 1 to 5, each on a new line.

---
The cube of 1 is 1
The cube of 2 is 8
The cube of 3 is 27
The cube of 4 is 64
The cube of 5 is 125
"""
from functools import partial


def pow_function(something, power):
    #n = None
    return something**power


partial_func = partial(pow_function, power=3)

#print(partial_func())

for i in range(1, 6):
    # 1, 2..5
    print(i, partial_func(i))  # 3 => 27

# a = dict.keys()
# print(a)

# if key in a:
# print(key, "exists")
