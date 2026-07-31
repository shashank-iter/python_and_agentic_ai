def serve_chai(flavor):
    try:
        if flavor == "unknown":
            raise ValueError("We don't have that!")
        print(f"Serving {flavor} chai")

    except ValueError as e:
        print("Error serving chai", e)
    else:
        print("Chai served successfully")
    finally:
        print("Cleaning up")


serve_chai("Masala")
serve_chai("unknown")
