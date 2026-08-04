from typing import List, Optional

from pydantic import BaseModel, field_validator


class Comment(BaseModel):
    id: int
    content: str
    # here while referencing to comments we are giving
    # model name in quotes, its called forward references
    replies: Optional[List["Comment"]] = None

    @field_validator("content")
    def is_lower_case(cls, v):
        if v.lower() != v:
            raise ValueError("content must be lower case")
        return v


# model_rebuild is required after defining self referencing model
# either we will see crazy model performance degradation
Comment.model_rebuild()

comment = Comment(
    id=1,
    content="first comment",
    replies=[
        Comment(id=2, content="reply1"),
        Comment(
            id=2, content="reply 2", replies=[Comment(id=4, content="nested reply")]
        ),
    ],
)

print(comment)
