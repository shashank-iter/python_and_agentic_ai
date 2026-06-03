# topics to learn
#  for and while loop
# range(), enumerate(), zip()
# break, continue, else
# for vs while
# range is never inclusive

for token in range(1, 11):
    print(f"Serving chai to token number: {token}")

for batch in range(1, 5):
    print(f"Preparing chai for batch: {batch}")

# looping through list of names
# use a list of queue and print order names

order_list = ["Shashank", "Shishimanu", "Hattori"]
for name in order_list:
    print(f"Preparing Chai for: {name}")

# why we use enumrate
menu = ["Chai", "Samosa", "Patties"]
# enumerate is used to make this numbered, or give numbering to items.

for idx, item in enumerate(menu, start=1):
    print(f"item number: {idx}, item: {item}")

# zip is used to iterate over 2 iteratables
# used to itereate simultaneously over two iterable objects
names = ["Shishimanu", "Hattori", "Sinzo", "Keo"]
bills = [40, 20, 100, 34]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

# while loop
temperature = 40
# Used to keep on doing the steps until some condition is met

while temperature < 100:
    print(f"Current Temp: {temperature}")
    temperature += 15

print("Boiled")

# skip and break, continue
# continue allows you to skip one iteration of loop
# break allows you to break out of loop completely

flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tusli"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":
        print("Discontinued item not found")
        break
    print(flavor)

# for-else syntax

staff = [("Amit", 16), ("Shashank", 17)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
# if you see here "else" is the part of for-loop not the "if" statement
else:
    print("No one is eligible")
