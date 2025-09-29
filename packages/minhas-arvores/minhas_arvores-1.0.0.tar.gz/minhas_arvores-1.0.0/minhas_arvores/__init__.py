"""
Biblioteca Minhas Árvores - Implementação dos algoritmos ID3, C4.5 e CART

- ID3: Ganho de informação, apenas categóricos
- C4.5: Razão de ganho, categóricos + contínuos, trata missing values
- CART: Índice Gini, sempre divisões binárias
"""

from .id3 import ID3
from .c45 import C45
from .cart import CART
from .utilidades import (
    calcular_entropia,
    calcular_gini,
    calcular_ganho_informacao,
    calcular_razao_ganho,
    encontrar_melhor_limiar
)
from .arvore_base import NoArvore

__version__ = "1.0.0"
__author__ = "Biblioteca de Aprendizado de Máquina"

__all__ = [
    'ID3',
    'C45',
    'CART',
    'NoArvore',
    'calcular_entropia',
    'calcular_gini',
    'calcular_ganho_informacao',
    'calcular_razao_ganho',
    'encontrar_melhor_limiar'
]
