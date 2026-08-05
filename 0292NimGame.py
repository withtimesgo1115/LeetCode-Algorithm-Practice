"""
Nim Game.
Two players take turns removing 1 to 3 stones from a pile.
The player who removes the last stone wins. You go first.
Determine whether you can win given n stones, assuming optimal play.
"""


def can_win_nim(n):
    """You lose only when n is a multiple of 4."""
    return n % 4 != 0
