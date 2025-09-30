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
            'unclosed_string': "Ой! Похоже, ты забыл закрыть кавычки в строке {line}. Компьютер не понимает, где заканчивается твой текст. ✍️",
            'invalid_character': "Хм... Я нашёл странный символ '{char}' в строке {line}. Может быть, это опечатка? 🤔",
            'invalid_number': "Кажется, число '{value}' в строке {line} написано с ошибкой. Попробуй написать его по-другому, например: 123 или 3.14. 🔢",
            
            # Синтаксические ошибки
            'missing_colon': "Почти готово! Ты забыл поставить двоеточие ':' после слова '{keyword}' в строке {line}. Это важно для команд. 🎯",
            'missing_paren': "Кажется, где-то потерялась закрывающая скобка ')'. Проверь строку {line} и убедись, что все скобки на месте. 🤝",
            'missing_bracket': "Не хватает закрывающей квадратной скобки ']'. Проверь строку {line}. 📦",
            'missing_brace': "Не хватает закрывающей фигурной скобки '}}'. Проверь строку {line}. 🏺",
            'unexpected_token': "Я не ожидал увидеть '{token}' в строке {line}. Проверь, правильно ли написано слово, или может быть, ты что-то пропустил? 🧐",
            'invalid_indentation': "Ой, отступы! В строке {line} что-то не так с отступами. В PyLite они очень важны для создания блоков кода. 📏",
            
            # Ошибки времени выполнения
            'undefined_variable': "Я не могу найти переменную с именем '{name}'. Ты точно её создал с помощью знака '='? 🔍",
            'division_by_zero': "Ого! Ты пытаешься делить на ноль, а это невозможно. Математика говорит 'нет-нет-нет'! 🚫",
            'type_error': "Похоже, ты пытаешься сделать '{operation}' с вещами, которые несовместимы, как, например, сложить яблоко и число. 🍎 + 🔢 = ?",
            'index_error': "Ты пытаешься достать элемент из списка по номеру {index}, но в списке всего {length} элементов. Помни, что счёт начинается с 0! 📊",
            'key_error': "В словаре нет ключа '{key}'. Проверь, правильно ли ты написал ключ, и есть ли он в словаре. 🔑",
            'attribute_error': "У этого объекта нет свойства '{attr}'. Может быть, ты хотел использовать другое свойство? 🏷️",
            'function_not_found': "Я не нашёл функцию с именем '{name}'. Ты точно её создал с помощью слова 'def'? 🧑‍💻",
            'wrong_arguments': "Функция '{name}' ждёт {expected} аргументов, а ты передал {actual}. Проверь, все ли аргументы на месте. 📦",
            
            # Ошибки валидации
            'too_deep_nesting': "Ух ты, как глубоко! У тебя больше 3 уровней вложенности. Попробуй упростить код, чтобы он был понятнее. 🌳",
            'line_too_long': "Строка {line} получилась очень длинной. Попробуй разбить её на несколько коротких строк, так будет удобнее читать. ✂️",
            'too_many_lines': "Твоя программа стала очень большой (больше 500 строк)! Попробуй разделить её на части или упростить. 📜",
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
                return f"💥 Системная ошибка: {error_type}: {error_message}\n   в коде, начинающемся с: {first_line}"
            else:
                return f"💥 Системная ошибка: {error_type}: {error_message}"
