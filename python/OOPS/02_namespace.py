# we can have variables, generators, functions anything
class Chai:
    # inside class variable are called properties
    # or attibutes
    origin = "India"


Chai.is_hot = True  # python formatter is giving error but it allows to run
print(Chai.is_hot)
print(Chai.origin)

# creating objects from Object chai
masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False
print(f"Masala : {masala.is_hot}")  # false
print(f"Class Chai : {Chai.is_hot}")  # true

# each object has its own namespace and change in objects won't affect class by default
masala.flavor = "Black Pepper"
print(masala.flavor)
