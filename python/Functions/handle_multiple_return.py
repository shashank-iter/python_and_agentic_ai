# handle_multiple return
# if you don't return anything, None will return
# you can return multiple values as well as early return
def make_chai():
    return
    # even if pass was there same result


value = make_chai()
print(value)


def sold_cups():
    return 120


value = sold_cups()
print(value)


def chai_status(cups_left):
    if cups_left == 0:
        return "Not Available"
    return "Chai Ready"


value1 = chai_status(0)
value2 = chai_status(5)
print(value1)
print(value2)

# multiple return


def multi_return():
    return 100, 20, 30


# what if you dont want all the 3 values, just put underscore
one, two, _ = multi_return()
