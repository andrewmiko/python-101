"""
Task 4: Generators

Objective: Demonstrate proficiency in creating and using generators in Python.

Problem:
Write a Python program that includes a generator function to produce an infinite sequence of random numbers between 0 and 9. Use this generator to count how many times each number appears in the 1,000,000 generated numbers and print the results in a dictionary.

Expected Output:

    •	The statistics for 10 numbers from 0 to 9 in dict each on a new line.

---
0: 60455
1: 42398
2: 2163
...

dict => unique keys => only one time in dict
dict => not unique values => key: value -> Any value (type)
"""

import random


def generator():
    while True:
        result = random.randint(0, 9)
        yield result


gener = generator()

# {0: 100, ...}
# numbers = 0..9
# slovar = {0: x, 1: x, ... 9: x}

slovar = {}
# for value in slovar.keys():
#     if value == 0:
#         print("exists")

# slovar[0] = "C"
# slovar[2] = "D"

# 1 ->
# slovar = {}
# generator => 0..9 (keys)
# 0 key is in slovar? - No -> slovar[0] = 0
# {0: 300_000, 1: ...}

peremennaja = 0
for i in range(1_000_000):
    # i => 0, 999_999 times calling generator "a"
    a = next(gener)  # => 0..9 (keys)
    # if a in slovar.keys():
    #     print(a)

    # OK
    if a not in slovar.keys():
        slovar[a] = 0
    slovar[a] += 1

print(slovar)
#slovar = something: appears_number
# print(appears_number)
