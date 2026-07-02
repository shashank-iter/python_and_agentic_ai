from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied")
            # here return statement is reqired
            # does give error when not returned
            # default reuturn None
        else:
            return func(user_role)
            # default reutrn None

    return wrapper


@require_admin
def access_tea_inventory(role):
    print("Access Granted")


access_tea_inventory("user")
access_tea_inventory("admin")
