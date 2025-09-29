import pytest
from furiek import Furiek, Request, Response
from furiek.exceptions import HTTPException


class MockReceive:
    """Mock для ASGI receive"""
    async def __call__(self):
        return {"type": "http.request", "body": b"", "more_body": False}


class MockSend:
    """Mock для ASGI send"""
    def __init__(self):
        self.messages = []
    
    async def __call__(self, message):
        self.messages.append(message)


def test_app_creation():
    """Тест создания приложения"""
    app = Furiek()
    assert app.debug is False
    assert len(app.routes) == 0
    
    app_debug = Furiek(debug=True)
    assert app_debug.debug is True


def test_route_decorator():
    """Тест декоратора маршрутов"""
    app = Furiek()
    
    @app.get("/test")
    def test_handler(request):
        return "test"
    
    assert len(app.routes) == 1
    route = app.routes[0]
    assert route.path == "/test"
    assert route.handler == test_handler
    assert "GET" in route.methods


def test_multiple_methods():
    """Тест маршрутов с разными методами"""
    app = Furiek()
    
    @app.post("/create")
    def create_handler(request):
        return "created"
    
    @app.put("/update")
    def update_handler(request):
        return "updated"
    
    @app.delete("/delete")
    def delete_handler(request):
        return "deleted"
    
    assert len(app.routes) == 3
    methods = [route.methods[0] for route in app.routes]
    assert "POST" in methods
    assert "PUT" in methods
    assert "DELETE" in methods


def test_route_with_params():
    """Тест маршрутов с параметрами"""
    app = Furiek()
    
    @app.get("/user/{user_id}")
    def user_handler(request, user_id: str):
        return f"user {user_id}"
    
    handler, params = app.router.find_route("GET", "/user/123")
    assert handler == user_handler
    assert params["user_id"] == "123"


def test_response_creation():
    """Тест создания ответов"""
    # Текстовый ответ
    response = Response("Hello")
    assert response.status_code == 200
    assert response.body == b"Hello"
    
    # JSON ответ
    json_response = Response.json({"key": "value"})
    assert json_response.status_code == 200
    assert b"key" in json_response.body
    
    # HTML ответ
    html_response = Response.html("<h1>Title</h1>")
    assert b"text/html" in html_response.headers[0][1]
    
    # Редирект
    redirect_response = Response.redirect("/new-location")
    assert redirect_response.status_code == 302
    assert b"Location" in redirect_response.headers[0][0]


def test_request_parsing():
    """Тест парсинга запроса"""
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/test",
        "query_string": b"param=value",
        "headers": [(b"content-type", b"application/json")]
    }
    
    request = Request(scope, MockReceive())
    
    assert request.method == "GET"
    assert request.path == "/test"
    assert request.query_params["param"] == "value"
    assert "content-type" in request.headers


@pytest.mark.asyncio
async def test_async_handler():
    """Тест асинхронных обработчиков"""
    app = Furiek()
    
    @app.get("/async")
    async def async_handler(request):
        return "async response"
    
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/async",
        "headers": []
    }
    
    receive = MockReceive()
    send = MockSend()
    
    await app(scope, receive, send)
    
    assert len(send.messages) == 2
    assert send.messages[0]["type"] == "http.response.start"
    assert send.messages[1]["type"] == "http.response.body"


def test_error_handlers():
    """Тест обработчиков ошибок"""
    app = Furiek()
    
    @app.error_handler(404)
    def not_found_handler(request):
        return "Страница не найдена"
    
    @app.error_handler(500)
    def server_error_handler(request):
        return "Ошибка сервера"
    
    assert 404 in app.error_handlers
    assert 500 in app.error_handlers
    assert app.error_handlers[404].__name__ == "not_found_handler"


def test_middleware():
    """Тест middleware"""
    app = Furiek()
    
    from furiek.middleware import CORSMiddleware
    app.add_middleware(CORSMiddleware)
    
    assert len(app.middleware) == 1
    assert isinstance(app.middleware[0], CORSMiddleware)


def test_startup_shutdown():
    """Тест обработчиков запуска и завершения"""
    app = Furiek()
    
    startup_called = []
    shutdown_called = []
    
    @app.on_startup
    def startup_handler():
        startup_called.append(True)
    
    @app.on_shutdown
    def shutdown_handler():
        shutdown_called.append(True)
    
    assert len(app.startup_handlers) == 1
    assert len(app.shutdown_handlers) == 1
    
    # Вызов обработчиков
    app.startup_handlers[0]()
    app.shutdown_handlers[0]()
    
    assert len(startup_called) == 1
    assert len(shutdown_called) == 1


def test_http_exceptions():
    """Тест HTTP исключений"""
    with pytest.raises(HTTPException) as exc_info:
        raise HTTPException(404, "Not Found")
    
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Not Found"
    
    # Специализированные исключения
    not_found = NotFound()
    assert not_found.status_code == 404
    
    bad_request = BadRequest("Invalid data")
    assert bad_request.status_code == 400


@pytest.mark.asyncio
async def test_json_request():
    """Тест JSON запросов"""
    app = Furiek()
    
    @app.post("/json")
    async def json_handler(request):
        data = await request.json()
        return {"received": data}
    
    class JSONReceive:
        def __init__(self, data):
            self.data = json.dumps(data).encode()
            self.called = False
        
        async def __call__(self):
            if not self.called:
                self.called = True
                return {"type": "http.request", "body": self.data, "more_body": False}
            return {"type": "http.request", "body": b"", "more_body": False}
    
    import json
    
    scope = {
        "type": "http",
        "method": "POST",
        "path": "/json",
        "headers": [(b"content-type", b"application/json")]
    }
    
    test_data = {"name": "test", "value": 123}
    receive = JSONReceive(test_data)
    send = MockSend()
    
    await app(scope, receive, send)
    
    # Проверяем, что ответ содержит отправленные данные
    response_body = send.messages[1]["body"]
    response_data = json.loads(response_body.decode())
    assert "received" in response_data
    assert response_data["received"]["name"] == "test"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])