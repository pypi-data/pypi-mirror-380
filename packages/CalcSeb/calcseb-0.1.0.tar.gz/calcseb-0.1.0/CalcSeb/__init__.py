"""
CalcSeb - Una calculadora colaborativa
"""

from .main import main
from .arithmetic.arithmetic import Aritmetica
from .areas.areas import Areas
from .trigonometry.trig import CalculadoraTrigonometrica
from .coolstuff import FrasesDesarrollador

__all__ = [
    "main",
    "Aritmetica",
    "Areas",
    "CalculadoraTrigonometrica",
    "FrasesDesarrollador",
]
