print("Hello, world!")

# func() -> call on function
# func -> definition of function -> doesn't call on function

# function definition
# def func_name(*args, **kwargs):
# -> code block
# -> return (default return = None)


def slozene(x, y):
    result = x + y
    return result


print(slozene(3, 6))  # 3,6 => x,y

# x, y = function aruments / args
# def slozene(x, y)


# x=10, y=10 = args default values
def multiply(x=10, y=10):
    return x * y


# args
# args = list of values (works by index)
print(multiply(3, 6))  # x=3, y=6
print(multiply(3))  # x=3, y=10

# kwargs
# kwargs = dict of values (works by keys)
print(multiply(y=3))  # x=10, y=3
print(multiply(y=2, x=3))  # y=2, x=3


# door
# program (global) scope
def to_power(num, power, *args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    # function scope - internal scope
    # closed room
    return num**power


# num=2, power=2, args=(3,4,5), kwargs={'x': 20}
to_power(2, 2, 3, 4, 5, x=20)


def multiply_many(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    # return None -> by default


print(multiply_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, x=10))

print(type(multiply_many))

# functional programming
# my_func = multiply_many
# print( my_func() )


def print_uppercase(string):
    return string.upper()


def print_lowercase(string):
    return string.lower()


# fruits = ["Apple", "Orange", "Banana"]
# for f in fruits:
#     # inner_func = None
#     if f == "Apple":
#         inner_func = print_uppercase
#     else:
#         inner_func = print_lowercase
#     print(inner_func(f))


def pprint(text, format_func=None):
    if format_func is None:
        print(text)
    else:
        print(format_func(text))


pprint("Hello, World!", print_uppercase)


def foo(list1, list2):
    # list1 = [3, 4, 5]
    # list2 = [0, 8, 6, 4]

    # list2 = [0, 8, 6, 4, "bla"]
    list2.append('bla')
    print(list2)

    # list2 = [0, 8, 6, 4, "bla", 3, 4, 5]
    list2.extend(list1)
    print(list2)

    # list3 = [x for i, x in enumerate(list2) if i % 2 == 0]
    # for key, value in dict.items():
    list3 = []
    for index, value in enumerate(list2):
        if index % 2 == 0:
            list3.append(value)
    return list3


list1 = [3, 4, 5]
list2 = [0, 8, 6, 4]

print(foo(list1, list2))

mode = 0
new_mode = False
new_mode = True if not new_mode else False
print(new_mode)

def toggle_mode():
    global mode
    # mode = 1 if not mode else 0
    if mode == 0:
        mode = 1
    else:
        mode = 0


print(mode)
toggle_mode()
print(mode)



GLOBAL_MODE = 0

def toggle_mode(mode):
    # mode = 1 + 1 tak ne pisatj
    result = 1 if not mode else 0
    return result

print(GLOBAL_MODE)
new_mode = toggle_mode(GLOBAL_MODE)
print(new_mode)