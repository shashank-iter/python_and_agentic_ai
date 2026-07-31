from multiprocessing import Value


def process_order(item, quantity):
    try:
        price = {"masala": 30}[item]
        # the above piece of code looks of item in the dict
        cost = int(price) * int(quantity)
        print(f"total cost {cost}")
    except KeyError:
        print("Sorry not available")
    except TypeError:
        print("Quantity must be in number")
    except ValueError as e:
        print("Quantity must be in number", e)


process_order("ginger", 2)
process_order("masala", "two")
