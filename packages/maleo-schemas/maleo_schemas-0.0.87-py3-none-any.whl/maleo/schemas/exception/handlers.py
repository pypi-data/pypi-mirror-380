import logging
from fastapi import Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import (
    HTTPException,
    RequestValidationError,
    ResponseValidationError,
)
from fastapi.requests import HTTPConnection
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.authentication import AuthenticationError
from maleo.logging.enums import Level, LoggerType
from ..error.constants import ERROR_CODE_STATUS_CODE_MAP
from ..error.enums import Code as ErrorCode
from ..response import (
    UnauthorizedResponse,
    UnprocessableEntityResponse,
    InternalServerErrorResponse,
    ErrorFactory as ErrorResponseFactory,
)
from .exc import MaleoException, exceptions


def authentication_error_handler(conn: HTTPConnection, exc: AuthenticationError):
    return JSONResponse(
        content=UnauthorizedResponse(
            other={
                "exc_type": type(exc).__name__,
                "exc_data": {
                    "message": str(exc),
                    "args": exc.args,
                },
            }
        ).model_dump(mode="json"),
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


async def general_exception_handler(request: Request, exc: Exception) -> Response:
    if isinstance(
        exc,
        (
            RequestValidationError,
            ResponseValidationError,
            ValidationError,
        ),
    ):
        return JSONResponse(
            content=UnprocessableEntityResponse(
                other=jsonable_encoder(exc.errors())
            ).model_dump(mode="json"),
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    elif isinstance(exc, HTTPException):
        other = {
            "exc_type": type(exc).__name__,
            "exc_data": {
                "status_code": exc.status_code,
                "detail": exc.detail,
                "headers": exc.headers,
            },
        }

        response_cls = ErrorResponseFactory.cls_from_code(exc.status_code)
        return JSONResponse(
            content=response_cls(other=other).model_dump(mode="json"),
            status_code=exc.status_code,
        )
    elif isinstance(exc, MaleoException):
        logger = logging.getLogger(
            f"{exc.application_context.environment} - {exc.application_context.key} - {LoggerType.EXCEPTION}"
        )

        exc.operation.log(logger, Level.ERROR)

        return JSONResponse(
            content=exc.response.model_dump(mode="json"),
            status_code=exc.error.spec.status_code,
        )
    elif isinstance(exc, exceptions):
        logger = logging.getLogger(
            f"{exc.application_context.environment} - {exc.application_context.key} - {LoggerType.EXCEPTION}"
        )

        exc.operation.log(logger, Level.ERROR)

        return JSONResponse(
            content=exc.response.model_dump(mode="json"),
            status_code=exc.error.spec.status_code,
        )

    other = {
        "exc_type": type(exc).__name__,
        "exc_data": {
            "message": str(exc),
            "args": exc.args,
        },
    }

    # Get the first arg as a potential ErrorCode
    code = exc.args[0] if exc.args else None

    if isinstance(code, ErrorCode):
        error_code = code
    elif isinstance(code, str) and code in ErrorCode:
        error_code = ErrorCode[code]
    else:
        error_code = None

    if error_code is not None:
        status_code = ERROR_CODE_STATUS_CODE_MAP.get(error_code, None)

        if status_code is not None:
            response_cls = ErrorResponseFactory.cls_from_code(status_code)
            return JSONResponse(
                content=response_cls(other=other).model_dump(mode="json"),
                status_code=status_code,
            )

    return JSONResponse(
        content=InternalServerErrorResponse(other=other).model_dump(mode="json"),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
