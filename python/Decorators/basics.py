# Just a wrapper around your function
from functools import wraps


def my_decorator(func):
    @wraps(func)  # preserve function name and metadata, output will
    # print "wrapper" if this wrap is not used
    def wrapper():
        print("Before Function runs")
        func()
        print("After Function runs")

    return wrapper


@my_decorator
def greet():
    print("Decorator Test")


greet()
print(greet.__name__)
