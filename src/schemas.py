from pydantic import BaseModel


class RequestLogScheme(BaseModel):
    request_url: str
    request_method: str
    response_status_code: int
    response_headers: dict
