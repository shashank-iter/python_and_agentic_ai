from typing import Dict, List, Optional

from pydantic import BaseModel

# we can use pydantic and typing lib together
# typing bring more types which pydantic lacks
# we can have our own types too


class Cart(BaseModel):
    user_id: int
    items: List[str]  # A list containing only strings
    quantities: Dict[str, int]  # Dict with key as str and value as int


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = (
        None  # optional but will be str and defualt value is None
    )


cart_data = {
    "user_id": 1,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3},
}

cart = Cart(**cart_data)
print(cart)
