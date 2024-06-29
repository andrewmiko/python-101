"""
Using Generators to Count the Number of Words in a Large Text File

1. Create a generator function to read lines from a large text file:
 - Define a generator function `read_lines` that takes a file path as an argument uses loop and yields each line from the file one by one.
 - Use line.strip() to remove unneccesary symbols from string

2. Create a function to count the number of words in each line:
 - Define a function `count_words` that takes a string of text (a line) and returns the number of words in it.
 - Use line.split() to split string into list of words

3. Use the generator to process a large text file and count the total number of words:
 - Create a script that reads through the entire text file using the generator function.
 - For each line, use the `count_words` function to count the words and sum them up to get the total word count.

4. Assign result to check for correct values:
 - Assign result to `RESULT_WORDS_COUNT`

File operations:

for open as file:
    open
==
def read_lines(file_path):
    with open(file_path, "r") as file:
        ...
        yield line
"""

import os

CURR_PATH = os.getcwd()
FILE_PATH = f"{CURR_PATH}/lessons/lesson-8/harry-potter-and-the-order-of-the-phoenix.txt"
RESULT = 266181
RESULT_WORDS_COUNT = 0

# Step 1: Define the generator `read_lines` function to read lines from a large text file


def read_lines(path):
    with open(path, "r") as file:
        for line in file.readlines():
            yield line


# read_lines(FILE_PATH)

# Step 2: Create a function to count the number of words in each line


def count_words(string):
    # res = x + y
    # string.strip().split() => []
    # print(string)
    a = string.strip().split()
    #print(string)
    # print("a", a)
    # print(len(a))

    #  print(string)
    return len(a)


#print(count_words("ddd fff sss"))

# Step 3: Use the generator to process the text file and count the total number of words

#print(read_lines(FILE_PATH))
#print(FILE_PATH)

gener = read_lines(FILE_PATH)

kolvo_strok = 0
for stroka in gener:

    d = count_words(stroka)
    kolvo_strok += d
    #print(kolvo_strok)

RESULT_WORDS_COUNT = kolvo_strok

# DO NOT TOUCH!
print()
print("# RESULT #")
print(RESULT)
print(RESULT_WORDS_COUNT)
print("-" * 10)
print()

try:
    assert RESULT == RESULT_WORDS_COUNT
except Exception as e:
    raise e
