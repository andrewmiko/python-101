"""
Task 5: Decorators

Objective: Demonstrate proficiency in creating and using decorators in Python.

Problem:
Write a Python program that includes a decorator to measure the execution time of a function. Apply this decorator to a function that calculates the factorial of a given number.

Factorial: 6 is 1*2*3*4*5*6 = 720

Expected Output:

    •	The factorial of the number.
    •	The execution time of the function.

---
Execution time: 0.0 seconds
Factorial of 6 is 720
"""

import time


def decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)
        end = time.time()

        overal_time = end - start
        print("Execution time:", overal_time, "seconds")
        return result

    return wrapper


@decorator
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        #something = ("Factorial of",n,"is", factorial)
    return factorial


x = 6
print(f"Factorial of {x} is: {factorial(x)}")
# print("Factorial of",x,"is", factorial(x))
