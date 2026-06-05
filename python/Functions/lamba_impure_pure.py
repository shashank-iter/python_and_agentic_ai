# Pure vs Impure function
# recursive funtions
# Lambda / Anonymous Functions


def pure_chai(cups):
    return cups * 10


total_chai = 0


# not recommended
# impure function, alters a global variable
def impure_chai(cups):
    global total_chai
    total_chai += cups


# Recursive Functions
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)


print(pour_chai(5))

# lambda
chai_type = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_type))

print(strong_chai)
print(chai_type)
