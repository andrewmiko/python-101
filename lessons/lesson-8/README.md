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