class InvalidChaiError(Exception):
    pass


def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Chai not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be int")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} of {flavor} chai: rupee {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting us!")


bill("mint", 2)
bill("masala", "three")
bill("masala", 2)
