seat_type = input("Enter seat type: (sleeper/AC/general/luxe)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper Available")
    case "ac":
        print("AC Available")
    case "general":
        print("General Class")
    case "luxe":
        print("Suites Luxes")
    case _:
        print("Invalid  Seat")

# ternary operator
order_amount = int(input("Order Amount"))
delivery_fee = 0 if order_amount > 300 else 30
print(delivery_fee)

snack = input("Enter your preffered snack").lower()
if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa and tea!")
