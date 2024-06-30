"""
Implementing and Using Curried Functions with Dynamic Discount Calculation

1.	Create a curried function to calculate discounted price with dynamic discount:
 - Define a function `apply_discount` that takes one argument: `base_discount` (as a int value - example - 10).
 - Inside this function, define another function `discount_applier` that takes one argument: `price`.
 - The inner function should check if the price is greater than 100. If it is, apply an additional 5% (int value) discount on top of the `base_discount` (10 + 5). Calculate the discounted price using the formula: price - (price * (total_discount / 100)).

2.	Create a curried function to apply a fixed base discount:
 - Use the `apply_discount` function to create a new function `apply_10_percent_discount` that applies a 10% (int value) base discount.

3.	Map the new curried function ove a given list:
 - Use the new curried function and the map function to calculate the discounted prices.

4. Assign result to check for correct values:
 - Assign result of new calculated prices to PRICES_DICSOUNT_RESULT

Formula to apply discout: (price * (total_discount / 100))
"""
"""
Curring example

# 3 args
def add(x, y, z):
    return x + y + z

# 3 funcs
def add1(x):
   def add_y(y):
      def add_z(z):
         return x + y + z
      return add_y
   return add1
         
"""

# def add(x, y, z):
#    return x + y + z

# def add1(x):
#    def add_y(y):
#       def add_z(z):
#          return x + y + z
#       return add_z
#    return add_y

# result = add1(1)(1)(1)
# print(result)

PRICES = [10, 120, 99, 1, 555]
RESULT = [9.0, 102.0, 89.1, 0.9, 471.75]
PRICES_DICSOUNT_RESULT = []

# Step 1: Define the curried function to calculate discounted price with dynamic discount


def apply_discount(base_discount):
   # base_discount = 10
   def discount_applier(price):
      # total_discount = base_discount
      total_discount = base_discount
      if price > 100:
         # total_discount += 5
         total_discount += 5
      discounted_price = price - (price * (total_discount / 100))
      return discounted_price

   return discount_applier


# apply_10_percent_discount = apply_discount(10)
# print(apply_10_percent_discount(90))
# print(apply_10_percent_discount(115))

# def apply_discount(base_discount):
#       def discount_applier(price):
#          if price > 100:
#             base_discount += 5
#          discounted_price = price - (price * (total_discount / 100))
#          return "sss"
#             #print("ff", discounted_price)

# Step 2: Create a curried function to apply a fixed base discount

apply_10_percent_discount = apply_discount(10)
#print(apply_10_percent_discount)

# Step 3: Create a list of prices and map the new curried function over it

PRICES_DICSOUNT_RESULT = list(map(apply_10_percent_discount, PRICES))

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
