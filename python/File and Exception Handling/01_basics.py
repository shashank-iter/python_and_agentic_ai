# Exception and File Handling
# Index Error: Index out of bound
# Key Error: Key not in Dict
# ZeroDivisonError
# Type Error
# Name Error
orders = ["Masala", "Gingers"]

# print(orders[2]) index out of List

chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("Key not found")
