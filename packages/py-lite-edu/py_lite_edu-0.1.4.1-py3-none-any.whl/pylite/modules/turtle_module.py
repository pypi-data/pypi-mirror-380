"""
Модуль turtle для PyLite, использующий PyQt5 для отображения графики в окне.
"""

import sys
import math
from typing import Dict, Any, List, Tuple

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPointF

from ..types import BuiltinFunction
from ..error_handler import RuntimeError as PyLiteRuntimeError

# --- Глобальное состояние и классы PyQt ---
_app = None
_canvas = None

class TurtleCanvas(QWidget):
    """Виджет, на котором рисует черепашка."""
    def __init__(self):
        super().__init__()
        self.paths: List[Tuple[QPointF, QPointF, QColor, float]] = []
        self.setWindowTitle("PyLite Turtle Graphics")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: white;")

    def add_path(self, start: QPointF, end: QPointF, color: QColor, width: float):
        self.paths.append((start, end, color, width))
        self.update()  # Запрашиваем перерисовку

    def clear_canvas(self):
        self.paths = []
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for start, end, color, width in self.paths:
            pen = QPen(color, width, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(start, end)

# --- Глобальное состояние черепашки ---
_position: Tuple[float, float] = (0.0, 0.0)
_angle: float = 0.0
_pen_down: bool = True
_pen_color: QColor = QColor("black")
_pen_width: float = 2.0

def _initialize_qt():
    """Инициализирует QApplication и холст."""
    global _app, _canvas
    if _app is None:
        # QApplication.instance() возвращает существующий экземпляр или None
        _app = QApplication.instance() or QApplication(sys.argv)
    if _canvas is None:
        _canvas = TurtleCanvas()
        # Центрируем начальную позицию
        global _position
        _position = (_canvas.width() / 2, _canvas.height() / 2)

def _reset_state():
    """Сбрасывает состояние черепашки."""
    _initialize_qt()
    global _position, _angle, _pen_down, _pen_color, _pen_width
    _position = (_canvas.width() / 2, _canvas.height() / 2)
    _angle = 0.0
    _pen_down = True
    _pen_color = QColor("black")
    _pen_width = 2.0
    _canvas.clear_canvas()

def _to_radians(degrees: float) -> float:
    return degrees * (math.pi / 180.0)

# --- Функции, видимые в PyLite ---

def pylite_forward(distance: float):
    _initialize_qt()
    global _position
    start_x, start_y = _position
    rad_angle = _to_radians(_angle)
    end_x = start_x + distance * math.cos(rad_angle)
    end_y = start_y + distance * math.sin(rad_angle)
    
    if _pen_down:
        start_point = QPointF(start_x, start_y)
        end_point = QPointF(end_x, end_y)
        _canvas.add_path(start_point, end_point, _pen_color, _pen_width)
        
    _position = (end_x, end_y)

def pylite_backward(distance: float):
    pylite_forward(-distance)

def pylite_left(degrees: float):
    global _angle
    _angle = (_angle - degrees) % 360

def pylite_right(degrees: float):
    global _angle
    _angle = (_angle + degrees) % 360

def pylite_penup():
    global _pen_down
    _pen_down = False

def pylite_pendown():
    global _pen_down
    _pen_down = True

def pylite_color(color_name: str):
    global _pen_color
    try:
        _pen_color = QColor(color_name)
        if not _pen_color.isValid():
            raise ValueError
    except ValueError:
        raise PyLiteRuntimeError(f"Неизвестный цвет: '{color_name}'.")

def pylite_speed(speed_value: int):
    # В этой реализации скорость не влияет на отрисовку, но мы оставим функцию для совместимости
    if not 0 <= speed_value <= 10:
        raise PyLiteRuntimeError("Скорость должна быть числом от 0 до 10.")

def pylite_reset():
    _reset_state()

def pylite_done():
    global _app, _canvas
    _initialize_qt()
    _canvas.show()
    print("\n🐢 Окно с графикой открыто. Закройте его, чтобы продолжить.")
    _app.exec_()
    print("Окно закрыто.")
    # Сбрасываем состояние после закрытия окна
    _canvas = None # Позволит создать новое окно при следующем запуске

# --- Инициализация модуля ---

def create_turtle_module() -> Dict[str, Any]:
    """Создает модуль turtle."""
    return {
        'forward': BuiltinFunction('forward', pylite_forward, 1, 1),
        'backward': BuiltinFunction('backward', pylite_backward, 1, 1),
        'left': BuiltinFunction('left', pylite_left, 1, 1),
        'right': BuiltinFunction('right', pylite_right, 1, 1),
        'penup': BuiltinFunction('penup', pylite_penup, 0, 0),
        'pendown': BuiltinFunction('pendown', pylite_pendown, 0, 0),
        'color': BuiltinFunction('color', pylite_color, 1, 1),
        'speed': BuiltinFunction('speed', pylite_speed, 1, 1),
        'reset': BuiltinFunction('reset', pylite_reset, 0, 0),
        'done': BuiltinFunction('done', pylite_done, 0, 0),
    }
