# Tranformation for pydantic models to better operatable and
# storable formats like JSON, Dict or XML
from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []


# encoding date time as json
model_config = ConfigDict(
    json_encoders={datetime: lambda v: v.strftime("%d-%m=Y %H:%M:%S")}
)
# not using the above code will lead to date time appearing in standaed time format
# when converted to json dump

user = User(
    id=1,
    name="John Doe",
    email="john@example.com",
    createdAt=datetime(2024, 3, 15, 14, 30, 20),
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345",
    ),
    tags=["tag1", "tag2"],
)

python_dict = user.model_dump()
print(user)
print("=" * 60)
print(python_dict)
print("=" * 60)
json_str = user.model_dump_json()
