# src/my_math_package/internal_utils.py

# Имена с подчеркиванием считаются "internal"
class _InputValidator:
    """Internal класс - не предназначен для внешнего использования"""
    
    @staticmethod
    def validate_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
    
    @staticmethod
    def validate_positive(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if value <= 0:
            raise ValueError("Значение должно быть положительным")

# Internal функция
def _advanced_calculation(x, y):
    """Internal функция - не предназначена для внешнего использования"""
    return (x ** 2) + (y ** 2)