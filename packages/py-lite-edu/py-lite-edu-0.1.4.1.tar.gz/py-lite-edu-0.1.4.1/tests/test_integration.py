"""
Интеграционные тесты для PyLite
"""

import unittest
import tempfile
import os
from pylite.cli import PyLiteRunner


class TestIntegration(unittest.TestCase):
    """Интеграционные тесты полной системы"""
    
    def setUp(self):
        self.runner = PyLiteRunner()
    
    def _create_temp_file(self, content: str) -> str:
        """Создает временный .pyl файл с содержимым"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pyl', delete=False, encoding='utf-8') as f:
            f.write(content)
            return f.name
    
    def _cleanup_temp_file(self, filename: str):
        """Удаляет временный файл"""
        if os.path.exists(filename):
            os.unlink(filename)
    
    def test_simple_program(self):
        """Тест простой программы"""
        program = """
def greet(name):
    print("Привет, " + name + "!")

greet("Мир")
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)  # Успешное выполнение
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_math_calculations(self):
        """Тест математических вычислений"""
        program = """
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

area = calculate_circle_area(5)
print("Площадь круга:", area)
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_list_processing(self):
        """Тест обработки списков"""
        program = """
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total = total + num

print("Сумма:", total)
print("Среднее:", total / len(numbers))
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_class_example(self):
        """Тест использования классов"""
        program = """
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def study(self):
        print(self.name + " изучает программирование!")
    
    def get_info(self):
        return self.name + " учится в " + str(self.grade) + " классе"

student = Student("Анна", 7)
student.study()
print(student.get_info())
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_game_example(self):
        """Тест простой игры - угадай число"""
        program = """
import random

def guess_game():
    secret = random.randint(1, 10)
    print("Я загадал число от 1 до 10!")
    
    # Для тестирования просто угадаем правильно с первого раза
    guess = secret
    
    if guess == secret:
        print("Поздравляю! Ты угадал!")
    else:
        print("Не угадал. Число было", secret)

guess_game()
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_error_handling(self):
        """Тест обработки ошибок"""
        program = """
# Эта программа содержит ошибку
print(undefined_variable)
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 1)  # Ошибка выполнения
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_syntax_error_handling(self):
        """Тест обработки синтаксических ошибок"""
        program = """
# Эта программа содержит синтаксическую ошибку
if True
    print("Забыли двоеточие")
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 1)  # Ошибка выполнения
        finally:
            self._cleanup_temp_file(temp_file)
    
    def test_file_not_found(self):
        """Тест обработки отсутствующего файла"""
        result = self.runner.run_file("nonexistent_file.pyl")
        self.assertEqual(result, 1)  # Ошибка - файл не найден
    
    def test_comprehensive_example(self):
        """Тест комплексного примера с различными конструкциями"""
        program = """
# Комплексный пример использования PyLite

import math
import random

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history = self.history + [str(a) + " + " + str(b) + " = " + str(result)]
        return result
    
    def sqrt(self, x):
        if x < 0:
            print("Ошибка: нельзя извлекать корень из отрицательного числа")
            return None
        result = math.sqrt(x)
        self.history = self.history + ["sqrt(" + str(x) + ") = " + str(result)]
        return result
    
    def show_history(self):
        print("История вычислений:")
        for operation in self.history:
            print("  " + operation)

def main():
    calc = Calculator()
    
    # Выполняем несколько операций
    sum_result = calc.add(10, 5)
    sqrt_result = calc.sqrt(16)
    
    print("Результаты:")
    print("Сумма:", sum_result)
    print("Корень:", sqrt_result)
    
    calc.show_history()
    
    # Генерируем случайные числа
    random_numbers = []
    for i in range(5):
        num = random.randint(1, 100)
        random_numbers = random_numbers + [num]
    
    print("Случайные числа:", random_numbers)
    
    # Находим максимум и минимум
    max_num = max(random_numbers)
    min_num = min(random_numbers)
    
    print("Максимум:", max_num)
    print("Минимум:", min_num)

main()
"""
        
        temp_file = self._create_temp_file(program)
        try:
            result = self.runner.run_file(temp_file)
            self.assertEqual(result, 0)
        finally:
            self._cleanup_temp_file(temp_file)


if __name__ == '__main__':
    unittest.main()
