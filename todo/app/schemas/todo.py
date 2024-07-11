from typing import Optional
from fastapi import Form
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: Optional[int] = Field(default=None)  # int | None 여기서도 Default 지정이 필요
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)
