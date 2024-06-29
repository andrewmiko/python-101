"""
Implementing and Using Curried Functions with Dynamic Discount Calculation

1.	Create a curried function to calculate discounted price with dynamic discount:
 - Define a function apply_discount that takes one argument: base_discount (as a percentage).
 - Inside this function, define another function discount_applier that takes one argument: price.
 - The inner function should check if the price is greater than 100. If it is, apply an additional 5% discount on top of the base_discount. Calculate the discounted price using the formula: price - (price * (total_discount / 100)).

2.	Create a curried function to apply a fixed base discount:
 - Use the apply_discount function to create a new function apply_10_percent_discount that applies a 10% base discount.

3.	Map the new curried function over a given list:
 - Create a list of prices.
 - Use the new curried function and the map function to calculate the discounted prices.

4. Assign result to check for correct values:
 - Assign result of new calculated prices to PRICES_DICSOUNT_RESULT

Formula to apply discout: (price * (total_discount / 100))
"""

PRICES = [10, 120, 99, 1, 555]
RESULT = [9.0, 102.0, 89.1, 0.9, 471.75]
PRICES_DICSOUNT_RESULT = []

# Step 1: Define the curried function to calculate discounted price with dynamic discount
# Step 2: Create a curried function to apply a fixed base discount
# Step 3: Create a list of prices and map the new curried function over it

# DO NOT TOUCH!
print()
print("# RESULT #")
print(RESULT)
print(PRICES_DICSOUNT_RESULT)
print("-" * 10)
print()

try:
   assert RESULT == PRICES_DICSOUNT_RESULT
except Exception as e:
   raise e
