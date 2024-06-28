# 1. function to count factorial on based on given number
# 2. apply map on factorial function with given list of numbers
# 3. write decorator to count how much time function have worked in seconds (print debug messages - result sec: {})
# 4. add debug message of functional call name
# 4.1 add debug message of args and kwargs sent to function

import time

n = [3, 5, 6]

# def dec(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper


def decorator(func):

    def wrapper(*args, **kwargs):
        print(f"func_name: {func}")
        start = time.time()
        result = func(*args, **kwargs)
        print(f"args and kwargs sent to: {func}")
        end = time.time()
        taimer = end - start
        print(f"result sec: {taimer}")
        return result

    return wrapper


# @decorator
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


"""
iterable => list, tuple, set, dict...
map(function, iterable) =>
---
for i in iterable:
    return function(i)
"""
print(list(map(factorial, n)))

# 1 = dec_func = decorator( function ) => deco func preparation
# 2 = list(map(dec_func, iterable)) => function map result with deco func

a = decorator(factorial)
print(list(map(a, n)))
