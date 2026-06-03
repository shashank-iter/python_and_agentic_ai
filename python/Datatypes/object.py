# Objects are mutable
# sugar_amount = 2
# print(f"Initial_amount: {sugar_amount}")

# # sugar_amount = 12
# print(f"Second_amount: {sugar_amount}")

# print(f"id of 2: {id(2)}")
# print(f"id of 12: {id(12)}")
# print(f"id of sugar_amount: {id(sugar_amount)}")

spice_mix = set()
spice_mix.add("Ginger")
print(f"id of spice_mix: {id(spice_mix)}")
# {"Ginger"} --> id = 0223
spice_mix.add("Honey")
print(f"id of spice_mix after adding Honey: {id(spice_mix)}")

# if immutable
# {"Ginger", "Honey"} --> id = id = 0224
# but its mutable, so id stays the same, but the contents change
