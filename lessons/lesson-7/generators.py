# create new geneartor which in infinite way returns dict structure
# "random_key" => randomint(0, 1_000_000)
# "time": time in sec
# {"random": True, "random_key": RANDOM_VALUE, "time": TIME_IN_SEC}
# call generator only 100 times

# extra task
# count how many random_values there is odd vs even

import random
import time


def generator():
    while True:
        result = {
            "random": True,
            "random_key": random.randint(0, 1_000_000),
            "time": int(time.time())
        }
        yield result


gen = generator()  # vazno obazatelnoi присваивать переменную
print(next(gen))
print(next(gen))
print(next(gen))

count_odd = 0
count_even = 0
for i in range(1_000_000):
    res = next(gen)
    # print(res, res["random_key"])
    if res["random_key"] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Even numbers count: {count_even}")
print(f"Odd numbers count: {count_odd}")
