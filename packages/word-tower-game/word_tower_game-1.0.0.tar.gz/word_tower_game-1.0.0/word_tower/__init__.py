"""
Word Tower - Multiplayer Real-time Word Game
============================================

A multiplayer word game where players must form a "tower of words" 
where each word starts with the last letter of the previous word.

Installation:
    pip install word-tower-game

Usage:
    word-tower

Features:
    - Real-time multiplayer gameplay
    - WebSocket communication
    - Multiple difficulty levels
    - Timer-based elimination system
    - Portuguese word dictionary validation
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"
__email__ = "seu.email@exemplo.com"

from .main import run_game

__all__ = ["run_game"]