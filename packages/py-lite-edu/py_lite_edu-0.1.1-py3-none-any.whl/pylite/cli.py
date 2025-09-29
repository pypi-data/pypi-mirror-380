"""
Интерфейс командной строки для PyLite
"""

import sys
import os
import argparse
from typing import Optional, List
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .error_handler import ErrorHandler, PyLiteError


class REPL:
    """Интерактивная оболочка PyLite (Read-Eval-Print Loop)"""
    
    def __init__(self, mode: str = 'basic'):
        self.interpreter = Interpreter(mode)
        self.error_handler = ErrorHandler()
        self.mode = mode
    
    def run(self):
        """Запускает интерактивный режим"""
        print("🐍 Добро пожаловать в PyLite!")
        print(f"Режим: {'базовый' if self.mode == 'basic' else 'расширенный'}")
        print("Наберите 'quit()' или 'exit()' для выхода.\n")
        
        while True:
            try:
                # Получаем ввод от пользователя
                line = input("pylite> ")
                
                # Проверяем команды выхода
                if line.strip().lower() in ['quit()', 'exit()', 'quit', 'exit']:
                    print("До свидания! 👋")
                    break
                
                # Пропускаем пустые строки
                if not line.strip():
                    continue
                
                # Выполняем код
                result = self._execute_line(line)
                
                # Выводим результат, если он не None
                if result is not None:
                    print(result)
                    
            except KeyboardInterrupt:
                print("\nИспользуйте quit() для выхода.")
            except EOFError:
                print("\nДо свидания! 👋")
                break
    
    def _execute_line(self, line: str) -> Optional[str]:
        """Выполняет строку кода"""
        try:
            # Лексический анализ
            lexer = Lexer(line)
            tokens = lexer.tokenize()
            
            # Синтаксический анализ
            parser = Parser(tokens)
            program = parser.parse()
            
            # Выполнение
            result = self.interpreter.interpret(program)
            
            return result
            
        except PyLiteError as e:
            return self.error_handler.format_error(e)
        except Exception as e:
            return self.error_handler.handle_exception(e, line)


class PyLiteRunner:
    """Класс для выполнения .pyl файлов"""
    
    def __init__(self, mode: str = 'basic'):
        self.interpreter = Interpreter(mode)
        self.error_handler = ErrorHandler()
        self.mode = mode
    
    def run_file(self, filename: str) -> int:
        """Выполняет файл .pyl"""
        try:
            # Проверяем существование файла
            if not os.path.exists(filename):
                print(f"❌ Файл '{filename}' не найден.")
                return 1
            
            # Читаем содержимое файла
            with open(filename, 'r', encoding='utf-8') as f:
                source_code = f.read()
            
            # Выполняем код
            self._execute_code(source_code)
            return 0
            
        except PyLiteError as e:
            print(self.error_handler.format_error(e))
            return 1
        except Exception as e:
            print(self.error_handler.handle_exception(e, source_code))
            return 1
    
    def _execute_code(self, source_code: str):
        """Выполняет исходный код"""
        # Лексический анализ
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        # Синтаксический анализ
        parser = Parser(tokens)
        program = parser.parse()
        
        # Выполнение
        result = self.interpreter.interpret(program)


def main():
    """Главная функция CLI"""
    parser = argparse.ArgumentParser(
        description='PyLite - упрощённый Python для детей',
        prog='pylite'
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='Файл .pyl для выполнения (если не указан, запускается REPL)'
    )
    
    parser.add_argument(
        '--mode',
        choices=['basic', 'extended'],
        default='basic',
        help='Режим работы: basic (базовый) или extended (расширенный)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='PyLite 0.1.0'
    )
    
    args = parser.parse_args()
    
    if args.file:
        # Режим выполнения файла
        runner = PyLiteRunner(args.mode)
        return runner.run_file(args.file)
    else:
        # Интерактивный режим (REPL)
        repl = REPL(args.mode)
        repl.run()
        return 0


if __name__ == '__main__':
    sys.exit(main())
