"""
Встроенные функции и модули PyLite
"""

import sys
import math
import random
import time
from typing import Any, List, Dict, Callable
from .error_handler import RuntimeError as PyLiteRuntimeError, ErrorHandler
from .types import BuiltinFunction
from .modules.turtle_module import create_turtle_module
from .modules.sound_module import create_sound_module


def create_builtins() -> Dict[str, Any]:
    """Создает словарь встроенных функций и переменных"""
    error_handler = ErrorHandler()
    
    def pylite_print(*args):
        """Встроенная функция print"""
        output = ' '.join(str(arg) for arg in args)
        print(output)
        return None
    
    def pylite_input(prompt=""):
        """Встроенная функция input"""
        return input(str(prompt))
    
    def pylite_len(obj):
        """Встроенная функция len"""
        if isinstance(obj, (list, dict, str)):
            return len(obj)
        else:
            raise PyLiteRuntimeError(
                f"Объект типа {type(obj).__name__} не имеет длины"
            )
    
    def pylite_type(obj):
        """Встроенная функция type"""
        if obj is None:
            return "NoneType"
        elif isinstance(obj, bool):
            return "bool"
        elif isinstance(obj, int):
            return "int"
        elif isinstance(obj, float):
            return "float"
        elif isinstance(obj, str):
            return "str"
        elif isinstance(obj, list):
            return "list"
        elif isinstance(obj, dict):
            return "dict"
        else:
            return type(obj).__name__
    
    def pylite_str(obj):
        """Встроенная функция str"""
        return str(obj)
    
    def pylite_int(obj):
        """Встроенная функция int"""
        try:
            if isinstance(obj, str):
                return int(obj)
            elif isinstance(obj, float):
                return int(obj)
            elif isinstance(obj, bool):
                return int(obj)
            else:
                return int(obj)
        except (ValueError, TypeError):
            raise PyLiteRuntimeError(
                f"Нельзя превратить {type(obj).__name__} в число"
            )
    
    def pylite_float(obj):
        """Встроенная функция float"""
        try:
            return float(obj)
        except (ValueError, TypeError):
            raise PyLiteRuntimeError(
                f"Нельзя превратить {type(obj).__name__} в дробное число"
            )
    
    def pylite_bool(obj):
        """Встроенная функция bool"""
        if obj is None or obj is False:
            return False
        elif obj is True:
            return True
        elif isinstance(obj, (int, float)):
            return obj != 0
        elif isinstance(obj, str):
            return len(obj) > 0
        elif isinstance(obj, (list, dict)):
            return len(obj) > 0
        else:
            return True
    
    def pylite_range(*args):
        """Встроенная функция range"""
        if len(args) == 1:
            return list(range(args[0]))
        elif len(args) == 2:
            return list(range(args[0], args[1]))
        elif len(args) == 3:
            return list(range(args[0], args[1], args[2]))
        else:
            raise PyLiteRuntimeError(
                "Функция range принимает от 1 до 3 аргументов"
            )
    
    def pylite_abs(x):
        """Встроенная функция abs"""
        if isinstance(x, (int, float)):
            return abs(x)
        else:
            raise PyLiteRuntimeError(
                "abs() можно применять только к числам"
            )
    
    def pylite_min(*args):
        """Встроенная функция min"""
        if len(args) == 0:
            raise PyLiteRuntimeError("min() нужен хотя бы один аргument")
        
        if len(args) == 1 and isinstance(args[0], list):
            if len(args[0]) == 0:
                raise PyLiteRuntimeError("min() не может работать с пустым списком")
            return min(args[0])
        else:
            return min(args)
    
    def pylite_max(*args):
        """Встроенная функция max"""
        if len(args) == 0:
            raise PyLiteRuntimeError("max() нужен хотя бы один аргумент")
        
        if len(args) == 1 and isinstance(args[0], list):
            if len(args[0]) == 0:
                raise PyLiteRuntimeError("max() не может работать с пустым списком")
            return max(args[0])
        else:
            return max(args)
    
    def pylite_sum(iterable, start=0):
        """Встроенная функция sum"""
        if isinstance(iterable, list):
            return sum(iterable, start)
        else:
            raise PyLiteRuntimeError("sum() работает только со списками")
    
    # Возвращаем словарь встроенных функций
    return {
        'print': BuiltinFunction('print', pylite_print, 0, 999),
        'input': BuiltinFunction('input', pylite_input, 0, 1),
        'len': BuiltinFunction('len', pylite_len, 1, 1),
        'type': BuiltinFunction('type', pylite_type, 1, 1),
        'str': BuiltinFunction('str', pylite_str, 1, 1),
        'int': BuiltinFunction('int', pylite_int, 1, 1),
        'float': BuiltinFunction('float', pylite_float, 1, 1),
        'bool': BuiltinFunction('bool', pylite_bool, 1, 1),
        'range': BuiltinFunction('range', pylite_range, 1, 3),
        'abs': BuiltinFunction('abs', pylite_abs, 1, 1),
        'min': BuiltinFunction('min', pylite_min, 1, 999),
        'max': BuiltinFunction('max', pylite_max, 1, 999),
        'sum': BuiltinFunction('sum', pylite_sum, 1, 2),
    }


def create_math_module() -> Dict[str, Any]:
    """Создает модуль math"""
    def safe_sqrt(x):
        if x < 0:
            raise PyLiteRuntimeError("Нельзя извлекать корень из отрицательного числа")
        return math.sqrt(x)
    
    def safe_log(x, base=math.e):
        if x <= 0:
            raise PyLiteRuntimeError("Логарифм можно брать только от положительных чисел")
        return math.log(x, base)
    
    return {
        'pi': math.pi,
        'e': math.e,
        'sqrt': BuiltinFunction('sqrt', safe_sqrt, 1, 1),
        'pow': BuiltinFunction('pow', pow, 2, 2),
        'abs': BuiltinFunction('abs', abs, 1, 1),
        'sin': BuiltinFunction('sin', math.sin, 1, 1),
        'cos': BuiltinFunction('cos', math.cos, 1, 1),
        'tan': BuiltinFunction('tan', math.tan, 1, 1),
        'floor': BuiltinFunction('floor', math.floor, 1, 1),
        'ceil': BuiltinFunction('ceil', math.ceil, 1, 1),
        'round': BuiltinFunction('round', round, 1, 2),
        'log': BuiltinFunction('log', safe_log, 1, 2),
    }


def create_random_module() -> Dict[str, Any]:
    """Создает модуль random"""
    return {
        'random': BuiltinFunction('random', random.random, 0, 0),
        'randint': BuiltinFunction('randint', random.randint, 2, 2),
        'choice': BuiltinFunction('choice', random.choice, 1, 1),
        'shuffle': BuiltinFunction('shuffle', lambda lst: random.shuffle(lst) or lst, 1, 1),
    }


def create_time_module() -> Dict[str, Any]:
    """Создает модуль time"""
    return {
        'time': BuiltinFunction('time', time.time, 0, 0),
        'sleep': BuiltinFunction('sleep', time.sleep, 1, 1),
    }


from .modules.turtle_module import create_turtle_module
from .modules.sound_module import create_sound_module

def create_modules() -> Dict[str, Dict[str, Any]]:
    """Создает все доступные модули"""
    return {
        'math': create_math_module(),
        'random': create_random_module(),
        'time': create_time_module(),
        'turtle': create_turtle_module(),
        'sound': create_sound_module(),
    }
