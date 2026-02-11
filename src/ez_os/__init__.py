"""
EZ-OS: Sistema Operacional de Memória Lúdica Offline

Um sistema de memória factual para jogos retro que registra eventos reais
e expressa o histórico através de um mascote procedural determinístico.
"""

__version__ = "1.0.0"
__author__ = "João"

from ez_os.core import memory, governance, companion
from ez_os.ui import tui
from ez_os.launcher import launcher, indexer

__all__ = [
    "memory",
    "governance",
    "companion",
    "tui",
    "launcher",
    "indexer",
]
