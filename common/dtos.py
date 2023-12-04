from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    status_code: int
    message: str
    data: Optional[T] = Field(default=None)
