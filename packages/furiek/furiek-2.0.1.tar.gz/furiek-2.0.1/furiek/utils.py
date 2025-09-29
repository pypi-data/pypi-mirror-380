import json
from typing import Any, Dict
from .response import Response


def json_response(data: Any, status: int = 200, **kwargs) -> Response:
    """Утилита для создания JSON ответов"""
    return Response.json(data, status, **kwargs)


def html_response(content: str, status: int = 200, **kwargs) -> Response:
    """Утилита для создания HTML ответов"""
    return Response.html(content, status, **kwargs)