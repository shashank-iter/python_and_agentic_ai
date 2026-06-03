# mutable
# cousin of array


ingredients = ["Water", "Milk", "Black Tea"]
ingredients.append("Sugar")
print(f"Ingredients {ingredients}")

ingredients.remove("Water")
print(f"Ingredients {ingredients}")

spice_options = ["Ginger", "Cardamom"]
chai_ingredients = ["Water", "Milk"]
chai_ingredients.extend(spice_options)
print(f"Chai Ingredients {chai_ingredients}")
chai_ingredients.insert(2, "Black Tea")
print(f"Chai Ingredients {chai_ingredients}")

x = chai_ingredients.pop()  # removes last element
print(x)
chai_ingredients.reverse()
print(f"Chai Ingredients {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai Ingredients {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"MAX: {max(sugar_levels)}")
print(f"Min: {min(sugar_levels)}")

# operator overloading
# + was not supposed to do this but it does
base_liquid = ["Water", "Milk"]
extra_flavor = ["Ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(full_liquid_mix)

strong_brew = ["black_tea", "water"] * 3
print(strong_brew)

# from operator import itemgetter
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinna", b"Card")
print(raw_spice_data)
