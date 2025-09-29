"""
Обработчик ошибок с дружелюбными сообщениями для детей
"""

from typing import Optional, List, Dict
import traceback


class PyLiteError(Exception):
    """Базовый класс для всех ошибок PyLite"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)


class LexerError(PyLiteError):
    """Ошибка лексического анализа"""
    pass


class ParserError(PyLiteError):
    """Ошибка синтаксического анализа"""
    pass


class RuntimeError(PyLiteError):
    """Ошибка времени выполнения"""
    pass


class ValidationError(PyLiteError):
    """Ошибка валидации ограничений PyLite"""
    pass


class ErrorHandler:
    """Класс для обработки и форматирования ошибок"""
    
    def __init__(self):
        self.error_messages = self._init_error_messages()
    
    def _init_error_messages(self) -> Dict[str, str]:
        """Инициализирует дружелюбные сообщения об ошибках"""
        return {
            # Лексические ошибки
            'unclosed_string': "Ой! Ты забыл закрыть кавычки в строке {line}.",
            'invalid_character': "Странный символ '{char}' в строке {line}. Проверь, не опечатка ли это?",
            'invalid_number': "Число '{value}' написано неправильно в строке {line}. Попробуй ещё раз!",
            
            # Синтаксические ошибки
            'missing_colon': "Ты забыл поставить двоеточие ':' после {keyword} в строке {line}.",
            'missing_paren': "Не хватает закрывающей скобки ')' в строке {line}.",
            'missing_bracket': "Не хватает закрывающей квадратной скобки ']' в строке {line}.",
            'missing_brace': "Не хватает закрывающей фигурной скобки '}}' в строке {line}.",
            'unexpected_token': "Неожиданное слово '{token}' в строке {line}. Проверь правописание!",
            'invalid_indentation': "Неправильные отступы в строке {line}. В Python отступы очень важны!",
            
            # Ошибки времени выполнения
            'undefined_variable': "Переменная '{name}' не определена. Ты забыл её создать?",
            'division_by_zero': "Нельзя делить на ноль! Математика это не любит.",
            'type_error': "Нельзя использовать '{operation}' с типами {type1} и {type2}.",
            'index_error': "Индекс {index} слишком большой для списка длиной {length}.",
            'key_error': "Ключа '{key}' нет в словаре.",
            'attribute_error': "У объекта типа {type} нет свойства '{attr}'.",
            'function_not_found': "Функция '{name}' не найдена. Ты её определил?",
            'wrong_arguments': "Функции '{name}' нужно {expected} аргументов, а ты дал {actual}.",
            
            # Ошибки валидации
            'too_deep_nesting': "Слишком много уровней вложенности (больше 3). Попробуй упростить код.",
            'line_too_long': "Строка {line} слишком длинная. Попробуй разбить её на части.",
            'too_many_lines': "В программе слишком много строк (больше 500). Попробуй сделать её короче.",
        }
    
    def format_error(self, error: PyLiteError) -> str:
        """Форматирует ошибку в дружелюбное сообщение"""
        if isinstance(error, LexerError):
            return self._format_lexer_error(error)
        elif isinstance(error, ParserError):
            return self._format_parser_error(error)
        elif isinstance(error, RuntimeError):
            return self._format_runtime_error(error)
        elif isinstance(error, ValidationError):
            return self._format_validation_error(error)
        else:
            return f"Ошибка: {error.message}"
    
    def _format_lexer_error(self, error: LexerError) -> str:
        """Форматирует лексическую ошибку"""
        return f"📝 {error.message}"
    
    def _format_parser_error(self, error: ParserError) -> str:
        """Форматирует синтаксическую ошибку"""
        return f"🔍 {error.message}"
    
    def _format_runtime_error(self, error: RuntimeError) -> str:
        """Форматирует ошибку времени выполнения"""
        return f"🚀 {error.message}"
    
    def _format_validation_error(self, error: ValidationError) -> str:
        """Форматирует ошибку валидации"""
        return f"📏 {error.message}"
    
    def create_friendly_message(self, error_type: str, **kwargs) -> str:
        """Создает дружелюбное сообщение об ошибке"""
        template = self.error_messages.get(error_type, "Произошла ошибка: {error_type}")
        try:
            return template.format(**kwargs)
        except KeyError as e:
            return f"Ошибка в сообщении об ошибке: {e}"
    
    def handle_exception(self, exception: Exception, source_code: str = "") -> str:
        """Обрабатывает исключение и возвращает дружелюбное сообщение"""
        if isinstance(exception, PyLiteError):
            return self.format_error(exception)
        else:
            # Неожиданная ошибка Python
            error_type = type(exception).__name__
            error_message = str(exception)
            first_line = source_code.split('\n')[0].strip()
            if first_line:
                return f"� Системная ошибка: {error_type}: {error_message}\n   в коде, начинающемся с: {first_line}"
            else:
                return f"💥 Системная ошибка: {error_type}: {error_message}"
