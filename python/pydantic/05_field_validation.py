from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    # to be added at last after adding all attributes
    @field_validator("username")
    def username_length(
        cls, v
    ):  # cls = class parameter, function has access to entire class
        # just validates one field
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v  # return is required either rest of thing validation won't work


class SignUpData(BaseModel):
    password = str
    confirm_password = str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.passwords != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values
