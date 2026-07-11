# Constructors and Init in Python
# Initialization: Initializing and instance of class with some arguements, done by constructor


class ChaiOrder:
    # this is a constuctor, so whenever an instance of class is created, we can pass on these values,
    # we can have default values for these too actually
    def __init__(self, type_="Default", size=100) -> None:
        # why type_ has underscore in variable, as type is also an operator, thus dont confuse please.
        # avoid any reserved keywords
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} Chai"


order = ChaiOrder("Black", 200)
# instance of ChaiOrder is created
print(order.summary())

order2 = ChaiOrder("Green", 150)
print(order2.summary())

order3 = ChaiOrder()
print(order3.summary())
