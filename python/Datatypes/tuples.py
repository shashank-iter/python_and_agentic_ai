# tuples are immutable
masala_spices = ("Cardamom", "Cloves", "Cinnamon")
(spice1, spice2, spice3) = masala_spices
print(f"Spice1: {spice1}, Spice2: {spice2}, Spice3: {spice3}")

ginger_ratio, cardamom = 2, 1
print(f"Ratio G: {ginger_ratio} and C:{cardamom}")
ginger_ratio, cardamom = cardamom, ginger_ratio
print(f"Ratio G: {ginger_ratio} and C:{cardamom}")

# membership test
print(f" Is ginger available ? {'Ginger' in masala_spices}")
print(f" Is Cardamom available ? {'Cardamom' in masala_spices}")
print(f" Is cardamom available ? {'cardamom' in masala_spices}")
