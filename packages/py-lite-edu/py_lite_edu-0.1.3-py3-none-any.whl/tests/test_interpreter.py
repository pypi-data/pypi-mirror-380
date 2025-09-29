"""
Тесты для интерпретатора
"""

import unittest
import io
import sys
from contextlib import redirect_stdout
from pylite.lexer import Lexer
from pylite.parser import Parser
from pylite.interpreter import Interpreter
from pylite.error_handler import RuntimeError as PyLiteRuntimeError


class TestInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = Interpreter()
    
    def _execute_code(self, code: str):
        """Вспомогательная функция для выполнения кода"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        program = parser.parse()
        return self.interpreter.interpret(program)
    
    def _capture_output(self, code: str) -> str:
        """Выполняет код и захватывает вывод print"""
        output = io.StringIO()
        with redirect_stdout(output):
            self._execute_code(code)
        return output.getvalue().strip()
    
    def test_simple_arithmetic(self):
        """Тест простой арифметики"""
        result = self._execute_code("result = 2 + 3 * 4")
        # Проверяем, что переменная установлена правильно
        self.assertEqual(self.interpreter.environment.get("result"), 14)
    
    def test_string_operations(self):
        """Тест операций со строками"""
        result = self._execute_code('greeting = "Hello, " + "World!"')
        self.assertEqual(self.interpreter.environment.get("greeting"), "Hello, World!")
    
    def test_print_function(self):
        """Тест встроенной функции print"""
        output = self._capture_output('print("Hello, PyLite!")')
        self.assertEqual(output, "Hello, PyLite!")
    
    def test_function_definition_and_call(self):
        """Тест определения и вызова функции"""
        code = """
def add(a, b):
    return a + b

result = add(5, 3)
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("result"), 8)
    
    def test_if_statement(self):
        """Тест условных выражений"""
        code = """
x = 10
if x > 5:
    result = "big"
else:
    result = "small"
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("result"), "big")
    
    def test_for_loop(self):
        """Тест цикла for"""
        code = """
total = 0
for i in range(5):
    total = total + i
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("total"), 10)  # 0+1+2+3+4
    
    def test_while_loop(self):
        """Тест цикла while"""
        code = """
count = 0
while count < 3:
    count = count + 1
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("count"), 3)
    
    def test_list_operations(self):
        """Тест операций со списками"""
        code = """
numbers = [1, 2, 3]
first = numbers[0]
length = len(numbers)
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("first"), 1)
        self.assertEqual(self.interpreter.environment.get("length"), 3)
    
    def test_dict_operations(self):
        """Тест операций со словарями"""
        code = """
person = {"name": "Alice", "age": 25}
name = person["name"]
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("name"), "Alice")
    
    def test_builtin_functions(self):
        """Тест встроенных функций"""
        code = """
num_str = str(42)
num_int = int("10")
num_float = float("3.14")
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("num_str"), "42")
        self.assertEqual(self.interpreter.environment.get("num_int"), 10)
        self.assertEqual(self.interpreter.environment.get("num_float"), 3.14)
    
    def test_math_module(self):
        """Тест модуля math"""
        code = """
import math
result = math.sqrt(16)
pi_value = math.pi
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("result"), 4.0)
        self.assertAlmostEqual(self.interpreter.environment.get("pi_value"), 3.14159, places=4)
    
    def test_class_definition_and_usage(self):
        """Тест определения и использования класса"""
        code = """
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return "Hello, I'm " + self.name

p = Person("Alice")
greeting = p.greet()
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("greeting"), "Hello, I'm Alice")
    
    def test_error_division_by_zero(self):
        """Тест ошибки деления на ноль"""
        with self.assertRaises(PyLiteRuntimeError) as context:
            self._execute_code("result = 10 / 0")
        
        self.assertIn("делить на ноль", str(context.exception))
    
    def test_error_undefined_variable(self):
        """Тест ошибки неопределённой переменной"""
        with self.assertRaises(PyLiteRuntimeError) as context:
            self._execute_code("print(undefined_var)")
        
        self.assertIn("не определена", str(context.exception))
    
    def test_error_index_out_of_range(self):
        """Тест ошибки выхода за границы списка"""
        with self.assertRaises(PyLiteRuntimeError) as context:
            self._execute_code("numbers = [1, 2, 3]; print(numbers[10])")
        
        self.assertIn("слишком большой", str(context.exception))
    
    def test_logical_operations(self):
        """Тест логических операций"""
        code = """
result1 = True and False
result2 = True or False  
result3 = not True
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("result1"), False)
        self.assertEqual(self.interpreter.environment.get("result2"), True)
        self.assertEqual(self.interpreter.environment.get("result3"), False)
    
    def test_nested_function_calls(self):
        """Тест вложенных вызовов функций"""
        code = """
def double(x):
    return x * 2

def add_one(x):
    return x + 1

result = double(add_one(5))
"""
        self._execute_code(code)
        self.assertEqual(self.interpreter.environment.get("result"), 12)  # (5+1)*2


if __name__ == '__main__':
    unittest.main()
