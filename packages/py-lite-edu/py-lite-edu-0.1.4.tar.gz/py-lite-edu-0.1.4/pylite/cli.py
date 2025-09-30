"""
Интерфейс командной строки для PyLite
"""

import sys
import os
import argparse
import readline
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
        
        buffer = []
        while True:
            try:
                prompt = "...  " if buffer else "pyl> "
                line = input(prompt)

                if not buffer and line.strip().lower() in ['quit()', 'exit()', 'quit', 'exit']:
                    print("До свидания! 👋")
                    break

                buffer.append(line)

                # Execute when an empty line is entered after a code block
                if not line.strip() and len(buffer) > 1:
                    code_to_execute = "\n".join(buffer)
                    buffer = []
                    result = self._execute_line(code_to_execute)
                    if result is not None:
                        print(result)
                    continue
                
                # Continue collecting lines if it's the start of a block or an indented line
                if line.strip().endswith(':') or (buffer and (line.startswith(' ') or line.startswith('\t'))):
                    continue

                # Execute single-line commands
                if buffer:
                    code_to_execute = "\n".join(buffer)
                    buffer = []
                    result = self._execute_line(code_to_execute)
                    if result is not None:
                        print(result)
            
            except KeyboardInterrupt:
                print("\nИспользуйте quit() для выхода.")
                buffer = [] # Reset buffer on interrupt
            except EOFError:
                print("\nДо свидания! 👋")
                break
    
    def _execute_line(self, code: str) -> Optional[str]:
        """Выполняет блок кода"""
        try:
            # Лексический анализ
            lexer = Lexer(code)
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
            return self.error_handler.handle_exception(e, code)


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
