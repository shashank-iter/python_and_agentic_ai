# set comprehension
# { expression for item in iterable if condition}
fav = [
    "Amul Masti",
    "Masti Dahi",
    "Suddh Paneer",
    "Khoya",
    "Masti Dahi",
    "Suddh Paneer",
]

unique_items = {unique for unique in fav}  # condition can also be added
# we are using curly braces for writing comprehension thus its
# set and will only put unique elements while looping over.
print(unique_items)

# recipes = {
#     "Base": "Dahi and Tomato Gravy",
#     "Masala": ["Dhaniya", "Pudina", "Lehsun", "Lal Mirch"],
#     "Aroma": "Elaichi",
#     "Flame": "Medium",
# }

recipes = {
    "Masala_1": ["Dhaniya", "Pudina", "Lehsun", "Lal Mirch"],
    "Masala_2": ["Dhaniya", "Haldi", "Lehsun", "Deggi Mirch"],
}

unique_spices = {spice for uni in recipes.values() for spice in uni}
# getting unique item from a dict containing list
# exp (spice) (final thing to returned to be used as exp) -->
# for uni(var) in recipes.values()(getting all the values, i:e list) -->
# for spice (second var, returned and used as exp too) -->
# in uni (var where lists were stored from dict values)
print(unique_spices)
