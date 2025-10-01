"""
Тесты для синтаксического анализатора
"""

import unittest
from pylite.lexer import Lexer
from pylite.parser import Parser
from pylite.ast_nodes import *
from pylite.error_handler import ParserError


class TestParser(unittest.TestCase):
    
    def _parse_code(self, code: str) -> Program:
        """Вспомогательная функция для парсинга кода"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        return parser.parse()
    
    def test_simple_assignment(self):
        """Тест простого присваивания"""
        program = self._parse_code("x = 42")
        
        self.assertEqual(len(program.statements), 1)
        stmt = program.statements[0]
        
        self.assertIsInstance(stmt, AssignmentStmt)
        self.assertEqual(stmt.target, "x")
        self.assertIsInstance(stmt.value, LiteralExpr)
        self.assertEqual(stmt.value.value, 42)
    
    def test_function_definition(self):
        """Тест определения функции"""
        code = """def greet(name):
    print("Hello, " + name)
"""
        program = self._parse_code(code)
        
        self.assertEqual(len(program.statements), 1)
        func_def = program.statements[0]
        
        self.assertIsInstance(func_def, FunctionDef)
        self.assertEqual(func_def.name, "greet")
        self.assertEqual(func_def.parameters, ["name"])
        self.assertEqual(len(func_def.body), 1)
    
    def test_if_statement(self):
        """Тест условного выражения"""
        code = """if x > 5:
    print("big")
else:
    print("small")
"""
        program = self._parse_code(code)
        
        self.assertEqual(len(program.statements), 1)
        if_stmt = program.statements[0]
        
        self.assertIsInstance(if_stmt, IfStmt)
        self.assertIsInstance(if_stmt.condition, BinaryOpExpr)
        self.assertEqual(len(if_stmt.then_body), 1)
        self.assertIsNotNone(if_stmt.else_body)
        self.assertEqual(len(if_stmt.else_body), 1)
    
    def test_for_loop(self):
        """Тест цикла for"""
        code = """for i in range(5):
    print(i)
"""
        program = self._parse_code(code)
        
        self.assertEqual(len(program.statements), 1)
        for_stmt = program.statements[0]
        
        self.assertIsInstance(for_stmt, ForStmt)
        self.assertEqual(for_stmt.target, "i")
        self.assertIsInstance(for_stmt.iterable, CallExpr)
    
    def test_while_loop(self):
        """Тест цикла while"""
        code = """while x < 10:
    x = x + 1
"""
        program = self._parse_code(code)
        
        self.assertEqual(len(program.statements), 1)
        while_stmt = program.statements[0]
        
        self.assertIsInstance(while_stmt, WhileStmt)
        self.assertIsInstance(while_stmt.condition, BinaryOpExpr)
        self.assertEqual(len(while_stmt.body), 1)
    
    def test_binary_operations(self):
        """Тест бинарных операций"""
        program = self._parse_code("result = a + b * c")
        
        stmt = program.statements[0]
        self.assertIsInstance(stmt, AssignmentStmt)
        
        # Должно быть: a + (b * c) из-за приоритета операторов
        expr = stmt.value
        self.assertIsInstance(expr, BinaryOpExpr)
        self.assertEqual(expr.operator, "+")
        self.assertIsInstance(expr.right, BinaryOpExpr)
        self.assertEqual(expr.right.operator, "*")
    
    def test_function_call(self):
        """Тест вызова функции"""
        program = self._parse_code("print(x, y, z)")
        
        stmt = program.statements[0]
        self.assertIsInstance(stmt, ExpressionStmt)
        
        call_expr = stmt.expression
        self.assertIsInstance(call_expr, CallExpr)
        self.assertIsInstance(call_expr.function, IdentifierExpr)
        self.assertEqual(len(call_expr.arguments), 3)
    
    def test_list_and_dict_literals(self):
        """Тест литералов списков и словарей"""
        program = self._parse_code('numbers = [1, 2, 3]\ndata = {"name": "Alice", "age": 25}')
        
        # Список
        list_stmt = program.statements[0]
        self.assertIsInstance(list_stmt.value, ListExpr)
        self.assertEqual(len(list_stmt.value.elements), 3)
        
        # Словарь
        dict_stmt = program.statements[1]
        self.assertIsInstance(dict_stmt.value, DictExpr)
        self.assertEqual(len(dict_stmt.value.pairs), 2)
    
    def test_error_missing_colon(self):
        """Тест ошибки отсутствующего двоеточия"""
        with self.assertRaises(ParserError):
            self._parse_code("if True\n    print('hello')")
    
    def test_class_definition(self):
        """Тест определения класса"""
        code = """class Person:
    def __init__(self, name):
        self.name = name
"""
        program = self._parse_code(code)
        
        self.assertEqual(len(program.statements), 1)
        class_def = program.statements[0]
        
        self.assertIsInstance(class_def, ClassDef)
        self.assertEqual(class_def.name, "Person")
        self.assertIsNone(class_def.superclass)
        self.assertEqual(len(class_def.body), 1)


if __name__ == '__main__':
    unittest.main()
