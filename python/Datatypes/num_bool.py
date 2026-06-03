import sys

# from decimal import Decimal as D
# from fractions import Fraction as F

# integers
black_tea_grams = 4
ginger_grams = 2
total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remainaing: {remaining_tea}")

# floating point division
milk = 7
per_serve = 4
milk_per_serve = milk / per_serve
print(f"milk per serve:{milk_per_serve}")

# integer division
milk_per_serve = milk // per_serve
print(f"milk per serve:{milk_per_serve}")

# modulo
modulo = milk % per_serve
print(f"milk left over:{modulo}")

# power
power = milk**per_serve
print(f"milk power:{power}")

# writing separated number
total_tea_leaves = 1_000_000_000  # for readability
print(total_tea_leaves)

# boolean
isBoiling = True
count = 5
print(isBoiling + count)  # upcasting --> True = 1
print(bool(milk))  # value casted to true, 0 casted to false, None casted to false

# logical operations
# and, or, not

# Real numbers


ideal_temp = 95.5
current_temp = 95.49
print(f"{ideal_temp}")
print(f"{current_temp}")
print(f"Diff {ideal_temp - current_temp}")  # precision issue
print(sys.float_info)
