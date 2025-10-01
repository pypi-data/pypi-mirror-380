"""
Vibe Binary - библиотека бинарных алгоритмов с AI-магией 🪄
"""

from .search import binary_search, binary_search_c
from .neural_guess import neural_guess_number, neural_guess_c, NeuralGuesser
from .ai_api import NeuralAPI

__version__ = "0.1.0"
__all__ = [
    'binary_search',
    'binary_search_c',
    'neural_guess_number',
    'neural_guess_c',
    'NeuralGuesser',
    'NeuralAPI'
]