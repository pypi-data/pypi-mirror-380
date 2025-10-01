"""
Модуль sound для PyLite, предоставляющий функции для воспроизведения звуков.
"""
import os
import pygame
from typing import Dict, Any
from importlib import resources
from ..types import BuiltinFunction
from ..error_handler import RuntimeError as PyLiteRuntimeError

# Инициализация микшера pygame
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

# Глобальная громкость
_global_volume = 1.0

def pylite_play(sound_name: str):
    """Воспроизводит звуковой файл по имени, относительному или полному пути."""
    sound_path = None

    # 1. Проверяем, является ли это полным путем
    if os.path.isabs(sound_name) and os.path.exists(sound_name):
        sound_path = sound_name
    
    # 2. Если нет, проверяем относительный путь от текущей директории
    if not sound_path:
        relative_path = os.path.abspath(sound_name)
        if os.path.exists(relative_path):
            sound_path = relative_path

    # 3. Если ничего не найдено, ищем встроенный звук
    if not sound_path:
        if not sound_name.endswith(('.wav', '.ogg')):
            sound_name += '.wav'
        
        try:
            with resources.path('pylite.assets.sounds', sound_name) as path:
                sound_path = str(path)
        except FileNotFoundError:
            raise PyLiteRuntimeError(f"Звуковой файл не найден: {sound_name}")

    # Воспроизводим звук по найденному пути
    try:
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(_global_volume)
        channel = pygame.mixer.find_channel()
        if channel:
            channel.play(sound)
        else:
            raise PyLiteRuntimeError("Все звуковые каналы заняты.")
    except pygame.error as e:
        raise PyLiteRuntimeError(f"Ошибка воспроизведения звука: {e}")

def pylite_stop():
    """Останавливает воспроизведение всех звуков."""
    pygame.mixer.stop()

def pylite_set_volume(volume: float):
    """Устанавливает общую громкость для всех последующих звуков (от 0.0 до 1.0)."""
    global _global_volume
    if not 0.0 <= volume <= 1.0:
        raise PyLiteRuntimeError("Громкость должна быть от 0.0 до 1.0")
    _global_volume = volume

def create_sound_module() -> Dict[str, Any]:
    """Создает модуль sound."""
    return {
        'play': BuiltinFunction('play', pylite_play, 1, 1),
        'stop': BuiltinFunction('stop', pylite_stop, 0, 0),
        'set_volume': BuiltinFunction('set_volume', pylite_set_volume, 1, 1),
    }

