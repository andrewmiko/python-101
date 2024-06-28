import random
from functools import partial


def add_numbers(x, y, z):
    return x + y + z


numbers = list([random.randint(1, 30) for n in range(11)])

# print(add_numbers(1, 1, 1))

# add_numbers_v2 = partial(add_numbers, 2)
# print(add_numbers_v2(1, 1))

# add_numbers_v3 = partial(add_numbers, 2, 3)
# print(add_numbers_v3(1))

# add_numbers_v4 = partial(add_numbers, y=5)
# print(add_numbers_v4(x=1, z=2))

# 1. create function count_power which count of any number in any power (default power = 2)
# func (number, power=2) => return res
# 2. create partial partial_power of count_power function which overwrites power to 5
# 3. make calculation of given numbers from list with map and partial power function

# add_numbers_v4 = partial(add_numbers, y=5)
# func = ddd(add_numbers_v4, somethig)


def count_power(num, power):
    #power = 10
    return num**power


partial_power = partial(count_power, power=2)
print(list(map(partial_power, numbers)))
