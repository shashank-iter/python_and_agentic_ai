from typing import List, Optional

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address  # nested pydantic model inside


address = Address(street="12", city="Zurich", postal_code="E3749D9")
user = User(id=1, name="John Doe", address=address)

print(user)

user_data = {
    "id": 1,
    "name": "Shashank",
    "address": {"street": "321 something", "city": "Paris", "postal_code": "fh380k"},
}

user2 = User(**user_data)
print(user2)
