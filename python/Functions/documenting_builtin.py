# Built in in python


def chai_flavor(flavor="masala"):
    # the below string is a doc string and it need to be the
    # very first line in the function, either uske up
    """Return the flavor of chai"""
    return flavor


# this thing is called dunder, which is inbuilt, helps in log trace
# other also available
print(chai_flavor.__doc__)
print(chai_flavor.__name__)


# all the help you need for any builtin function
# help(len)
#
def generate_bill(chai=0, samosa=0):
    """Calculate the total number of chai and samosa
    param chai: total no of chai 10 rupee each
    param samosa total no of samosa 15 rupee each
    return: all the shit
    """
    total = chai * 10 + samosa * 15
    return total, "thank you for visitng chaicode.com"
