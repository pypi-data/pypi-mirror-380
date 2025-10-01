# src/my_math_package/geometry.py
import math
from .internal_utils import _InputValidator

class Geometry:
    """Public класс - доступен извне пакета"""
    
    def circle_area(self, radius):
        """Public метод"""
        _InputValidator.validate_positive(radius)
        return math.pi * radius ** 2
    
    def _circle_circumference(self, radius):
        """Protected метод - не рекомендуется использовать извне"""
        _InputValidator.validate_positive(radius)
        return 2 * math.pi * radius