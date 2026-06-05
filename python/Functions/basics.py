# Functions: to remove code duplications and reusability


def print_order(name, chai_type):  # parameters
    # pass: for dummy functions
    print(f"Order for {name} is {chai_type}")


print_order("Shashank", "Masala Chai!")  # arguements


def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()


# generate_report(): this won't work here


def fetch_sales():
    print("Fetched Sales Data")


def filter_valid_orders():
    print("Filtered Valid Sales Data")


def summarize_data():
    print("Data Summarised")


generate_report()  # works here

# Separation of Concern: Design Pattern


def get_input():
    print("Getting user Input")


def validate_input():
    print("validating data")


def save_to_db():
    print("Saving to DB")


def register_user():
    get_input()
    validate_input()
    save_to_db()


register_user()


# Improving Readability
def calculate_bill(number_of_cups, price_per_cup):
    return number_of_cups * price_per_cup


bill = calculate_bill(15, 200)
print(f"Bill is: {bill}")
print("Bill directly from print statement: ", calculate_bill(15, 200))


# Improving Tracability
def add_vat(price, vat_rate=10):
    vat = price * vat_rate // 100
    return vat + price


orders = [299, 566, 788]

for price in orders:
    final_amt = add_vat(price)
    print(f"Original: {price}, Final with VAT: {final_amt}")
