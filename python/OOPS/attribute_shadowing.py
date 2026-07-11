class Chai:
    temp = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temp)
cutting.temp = "super hot"
cutting.cup = "small"
print("After Changing", cutting.temp)  # we change the attribute in object namespace
print(
    "Direct in class", Chai.temp
)  # this will print value of attribute available in class

del cutting.temp  # deleted attribute from object's namespace
del cutting.cup
# print(cutting.cup) error comes up attribute error
#
print(cutting.temp)  # attribute fallsback to original class value
