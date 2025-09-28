
from __future__ import annotations

def dyadic_horizon_crossed(n: int, L: int) -> bool:
    """
    Phase trigger: 'universe scale' 2^n crosses critical 2^L.
    """
    return n >= L

def prime_power_spike(m: int) -> bool:
    """
    Heuristic tag: True if m is p^k for odd prime p.
    """
    x = m
    p = None
    d = 2
    found = False
    while d * d <= x:
        e = 0
        while x % d == 0:
            x //= d; e += 1
        if e:
            if p is None: p = d
            else: return False
            found = True
        d = 3 if d == 2 else d + 2
    if x > 1:
        if p is None: p = x; found = True
        else: return False
    return found and (p % 2 == 1)
