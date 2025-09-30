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
    """Воспроизводит звуковой файл по имени или по полному пути."""
    sound_path = None
    sound_path_manager = None

    # Проверяем, является ли sound_name полным путем к файлу
    if os.path.isabs(sound_name) and os.path.exists(sound_name):
        sound_path = sound_name
    else:
        # Иначе, ищем встроенный звук
        if not sound_name.endswith(('.wav', '.ogg')):
            sound_name += '.wav'
        
        try:
            # Используем importlib.resources для надежного доступа к файлам данных
            sound_path_manager = resources.path('pylite.assets.sounds', sound_name)
        except FileNotFoundError:
            raise PyLiteRuntimeError(f"Звуковой файл не найден: {sound_name}")

    # Воспроизводим звук по найденному пути
    try:
        # Если это встроенный звук, нам нужно войти в контекст
        if sound_path_manager:
            with sound_path_manager as path:
                sound = pygame.mixer.Sound(path)
                sound.set_volume(_global_volume)
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(sound)
                else:
                    raise PyLiteRuntimeError("Все звуковые каналы заняты.")
        elif sound_path:
            # Если это внешний файл
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(_global_volume)
            channel = pygame.mixer.find_channel()
            if channel:
                channel.play(sound)
            else:
                raise PyLiteRuntimeError("Все звуковые каналы заняты.")
        else:
            # Эта ветка не должна быть достигнута, но на всякий случай
            raise PyLiteRuntimeError(f"Не удалось определить путь к звуковому файлу: {sound_name}")

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

