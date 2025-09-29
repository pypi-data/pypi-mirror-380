"""
PyLite - Упрощённый Python для детей

PyLite - это упрощённая версия языка Python, созданная специально 
для обучения детей программированию.
"""

__version__ = "0.1.0"
__author__ = "PyLite Team"

from .lexer import Lexer
from .parser import Parser  
from .interpreter import Interpreter
from .error_handler import ErrorHandler

__all__ = ['Lexer', 'Parser', 'Interpreter', 'ErrorHandler']
