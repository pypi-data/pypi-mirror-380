"""
Окружение для хранения переменных и функций
"""

from typing import Any, Dict, Optional, List
from .error_handler import RuntimeError as PyLiteRuntimeError, ErrorHandler


class Environment:
    """Класс для хранения переменных в области видимости"""
    
    def __init__(self, parent: Optional['Environment'] = None):
        self.parent = parent
        self.variables: Dict[str, Any] = {}
        self.error_handler = ErrorHandler()
    
    def define(self, name: str, value: Any):
        """Определяет переменную в текущей области видимости"""
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        """Получает значение переменной"""
        if name in self.variables:
            return self.variables[name]
        
        if self.parent is not None:
            return self.parent.get(name)
        
        raise PyLiteRuntimeError(
            self.error_handler.create_friendly_message(
                'undefined_variable',
                name=name
            )
        )
    
    def assign(self, name: str, value: Any):
        """Присваивает значение переменной"""
        if name in self.variables:
            self.variables[name] = value
            return
        
        if self.parent is not None:
            try:
                self.parent.assign(name, value)
                return
            except PyLiteRuntimeError:
                pass
        
        # Если переменная не найдена, создаем её в текущей области видимости
        self.variables[name] = value
    
    def contains(self, name: str) -> bool:
        """Проверяет, содержится ли переменная в области видимости"""
        if name in self.variables:
            return True
        
        if self.parent is not None:
            return self.parent.contains(name)
        
        return False


class CallableFunction:
    """Класс для хранения пользовательских функций"""
    
    def __init__(self, name: str, parameters: List[str], body: List, closure: Environment):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.closure = closure
        self.error_handler = ErrorHandler()
    
    def call(self, interpreter, arguments: List[Any]) -> Any:
        """Вызывает функцию с переданными аргументами"""
        if len(arguments) != len(self.parameters):
            raise PyLiteRuntimeError(
                self.error_handler.create_friendly_message(
                    'wrong_arguments',
                    name=self.name,
                    expected=len(self.parameters),
                    actual=len(arguments)
                )
            )
        
        # Создаем новую область видимости для функции
        environment = Environment(self.closure)
        
        # Связываем параметры с аргументами
        for i, param in enumerate(self.parameters):
            environment.define(param, arguments[i])
        
        # Сохраняем предыдущее окружение
        previous = interpreter.environment
        interpreter.environment = environment
        
        try:
            # Выполняем тело функции
            result = None
            for stmt in self.body:
                result = interpreter.execute_statement(stmt)
                # Проверяем на return
                if isinstance(result, ReturnValue):
                    return result.value
            
            return None  # Функция без return возвращает None
            
        finally:
            # Восстанавливаем предыдущее окружение
            interpreter.environment = previous
    
    def __str__(self):
        return f"<function {self.name}>"


class ReturnValue:
    """Специальный класс для обработки return"""
    
    def __init__(self, value: Any):
        self.value = value


class PyLiteClass:
    """Класс для хранения определений классов"""
    
    def __init__(self, name: str, superclass: Optional['PyLiteClass'], methods: Dict[str, CallableFunction]):
        self.name = name
        self.superclass = superclass
        self.methods = methods
    
    def find_method(self, name: str) -> Optional[CallableFunction]:
        """Ищет метод в классе или родительских классах"""
        if name in self.methods:
            return self.methods[name]
        
        if self.superclass is not None:
            return self.superclass.find_method(name)
        
        return None
    
    def call(self, interpreter, arguments: List[Any]) -> 'PyLiteInstance':
        """Создает экземпляр класса"""
        instance = PyLiteInstance(self)
        
        # Ищем конструктор __init__
        initializer = self.find_method('__init__')
        if initializer is not None:
            # Вызываем конструктор с экземпляром как первым аргументом
            initializer.call(interpreter, [instance] + arguments)
        
        return instance
    
    def __str__(self):
        return f"<class {self.name}>"


class PyLiteInstance:
    """Экземпляр класса PyLite"""
    
    def __init__(self, klass: PyLiteClass):
        self.klass = klass
        self.fields: Dict[str, Any] = {}
        self.error_handler = ErrorHandler()
    
    def get(self, name: str) -> Any:
        """Получает поле или метод экземпляра"""
        if name in self.fields:
            return self.fields[name]
        
        method = self.klass.find_method(name)
        if method is not None:
            # Возвращаем связанный метод
            return BoundMethod(self, method)
        
        raise PyLiteRuntimeError(
            self.error_handler.create_friendly_message(
                'attribute_error',
                type=self.klass.name,
                attr=name
            )
        )
    
    def set(self, name: str, value: Any):
        """Устанавливает поле экземпляра"""
        self.fields[name] = value
    
    def __str__(self):
        return f"<{self.klass.name} instance>"


class BoundMethod:
    """Связанный метод (метод с привязанным экземпляром)"""
    
    def __init__(self, instance: PyLiteInstance, method: CallableFunction):
        self.instance = instance
        self.method = method
    
    def call(self, interpreter, arguments: List[Any]) -> Any:
        """Вызывает метод с экземпляром как первым аргументом"""
        return self.method.call(interpreter, [self.instance] + arguments)
    
    def __str__(self):
        return f"<bound method {self.method.name}>"
