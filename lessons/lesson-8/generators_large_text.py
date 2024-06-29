"""
Using Generators to Count the Number of Words in a Large Text File

1. Create a generator function to read lines from a large text file:
 - Define a generator function read_lines that takes a file path as an argument uses loop and yields each line from the file one by one.
 - Use line.strip() to remove unneccesary symbols from string

2. Create a function to count the number of words in each line:
 - Define a function count_words that takes a string of text (a line) and returns the number of words in it.
 - Use line.split() to split string into list of words

3. Use the generator to process a large text file and count the total number of words:
 - Create a script that reads through the entire text file using the generator function.
 - For each line, use the count_words function to count the words and sum them up to get the total word count.

4. Assign result to check for correct values:
 - Assign result to RESULT_WORDS_COUNT
"""

FILE_PATH = "./harry-potter-and-the-order-of-the-phoenix.txt"
RESULT = 266181
RESULT_WORDS_COUNT = 0

# Step 1: Define the generator function to read lines from a large text file
# Step 2: Create a function to count the number of words in each line
# Step 3: Use the generator to process the text file and count the total number of words

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
