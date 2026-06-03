essentials = {"Cardamom", "Ginger", "Black Pepper"}
normal = {"Clove", "Ginger", "Yellow Pepper"}

union = essentials | normal
print(union)

intersection = essentials & normal
print(intersection)

only_in_essentials = essentials - normal
print(only_in_essentials)

# membership check
print("Clove" in normal)
