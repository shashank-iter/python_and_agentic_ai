# whenever we try to open a file in a python program
# it is loaded on the memory and then opened
# once its closed, its loaded off the memory
# mishaps can happen in between this process thus
# we need try except to handle this
# file = open("order.txt", "w")
# # if this file is not there, a new one will be created

# try:
#     file.write("Ginger Chai = 2 Cups")
# finally:
#     file.close()

# this piece of code does same thing as above
with open("order.txt", "w") as file:
    file.write("Javascript")

# as soon as we take the reference of the file
# it invokes a dunder file.__enter__ on opening it
# and file.__close__ on closing the file.
#
# with keyword calls all these automatically
# There are lot many file handling libraries out there
# you should use then instead of directly using this.
