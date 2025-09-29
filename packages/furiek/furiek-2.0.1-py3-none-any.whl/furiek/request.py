from typing import Dict, List, Optional
import json


class Request:
    def __init__(self, scope, receive):
        self.scope = scope
        self.receive = receive
        self._body = None
    
    @property
    def method(self) -> str:
        return self.scope["method"]
    
    @property
    def path(self) -> str:
        return self.scope["path"]
    
    @property
    def headers(self) -> Dict[str, str]:
        return {
            key.decode().lower(): value.decode() 
            for key, value in self.scope["headers"]
        }
    
    @property
    def query_params(self) -> Dict[str, str]:
        query_string = self.scope.get("query_string", b"").decode()
        params = {}
        if query_string:
            for param in query_string.split("&"):
                if "=" in param:
                    key, value = param.split("=", 1)
                    params[key] = value
        return params
    
    async def body(self) -> bytes:
        if self._body is None:
            self._body = b""
            more_body = True
            while more_body:
                message = await self.receive()
                self._body += message.get("body", b"")
                more_body = message.get("more_body", False)
        return self._body
    
    async def json(self) -> Optional[Dict]:
        body = await self.body()
        if body:
            return json.loads(body.decode())
        return None
    
    async def form(self) -> Dict[str, str]:
        body = await self.body()
        form_data = {}
        if body:
            for param in body.decode().split("&"):
                if "=" in param:
                    key, value = param.split("=", 1)
                    form_data[key] = value
        return form_data