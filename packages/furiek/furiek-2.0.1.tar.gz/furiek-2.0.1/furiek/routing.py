import re
from typing import Dict, List, Callable, Any, Optional, Tuple
from .request import Request


class Route:
    def __init__(self, path: str, handler: Callable, methods: List[str], **kwargs):
        self.path = path
        self.handler = handler
        self.methods = methods
        self.kwargs = kwargs
        self.pattern = self._compile_pattern(path)
    
    def _compile_pattern(self, path: str) -> Tuple[re.Pattern, List[str]]:
        """Компиляция паттерна пути с параметрами"""
        pattern = path
        param_names = []
        
        # Замена параметров вида {param} на именованные группы
        param_pattern = r"\{(\w+)\}"
        matches = re.findall(param_pattern, path)
        
        for match in matches:
            param_names.append(match)
            pattern = pattern.replace(f"{{{match}}}", f"(?P<{match}>[^/]+)")
        
        pattern = f"^{pattern}$"
        return re.compile(pattern), param_names
    
    def match(self, path: str) -> Tuple[bool, Dict[str, str]]:
        """Проверка соответствия пути"""
        match = self.pattern[0].match(path)
        if match:
            params = match.groupdict()
            return True, params
        return False, {}


class Router:
    def __init__(self):
        self.routes: List[Route] = []
    
    def add_route(self, path: str, handler: Callable, methods: List[str], **kwargs):
        """Добавление маршрута"""
        route = Route(path, handler, methods, **kwargs)
        self.routes.append(route)
    
    def find_route(self, method: str, path: str) -> Tuple[Optional[Callable], Dict]:
        """Поиск маршрута по методу и пути"""
        for route in self.routes:
            if method in route.methods:
                matches, params = route.match(path)
                if matches:
                    return route.handler, params
        
        return None, {}