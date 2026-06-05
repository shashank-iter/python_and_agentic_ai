chai_type = "Plain"


def front_desk():
    def kitchen():
        # reference to global object from anywhere
        global chai_type
        chai_type = "Irani"

    kitchen()
    print(f"Chai type: {chai_type}")


front_desk()
