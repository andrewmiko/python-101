### Lesson 3: Working with Loops

#### Objectives:
- Understand and apply loops in Python.

#### Topics Covered:
1. **For Loops:**
    - Basic structure
    - Using loops with lists, strings, and dictionaries
2. **While Loops:**
    - Basic structure
    - Using while loops with conditions
3. **Range Function and Loop Applications:**
    - Using `range()` with for loops
    - Common loop applications and patterns

---

### For Loops

**Basic Structure**

For loops allow you to iterate over a sequence (such as a list, string, or range) and execute a block of code for each element in the sequence.

**Syntax:**

```python
for variable in sequence:
    # code to execute for each element in sequence
```

**Examples:**

1. **Looping through a list:**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

2. **Looping through a string:**

```python
word = "Python"

for letter in word:
    print(letter)
```

3. **Looping through a dictionary:**

```python
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")
```

### While Loops

**Basic Structure**

While loops allow you to execute a block of code as long as a condition is true.

**Syntax:**

```python
while condition:
    # code to execute as long as condition is true
```

**Examples:**

1. **Basic while loop:**

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

2. **Using a while loop with user input:**

```python
user_input = ""

while user_input.lower() != "exit":
    user_input = input("Type 'exit' to end the loop: ")
    print(f"You typed: {user_input}")
```

### Range Function and Loop Applications

**Using `range()` with For Loops**

The `range()` function generates a sequence of numbers, which is useful for looping a specific number of times.

**Syntax:**

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

**Examples:**

1. **Looping a specific number of times:**

```python
for i in range(5):
    print(i)
```

2. **Looping with a start and stop value:**

```python
for i in range(1, 6):
    print(i)
```

3. **Looping with a step value:**

```python
for i in range(0, 10, 2):
    print(i)
```

**Common Loop Applications and Patterns**

1. **Calculating the sum of a list:**

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print(f"Total: {total}")
```

2. **Finding the maximum value in a list:**

```python
numbers = [10, 20, 30, 40, 50]
max_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

print(f"Max value: {max_value}")
```

3. **Reversing a string:**

```python
word = "Python"
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

print(f"Reversed word: {reversed_word}")
```

4. **Using break and continue in loops:**

```python
# Using break
for i in range(10):
    if i == 5:
        break
    print(i)

# Using continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### Conclusion

Understanding and applying loops in Python is crucial for performing repetitive tasks efficiently. By mastering for loops, while loops, and the range function, you can handle a wide variety of programming challenges.