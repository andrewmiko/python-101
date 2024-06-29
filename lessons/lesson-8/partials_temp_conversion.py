"""
Implementing and Using Partial Functions with Temperature Conversion

1. Create a function to convert temperature:
- The function should take two arguments: temp (temperature value) and unit (target unit, either ‘C’ for Celsius or ‘F’ for Fahrenheit).

2. Overwrite the function with partials:
- Use functools.partial to create a new function that converts temperatures from Fahrenheit to Celsius.

3. Map the new partial function over a given list:
 - Create a list of temperatures in Fahrenheit.
 - Use the new partial function and the map function to convert the temperatures to Celsius.

4. Assign results to check for correct values:
- Assign result to RESULT_F_TO_C which is a list of values in C
- Assign result to RESULT_C_TO_F which is a list of values in F

Formula to convert C to F: (temp - 32) * 5.0 / 9.0
Formula to convert F to C: temp * 9.0 / 5.0 + 32
"""

C_TEMPS = [-20, -5, 0, 10, 23]
F_TEMPS = [32, 45, 64, 77, 100]

C_RESULT = [0.0, 7.222222222222222, 17.77777777777778, 25.0, 37.77777777777778]
F_RESULT = [-4.0, 23.0, 32.0, 50.0, 73.4]

RESULT_F_TO_C = []
RESULT_C_TO_F = []

# Step 1: Define the function to convert temperature
# Step 2: Create a partial function to convert Fahrenheit to Celsius
# Step 3: Use given temperatures in Fahrenheit and Celsius and map the new partial function over it

# DO NOT TOUCH!
print()
print("# RESULT F TO C #")
print(C_RESULT)
print(RESULT_F_TO_C)
print("-" * 10)
print()

print()
print("# RESULT C TO F #")
print(F_RESULT)
print(RESULT_C_TO_F)
print("-" * 10)
print()

try:
    assert C_RESULT == RESULT_F_TO_C
    assert F_RESULT == RESULT_C_TO_F
except Exception as e:
    raise e
