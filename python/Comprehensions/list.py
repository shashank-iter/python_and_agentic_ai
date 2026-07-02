# List Comprehension
# [expression for item in iterable if condition]

menu = ["Chole bhature", "Vada Pav", "Lemon Rice", "Ginger Chai"]

nashta = [nashta for nashta in menu if "bhature" in nashta]
#        var nashta --> for nashta in menu (iterable) --> return if "bhature" occurs in nashta (condition can be anything)
print(nashta)
