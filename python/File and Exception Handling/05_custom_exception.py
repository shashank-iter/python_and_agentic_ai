class OutOfIngregientError(Exception):
    pass


def make_chai(milk, sugar):
    try:
        if milk == 0 or sugar == 0:
            raise OutOfIngregientError("Not enough ingregients")
    except OutOfIngregientError as e:
        # handling custom exception
        print("Error", e)

    print("chai is ready")


make_chai(0, 0)
