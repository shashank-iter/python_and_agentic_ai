# used for saving the memory
# (expression for item in iterable if conditon) just in parenthesis
# [for x in items] --> makes entire list in memory
# (x for x in items) --> like a stream, returns things on the go

daily_sales = [1, 45, 3, 6, 2, 6, 2, 63, 6, 3]

total_cups_above_15 = sum(sale for sale in daily_sales if sale > 5)
# this generator is directly unusable, you need to consume it, here the sum() actually consumes it.
print(total_cups_above_15)

# generators with yeilds
