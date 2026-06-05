# Scope and Named functions
# Scopes and Name Resolution
# Local Scope - inside a function
# Enclosing - from outer function if nested
# Global - Top level
# Built in
# L-E-G_B Rule


def serve_chai():
    chai_type = "Masala"  # local_scope
    print(f"Inside Function {chai_type}")


chai_type = "Lemon"  # wont pick this scope as local is available
serve_chai()
print(f"Outside Function: {chai_type}")

chai_order = "Tusli"


def chai_counter():
    chai_order = "lemon"  # enclosing scope

    def print_order():
        chai_order = "Ginger"
        print(f"Inner {chai_order}")

    print_order()

    print(f"Outer: {chai_order}")


chai_counter()
print(f"Global: {chai_order}")
