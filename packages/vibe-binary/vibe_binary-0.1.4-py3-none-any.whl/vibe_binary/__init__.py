"""
Vibe Binary - библиотека бинарных алгоритмов 🪄
"""

from .search import binary_search, binary_search_c
from .neural_guess import neural_guess_number, neural_guess_c, NeuralGuesser

__version__ = "0.1.3"
__all__ = [
    'binary_search',
    'binary_search_c',
    'neural_guess_number',
    'neural_guess_c',
    'NeuralGuesser'
]