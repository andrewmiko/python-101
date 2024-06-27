# partials ->
# decorators time complexity (time spent for factorial)
# map, factorial, decorator

# generators -> yeild return dict random.randit, key = value
# random.randit(1, 100) => 1, 99
# function to count values ...
# count how much keys(unique) or values are even or odd
# count how much values are there >= 20
# count how much values are == 2

# threads ->
# rlocks?
# semafors?

# pandas ->
# open file
# find any NaN values
# find max value
# axis = 1 ?
# isnull
# isnan

# def sum_of_squares():

#     def random_numbers(n):
#         return range(n)

#     def new_random_numbers(n):

#         def func(n):
#             return range(n)

#         nums = func(n)
#         return nums

#     nums = random_numbers(10)
#     return sum(n**2 for n in nums)

# simple decorator
# def decorator(func):

#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")

#     return wrapper

# @decorator
# def say_whee():
#     print("Whee!")

# say_whee()

# def debug(func):  # -> def debug(sum_of_numbers)

#     def wrapper(*args, **kwargs):
#         print(f"DEBUG - FUNC: {func}")
#         print(f"DEBUG - ARGS: {args}")
#         print(f"DEBUG - KWARGS: {kwargs}")

#         # print("DEBUG - FUNC START")
#         res = func(*args, **kwargs)
#         # print(f"DEBUG - RESULT: {res}")
#         # print("DEBUG - FUNC FINISH")
#         return res

#     return wrapper

# @debug
# def sum_of_squares(nums):
#     return sum(n**2 for n in nums)

# @debug
# def sum_of_numbers(nums, *args, **kwargs):
#     return sum(nums)

# my_nums = range(10)
# sum_of_numbers(my_nums, debug=True)
# sum_of_squares(my_nums)

# x = 10
# def cubic(x):
#     # range(x) => [0,1,2,3,4,5,6,7,8,9]
#     for i in range(x):
#         # i = 0
#         # sum(i**3) => sum(0) => error
#         # sum([0])
#         return sum(list(i**3))de

import time
# time.perf_counter()


def decorator(func):

    def wrapper(*args, **kwargs):
        time_start = time.time()
        print(f"name of func:{func}")  # nazvanie funkcii
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f"time: {time_end - time_start}")
        return result

    return wrapper


@decorator
def cubic(max_number):
    # max_number = 10
    # range(max_number) => [0,1,2,3,4,5,6,7,8,9]
    res = 0
    for n in range(max_number):
        res += n**3
    return res


rastojanie = 10
print(cubic(rastojanie))

# generate partial q1:  funcija = partial(base, exponent=2)

# q 2 something = d(funcija, numbers)

# q 3 def factorial(n):
#          return[map for i in factorial(numbers)]

# map => high order function
# filter => high order function
# reduce => high order function
# map(func, iterable) =>
"""
make function call on each element in iterable
return new iterable with changes

map =>
for i in iterable:
    func(i)
"""
"""
make function call and filter by condition on each element in iterable
return filtered elements

filter =>
for i in iterable:
    if condition:
        return i
"""


def square(n):
    return n**2


def is_even(n):
    if n % 2 == 0:
        return True


my_nums = range(1, 11)  # => [1,2,3,4,5,6,7,8,9,10]
print(list(map(square, my_nums)))
print(list(filter(is_even, my_nums)))

# lambda = one line anonymous function
# lambda x: print("-{}.".format(x))

# lambda = def func()
# lambda x: = def func(x):
# lambda x: print(x) = def func(x): print(x)

l_square = lambda n: n**2
"""
l_square = lambda n: n**2
== 
def l_square(n):
    return n**2
"""

print(list(map(lambda n: n**2, range(10))))
"""
print(list(map(lambda n: n**2, range(10))))

map =>
def map(func, iterable):
    for i in iterable:
        res = func(i)
    return res

lambda n: n**2 =>
def lambda(n):
    return n**2

range(10) => [0..9]
------------------------

map(lambda(n), [0..9]):
    lambda(0) => 0**2 => 0
    lambda(1) => 1**2 => 1
    lambda(2) => 4**2 => 4
return [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

# l_dict = lambda key, value: print(f"{key} => {value}")
# user = {"username": "andrew", "email": "andrew@gmail.com"}
# l_dict(user.items())
