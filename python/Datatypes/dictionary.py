# storing data as key-values
chai_order = dict(type="Masala Chai", size="Large", sugar="2")
print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in chai order? {'sugar' in chai_order}")
# print(f"Order Details (keys): {chai_order.keys()}")
# print(f"Order Details (Values): {chai_order.values()}")
# print(f"Order Details (Items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Remove last Item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai Recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai Size: {chai_size}")

# safe way of getting items from dict without crashing
customer_note = chai_order.get("Customer Note", "no note")
print(f"Customer Note: {customer_note}")
