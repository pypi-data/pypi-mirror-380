"""
Узлы абстрактного синтаксического дерева (AST) для PyLite
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union
from dataclasses import dataclass


class ASTNode(ABC):
    """Базовый класс для всех узлов AST"""
    pass


class Statement(ASTNode):
    """Базовый класс для всех выражений-команд"""
    pass


class Expression(ASTNode):
    """Базовый класс для всех выражений"""
    pass


# === ВЫРАЖЕНИЯ ===

@dataclass
class LiteralExpr(Expression):
    """Литеральное значение (число, строка, булево, None)"""
    value: Any
    
    def __repr__(self):
        return f"Literal({self.value})"


@dataclass
class IdentifierExpr(Expression):
    """Идентификатор (имя переменной)"""
    name: str
    
    def __repr__(self):
        return f"Identifier({self.name})"


@dataclass
class BinaryOpExpr(Expression):
    """Бинарная операция (a + b, a == b, и т.д.)"""
    left: Expression
    operator: str
    right: Expression
    
    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


@dataclass
class UnaryOpExpr(Expression):
    """Унарная операция (-x, not x)"""
    operator: str
    operand: Expression
    
    def __repr__(self):
        return f"UnaryOp({self.operator} {self.operand})"


@dataclass
class CallExpr(Expression):
    """Вызов функции"""
    function: Expression
    arguments: List[Expression]
    
    def __repr__(self):
        return f"Call({self.function}({', '.join(map(str, self.arguments))}))"


@dataclass
class ListExpr(Expression):
    """Литерал списка [1, 2, 3]"""
    elements: List[Expression]
    
    def __repr__(self):
        return f"List([{', '.join(map(str, self.elements))}])"


@dataclass
class DictExpr(Expression):
    """Литерал словаря {key: value}"""
    pairs: List[tuple[Expression, Expression]]
    
    def __repr__(self):
        pairs_str = ', '.join(f"{k}: {v}" for k, v in self.pairs)
        return f"Dict({{{pairs_str}}})"


@dataclass
class IndexExpr(Expression):
    """Индексирование obj[index]"""
    object: Expression
    index: Expression
    
    def __repr__(self):
        return f"Index({self.object}[{self.index}])"


@dataclass
class AttributeExpr(Expression):
    """Обращение к атрибуту obj.attr"""
    object: Expression
    attribute: str
    
    def __repr__(self):
        return f"Attribute({self.object}.{self.attribute})"


# === ВЫРАЖЕНИЯ-КОМАНДЫ ===

@dataclass
class ExpressionStmt(Statement):
    """Выражение как команда (например, вызов функции)"""
    expression: Expression
    
    def __repr__(self):
        return f"ExprStmt({self.expression})"


@dataclass
class AssignmentStmt(Statement):
    """Присваивание переменной или атрибута"""
    target: Union[str, AttributeExpr]  # Поддерживаем как простые переменные, так и атрибуты
    value: Expression
    
    def __repr__(self):
        return f"Assignment({self.target} = {self.value})"


@dataclass
class IfStmt(Statement):
    """Условное выражение if/elif/else"""
    condition: Expression
    then_body: List[Statement]
    elif_parts: List[tuple[Expression, List[Statement]]]  # (condition, body)
    else_body: Optional[List[Statement]]
    
    def __repr__(self):
        return f"If({self.condition})"


@dataclass
class WhileStmt(Statement):
    """Цикл while"""
    condition: Expression
    body: List[Statement]
    
    def __repr__(self):
        return f"While({self.condition})"


@dataclass
class ForStmt(Statement):
    """Цикл for"""
    target: str
    iterable: Expression
    body: List[Statement]
    
    def __repr__(self):
        return f"For({self.target} in {self.iterable})"


@dataclass
class FunctionDef(Statement):
    """Определение функции"""
    name: str
    parameters: List[str]
    body: List[Statement]
    
    def __repr__(self):
        params = ', '.join(self.parameters)
        return f"FunctionDef({self.name}({params}))"


@dataclass
class ClassDef(Statement):
    """Определение класса"""
    name: str
    superclass: Optional[str]
    body: List[Statement]
    
    def __repr__(self):
        super_str = f"({self.superclass})" if self.superclass else ""
        return f"ClassDef({self.name}{super_str})"


@dataclass
class ReturnStmt(Statement):
    """Команда return"""
    value: Optional[Expression]
    
    def __repr__(self):
        return f"Return({self.value})"


@dataclass
class ImportStmt(Statement):
    """Команда import"""
    module: str
    alias: Optional[str] = None
    
    def __repr__(self):
        alias_str = f" as {self.alias}" if self.alias else ""
        return f"Import({self.module}{alias_str})"


@dataclass
class FromImportStmt(Statement):
    """Команда from ... import ..."""
    module: str
    names: List[str]
    
    def __repr__(self):
        names_str = ', '.join(self.names)
        return f"FromImport(from {self.module} import {names_str})"


@dataclass
class Program(ASTNode):
    """Корневой узел программы"""
    statements: List[Statement]
    
    def __repr__(self):
        return f"Program({len(self.statements)} statements)"
