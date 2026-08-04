from pydantic import BaseModel

# majority of tasks: basemodel is used


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 101, "name": "Shashank", "is_active": True}
user = User(**input_data)
# unpack the dict(input_data) with ** either it won't work
print(user)

# always import base model
# add type annotation
# always unpack dict while using pydantic
# automatic validations: pydantic automatically convert types into
# defined type annotations, like '101' won't give error for int type as
# it gets converted
