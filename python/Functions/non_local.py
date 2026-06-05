# Non Local vs Global Scope


def update_order():
    chai_type = "Elaichi"

    def kitchen():
        # non local looks just above the function not outside that. If nothing present error comes.
        nonlocal chai_type  # iska mtlb refer to outer function, it will update outer chai_type variable
        # if the above line is not there the outer variable won't be there.
        chai_type = "Kesar"

    kitchen()
    print(f"Chai Type {chai_type}")


update_order()
