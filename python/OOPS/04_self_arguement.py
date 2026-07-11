class Chaicup:
    size = 150

    def describe(self):
        # self arguement will give refernce to class attributes
        # self is reference to all attributes in class
        return f"A {self.size}"


cup = Chaicup()
print(
    cup.describe()
)  # here an object is made and then describe is called, thus it has reference that object has called describe
# print(Chaicup.describe()) gives error as we are directly trying to execute describe method from the class
# and that method has self arguement, which is not provided here while calling thus it doesn't know who is calling the describe method.
#
print(Chaicup.describe(cup))  # we have provided object ref here, thus it will work
cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))  # reference of cup_two passed

# when you call a method from object, they have the context, but when calling from class, you need to pass the context to the method too.
