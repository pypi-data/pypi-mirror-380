from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Annotated, Generic, TypeVar
from maleo.types.dict import OptionalStringToAnyDict


TypeT = TypeVar("TypeT", bound=StrEnum)


class BaseOperationAction(BaseModel, Generic[TypeT]):
    type: Annotated[TypeT, Field(..., description="Action's type")]


class SimpleOperationAction(BaseOperationAction[TypeT], Generic[TypeT]):
    details: Annotated[
        OptionalStringToAnyDict, Field(None, description="Action's details")
    ] = None
