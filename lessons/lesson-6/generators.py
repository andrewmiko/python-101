# nums = range(0, 1_000_000)
# for n in nums:
#     print(n)


def infinite_sequence():
    num = 0
    while True:
        yield num  # return value and pause (wait...) 0 - pause - 1 - pause - 2 - pause ...
        num += 1


gen = infinite_sequence()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Infinite loop over generator
# for n in gen:
#     # print(n) -> print(next(n))
#     print(n)

nums_squared_lc = [num**2 for num in range(5)]  # => list
nums_squared_gc = (num**2 for num in range(5))  # => generator ()
nums_squared_tp = tuple(num**2 for num in range(5))  # => tuple (0)

print(type((0, )))  # tuple => sensative (,)!
print(type(nums_squared_lc))
print(type(nums_squared_gc))

import random


def infinite_dict():
    num = 0
    while True:
        # 1 - {0: 0}
        # 2 - {1: 1}
        # 3 - {2: 4}
        result = {
            "auto": True,
            "random_int": random.randint(0, 100),
            "result": num**2,
        }
        # print(random.choices()
        yield result
        num += 1


# for d in infinite_dict():
#     print(d)

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
# print(mylist)

# import math

# result = [5040, 24, 120, 720]
numbers = [7, 4, 5, 6]

# !7 = 1 * 2 * 3 * 4 * 5 * 6
# def factorial(n):
#     print()
#     print("#" * 10)
#     print(f"n: {n}")
#     # return math.factorial(n)
#     factorial = 1
#     for i in range(1, n + 1):
#         print(f"i: {i}")
#         print(f"f before -> {factorial}")
#         factorial = factorial * i
#         print(f"f after: {factorial}")
#     return factorial

import time


def decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_result = end - start
        print(time_result)
        return result

    return wrapper


@decorator
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


print(list(map(factorial, numbers)))

# res = decorator(factorial)
# print(res(numbers))
