"""
Task 2: Dicts

Objective: Demonstrate proficiency in handling dictionaries in Python.

Problem:
Write a Python program that performs the following operations:

    1.	Create a dictionary where the keys are the integers from 1 to 5 and the values are their respective squares.
    2.	Add a new key-value pair to the dictionary where the key is 6 and the value is its square.
    3.	Update the value of key 3 to be "A".
    4.	Delete the key-value pair with key 4.
    5.	Iterate over the dictionary and print each key-value pair.

Expected Output:

    •	The dictionary after each modification.
    •	The final dictionary.
    •	Each key-value pair printed on a new line.

---
Initial dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
After adding key 6: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
After updating key 3: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
After deleting key 4: {1: 1, 2: 4, 3: 9, 5: 25, 6: 36}
Final dictionary:
1: 1
2: 4
3: 9
5: 25
6: 36
"""

# [n for n in range()]
# "6" != 6

dict12 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(dict12)

dict12[6] = 36
print(dict12)

dict12[3] = "A"
print(dict12)

dict13 = dict12.pop(4)
# dict12.pop(4) -> OK
# dict12.pop(4:16) - NOT OK
# dict12.pop(4,16) - OK, but with DEFAULT=16
print(dict13)
print(dict12)

for key, value in dict12.items():
    print(key, value)
