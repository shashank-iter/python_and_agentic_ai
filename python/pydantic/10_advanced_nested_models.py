from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Address1(BaseModel):
    street: str
    city: str
    postal_code: str


# Optional Nested Model


class Company(BaseModel):
    name: str
    address: Optional[Address1] = None


class Employee(BaseModel):
    company: Optional[Company] = None


# Mixed Data Types


class TextContent(BaseModel):
    # new way to define types and attributes
    type: str = "Text"
    content = str


class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]


# Deeply Nested Structure


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Address(BaseModel):
    street: str
    city: City
    postal_code: str


class Organization(BaseModel):
    name: str
    hq: Address
    branches: List[Address] = []
