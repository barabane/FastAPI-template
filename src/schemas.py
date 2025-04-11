from typing import Optional
from pydantic import BaseModel
from fastapi import Request

class RequestLogScheme(BaseModel):
    request_url: str
    request_method: str
    response_status_code: int
    response_headers: dict
    