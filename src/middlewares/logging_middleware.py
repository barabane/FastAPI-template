from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from ..logger import logger
from ..schemas import RequestLogScheme


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        exception_object = None

        try:
            response: Response = await call_next(request)
        except Exception as e:
            exception_object = e

        message = RequestLogScheme(
            request_url=str(request.url),
            request_method=request.method,
            response_status_code=response.status_code,
            response_headers={**response.headers},
        ).model_dump_json(indent=2)

        logger.info(msg=message)

        return response
