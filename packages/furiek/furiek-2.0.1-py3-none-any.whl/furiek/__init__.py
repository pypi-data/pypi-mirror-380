"""
Furiek - Современный веб-фреймворк для Python 3.11+
Быстрый, простой и эффективный фреймворк для создания веб-приложений.
"""

__version__ = "2.0.1"
__author__ = "Furieks"
__email__ = "furieks@bk.ru"

from .app import Furiek
from .request import Request
from .response import Response
from .exceptions import HTTPException

__all__ = ["Furiek", "Request", "Response", "HTTPException"]