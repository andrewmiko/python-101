"""
Task 3: Maps and Filters

Objective: Demonstrate proficiency in using map and filter functions in Python.

Problem:
Write a Python program that performs the following operations:

    1.	Create a list of integers from 1 to 10.
    2.	Use the `map` function to create a new list where each element is the square of the corresponding element in the original list.
    3.	Use the `filter` function to create a new list from the squared list that contains only even numbers.
    4.	Combine the results to print both the squared list and the filtered list.

Expected Output:

    •	The list of squares.
    •	The filtered list of even squares.

---
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squared list: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Filtered list (even squares): [4, 16, 36, 64, 100]
"""

#integer_list = range(1, 10)
#print(integer_list)

integer_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integer_list1)


def square(stepen):

    #result = 0
    #for num in integer_list1:
    return stepen**2


new_list = list(map(square, integer_list1))
print(new_list)

#new_list2 = []


def filters(num):
    # 1 ? -> None
    # 4 ? -> 4
    # 9 ? -> None
    # 16 ? -> 16
    # ...
    if num % 2 == 0:
        return num


"""
iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = square
map(func, iterable): =>
for i in iterable:
    return func(i)
return = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
"""
iterable = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
func = filters
filter(filters, iterable): =>
for i in iterable:
    if func(i) == True?:
        return i
return = [4, 16, 36, 64, 100]
"""

new_list2 = list(filter(filters, new_list))
print(new_list2)
