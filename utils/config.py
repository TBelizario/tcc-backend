from app.sensores.routes import sensoresRoutes, leituraSensorRoutes
from utils.exceptions.exceptions import (
    BadRequest, Forbidden, NotAuthorized,
    NotFound, ServerError, UnprocessableEntity)
from utils.exceptions.excpetionHandlers import (bad_request_exception_handler,
                                                forbidden_exception_handler,
                                                not_authorized_exception_handler,
                                                not_found_exception_handler,
                                                server_exception_handler,
                                                unprocessable_exception_handler)


def routes(app):
    app.include_router(sensoresRoutes.router)
    app.include_router(leituraSensorRoutes.router)


def errorHandler(app):
    app.add_exception_handler(NotFound, not_found_exception_handler)
    app.add_exception_handler(UnprocessableEntity,
                              unprocessable_exception_handler)
    app.add_exception_handler(BadRequest, bad_request_exception_handler)
    app.add_exception_handler(Forbidden, forbidden_exception_handler)
    app.add_exception_handler(NotAuthorized, not_authorized_exception_handler)
    app.add_exception_handler(ServerError, server_exception_handler)
