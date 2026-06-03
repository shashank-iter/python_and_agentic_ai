# walrun operator
# Assignment (x=5) and Expresession (3+3)

# here bascially we calculate and store the remainder and then check for a condition to print stuff


value = 13
remainder = value % 5
if remainder:
    print(f"Not divisible remaineder is {remainder}")

# all this calculation and assignment to remainder can be done withiin if statement with walrus operator
if remainder := value % 5:
    print(f"Not divisible remaineder is {remainder}")

# example
avail_size = ["s", "m", "l"]
if req_size := input("Enter Size"):
    print(f"Serving {req_size} chai")

# example
flavors = ["Ginger", "Tulsi"]
while (flavor := input("Enter Flavor")) not in flavors:
    print(f"Sorry, {flavor} in not available")
print(f"You chose {flavor}")
