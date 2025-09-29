class HTTPException(Exception):
    """Базовое исключение HTTP"""
    
    def __init__(self, status_code: int, detail: str = ""):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"{status_code}: {detail}")


class NotFound(HTTPException):
    """404 Not Found"""
    def __init__(self, detail: str = "Not Found"):
        super().__init__(404, detail)


class BadRequest(HTTPException):
    """400 Bad Request"""
    def __init__(self, detail: str = "Bad Request"):
        super().__init__(400, detail)


class InternalServerError(HTTPException):
    """500 Internal Server Error"""
    def __init__(self, detail: str = "Internal Server Error"):
        super().__init__(500, detail)