# Inheritance and Composition is really used in production


class BaseBurger:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} Burger")


class BigBurger(BaseBurger):
    # big burger class as all the methods from BaseBurger and additionally add_filling() method too
    def add_filling(self):
        print("Added Tomato")
        print("Added Lettuce")


# composition
class BurgerKing:
    # here we are not creating an instance out of Base Burger
    # we are inheriting its values, hence we do not need parenthesis after BaseBurger
    burger_class = BaseBurger

    def __init__(self):
        self.burger = self.burger_class("Big Mac")

    def serve(self):
        print(f"Serving {self.burger.type} in BurgerKing")
        self.burger.prepare()


class FancyBurger(BurgerKing):
    burger_class = BigBurger


shop = BurgerKing()
fancy = FancyBurger()

shop.serve()
fancy.serve()
# python binds add_filling() to burger
fancy.burger.add_filling()
