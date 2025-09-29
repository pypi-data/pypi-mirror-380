"""
Интерпретатор PyLite
"""

from typing import Any, Dict, List, Optional
from .ast_nodes import *
from .environment import Environment, CallableFunction, ReturnValue, PyLiteClass, PyLiteInstance, BoundMethod
from .builtins import create_builtins, create_modules
from .error_handler import RuntimeError as PyLiteRuntimeError, ValidationError, ErrorHandler


class Interpreter:
    """Интерпретатор PyLite"""
    
    def __init__(self, mode: str = 'basic'):
        self.mode = mode  # 'basic' или 'extended'
        self.globals = Environment()
        self.environment = self.globals
        self.modules = create_modules()
        self.error_handler = ErrorHandler()
        
        # Инициализируем встроенные функции
        builtins = create_builtins()
        for name, func in builtins.items():
            self.globals.define(name, func)
    
    def interpret(self, program: Program) -> Any:
        """Выполняет программу"""
        try:
            # Валидация ограничений PyLite
            if self.mode == 'basic':
                self._validate_program(program)
            
            result = None
            for statement in program.statements:
                result = self.execute_statement(statement)
                
                # Обрабатываем return на верхнем уровне
                if isinstance(result, ReturnValue):
                    return result.value
            
            return result
            
        except Exception as e:
            if isinstance(e, (PyLiteRuntimeError, ValidationError)):
                raise e
            else:
                raise PyLiteRuntimeError(f"Неожиданная ошибка: {str(e)}")
    
    def execute_statement(self, stmt: Statement) -> Any:
        """Выполняет одну команду"""
        if isinstance(stmt, ExpressionStmt):
            return self.evaluate_expression(stmt.expression)
        
        elif isinstance(stmt, AssignmentStmt):
            value = self.evaluate_expression(stmt.value)
            self.environment.assign(stmt.target, value)
            return value
        
        elif isinstance(stmt, IfStmt):
            return self._execute_if(stmt)
        
        elif isinstance(stmt, WhileStmt):
            return self._execute_while(stmt)
        
        elif isinstance(stmt, ForStmt):
            return self._execute_for(stmt)
        
        elif isinstance(stmt, FunctionDef):
            return self._execute_function_def(stmt)
        
        elif isinstance(stmt, ClassDef):
            return self._execute_class_def(stmt)
        
        elif isinstance(stmt, ReturnStmt):
            value = None
            if stmt.value is not None:
                value = self.evaluate_expression(stmt.value)
            return ReturnValue(value)
        
        elif isinstance(stmt, ImportStmt):
            return self._execute_import(stmt)
        
        elif isinstance(stmt, FromImportStmt):
            return self._execute_from_import(stmt)
        
        else:
            raise PyLiteRuntimeError(f"Неизвестный тип команды: {type(stmt)}")
    
    def evaluate_expression(self, expr: Expression) -> Any:
        """Вычисляет выражение"""
        if isinstance(expr, LiteralExpr):
            return expr.value
        
        elif isinstance(expr, IdentifierExpr):
            return self.environment.get(expr.name)
        
        elif isinstance(expr, BinaryOpExpr):
            return self._evaluate_binary_op(expr)
        
        elif isinstance(expr, UnaryOpExpr):
            return self._evaluate_unary_op(expr)
        
        elif isinstance(expr, CallExpr):
            return self._evaluate_call(expr)
        
        elif isinstance(expr, ListExpr):
            return [self.evaluate_expression(elem) for elem in expr.elements]
        
        elif isinstance(expr, DictExpr):
            result = {}
            for key_expr, value_expr in expr.pairs:
                key = self.evaluate_expression(key_expr)
                value = self.evaluate_expression(value_expr)
                result[key] = value
            return result
        
        elif isinstance(expr, IndexExpr):
            return self._evaluate_index(expr)
        
        elif isinstance(expr, AttributeExpr):
            return self._evaluate_attribute(expr)
        
        else:
            raise PyLiteRuntimeError(f"Неизвестный тип выражения: {type(expr)}")
    
    def _execute_if(self, stmt: IfStmt) -> Any:
        """Выполняет условное выражение"""
        condition_value = self.evaluate_expression(stmt.condition)
        
        if self._is_truthy(condition_value):
            return self._execute_block(stmt.then_body)
        
        # Проверяем elif части
        for elif_condition, elif_body in stmt.elif_parts:
            elif_value = self.evaluate_expression(elif_condition)
            if self._is_truthy(elif_value):
                return self._execute_block(elif_body)
        
        # Выполняем else, если есть
        if stmt.else_body is not None:
            return self._execute_block(stmt.else_body)
        
        return None
    
    def _execute_while(self, stmt: WhileStmt) -> Any:
        """Выполняет цикл while"""
        result = None
        
        while True:
            condition_value = self.evaluate_expression(stmt.condition)
            if not self._is_truthy(condition_value):
                break
            
            result = self._execute_block(stmt.body)
            
            # Обрабатываем return
            if isinstance(result, ReturnValue):
                return result
        
        return result
    
    def _execute_for(self, stmt: ForStmt) -> Any:
        """Выполняет цикл for"""
        iterable_value = self.evaluate_expression(stmt.iterable)
        
        if not isinstance(iterable_value, list):
            raise PyLiteRuntimeError(
                f"Нельзя итерировать по объекту типа {type(iterable_value).__name__}"
            )
        
        result = None
        
        for item in iterable_value:
            self.environment.assign(stmt.target, item)
            result = self._execute_block(stmt.body)
            
            # Обрабатываем return
            if isinstance(result, ReturnValue):
                return result
        
        return result
    
    def _execute_function_def(self, stmt: FunctionDef) -> Any:
        """Выполняет определение функции"""
        function = CallableFunction(stmt.name, stmt.parameters, stmt.body, self.environment)
        self.environment.define(stmt.name, function)
        return function
    
    def _execute_class_def(self, stmt: ClassDef) -> Any:
        """Выполняет определение класса"""
        superclass = None
        if stmt.superclass is not None:
            superclass_value = self.environment.get(stmt.superclass)
            if not isinstance(superclass_value, PyLiteClass):
                raise PyLiteRuntimeError(
                    f"Родительский класс должен быть классом, а не {type(superclass_value).__name__}"
                )
            superclass = superclass_value
        
        # Создаем окружение для методов класса
        class_env = Environment(self.environment)
        previous = self.environment
        self.environment = class_env
        
        # Выполняем тело класса
        methods = {}
        try:
            for statement in stmt.body:
                if isinstance(statement, FunctionDef):
                    method = CallableFunction(statement.name, statement.parameters, 
                                            statement.body, self.environment)
                    methods[statement.name] = method
                else:
                    # Выполняем другие команды в теле класса
                    self.execute_statement(statement)
        finally:
            self.environment = previous
        
        klass = PyLiteClass(stmt.name, superclass, methods)
        self.environment.define(stmt.name, klass)
        return klass
    
    def _execute_import(self, stmt: ImportStmt) -> Any:
        """Выполняет команду import"""
        if stmt.module not in self.modules:
            raise PyLiteRuntimeError(
                f"Модуль '{stmt.module}' не найден"
            )
        
        module_dict = self.modules[stmt.module]
        
        # Создаем объект модуля
        module_obj = type('Module', (), module_dict)()
        
        name = stmt.alias if stmt.alias else stmt.module
        self.environment.define(name, module_obj)
        
        return module_obj
    
    def _execute_from_import(self, stmt: FromImportStmt) -> Any:
        """Выполняет команду from ... import ..."""
        if stmt.module not in self.modules:
            raise PyLiteRuntimeError(
                f"Модуль '{stmt.module}' не найден"
            )
        
        module_dict = self.modules[stmt.module]
        
        for name in stmt.names:
            if name not in module_dict:
                raise PyLiteRuntimeError(
                    f"В модуле '{stmt.module}' нет '{name}'"
                )
            self.environment.define(name, module_dict[name])
        
        return None
    
    def _execute_block(self, statements: List[Statement]) -> Any:
        """Выполняет блок команд"""
        result = None
        
        for statement in statements:
            result = self.execute_statement(statement)
            
            # Обрабатываем return
            if isinstance(result, ReturnValue):
                return result
        
        return result
    
    def _evaluate_binary_op(self, expr: BinaryOpExpr) -> Any:
        """Вычисляет бинарную операцию"""
        left = self.evaluate_expression(expr.left)
        
        # Короткое вычисление для логических операторов
        if expr.operator == 'and':
            if not self._is_truthy(left):
                return left
            return self.evaluate_expression(expr.right)
        
        if expr.operator == 'or':
            if self._is_truthy(left):
                return left
            return self.evaluate_expression(expr.right)
        
        right = self.evaluate_expression(expr.right)
        
        # Арифметические операции
        if expr.operator == '+':
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            elif isinstance(left, list) and isinstance(right, list):
                return left + right
            elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='+',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        elif expr.operator == '-':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left - right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='-',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        elif expr.operator == '*':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left * right
            elif isinstance(left, str) and isinstance(right, int):
                return left * right
            elif isinstance(left, int) and isinstance(right, str):
                return left * right
            elif isinstance(left, list) and isinstance(right, int):
                return left * right
            elif isinstance(left, int) and isinstance(right, list):
                return left * right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='*',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        elif expr.operator == '/':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise PyLiteRuntimeError(
                        self.error_handler.create_friendly_message('division_by_zero')
                    )
                return left / right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='/',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        elif expr.operator == '%':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise PyLiteRuntimeError(
                        self.error_handler.create_friendly_message('division_by_zero')
                    )
                return left % right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='%',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        elif expr.operator == '**':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left ** right
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'type_error',
                        operation='**',
                        type1=type(left).__name__,
                        type2=type(right).__name__
                    )
                )
        
        # Операции сравнения
        elif expr.operator == '==':
            return left == right
        elif expr.operator == '!=':
            return left != right
        elif expr.operator == '<':
            return left < right
        elif expr.operator == '>':
            return left > right
        elif expr.operator == '<=':
            return left <= right
        elif expr.operator == '>=':
            return left >= right
        
        else:
            raise PyLiteRuntimeError(f"Неизвестная операция: {expr.operator}")
    
    def _evaluate_unary_op(self, expr: UnaryOpExpr) -> Any:
        """Вычисляет унарную операцию"""
        operand = self.evaluate_expression(expr.operand)
        
        if expr.operator == '-':
            if isinstance(operand, (int, float)):
                return -operand
            else:
                raise PyLiteRuntimeError(
                    f"Нельзя применить унарный минус к {type(operand).__name__}"
                )
        elif expr.operator == '+':
            if isinstance(operand, (int, float)):
                return +operand
            else:
                raise PyLiteRuntimeError(
                    f"Нельзя применить унарный плюс к {type(operand).__name__}"
                )
        elif expr.operator == 'not':
            return not self._is_truthy(operand)
        else:
            raise PyLiteRuntimeError(f"Неизвестная унарная операция: {expr.operator}")
    
    def _evaluate_call(self, expr: CallExpr) -> Any:
        """Вычисляет вызов функции"""
        callee = self.evaluate_expression(expr.function)
        arguments = [self.evaluate_expression(arg) for arg in expr.arguments]
        
        if hasattr(callee, 'call'):
            return callee.call(self, arguments)
        else:
            raise PyLiteRuntimeError(
                f"'{callee}' не является функцией"
            )
    
    def _evaluate_index(self, expr: IndexExpr) -> Any:
        """Вычисляет индексирование"""
        obj = self.evaluate_expression(expr.object)
        index = self.evaluate_expression(expr.index)
        
        try:
            if isinstance(obj, list):
                if not isinstance(index, int):
                    raise PyLiteRuntimeError(
                        "Индекс списка должен быть числом"
                    )
                return obj[index]
            
            elif isinstance(obj, dict):
                return obj[index]
            
            elif isinstance(obj, str):
                if not isinstance(index, int):
                    raise PyLiteRuntimeError(
                        "Индекс строки должен быть числом"
                    )
                return obj[index]
            
            else:
                raise PyLiteRuntimeError(
                    f"Нельзя индексировать объект типа {type(obj).__name__}"
                )
                
        except IndexError:
            raise PyLiteRuntimeError(
                self.error_handler.create_friendly_message(
                    'index_error',
                    index=index,
                    length=len(obj)
                )
            )
        except KeyError:
            raise PyLiteRuntimeError(
                self.error_handler.create_friendly_message(
                    'key_error',
                    key=index
                )
            )
    
    def _evaluate_attribute(self, expr: AttributeExpr) -> Any:
        """Вычисляет обращение к атрибуту"""
        obj = self.evaluate_expression(expr.object)
        
        if isinstance(obj, PyLiteInstance):
            return obj.get(expr.attribute)
        else:
            # Для встроенных типов проверяем некоторые методы
            if isinstance(obj, list) and expr.attribute == 'append':
                def append_method(item):
                    obj.append(item)
                    return None
                from .builtins import BuiltinFunction
                return BuiltinFunction('append', append_method, 1, 1)
            
            elif hasattr(obj, expr.attribute):
                return getattr(obj, expr.attribute)
            else:
                raise PyLiteRuntimeError(
                    self.error_handler.create_friendly_message(
                        'attribute_error',
                        type=type(obj).__name__,
                        attr=expr.attribute
                    )
                )
    
    def _is_truthy(self, value: Any) -> bool:
        """Определяет истинность значения"""
        if value is None or value is False:
            return False
        elif value is True:
            return True
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return len(value) > 0
        elif isinstance(value, (list, dict)):
            return len(value) > 0
        else:
            return True
    
    def _validate_program(self, program: Program):
        """Валидирует программу согласно ограничениям PyLite"""
        # Проверяем количество строк
        if len(program.statements) > 500:
            raise ValidationError(
                self.error_handler.create_friendly_message(
                    'too_many_lines'
                ),
                0, 0
            )
        
        # TODO: Добавить другие проверки (вложенность, длина строк и т.д.)
