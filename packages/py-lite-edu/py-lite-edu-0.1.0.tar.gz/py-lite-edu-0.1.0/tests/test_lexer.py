"""
Тесты для лексического анализатора
"""

import unittest
from pylite.lexer import Lexer
from pylite.tokens import TokenType
from pylite.error_handler import LexerError


class TestLexer(unittest.TestCase):
    
    def test_numbers(self):
        """Тест разбора чисел"""
        lexer = Lexer("42 3.14")
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.INTEGER)
        self.assertEqual(tokens[0].value, 42)
        
        self.assertEqual(tokens[1].type, TokenType.FLOAT)
        self.assertEqual(tokens[1].value, 3.14)
    
    def test_strings(self):
        """Тест разбора строк"""
        lexer = Lexer('"hello" \'world\'')
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, "hello")
        
        self.assertEqual(tokens[1].type, TokenType.STRING)
        self.assertEqual(tokens[1].value, "world")
    
    def test_identifiers_and_keywords(self):
        """Тест идентификаторов и ключевых слов"""
        lexer = Lexer("def my_func if True")
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.DEF)
        
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].value, "my_func")
        
        self.assertEqual(tokens[2].type, TokenType.IF)
        
        self.assertEqual(tokens[3].type, TokenType.BOOLEAN)
        self.assertEqual(tokens[3].value, True)
    
    def test_operators(self):
        """Тест операторов"""
        lexer = Lexer("+ - * / == != < > <= >=")
        tokens = lexer.tokenize()
        
        expected_types = [
            TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE,
            TokenType.EQUAL, TokenType.NOT_EQUAL, TokenType.LESS_THAN,
            TokenType.GREATER_THAN, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL
        ]
        
        for i, expected_type in enumerate(expected_types):
            self.assertEqual(tokens[i].type, expected_type)
    
    def test_indentation(self):
        """Тест обработки отступов"""
        code = """def test():
    print("hello")
    if True:
        print("nested")
"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Должны быть токены INDENT и DEDENT
        token_types = [token.type for token in tokens]
        self.assertIn(TokenType.INDENT, token_types)
        self.assertIn(TokenType.DEDENT, token_types)
    
    def test_error_unclosed_string(self):
        """Тест ошибки незакрытой строки"""
        lexer = Lexer('"unclosed string')
        
        with self.assertRaises(LexerError):
            lexer.tokenize()
    
    def test_comments(self):
        """Тест обработки комментариев"""
        lexer = Lexer("x = 5  # это комментарий")
        tokens = lexer.tokenize()
        
        # Комментарии должны быть проигнорированы
        token_values = [token.value for token in tokens if token.type != TokenType.EOF]
        self.assertNotIn("# это комментарий", token_values)


if __name__ == '__main__':
    unittest.main()
