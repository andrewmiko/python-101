"""
Task 1: Lists

Objective: Demonstrate proficiency in handling lists in Python.

Problem:
Write a Python program that performs the following operations on a list of integers:

    1.	Create a list of integers from 1 to 20.
    2.	Remove all even numbers from the list.
    3.	Find the sum of the remaining numbers.
    4.	Find the maximum and minimum values from the remaining numbers.
    5.	Reverse the list.

Expected Output:

    •	The modified list after removing even numbers.
    •	The sum of the remaining numbers.
    •	The maximum and minimum values from the remaining numbers.
    •	The reversed list.

---
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
List after removing even numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Sum of remaining numbers: 100
Maximum value: 19
Minimum value: 1
Reversed list: [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
"""

# step 1
original_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]
# original_list = range(1, 21)

novi_list = []
for num in original_list:
    if num % 2 != 0:
        novi_list.append(num)

print(novi_list)  # step 2 gptpvp

# summa = 0
# for nomer in novi_list :
#     #print(nomer)
#     summa += nomer

# print(summa) # step 3 gotova

print(sum(novi_list))
print(max(novi_list))
print(min(novi_list))

# sorted()
# novi_list.sort(reverse=True)
# novi_list.reverse() = novi_list.sort(reverse=True)
# => return None

novi_list.sort(reverse=True)
# a = novi_list.sort(reverse=True)
print(novi_list)
