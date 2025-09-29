"""
Лексический анализатор для PyLite
"""

import re
import string
from typing import List, Optional, Iterator, Tuple
from .tokens import Token, TokenType, KEYWORDS
from .error_handler import LexerError, ErrorHandler


class Lexer:
    """Лексический анализатор - разбивает исходный код на токены"""
    
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        self.indent_stack: List[int] = [0]  # Стек для отслеживания отступов
        self.error_handler = ErrorHandler()
    
    def tokenize(self) -> List[Token]:
        """Основной метод токенизации"""
        try:
            at_line_start = True
            
            while self.position < len(self.source):
                # Обработка новых строк
                if self.current_char() == '\n':
                    self._handle_newline()
                    at_line_start = True
                    continue
                
                # Обработка отступов в начале логической строки
                if at_line_start:
                    self._handle_indentation()
                    at_line_start = False
                
                self._skip_whitespace_and_comments()
                
                if self.position >= len(self.source):
                    break
                
                # Пропускаем новые строки после пробелов/комментариев
                if self.current_char() == '\n':
                    continue
                
                token = self._next_token()
                if token:
                    self.tokens.append(token)
            
            # Добавляем DEDENT токены для закрытия всех блоков
            while len(self.indent_stack) > 1:
                self.indent_stack.pop()
                self.tokens.append(Token(TokenType.DEDENT, None, self.line, self.column))
            
            # EOF токен
            self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
            
            return self.tokens
            
        except Exception as e:
            if isinstance(e, LexerError):
                raise e
            else:
                raise LexerError(
                    self.error_handler.create_friendly_message(
                        'invalid_character', 
                        char=str(e), 
                        line=self.line
                    ),
                    self.line,
                    self.column
                )
    
    def current_char(self) -> Optional[str]:
        """Возвращает текущий символ"""
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """Возвращает символ со смещением без изменения позиции"""
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> Optional[str]:
        """Переходит к следующему символу"""
        if self.position >= len(self.source):
            return None
        
        char = self.source[self.position]
        self.position += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def _skip_whitespace_and_comments(self):
        """Пропускает пробелы и комментарии (кроме новых строк)"""
        while self.current_char() is not None:
            char = self.current_char()
            
            # Пропускаем пробелы и табы (но не новые строки)
            if char in ' \t':
                self.advance()
            # Пропускаем комментарии
            elif char == '#':
                while self.current_char() is not None and self.current_char() != '\n':
                    self.advance()
            else:
                break
    
    def _handle_newline(self):
        """Обрабатывает символы новой строки"""
        self.advance()  # Пропускаем \n
        self.tokens.append(Token(TokenType.NEWLINE, '\n', self.line - 1, self.column))
    
    def _handle_indentation(self):
        """Обрабатывает отступы в начале строки"""
        indent_start_pos = self.position
        indent_level = 0
        
        # Считаем отступы (пробелы и табы)
        while self.current_char() in ' \t':
            if self.current_char() == ' ':
                indent_level += 1
            else:  # tab
                indent_level += 4  # Считаем таб как 4 пробела
            self.advance()
        
        # Если строка пустая или это комментарий, игнорируем отступы
        if self.current_char() in ['\n', '#', None]:
            return
        
        current_indent = self.indent_stack[-1]
        
        if indent_level > current_indent:
            # Увеличение отступа - новый блок
            self.indent_stack.append(indent_level)
            self.tokens.append(Token(TokenType.INDENT, None, self.line, 1))
        elif indent_level < current_indent:
            # Уменьшение отступа - закрытие блоков
            while len(self.indent_stack) > 1 and self.indent_stack[-1] > indent_level:
                self.indent_stack.pop()
                self.tokens.append(Token(TokenType.DEDENT, None, self.line, 1))
            
            # Проверяем, что отступ соответствует одному из предыдущих уровней
            if len(self.indent_stack) == 0 or self.indent_stack[-1] != indent_level:
                raise LexerError(
                    self.error_handler.create_friendly_message(
                        'invalid_indentation',
                        line=self.line
                    ),
                    self.line,
                    1
                )
    
    def _next_token(self) -> Optional[Token]:
        """Возвращает следующий токен"""
        char = self.current_char()
        
        if char is None:
            return None
        
        # Пропускаем пробелы
        if char in ' \t':
            self.advance()
            return None
        
        # Числа
        if char.isdigit() or (char == '.' and self.peek_char() and self.peek_char().isdigit()):
            return self._read_number()
        
        # Идентификаторы и ключевые слова
        if char.isalpha() or char == '_':
            return self._read_identifier()
        
        # Строки
        if char in ['"', "'"]:
            return self._read_string()
        
        # Операторы и разделители
        return self._read_operator_or_delimiter()
    
    def _read_number(self) -> Token:
        """Читает числовой литерал"""
        start_pos = self.position
        start_col = self.column
        is_float = False
        
        # Читаем цифры до точки
        while self.current_char() and self.current_char().isdigit():
            self.advance()
        
        # Проверяем точку для float
        if self.current_char() == '.' and self.peek_char() and self.peek_char().isdigit():
            is_float = True
            self.advance()  # Пропускаем точку
            
            while self.current_char() and self.current_char().isdigit():
                self.advance()
        
        number_str = self.source[start_pos:self.position]
        
        try:
            if is_float:
                value = float(number_str)
                return Token(TokenType.FLOAT, value, self.line, start_col)
            else:
                value = int(number_str)
                return Token(TokenType.INTEGER, value, self.line, start_col)
        except ValueError:
            raise LexerError(
                self.error_handler.create_friendly_message(
                    'invalid_number',
                    value=number_str,
                    line=self.line
                ),
                self.line,
                start_col
            )
    
    def _read_identifier(self) -> Token:
        """Читает идентификатор или ключевое слово"""
        start_pos = self.position
        start_col = self.column
        
        # Первый символ - буква или _
        self.advance()
        
        # Последующие символы - буквы, цифры или _
        while (self.current_char() and 
               (self.current_char().isalnum() or self.current_char() == '_')):
            self.advance()
        
        identifier = self.source[start_pos:self.position]
        
        # Проверяем, является ли это ключевым словом
        token_type = KEYWORDS.get(identifier, TokenType.IDENTIFIER)
        
        # Специальная обработка булевых значений
        if token_type == TokenType.TRUE:
            return Token(TokenType.BOOLEAN, True, self.line, start_col)
        elif token_type == TokenType.FALSE:
            return Token(TokenType.BOOLEAN, False, self.line, start_col)
        elif token_type == TokenType.NONE:
            return Token(token_type, None, self.line, start_col)
        
        return Token(token_type, identifier, self.line, start_col)
    
    def _read_string(self) -> Token:
        """Читает строковый литерал"""
        start_col = self.column
        quote_char = self.current_char()
        self.advance()  # Пропускаем открывающую кавычку
        
        value = ""
        
        while self.current_char() is not None and self.current_char() != quote_char:
            char = self.current_char()
            
            # Обработка escape-последовательностей
            if char == '\\':
                self.advance()
                next_char = self.current_char()
                
                if next_char is None:
                    break
                elif next_char == 'n':
                    value += '\n'
                elif next_char == 't':
                    value += '\t'
                elif next_char == 'r':
                    value += '\r'
                elif next_char == '\\':
                    value += '\\'
                elif next_char == quote_char:
                    value += quote_char
                else:
                    value += next_char
                
                self.advance()
            else:
                value += char
                self.advance()
        
        # Проверяем закрывающую кавычку
        if self.current_char() != quote_char:
            raise LexerError(
                self.error_handler.create_friendly_message(
                    'unclosed_string',
                    line=self.line
                ),
                self.line,
                start_col
            )
        
        self.advance()  # Пропускаем закрывающую кавычку
        
        return Token(TokenType.STRING, value, self.line, start_col)
    
    def _read_operator_or_delimiter(self) -> Optional[Token]:
        """Читает операторы и разделители"""
        char = self.current_char()
        start_col = self.column
        
        # Двухсимвольные операторы
        two_char = char + (self.peek_char() or '')
        
        if two_char == '==':
            self.advance()
            self.advance()
            return Token(TokenType.EQUAL, '==', self.line, start_col)
        elif two_char == '!=':
            self.advance()
            self.advance()
            return Token(TokenType.NOT_EQUAL, '!=', self.line, start_col)
        elif two_char == '<=':
            self.advance()
            self.advance()
            return Token(TokenType.LESS_EQUAL, '<=', self.line, start_col)
        elif two_char == '>=':
            self.advance()
            self.advance()
            return Token(TokenType.GREATER_EQUAL, '>=', self.line, start_col)
        elif two_char == '**':
            self.advance()
            self.advance()
            return Token(TokenType.POWER, '**', self.line, start_col)
        
        # Односимвольные операторы и разделители
        single_char_tokens = {
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.MULTIPLY,
            '/': TokenType.DIVIDE,
            '%': TokenType.MODULO,
            '=': TokenType.ASSIGN,
            '<': TokenType.LESS_THAN,
            '>': TokenType.GREATER_THAN,
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '[': TokenType.LEFT_BRACKET,
            ']': TokenType.RIGHT_BRACKET,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            ',': TokenType.COMMA,
            ':': TokenType.COLON,
            '.': TokenType.DOT,
            ';': TokenType.SEMICOLON,
        }
        
        if char in single_char_tokens:
            self.advance()
            return Token(single_char_tokens[char], char, self.line, start_col)
        
        # Неизвестный символ
        self.advance()
        raise LexerError(
            self.error_handler.create_friendly_message(
                'invalid_character',
                char=char,
                line=self.line
            ),
            self.line,
            start_col
        )
