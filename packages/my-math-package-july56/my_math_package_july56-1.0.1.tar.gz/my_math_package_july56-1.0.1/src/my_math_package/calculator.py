# src/my_math_package/calculator.py
from .internal_utils import _InputValidator

class Calculator:
    """Public класс - доступен извне пакета"""
    
    def add(self, a, b):
        """Public метод"""
        _InputValidator.validate_numbers(a, b)
        return a + b
    
    def subtract(self, a, b):
        """Public метод"""
        _InputValidator.validate_numbers(a, b)
        return a - b
    
    def _multiply(self, a, b):
        """Protected метод (аналог internal) - не рекомендуется использовать извне"""
        _InputValidator.validate_numbers(a, b)
        return a * b