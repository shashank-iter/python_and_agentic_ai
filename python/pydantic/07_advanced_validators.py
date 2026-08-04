from datetime import datetime

from pydantic import BaseModel, field_validator, model_validator


class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalize(cls, v):
        print(v)
        if not v.istitle():
            raise ValueError("Name must be capitalized")
        return v


person = Person(first_name="Shashank", last_name="Pandey")
print(person)


class User(BaseModel):
    email: str

    @field_validator("email")
    def is_lower_case(cls, v):
        if v.lower() != v:
            raise ValueError("Email must be in lower case")
        return v


user = User(email="hello@microsoft.com")
print(user)


class Product(BaseModel):
    price: str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date(cls, v):
        if v.start_date >= v.end_date:
            raise ValueError("start_date must be before end_date")
        return v

date = DateRange(start_date=datetime(2024, 1, 1), end_date=datetime(2024, 12, 31))
print(date)
