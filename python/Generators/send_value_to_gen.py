# send value to generator
# till here we have seen that yelid gives the data
# we can also send data to yield


def chai_customer():
    print("Order Pls")
    order = yield  # revieves from .send
    while True:
        print(f"{order}")
        order = yield  # if not here loop keeps printing infinite


stall = chai_customer()
next(stall)  # start generator
stall.send("masala chai")
stall.send("lemon chai")
