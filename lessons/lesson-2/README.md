### Lesson 2: Working with Lists, Dictionaries, and Other Collections

#### Objectives:
- Teach the basics of working with dictionaries.
- Provide an overview of other collections: lists, tuples, sets.

#### Topics:

1. **Working with Lists:**
    - Creating and basic operations.
    - Methods available to lists.
2. **Working with Dictionaries:**
    - Creating, adding, and removing elements.
    - Examples of using dictionaries in tasks.
    - Methods available to dictionaries.
3. **Overview of Other Collections:**
    - Tuples: creating and usage.
    - Methods available to tuples.
    - Sets: creating and set operations.
    - Methods available to sets.

#### Notes:
- Show how to choose the right type of collection for a specific task.
- Explain the differences between mutable and immutable collections.

---

### Working with Lists

**Creating and Basic Operations**

Lists are ordered collections of items. They are mutable, meaning they can be changed after creation.

**Example:**

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Adding an item to the list
fruits.append("orange")

# Removing an item from the list
fruits.remove("banana")

# Accessing items by index
first_fruit = fruits[0]
last_fruit = fruits[-1]
```

**Methods Available to Lists**

1. `append()`: Adds an item to the end of the list.
    ```python
    fruits.append("grape")
    ```

2. `insert()`: Inserts an item at a given position.
    ```python
    fruits.insert(1, "blueberry")
    ```

3. `remove()`: Removes the first item with the specified value.
    ```python
    fruits.remove("cherry")
    ```

4. `pop()`: Removes and returns the item at the specified position.
    ```python
    last_fruit = fruits.pop()
    specific_fruit = fruits.pop(1)
    ```

5. `sort()`: Sorts the list in ascending order.
    ```python
    fruits.sort()
    ```

6. `reverse()`: Reverses the order of the list.
    ```python
    fruits.reverse()
    ```

7. `index()`: Returns the index of the first item with the specified value.
    ```python
    index_of_apple = fruits.index("apple")
    ```

8. `count()`: Returns the number of occurrences of the specified value.
    ```python
    apple_count = fruits.count("apple")
    ```

9. `clear()`: Removes all items from the list.
    ```python
    fruits.clear()
    ```

10. `extend()`: Adds the elements of a list (or any iterable) to the end of the current list.
    ```python
    more_fruits = ["mango", "pineapple"]
    fruits.extend(more_fruits)
    ```

### Working with Dictionaries

**Creating Dictionaries**

Dictionaries are collections of key-value pairs. They are useful for storing related pieces of information.

**Example:**

```python
# Creating an empty dictionary
student = {}

# Creating a dictionary with initial values
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science"]
}
```

**Adding and Removing Elements**

**Example:**

```python
# Adding a new key-value pair
student["grade"] = "A"

# Removing a key-value pair
del student["age"]

# Using pop method to remove an element and return its value
course = student.pop("courses")
```

**Using Dictionaries in Tasks**

**Example:**

```python
# Example of using a dictionary to store and access student information
student = {
    "name": "Bob",
    "age": 22,
    "major": "Computer Science"
}

print(f"Student Name: {student['name']}")
print(f"Student Age: {student['age']}")
print(f"Student Major: {student['major']}")
```

**Methods Available to Dictionaries**

1. `get()`: Returns the value for the specified key if the key is in the dictionary.
    ```python
    age = student.get("age", "Unknown")
    ```

2. `keys()`: Returns a view object that displays a list of all the keys in the dictionary.
    ```python
    keys = student.keys()
    ```

3. `values()`: Returns a view object that displays a list of all the values in the dictionary.
    ```python
    values = student.values()
    ```

4. `items()`: Returns a view object that displays a list of dictionary's key-value tuple pairs.
    ```python
    items = student.items()
    ```

5. `update()`: Updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.
    ```python
    student.update({"age": 23, "grade": "B"})
    ```

6. `clear()`: Removes all items from the dictionary.
    ```python
    student.clear()
    ```

7. `pop()`: Removes the specified key and returns the corresponding value.
    ```python
    major = student.pop("major", "Not Found")
    ```

8. `popitem()`: Removes the last inserted key-value pair.
    ```python
    last_item = student.popitem()
    ```

### Overview of Other Collections

#### Tuples

**Creating and Usage**

Tuples are ordered collections of items. They are immutable, meaning they cannot be changed after creation.

**Example:**

```python
# Creating a tuple
coordinates = (10, 20)

# Accessing items by index
x = coordinates[0]
y = coordinates[1]

# Tuples are often used to return multiple values from a function
def get_student_info():
    name = "Charlie"
    age = 23
    return (name, age)

name, age = get_student_info()
print(f"Name: {name}, Age: {age}")
```

**Methods Available to Tuples**

Tuples are immutable and have fewer methods available compared to lists and dictionaries. The main methods include:

1. `count()`: Returns the number of times a specified value appears in the tuple.
    ```python
    count_of_10 = coordinates.count(10)
    ```

2. `index()`: Returns the index of the first occurrence of the specified value.
    ```python
    index_of_20 = coordinates.index(20)
    ```

#### Sets

**Creating and Set Operations**

Sets are unordered collections of unique items. They are useful for membership testing and eliminating duplicate entries.

**Example:**

```python
# Creating a set
colors = {"red", "green", "blue"}

# Adding an item to the set
colors.add("yellow")

# Removing an item from the set
colors.remove("green")

# Set operations: union, intersection, difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union = set_a | set_b  # {1, 2, 3, 4, 5}
intersection = set_a & set_b  # {3}
difference = set_a - set_b  # {1, 2}
```

**Methods Available to Sets**

1. `add()`: Adds an element to the set.
    ```python
    colors.add("purple")
    ```

2. `remove()`: Removes the specified element from the set. Raises a KeyError if the element is not found.
    ```python
    colors.remove("blue")
    ```

3. `discard()`: Removes the specified element from the set if it is present.
    ```python
    colors.discard("orange")
    ```

4. `pop()`: Removes and returns an arbitrary set element. Raises a KeyError if the set is empty.
    ```python
    color = colors.pop()
    ```

5. `clear()`: Removes all elements from the set.
    ```python
    colors.clear()
    ```

6. `union()`: Returns a set that is the union of sets.
    ```python
    union_set = set_a.union(set_b)
    ```

7. `intersection()`: Returns a set that is the intersection of sets.
    ```python
    intersection_set = set_a.intersection(set_b)
    ```

8. `difference()`: Returns a set that is the difference of two or more sets.
    ```python
    difference_set = set_a.difference(set_b)
    ```

9. `symmetric_difference()`: Returns a set that contains all items from both sets, but not the items that are present in both sets.
    ```python
    symmetric_difference_set = set_a.symmetric_difference(set_b)
    ```

10. `issubset()`: Returns True if another set contains this set.
    ```python
    is_subset = set_a.issubset(set_b)
    ```

11. `issuperset()`: Returns True if this set contains another set.
    ```python
    is_superset = set_a.issuperset(set_b)
    ```

12. `isdisjoint()`: Returns True if two sets have a null intersection.
    ```python
    is_disjoint = set_a.isdisjoint(set_b)
    ```

### Choosing the Right Collection Type

**Mutable vs Immutable Collections**

- **Mutable Collections:**
    - Lists and dictionaries can be changed after creation.
    - Useful when you need to modify the collection after creating it.

- **Immutable Collections:**
    - Tuples cannot be changed after creation.
    - Useful when you want to ensure the collection remains constant.

**Choosing the Right Type**

- **Dictionaries:** Best for key-value pairs, fast lookups by key.
- **Lists:** Best for ordered collections of items, allows duplicate entries.
- **Tuples:** Best for fixed collections of items, function return values.
- **Sets:** Best for unique items, membership testing, and set operations.

---

These explanations and examples will help you understand how to work with lists, dictionaries, and other collections in Python. Below are additional examples and methods available for each data type to further clarify their usage.

### Working with Lists

**Additional Examples:**

```python
# Slicing a list
sub_list = fruits[1:3]  # ['banana', 'cherry']

# List comprehension
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Working with Dictionaries

**Additional Examples:**

```python
# Iterating over a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists in a dictionary
if "age" in student:
    print(f"Age: {student['age']}")

# Merging two dictionaries
additional_info = {"graduation_year": 2025, "GPA": 3.8}
student.update(additional_info)
```

### Working with Tuples

**Additional Examples:**

```python
# Tuple unpacking
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
```

### Working with Sets

**Additional Examples:**

```python
# Set comprehension
squared_set = {x**2 for x in range(10)}  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Checking if an item exists in a set
if "red" in colors:
    print("Red is in the set")

# Frozen set (immutable set)
frozen_colors = frozenset(["red", "green", "blue"])
```

### Choosing the Right Collection Type

**When to Use Each Collection Type:**

- **Dictionaries:** Use when you need a collection of unique keys mapping to values. Ideal for fast lookups and data retrieval by keys.
- **Lists:** Use when you need an ordered collection that can contain duplicates. Ideal for sequences of items where order matters.
- **Tuples:** Use when you need an immutable ordered collection. Ideal for fixed data sets or returning multiple values from a function.
- **Sets:** Use when you need a collection of unique items. Ideal for membership testing, eliminating duplicates, and set operations like unions and intersections.