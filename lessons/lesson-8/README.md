## Partials

In Python, the `functools.partial` function is used to create a new function with some of the arguments of an existing function pre-filled. This is known as partial application. It's particularly useful for simplifying function calls and creating more modular, reusable code.

### How `functools.partial` Works

`functools.partial` takes a function and any number of arguments or keyword arguments, and returns a new function. When you call this new function, it behaves like the original function but with the pre-filled arguments already provided.

### Example of `functools.partial`

Let's consider a function that calculates the power of a number:

```python
def power(base, exponent):
    return base ** exponent
```

You can use `functools.partial` to create a new function that always raises a number to the power of 2:

```python
from functools import partial

# Create a new function that always uses exponent 2
square = partial(power, exponent=2)

# Now, square only needs the base argument
result = square(5)
print(result)  # Output: 25
```

### Another Example with Keyword Arguments

`functools.partial` also works with keyword arguments. Here’s an example with a function that formats strings:

```python
def greet(greeting, name):
    return f"{greeting}, {name}!"

# Create a new function that always uses "Hello" as the greeting
say_hello = partial(greet, greeting="Hello")

# Now, say_hello only needs the name argument
result = say_hello("Alice")
print(result)  # Output: Hello, Alice!
```

### Practical Use Case: Configuring Logging

A practical use case for `functools.partial` is configuring logging in a consistent way across different parts of an application:

```python
import logging
from functools import partial

def setup_logger(name, level, format):
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(format))
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Create a partial function that always uses the same format
standard_logger = partial(setup_logger, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Now, create loggers with different names and levels, but with the same format
debug_logger = standard_logger(name="debugLogger", level=logging.DEBUG)
info_logger = standard_logger(name="infoLogger", level=logging.INFO)

debug_logger.debug("This is a debug message")
info_logger.info("This is an info message")
```

### Summary

- **Purpose**: `functools.partial` creates a new function with some arguments of the original function pre-filled.
- **Syntax**: `partial(func, *args, **kwargs)` where `func` is the original function, `args` are positional arguments to pre-fill, and `kwargs` are keyword arguments to pre-fill.
- **Usage**: Simplifies function calls, enables code reuse, and helps in configuring functions with consistent parameters.

By using `functools.partial`, you can create more concise and readable code, especially in cases where you repeatedly call a function with the same arguments.

## Currying

Currying is a concept in functional programming where a function that takes multiple arguments is transformed into a sequence of functions, each taking a single argument. This allows for more flexible function composition and partial application of functions.

In simpler terms, currying turns a function with multiple parameters into a series of functions that each take one parameter and return a new function expecting the next parameter, until all parameters have been provided. 

### Example of Currying

Let's consider a simple function that adds three numbers:

```python
def add(x, y, z):
    return x + y + z
```

In a curried form, this function would look like this:

```python
def curried_add(x):
    def add_y(y):
        def add_z(z):
            return x + y + z
        return add_z
    return add_y
```

You can then use this curried function like so:

```python
result = curried_add(1)(2)(3)  # This will return 6
print(result)  # Output: 6
```

### Currying in Python with `functools.partial`

While Python does not support currying out of the box, you can achieve similar behavior using the `functools.partial` function for partial application. However, true currying transforms the function in a more stepwise manner.

### Example Using `functools.partial`

If we want to partially apply the `add` function to create a new function that takes fewer arguments, we can use `functools.partial`.

```python
from functools import partial

def add(x, y, z):
    return x + y + z

# Create a new function that has the first argument fixed
add_with_1 = partial(add, 1)

# Now add_with_1 takes two arguments
result = add_with_1(2, 3)
print(result)  # Output: 6
```

### Summary

- **Currying**: Transforms a function with multiple arguments into a series of functions that each take a single argument.
- **Partial Application**: A specific use case where you fix a certain number of arguments of a function, creating a new function that takes the remaining arguments.

Currying is useful in functional programming for creating higher-order functions and enabling more modular code. Partial application, which can be achieved with tools like `functools.partial` in Python, allows you to fix some arguments of a function and create simpler, reusable functions.

## Closures

#### Definition
A **closure** is a function that retains access to the variables and scope in which it was created, even after the outer function has finished executing. Closures are created by defining an inner function within an outer function and returning the inner function. The inner function will have access to the variables and scope of the outer function, even after the outer function has completed.

#### Key Characteristics
- **Encapsulation**: Closures help in data hiding by encapsulating the variables within the outer function, providing a controlled access mechanism through the inner function.
- **Persistence**: Variables defined in the outer function remain in memory between calls to the inner function.

### Example and Explanation

Consider a function that creates and returns a function to add a specific number to its input.

#### Step-by-Step Example

##### Step 1: Define the outer function
- The outer function `make_adder` takes one argument `n`.

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder
```

##### Step 2: Create an instance of the closure
- Call the `make_adder` function with a specific value to create a closure.

```python
add_five = make_adder(5)
```

##### Step 3: Use the closure
- Call the inner function through the closure.

```python
print(add_five(10))  # Output: 15
```

### Explanation of the Example

1. **Outer Function**:
   - `make_adder` is the outer function that takes a single argument `n`.
   - Inside `make_adder`, an inner function `adder` is defined which takes another argument `x` and returns `x + n`.

2. **Returning the Inner Function**:
   - `make_adder` returns the inner function `adder`, creating a closure.
   - The returned function `adder` retains access to the variable `n` from the outer function's scope.

3. **Using the Closure**:
   - When `make_adder(5)` is called, it returns a new function `adder` that adds 5 to its input.
   - This returned function is stored in `add_five`.
   - Calling `add_five(10)` executes the inner function `adder` with `x = 10`, which uses the retained `n = 5` from the outer function's scope, resulting in `10 + 5 = 15`.

### Practical Use Cases

#### 1. **Data Encapsulation**:
Closures can be used to encapsulate data and provide controlled access to it.

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2
```

#### 2. **Factory Functions**:
Closures can be used to create factory functions that generate customized functions.

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
print(times_three(10))  # Output: 30
```

### Summary
- A closure is created by defining an inner function within an outer function and returning the inner function.
- Closures retain access to the variables and scope of the outer function even after the outer function has finished executing.
- They are useful for data encapsulation and creating factory functions.

Closures are a powerful feature in Python, enabling advanced programming techniques and helping to maintain clean and modular code.