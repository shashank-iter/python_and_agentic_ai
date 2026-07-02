# yeild from generator
def local_chai():
    yield "Masasla Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for Order"
    except:
        print("Stall closed, no more chai")


stall = chai_stall()
print(next(stall))
stall.close()
# triggers a generator exit method which cleans up memory
