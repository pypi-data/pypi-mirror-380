import asyncio
import inspect
from typing import Dict, List, Callable, Any, Optional
from .routing import Router
from .request import Request
from .response import Response
from .middleware import Middleware
from .exceptions import HTTPException
import json


class Furiek:
    """Основной класс приложения Furiek"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.router = Router()
        self.middleware: List[Middleware] = []
        self.error_handlers: Dict[int, Callable] = {}
        self.startup_handlers: List[Callable] = []
        self.shutdown_handlers: List[Callable] = []
        
    def route(self, path: str, methods: Optional[List[str]] = None, **kwargs):
        """Декоратор для регистрации маршрутов"""
        if methods is None:
            methods = ["GET"]
            
        def decorator(handler: Callable):
            self.router.add_route(path, handler, methods, **kwargs)
            return handler
        return decorator
    
    def get(self, path: str, **kwargs):
        """GET маршрут"""
        return self.route(path, ["GET"], **kwargs)
    
    def post(self, path: str, **kwargs):
        """POST маршрут"""
        return self.route(path, ["POST"], **kwargs)
    
    def put(self, path: str, **kwargs):
        """PUT маршрут"""
        return self.route(path, ["PUT"], **kwargs)
    
    def delete(self, path: str, **kwargs):
        """DELETE маршрут"""
        return self.route(path, ["DELETE"], **kwargs)
    
    def patch(self, path: str, **kwargs):
        """PATCH маршрут"""
        return self.route(path, ["PATCH"], **kwargs)
    
    def add_middleware(self, middleware_class):
        """Добавление middleware"""
        self.middleware.append(middleware_class())
    
    def error_handler(self, status_code: int):
        """Декоратор для обработчиков ошибок"""
        def decorator(handler: Callable):
            self.error_handlers[status_code] = handler
            return handler
        return decorator
    
    def on_startup(self, handler: Callable):
        """Добавление обработчика запуска"""
        self.startup_handlers.append(handler)
        return handler
    
    def on_shutdown(self, handler: Callable):
        """Добавление обработчика завершения"""
        self.shutdown_handlers.append(handler)
        return handler
    
    async def __call__(self, scope, receive, send):
        """ASGI интерфейс"""
        if scope["type"] == "http":
            await self.handle_http(scope, receive, send)
        elif scope["type"] == "lifespan":
            await self.handle_lifespan(scope, receive, send)
    
    async def handle_lifespan(self, scope, receive, send):
        """Обработка событий жизненного цикла"""
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                for handler in self.startup_handlers:
                    if inspect.iscoroutinefunction(handler):
                        await handler()
                    else:
                        handler()
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                for handler in self.shutdown_handlers:
                    if inspect.iscoroutinefunction(handler):
                        await handler()
                    else:
                        handler()
                await send({"type": "lifespan.shutdown.complete"})
                break
    
    async def handle_http(self, scope, receive, send):
        """Обработка HTTP запросов"""
        request = Request(scope, receive)
        response = await self.process_request(request)
        
        await send({
            "type": "http.response.start",
            "status": response.status_code,
            "headers": response.headers,
        })
        
        await send({
            "type": "http.response.body",
            "body": response.body,
        })
    
    async def process_request(self, request: Request) -> Response:
        """Обработка запроса через middleware и роутинг"""
        try:
            # Выполнение middleware до обработки
            for middleware in self.middleware:
                request = await middleware.process_request(request)
            
            # Поиск и выполнение обработчика
            handler, kwargs = self.router.find_route(request.method, request.path)
            
            if handler is None:
                raise HTTPException(404, "Not Found")
            
            # Вызов обработчика
            if inspect.iscoroutinefunction(handler):
                result = await handler(request, **kwargs)
            else:
                result = handler(request, **kwargs)
            
            # Преобразование результата в Response
            if isinstance(result, Response):
                response = result
            elif isinstance(result, dict):
                response = Response.json(result)
            elif isinstance(result, (str, bytes)):
                response = Response(result)
            else:
                response = Response(str(result))
            
        except HTTPException as e:
            response = await self.handle_error(e.status_code, e.detail)
        except Exception as e:
            if self.debug:
                response = Response(f"Server Error: {str(e)}", status=500)
            else:
                response = await self.handle_error(500, "Internal Server Error")
        
        # Выполнение middleware после обработки
        for middleware in reversed(self.middleware):
            response = await middleware.process_response(request, response)
        
        return response
    
    async def handle_error(self, status_code: int, detail: str) -> Response:
        """Обработка ошибок"""
        if status_code in self.error_handlers:
            handler = self.error_handlers[status_code]
            result = handler(Request({}, None))  # Mock request
            if isinstance(result, Response):
                return result
            return Response(str(result), status=status_code)
        
        return Response(detail, status=status_code)
    
    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs):
        """Запуск сервера разработки"""
        try:
            import uvicorn
        except ImportError:
            raise RuntimeError(
                "uvicorn не установлен. Установите: pip install uvicorn"
            )
        
        uvicorn.run(self, host=host, port=port, **kwargs)