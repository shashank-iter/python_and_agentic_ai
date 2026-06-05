chai = "Ginger Tea"


def prepare_chai(order):
    print(f"Preparing: {chai}")


prepare_chai(chai)

chai2 = [1, 2, 3]


def edit_chai(cup):
    cup[1] = 42


edit_chai(chai2)
print(chai2)

# args and *kwargs (keyword arguements)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low")
make_chai(tea="Green", sugar="High", milk="Yes")


# *args, **kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)


# all arguements without name are printed as tuple
# all arguements with keywords are there as dict
special_chai("Elaichi", "Laung", sweetner="honey", type="black")


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)


# # calling it twice would add two masala to the list, to avoid this
# chai_order()
# chai_order()


def chai_order(order=None):
    if order is None:
        order = []
    else:
        order.append("Masala")
    print(order)


# two different list, basically no double appending
chai_order([])
chai_order([])
