# Method Resolution Order (MRO)
# Multiple Inheritence


class A:
    label = "A: Base Class"


class B(A):
    label = "B: Masala Blend"


class C(A):
    label = "C: Herbal Blend"


class D(B, C):
    # if there is a common method in both B and C
    # then it will be called from class mentioned first
    pass


cup = D()
print(cup.label)
print(D.__mro__)  # dunder
