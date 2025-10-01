"""
Токены для лексического анализатора PyLite
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional

class TokenType(Enum):
    # Литералы
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    
    # Идентификаторы
    IDENTIFIER = auto()
    
    # Ключевые слова
    DEF = auto()
    IF = auto()
    ELIF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    IN = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    TRUE = auto()
    FALSE = auto()
    NONE = auto()
    RETURN = auto()
    CLASS = auto()
    IMPORT = auto()
    FROM = auto()
    
    # Операторы
    PLUS = auto()          # +
    MINUS = auto()         # -
    MULTIPLY = auto()      # *
    DIVIDE = auto()        # /
    MODULO = auto()        # %
    POWER = auto()         # **
    
    # Операторы сравнения
    EQUAL = auto()         # ==
    NOT_EQUAL = auto()     # !=
    LESS_THAN = auto()     # <
    GREATER_THAN = auto()  # >
    LESS_EQUAL = auto()    # <=
    GREATER_EQUAL = auto() # >=
    
    # Присваивание
    ASSIGN = auto()        # =
    
    # Разделители
    LEFT_PAREN = auto()    # (
    RIGHT_PAREN = auto()   # )
    LEFT_BRACKET = auto()  # [
    RIGHT_BRACKET = auto() # ]
    LEFT_BRACE = auto()    # {
    RIGHT_BRACE = auto()   # }
    COMMA = auto()         # ,
    COLON = auto()         # :
    DOT = auto()           # .
    SEMICOLON = auto()     # ;
    
    # Специальные
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, {self.line}:{self.column})"

# Ключевые слова
KEYWORDS = {
    'def': TokenType.DEF,
    'if': TokenType.IF,
    'elif': TokenType.ELIF,
    'else': TokenType.ELSE,
    'for': TokenType.FOR,
    'while': TokenType.WHILE,
    'in': TokenType.IN,
    'and': TokenType.AND,
    'or': TokenType.OR,
    'not': TokenType.NOT,
    'True': TokenType.TRUE,
    'False': TokenType.FALSE,
    'None': TokenType.NONE,
    'return': TokenType.RETURN,
    'class': TokenType.CLASS,
    'import': TokenType.IMPORT,
    'from': TokenType.FROM,
}
