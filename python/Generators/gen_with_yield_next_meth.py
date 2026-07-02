# generator with yield and next method
# you save memory
# you don't want the results immediately
# lazy evaluation
def serve_chai():
    yield "Cup1: Hello"
    yield "Cup2: World"


#  ex = serve_chai()
# print(ex)
# above code prints the generator object
#
stall = serve_chai()
# stall will hold the referece to the serve_chai generator
# and then when we run the loop it goes and extracts the value
# yield pauses the function and resumes it on next call from where it was paused
#

for cup in stall:
    print(cup)


# normal function
def get_chai_list():
    return ["Cup1", "Cup2"]


# generator function
def yield_chai_list():
    yield "Cup1"
    yield "Cup2"


chai = yield_chai_list()
# here the chai would hold ref to the generator func
# print(next(chai)) would actually call and print the first yield from the fucntion
# and pause the function
# and the function will still be in the memory
# on next it will give next value
# once values finish it will give error
# used a lot in fastapi, manageing data base connections and all.
print(next(chai))
