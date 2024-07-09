from pydantic import BaseModel


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "..?"
            }
        }
