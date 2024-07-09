from fastapi import Request
from fastapi.responses import JSONResponse
from utils.exceptions.exceptions import (
    NotFound,
    UnprocessableEntity,
    BadRequest,
    Forbidden,
    NotAuthorized
)


async def not_found_exception_handler(_: Request, exc: NotFound):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc.name} not found"}
    )


async def unprocessable_exception_handler(_: Request, exc: UnprocessableEntity):
    return JSONResponse(
        status_code=422,
        content={"message": f"{exc.message}"}
    )


async def bad_request_exception_handler(_: Request, exc: BadRequest):
    return JSONResponse(
        status_code=400,
        content={"message": f"{exc.message}"}
    )


async def not_authorized_exception_handler(_: Request, exc: NotAuthorized):
    return JSONResponse(
        status_code=401,
        content={"message": f"{exc.message}"}
    )


async def forbidden_exception_handler(_: Request, exc: Forbidden):
    return JSONResponse(
        status_code=403,
        content={"message": f"{exc.message}"}
    )


async def server_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error. Please contact us."}
    )
