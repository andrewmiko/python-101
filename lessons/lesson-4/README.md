### Lesson 4: Working with If-Else Statements

#### Objectives:
- Understand and apply if-else statements in Python.

#### Topics Covered:
1. Basic if-else structure.
2. Nested if-else statements.
3. Using if-else with different data types.
4. Examples and common use cases.

---

### Basic If-Else Structure

**What are if-else statements?**

If-else statements allow you to execute certain blocks of code based on conditions. They help in decision-making processes in your programs.

**Syntax:**

```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

**Examples:**

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Nested If-Else Statements

**What are nested if-else statements?**

Nested if-else statements are if-else statements inside other if-else statements. They allow for more complex decision-making processes.

**Syntax:**

```python
if condition1:
    # code to execute if condition1 is true
    if condition2:
        # code to execute if condition2 is true
    else:
        # code to execute if condition2 is false
else:
    # code to execute if condition1 is false
```

**Examples:**

```python
number = 10

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is non-positive.")
```

### Using If-Else with Different Data Types

**Strings:**

```python
name = "Alice"

if name == "Alice":
    print("Hello, Alice!")
else:
    print("Hello, stranger!")
```

**Integers:**

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")
```

**Booleans:**

```python
is_raining = True

if is_raining:
    print("Don't forget your umbrella!")
else:
    print("It's a sunny day!")
```

**Lists:**

```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")
```

### Examples and Common Use Cases

1. **Input Validation:**

```python
user_input = input("Enter a number: ")

if user_input.isdigit():
    print("Thank you for entering a number.")
else:
    print("That is not a valid number.")
```

2. **Menu Selection:**

```python
choice = input("Choose an option (A/B/C): ")

if choice == "A":
    print("You chose option A.")
elif choice == "B":
    print("You chose option B.")
elif choice == "C":
    print("You chose option C.")
else:
    print("Invalid choice.")
```

3. **Checking Conditions:**

```python
temperature = 30

if temperature > 30:
    print("It's a hot day.")
elif temperature < 10:
    print("It's a cold day.")
else:
    print("The weather is nice.")
```

4. **Complex Conditions:**

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")
```

### Conclusion

Understanding and using if-else statements are fundamental skills in programming. They allow your programs to make decisions and perform different actions based on conditions. By mastering if-else statements, you can create more dynamic and flexible code.