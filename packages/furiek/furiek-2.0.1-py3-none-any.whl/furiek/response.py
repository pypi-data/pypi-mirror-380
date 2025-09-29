from typing import Dict, Any, Optional
import json


class Response:
    def __init__(
        self, 
        content: Any = "", 
        status: int = 200, 
        headers: Optional[Dict[str, str]] = None,
        content_type: str = "text/plain"
    ):
        self.content = content
        self.status_code = status
        self.headers = []
        self._set_content_type(content_type)
        
        if headers:
            for key, value in headers.items():
                self.headers.append((key.lower().encode(), value.encode()))
    
    def _set_content_type(self, content_type: str):
        """Установка Content-Type заголовка"""
        self.headers.append((b"content-type", content_type.encode()))
    
    @property
    def body(self) -> bytes:
        if isinstance(self.content, bytes):
            return self.content
        elif isinstance(self.content, str):
            return self.content.encode()
        else:
            return str(self.content).encode()
    
    @classmethod
    def json(cls, data: Any, status: int = 200, **kwargs) -> "Response":
        """Создание JSON ответа"""
        content = json.dumps(data, ensure_ascii=False)
        return cls(content, status, content_type="application/json", **kwargs)
    
    @classmethod
    def html(cls, content: str, status: int = 200, **kwargs) -> "Response":
        """Создание HTML ответа"""
        return cls(content, status, content_type="text/html", **kwargs)
    
    @classmethod
    def redirect(cls, url: str, status: int = 302) -> "Response":
        """Перенаправление"""
        headers = {"Location": url}
        return cls("", status, headers=headers)