# src/my_math_package/__init__.py
from .calculator import Calculator
from .geometry import Geometry

__version__ = "1.0.0"
__all__ = ['Calculator', 'Geometry']  # Только public классы