from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # (default value)


product_one = Product(id=1, name="Laptop", price=99.89, in_stock=True)
product_two = Product(id=2, name="Mouse", price=99.89)
# product_three = Product(id=2, name="Mouse") # error missing param
print(product_one, product_two)

# Always use type annotations
# set sensible defaults whereever needed
# pydantic tries to convert data for you
