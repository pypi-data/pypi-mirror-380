from typing import Optional
from .request import Request
from .response import Response


class Middleware:
    """Базовый класс middleware"""
    
    async def process_request(self, request: Request) -> Request:
        """Обработка входящего запроса"""
        return request
    
    async def process_response(self, request: Request, response: Response) -> Response:
        """Обработка исходящего ответа"""
        return response


class CORSMiddleware(Middleware):
    """CORS middleware"""
    
    def __init__(self, allow_origins: list = None, allow_methods: list = None):
        self.allow_origins = allow_origins or ["*"]
        self.allow_methods = allow_methods or ["GET", "POST", "PUT", "DELETE"]
    
    async def process_response(self, request: Request, response: Response) -> Response:
        origin = request.headers.get("origin", "")
        
        if "*" in self.allow_origins or origin in self.allow_origins:
            response.headers.append((b"access-control-allow-origin", origin.encode()))
            response.headers.append((
                b"access-control-allow-methods", 
                ", ".join(self.allow_methods).encode()
            ))
            response.headers.append((b"access-control-allow-headers", b"*"))
        
        return response