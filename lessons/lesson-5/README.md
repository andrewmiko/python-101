### Lesson 5: Functions

#### Objectives:
- Learn to define and use functions in Python.

#### Topics Covered:
1. Defining and calling functions.
2. Function parameters and scope.
3. Common errors and troubleshooting.
4. Extra: Using `*args` and `**kwargs`.
5. Using the `global` keyword.
6. Default return value and returning multiple values.

---

### Defining and Calling Functions

**What are functions?**

Functions are reusable pieces of code that perform a specific task. They help in organizing code and avoiding repetition.

**Syntax:**

```python
def function_name(parameters):
    # code block
    return value
```

**Examples:**

1. **Simple Function:**

```python
def greet():
    print("Hello, World!")

greet()  # Calling the function
```

2. **Function with Parameters:**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

3. **Function with Return Value:**

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

4. **Function with Default Return Value (None):**

```python
def do_nothing():
    pass

result = do_nothing()
print(result)  # None
```

### Function Parameters and Scope

**Parameters and Arguments:**

Parameters are variables listed inside the parentheses in the function definition. Arguments are the values passed to the function when it is called.

**Example:**

```python
def multiply(a, b):
    return a * b

print(multiply(2, 3))  # 6
```

**Default Parameters:**

You can provide default values for parameters.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Hello, Guest!
greet("Alice")  # Hello, Alice!
```

**Scope:**

Variables defined inside a function are local to that function and cannot be accessed outside.

**Example:**

```python
def my_function():
    local_variable = 10
    print(local_variable)

my_function()
# print(local_variable)  # This will raise an error because local_variable is not defined outside the function.
```

### Using the `global` Keyword

**What is the `global` keyword?**

The `global` keyword is used to declare a variable as global, allowing it to be modified inside a function.

**Example:**

```python
x = 10

def my_function():
    global x
    x = 20

my_function()
print(x)  # 20
```

### Returning Multiple Values

**What does it mean to return multiple values?**

Python functions can return multiple values as a tuple.

**Example:**

```python
def get_user_info():
    name = "Alice"
    age = 25
    return name, age

user_name, user_age = get_user_info()
print(user_name)  # Alice
print(user_age)   # 25
```

### Common Errors and Troubleshooting

**Common Errors:**

1. **Syntax Errors:**

```python
def my_function()
    print("Hello!")  # Missing colon
```

2. **Indentation Errors:**

```python
def my_function():
print("Hello!")  # IndentationError: expected an indented block
```

3. **Name Errors:**

```python
print(variable)  # NameError: name 'variable' is not defined
```

**Troubleshooting Tips:**

1. **Check for typos.**
2. **Ensure correct indentation.**
3. **Verify variable scope.**
4. **Use print statements to debug.**

### Extra: Using `*args` and `**kwargs`

**`*args`:**

Allows you to pass a variable number of non-keyword arguments to a function.

**Example:**

```python
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)
```

**`**kwargs`:**

Allows you to pass a variable number of keyword arguments to a function.

**Example:**

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```

**Combining `*args` and `**kwargs`:**

You can use both in the same function.

**Example:**

```python
def show_details(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_details(1, 2, 3, name="Alice", age=25)
```

### Conclusion

Functions are essential for writing clean and efficient code. By defining and calling functions, understanding parameters and scope, handling common errors, utilizing `*args` and `**kwargs`, using the `global` keyword, and knowing how to handle return values, you can create powerful and flexible functions in Python.