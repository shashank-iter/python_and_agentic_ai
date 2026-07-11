# Object Oriented Prorgramming
# Paradigm of programming, way of writing code
# everything is python is object
# class is internally implemented via object only
class ChaiTime:
     pass

class Chai:
    pass


print(type(Chai))
ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea) is Chai) # <class '__main__.Chai'> belongs to Chai class
print(type(ginger_tea) is ChaiTime)
