"""
Синтаксический анализатор (парсер) для PyLite
"""

from typing import List, Optional, Union
from .tokens import Token, TokenType
from .ast_nodes import *
from .error_handler import ParserError, ErrorHandler


class Parser:
    """Синтаксический анализатор - строит AST из токенов"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
        self.error_handler = ErrorHandler()
    
    def parse(self) -> Program:
        """Основной метод парсинга"""
        try:
            statements = []
            
            # Пропускаем начальные NEWLINE
            self._skip_newlines()
            
            while not self._is_at_end():
                if self.current_token().type == TokenType.EOF:
                    break
                
                stmt = self._parse_statement()
                if stmt:
                    statements.append(stmt)
                
                self._skip_newlines()
            
            return Program(statements)
            
        except Exception as e:
            if isinstance(e, ParserError):
                raise e
            else:
                current = self.current_token()
                raise ParserError(
                    self.error_handler.create_friendly_message(
                        'unexpected_token',
                        token=str(current.value),
                        line=current.line
                    ),
                    current.line,
                    current.column
                )
    
    def current_token(self) -> Token:
        """Возвращает текущий токен"""
        if self.position >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[self.position]
    
    def peek_token(self, offset: int = 1) -> Token:
        """Возвращает токен со смещением"""
        pos = self.position + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[pos]
    
    def advance(self) -> Token:
        """Переходит к следующему токену"""
        if not self._is_at_end():
            self.position += 1
        return self.tokens[self.position - 1]
    
    def _is_at_end(self) -> bool:
        """Проверяет, достигнут ли конец токенов"""
        return self.current_token().type == TokenType.EOF
    
    def _check(self, token_type: TokenType) -> bool:
        """Проверяет тип текущего токена"""
        if self._is_at_end():
            return False
        return self.current_token().type == token_type
    
    def _match(self, *token_types: TokenType) -> bool:
        """Проверяет и потребляет токен, если он совпадает"""
        for token_type in token_types:
            if self._check(token_type):
                self.advance()
                return True
        return False
    
    def _consume(self, token_type: TokenType, message: str) -> Token:
        """Потребляет токен или выбрасывает ошибку"""
        if self._check(token_type):
            return self.advance()
        
        current = self.current_token()
        raise ParserError(message, current.line, current.column)
    
    def _skip_newlines(self):
        """Пропускает токены NEWLINE"""
        while self._match(TokenType.NEWLINE):
            pass
    
    def _parse_statement(self) -> Optional[Statement]:
        """Парсит выражение-команду"""
        # Пропускаем пустые строки
        if self._check(TokenType.NEWLINE):
            return None
        
        # Определения функций
        if self._check(TokenType.DEF):
            return self._parse_function_def()
        
        # Определения классов
        if self._check(TokenType.CLASS):
            return self._parse_class_def()
        
        # Условные выражения
        if self._check(TokenType.IF):
            return self._parse_if_statement()
        
        # Циклы
        if self._check(TokenType.WHILE):
            return self._parse_while_statement()
        
        if self._check(TokenType.FOR):
            return self._parse_for_statement()
        
        # Return
        if self._check(TokenType.RETURN):
            return self._parse_return_statement()
        
        # Import
        if self._check(TokenType.IMPORT):
            return self._parse_import_statement()
        
        if self._check(TokenType.FROM):
            return self._parse_from_import_statement()
        
        # Присваивание или выражение
        return self._parse_expression_statement()
    
    def _parse_function_def(self) -> FunctionDef:
        """Парсит определение функции"""
        self._consume(TokenType.DEF, "Ожидалось 'def'")
        
        name_token = self._consume(TokenType.IDENTIFIER, 
                                  "Ожидалось имя функции после 'def'")
        name = name_token.value
        
        self._consume(TokenType.LEFT_PAREN, 
                     self.error_handler.create_friendly_message(
                         'missing_paren', line=self.current_token().line))
        
        # Параметры функции
        parameters = []
        if not self._check(TokenType.RIGHT_PAREN):
            parameters.append(self._consume(TokenType.IDENTIFIER, 
                                          "Ожидалось имя параметра").value)
            
            while self._match(TokenType.COMMA):
                parameters.append(self._consume(TokenType.IDENTIFIER,
                                              "Ожидалось имя параметра").value)
        
        self._consume(TokenType.RIGHT_PAREN,
                     self.error_handler.create_friendly_message(
                         'missing_paren', line=self.current_token().line))
        
        self._consume(TokenType.COLON,
                     self.error_handler.create_friendly_message(
                         'missing_colon', keyword='def', line=self.current_token().line))
        
        self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
        
        # Тело функции
        body = self._parse_block()
        
        return FunctionDef(name, parameters, body)
    
    def _parse_class_def(self) -> ClassDef:
        """Парсит определение класса"""
        self._consume(TokenType.CLASS, "Ожидалось 'class'")
        
        name_token = self._consume(TokenType.IDENTIFIER, 
                                  "Ожидалось имя класса после 'class'")
        name = name_token.value
        
        # Наследование (опционально)
        superclass = None
        if self._match(TokenType.LEFT_PAREN):
            superclass_token = self._consume(TokenType.IDENTIFIER,
                                           "Ожидалось имя родительского класса")
            superclass = superclass_token.value
            self._consume(TokenType.RIGHT_PAREN, "Ожидалась ')'")
        
        self._consume(TokenType.COLON,
                     self.error_handler.create_friendly_message(
                         'missing_colon', keyword='class', line=self.current_token().line))
        
        self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
        
        # Тело класса
        body = self._parse_block()
        
        return ClassDef(name, superclass, body)
    
    def _parse_if_statement(self) -> IfStmt:
        """Парсит условное выражение"""
        self._consume(TokenType.IF, "Ожидалось 'if'")
        
        condition = self._parse_expression()
        
        self._consume(TokenType.COLON,
                     self.error_handler.create_friendly_message(
                         'missing_colon', keyword='if', line=self.current_token().line))
        
        self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
        
        then_body = self._parse_block()
        
        # elif части
        elif_parts = []
        while self._check(TokenType.ELIF):
            self.advance()
            elif_condition = self._parse_expression()
            self._consume(TokenType.COLON,
                         self.error_handler.create_friendly_message(
                             'missing_colon', keyword='elif', line=self.current_token().line))
            self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
            elif_body = self._parse_block()
            elif_parts.append((elif_condition, elif_body))
        
        # else часть
        else_body = None
        if self._check(TokenType.ELSE):
            self.advance()
            self._consume(TokenType.COLON,
                         self.error_handler.create_friendly_message(
                             'missing_colon', keyword='else', line=self.current_token().line))
            self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
            else_body = self._parse_block()
        
        return IfStmt(condition, then_body, elif_parts, else_body)
    
    def _parse_while_statement(self) -> WhileStmt:
        """Парсит цикл while"""
        self._consume(TokenType.WHILE, "Ожидалось 'while'")
        
        condition = self._parse_expression()
        
        self._consume(TokenType.COLON,
                     self.error_handler.create_friendly_message(
                         'missing_colon', keyword='while', line=self.current_token().line))
        
        self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
        
        body = self._parse_block()
        
        return WhileStmt(condition, body)
    
    def _parse_for_statement(self) -> ForStmt:
        """Парсит цикл for"""
        self._consume(TokenType.FOR, "Ожидалось 'for'")
        
        target_token = self._consume(TokenType.IDENTIFIER,
                                    "Ожидалось имя переменной после 'for'")
        target = target_token.value
        
        self._consume(TokenType.IN, "Ожидалось 'in' после переменной цикла")
        
        iterable = self._parse_expression()
        
        self._consume(TokenType.COLON,
                     self.error_handler.create_friendly_message(
                         'missing_colon', keyword='for', line=self.current_token().line))
        
        self._consume(TokenType.NEWLINE, "Ожидался переход на новую строку после ':'")
        
        body = self._parse_block()
        
        return ForStmt(target, iterable, body)
    
    def _parse_return_statement(self) -> ReturnStmt:
        """Парсит команду return"""
        self._consume(TokenType.RETURN, "Ожидалось 'return'")
        
        value = None
        if not self._check(TokenType.NEWLINE) and not self._is_at_end():
            value = self._parse_expression()
        
        return ReturnStmt(value)
    
    def _parse_import_statement(self) -> ImportStmt:
        """Парсит команду import"""
        self._consume(TokenType.IMPORT, "Ожидалось 'import'")
        
        module_token = self._consume(TokenType.IDENTIFIER,
                                    "Ожидалось имя модуля после 'import'")
        module = module_token.value
        
        # Алиас (as name)
        alias = None
        # Note: 'as' не входит в наши ключевые слова, поэтому пропускаем эту функциональность
        
        return ImportStmt(module, alias)
    
    def _parse_from_import_statement(self) -> FromImportStmt:
        """Парсит команду from ... import ..."""
        self._consume(TokenType.FROM, "Ожидалось 'from'")
        
        module_token = self._consume(TokenType.IDENTIFIER,
                                    "Ожидалось имя модуля после 'from'")
        module = module_token.value
        
        self._consume(TokenType.IMPORT, "Ожидалось 'import'")
        
        # Список имён для импорта
        names = []
        names.append(self._consume(TokenType.IDENTIFIER,
                                 "Ожидалось имя для импорта").value)
        
        while self._match(TokenType.COMMA):
            names.append(self._consume(TokenType.IDENTIFIER,
                                     "Ожидалось имя для импорта").value)
        
        return FromImportStmt(module, names)
    
    def _parse_expression_statement(self) -> Statement:
        """Парсит выражение как команду или присваивание"""
        expr = self._parse_expression()
        
        # Проверяем на присваивание
        if self._match(TokenType.ASSIGN):
            if not isinstance(expr, IdentifierExpr):
                current = self.current_token()
                raise ParserError(
                    "Присваивание возможно только переменным",
                    current.line, current.column
                )
            
            value = self._parse_expression()
            return AssignmentStmt(expr.name, value)
        
        return ExpressionStmt(expr)
    
    def _parse_block(self) -> List[Statement]:
        """Парсит блок команд (с отступами)"""
        self._consume(TokenType.INDENT, 
                     self.error_handler.create_friendly_message(
                         'invalid_indentation', line=self.current_token().line))
        
        statements = []
        
        while not self._check(TokenType.DEDENT) and not self._is_at_end():
            self._skip_newlines()
            
            if self._check(TokenType.DEDENT):
                break
            
            stmt = self._parse_statement()
            if stmt:
                statements.append(stmt)
        
        self._consume(TokenType.DEDENT, "Ожидалось уменьшение отступа")
        
        return statements
    
    def _parse_expression(self) -> Expression:
        """Парсит выражение (наивысший приоритет)"""
        return self._parse_or()
    
    def _parse_or(self) -> Expression:
        """Парсит логическое ИЛИ"""
        expr = self._parse_and()
        
        while self._match(TokenType.OR):
            operator = 'or'
            right = self._parse_and()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_and(self) -> Expression:
        """Парсит логическое И"""
        expr = self._parse_not()
        
        while self._match(TokenType.AND):
            operator = 'and'
            right = self._parse_not()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_not(self) -> Expression:
        """Парсит логическое НЕ"""
        if self._match(TokenType.NOT):
            operator = 'not'
            expr = self._parse_not()
            return UnaryOpExpr(operator, expr)
        
        return self._parse_equality()
    
    def _parse_equality(self) -> Expression:
        """Парсит операции сравнения на равенство"""
        expr = self._parse_comparison()
        
        while self._match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            operator = self.tokens[self.position - 1].value
            right = self._parse_comparison()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_comparison(self) -> Expression:
        """Парсит операции сравнения"""
        expr = self._parse_addition()
        
        while self._match(TokenType.GREATER_THAN, TokenType.GREATER_EQUAL,
                          TokenType.LESS_THAN, TokenType.LESS_EQUAL):
            operator = self.tokens[self.position - 1].value
            right = self._parse_addition()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_addition(self) -> Expression:
        """Парсит сложение и вычитание"""
        expr = self._parse_multiplication()
        
        while self._match(TokenType.PLUS, TokenType.MINUS):
            operator = self.tokens[self.position - 1].value
            right = self._parse_multiplication()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_multiplication(self) -> Expression:
        """Парсит умножение, деление и остаток"""
        expr = self._parse_power()
        
        while self._match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            operator = self.tokens[self.position - 1].value
            right = self._parse_power()
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_power(self) -> Expression:
        """Парсит возведение в степень"""
        expr = self._parse_unary()
        
        if self._match(TokenType.POWER):
            operator = '**'
            right = self._parse_power()  # Правоассоциативность
            expr = BinaryOpExpr(expr, operator, right)
        
        return expr
    
    def _parse_unary(self) -> Expression:
        """Парсит унарные операции"""
        if self._match(TokenType.MINUS, TokenType.PLUS):
            operator = self.tokens[self.position - 1].value
            expr = self._parse_unary()
            return UnaryOpExpr(operator, expr)
        
        return self._parse_postfix()
    
    def _parse_postfix(self) -> Expression:
        """Парсит постфиксные операции (вызовы, индексирование, атрибуты)"""
        expr = self._parse_primary()
        
        while True:
            if self._match(TokenType.LEFT_PAREN):
                # Вызов функции
                arguments = []
                if not self._check(TokenType.RIGHT_PAREN):
                    arguments.append(self._parse_expression())
                    while self._match(TokenType.COMMA):
                        arguments.append(self._parse_expression())
                
                self._consume(TokenType.RIGHT_PAREN,
                             self.error_handler.create_friendly_message(
                                 'missing_paren', line=self.current_token().line))
                expr = CallExpr(expr, arguments)
            
            elif self._match(TokenType.LEFT_BRACKET):
                # Индексирование
                index = self._parse_expression()
                self._consume(TokenType.RIGHT_BRACKET,
                             self.error_handler.create_friendly_message(
                                 'missing_bracket', line=self.current_token().line))
                expr = IndexExpr(expr, index)
            
            elif self._match(TokenType.DOT):
                # Обращение к атрибуту
                name = self._consume(TokenType.IDENTIFIER,
                                   "Ожидалось имя атрибута после '.'")
                expr = AttributeExpr(expr, name.value)
            
            else:
                break
        
        return expr
    
    def _parse_primary(self) -> Expression:
        """Парсит первичные выражения"""
        # Литералы
        if self._match(TokenType.INTEGER, TokenType.FLOAT, TokenType.STRING, TokenType.BOOLEAN):
            return LiteralExpr(self.tokens[self.position - 1].value)
        
        if self._match(TokenType.NONE):
            return LiteralExpr(None)
        
        # Идентификаторы
        if self._match(TokenType.IDENTIFIER):
            return IdentifierExpr(self.tokens[self.position - 1].value)
        
        # Группировка выражений
        if self._match(TokenType.LEFT_PAREN):
            expr = self._parse_expression()
            self._consume(TokenType.RIGHT_PAREN,
                         self.error_handler.create_friendly_message(
                             'missing_paren', line=self.current_token().line))
            return expr
        
        # Списки
        if self._match(TokenType.LEFT_BRACKET):
            elements = []
            if not self._check(TokenType.RIGHT_BRACKET):
                elements.append(self._parse_expression())
                while self._match(TokenType.COMMA):
                    elements.append(self._parse_expression())
            
            self._consume(TokenType.RIGHT_BRACKET,
                         self.error_handler.create_friendly_message(
                             'missing_bracket', line=self.current_token().line))
            return ListExpr(elements)
        
        # Словари
        if self._match(TokenType.LEFT_BRACE):
            pairs = []
            if not self._check(TokenType.RIGHT_BRACE):
                key = self._parse_expression()
                self._consume(TokenType.COLON, "Ожидалось ':' после ключа словаря")
                value = self._parse_expression()
                pairs.append((key, value))
                
                while self._match(TokenType.COMMA):
                    key = self._parse_expression()
                    self._consume(TokenType.COLON, "Ожидалось ':' после ключа словаря")
                    value = self._parse_expression()
                    pairs.append((key, value))
            
            self._consume(TokenType.RIGHT_BRACE,
                         self.error_handler.create_friendly_message(
                             'missing_brace', line=self.current_token().line))
            return DictExpr(pairs)
        
        # Неожиданный токен
        current = self.current_token()
        raise ParserError(
            self.error_handler.create_friendly_message(
                'unexpected_token',
                token=str(current.value),
                line=current.line
            ),
            current.line,
            current.column
        )
