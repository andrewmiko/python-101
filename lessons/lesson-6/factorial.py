# 1. function to count factorial on based number
# 2. apply map or factorial function with given list of numbers
# 3. write decorator to count how much time function have worked

import time

factorial_7 = 5040
numbers = [1, 3, 7, 9, 11, 13]


def decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"end-result: {end-start}")
        return result

    return wrapper


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


# Works, but there is questions
# def factorial_list(numbers):
#     result = []
#     for n in numbers:
#         factorial = 1
#         for i in range(1, n + 1):
#             factorial = factorial * i
#         result.append(factorial)
#     return result


# ?
# def factorial1(numbers):
#     # numbers = [1, 3, 7, 9, 11, 13]
#     factorial = 1
#     for num in range(1, numbers+1):
#         # 1: num = 1
#         factorial = factorial * num
#     return map(factorial1, numbers)

# Working - OK
# print(list(map(factorial, numbers)))

# des = decorator(factorial)
# print(list(map(des, numbers)))

# map(func, list)
# map => func(n) [n is from list]
"""
map(func, items):
map(factorial1, numbers)
# numbers = [1, 3, 7, 9, 11, 13]
for n in numbers:
    => 1
=>
for i in items:
    return func(i)
"""

# print(list(factorial1(numbers)))
# print(factorial_list(numbers))

# import math
# factorials = factorial_list(numbers)
# print(list(map(math.sqrt, factorials)))

# Should be correct
# map(factorial, numbers)