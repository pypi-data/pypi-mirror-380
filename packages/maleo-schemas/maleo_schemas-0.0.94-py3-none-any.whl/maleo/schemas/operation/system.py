from typing import Generic, Literal
from ..connection import OptionalConnectionContext
from ..error import (
    OptionalAnyErrorT,
    AnyErrorT,
)
from ..mixins.general import SuccessT
from ..response import ResponseT, ErrorResponseT, SuccessResponseT
from .action.system import SystemOperationAction
from .base import BaseOperation
from .enums import OperationType


class SystemOperation(
    BaseOperation[
        SystemOperationAction,
        None,
        SuccessT,
        OptionalAnyErrorT,
        OptionalConnectionContext,
        ResponseT,
        None,
    ],
    Generic[
        SuccessT,
        OptionalAnyErrorT,
        ResponseT,
    ],
):
    type: OperationType = OperationType.SYSTEM
    resource: None = None
    response_context: None = None


class FailedSystemOperation(
    SystemOperation[
        Literal[False],
        AnyErrorT,
        ErrorResponseT,
    ],
    Generic[AnyErrorT, ErrorResponseT],
):
    success: Literal[False] = False


class SuccessfulSystemOperation(
    SystemOperation[
        Literal[True],
        None,
        SuccessResponseT,
    ],
    Generic[SuccessResponseT],
):
    success: Literal[True] = True
    error: None = None
