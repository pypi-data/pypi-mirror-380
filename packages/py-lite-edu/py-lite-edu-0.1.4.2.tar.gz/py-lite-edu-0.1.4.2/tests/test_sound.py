"""
Тесты для модуля sound
"""

import unittest
from unittest.mock import patch, MagicMock
from pylite.lexer import Lexer
from pylite.parser import Parser
from pylite.interpreter import Interpreter
from pylite.error_handler import RuntimeError as PyLiteRuntimeError

class TestSoundModule(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = Interpreter()
    
    def _execute_code(self, code: str):
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        program = parser.parse()
        return self.interpreter.interpret(program)

    @patch('pylite.modules.sound_module.pygame.mixer.Sound')
    @patch('pylite.modules.sound_module.pygame.mixer.find_channel')
    @patch('pylite.modules.sound_module.resources.path')
    def test_play_builtin_sound(self, mock_resources_path, mock_find_channel, mock_sound):
        """Тест воспроизведения встроенного звука"""
        mock_channel = MagicMock()
        mock_find_channel.return_value = mock_channel
        
        # Мокируем путь к файлу, чтобы он "существовал"
        class MockPathManager:
            def __enter__(self):
                return '/fake/path/to/click.wav'
            def __exit__(self, exc_type, exc_val, exc_tb):
                pass
        
        mock_resources_path.return_value = MockPathManager()

        self._execute_code('import sound\nsound.play("click")')
        
        mock_resources_path.assert_called_with('pylite.assets.sounds', 'click.wav')
        mock_sound.assert_called_with('/fake/path/to/click.wav')
        mock_channel.play.assert_called_once()
        mock_sound.return_value.set_volume.assert_called_with(1.0) # Громкость по умолчанию

    @patch('pylite.modules.sound_module.pygame.mixer.Sound')
    @patch('pylite.modules.sound_module.pygame.mixer.find_channel')
    @patch('pylite.modules.sound_module.os.path.exists')
    @patch('pylite.modules.sound_module.os.path.isabs')
    def test_play_external_sound(self, mock_isabs, mock_exists, mock_find_channel, mock_sound):
        """Тест воспроизведения внешнего звукового файла"""
        mock_channel = MagicMock()
        mock_find_channel.return_value = mock_channel
        mock_isabs.return_value = True
        mock_exists.return_value = True

        external_path = '/my/custom/sound.wav'
        self._execute_code(f'import sound\nsound.play("{external_path}")')
        
        mock_sound.assert_called_with(external_path)
        mock_channel.play.assert_called_once()

    @patch('pylite.modules.sound_module.pygame.mixer.Sound')
    @patch('pylite.modules.sound_module.pygame.mixer.find_channel')
    @patch('pylite.modules.sound_module.resources.path')
    def test_set_volume(self, mock_resources_path, mock_find_channel, mock_sound):
        """Тест установки громкости"""
        mock_channel = MagicMock()
        mock_find_channel.return_value = mock_channel
        class MockPathManager:
            def __enter__(self): return '/fake/path/to/click.wav'
            def __exit__(self, et, ev, tb): pass
        mock_resources_path.return_value = MockPathManager()

        self._execute_code('import sound\nsound.set_volume(0.5)\nsound.play("click")')
        
        mock_sound.return_value.set_volume.assert_called_with(0.5)

    def test_invalid_volume(self):
        """Тест неверного значения громкости"""
        with self.assertRaises(PyLiteRuntimeError) as context:
            self._execute_code('import sound\nsound.set_volume(1.5)')
        self.assertIn("Громкость должна быть от 0.0 до 1.0", str(context.exception))

    @patch('pylite.modules.sound_module.resources.path')
    @patch('pylite.modules.sound_module.os.path.exists')
    @patch('pylite.modules.sound_module.os.path.isabs')
    def test_file_not_found(self, mock_isabs, mock_exists, mock_resources_path):
        """Тест ошибки 'файл не найден'"""
        mock_isabs.return_value = False
        mock_exists.return_value = False
        mock_resources_path.side_effect = FileNotFoundError
        with self.assertRaises(PyLiteRuntimeError) as context:
            self._execute_code('import sound\nsound.play("nonexistent")')
        self.assertIn("Звуковой файл не найден", str(context.exception))

if __name__ == '__main__':
    unittest.main()

