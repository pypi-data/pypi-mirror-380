from __future__ import annotations
import math

def staircase_level(n: int) -> int:
    """
    Kritische 'trapfunctie' op dyadische schalen.
    1 -> 1
    2..3 -> 2
    4..7 -> 3
    8..15 -> 4
    etc.
    """
    if n < 1:
        raise ValueError("n moet positief zijn")
    return 1 + (n.bit_length() - 1)


def horizon_bound(n: int, L: int) -> bool:
    """
    Horizon condition: if L = ord_{2n-1}(2) then n <= 2^{L-1},
    equivalently: L >= 1 + ceil(log2 n).
    """
    return L >= 1 + math.ceil(math.log2(n))
