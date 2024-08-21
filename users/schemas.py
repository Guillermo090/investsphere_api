from pydantic import BaseModel, Field
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int] = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    