"""
Определения базовых типов и классов для PyLite.
"""

from typing import Callable, List, Any
from .error_handler import RuntimeError as PyLiteRuntimeError, ErrorHandler

class BuiltinFunction:
    """Обертка для встроенных функций"""
    
    def __init__(self, name: str, func: Callable, min_args: int = 0, max_args: int = None):
        self.name = name
        self.func = func
        self.min_args = min_args
        self.max_args = max_args if max_args is not None else min_args
        self.error_handler = ErrorHandler()
    
    def call(self, interpreter, arguments: List[Any]) -> Any:
        """Вызывает встроенную функцию"""
        if len(arguments) < self.min_args or len(arguments) > self.max_args:
            raise PyLiteRuntimeError(
                self.error_handler.create_friendly_message(
                    'wrong_arguments',
                    name=self.name,
                    expected=f"{self.min_args}-{self.max_args}" if self.min_args != self.max_args else str(self.min_args),
                    actual=len(arguments)
                )
            )
        
        try:
            return self.func(*arguments)
        except Exception as e:
            raise PyLiteRuntimeError(f"Ошибка в функции {self.name}: {str(e)}")
    
    def __str__(self):
        return f"<builtin function {self.name}>"

