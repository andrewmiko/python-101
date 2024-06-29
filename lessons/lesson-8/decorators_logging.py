"""
Implementing and Using Decorators with Logging Execution Time and Word Count Function

1. Create a decorator to log execution time and debug information:
 - Define a decorator function debug that logs the time taken by the decorated function to execute and prints useful debug information.

2. Create a function to count the number of symbols in a given text using the decorator:
 - Define a function count_symbols that takes a string of text and returns the number of symbols in it.
 - Decorate this function with debug to log the execution time and debug information.

3. Map the decorated function over a given list of texts:
 - Create a list of text strings.
 - Use the map function to apply the decorated count_symbols function to each text in the list.

4. Assign result to check for correct values:
 - Assign result to SYMBOLS_COUNTS
"""

TEXTS = [
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be that is the question", "All that glitters is not gold",
    "A journey of a thousand miles begins with a single step",
    "You miss 100 percent of the shots you never take",
    "The only thing we have to fear is fear itself",
    "In the end we will remember not the words of our enemies but the silence of our friends",
    "The purpose of our lives is to be happy",
    "Life is what happens when you're busy making other plans",
    "Get busy living or get busy dying",
    "You have within you right now everything you need to deal with whatever the world can throw at you",
    "Believe you can and you're halfway there",
    "The only way to do great work is to love what you do",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful",
    "It is not the years in your life that count. It is the life in your years",
    "Your time is limited, don't waste it living someone else's life",
    "The greatest glory in living lies not in never falling, but in rising every time we fall",
    "In the end, it's not the years in your life that count. It's the life in your years",
    "To live is the rarest thing in the world. Most people exist, that is all",
    "Do not go where the path may lead, go instead where there is no path and leave a trail",
    "If life were predictable it would cease to be life, and be without flavor",
    "In three words I can sum up everything I've learned about life: it goes on",
    "To handle yourself, use your head; to handle others, use your heart",
    "Keep calm and carry on",
    "The best way to predict the future is to invent it",
    "The journey of a thousand miles begins with one step",
    "Life is 10% what happens to us and 90% how we react to it",
    "The only limit to our realization of tomorrow is our doubts of today",
    "You must be the change you wish to see in the world",
    "To give anything less than your best, is to sacrifice the gift"
]

RESULT = [
    43, 39, 29, 55, 48, 45, 87, 39, 56, 33, 98, 40, 52, 124, 73, 63, 88, 83,
    72, 86, 73, 74, 67, 22, 50, 52, 57, 68, 51, 62
]

SYMBOLS_COUNTS = []

# Step 1: Define the decorator to log execution time and debug information
# Step 2: Create a function to count the number of words in a given text and apply the debug decorator
# Step 3: Using map to apply the decorated function to each text

# DO NOT TOUCH!
print()
print("# RESULT #")
print(RESULT)
print(SYMBOLS_COUNTS)
print("-" * 10)
print()

try:
    assert RESULT == SYMBOLS_COUNTS
except Exception as e:
    raise e
