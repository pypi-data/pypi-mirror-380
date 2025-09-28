
from __future__ import annotations
import math
from typing import List, Tuple

def phi(n: int) -> int:
    """Euler's totient via factorization (simple)."""
    if n <= 0: raise ValueError("n must be positive")
    result = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p = 3 if p == 2 else p + 2  # skip evens
    if m > 1:
        result -= result // m
    return result

def multiplicative_order(a: int, m: int) -> int:
    """Smallest k>0 such that a^k ≡ 1 (mod m); assumes gcd(a,m)=1."""
    if math.gcd(a, m) != 1:
        raise ValueError("a and m must be coprime")
    # order divides phi(m): test divisors in increasing order
    t = phi(m)
    # factor t
    fac = {}
    x = t
    d = 2
    while d * d <= x:
        while x % d == 0:
            fac[d] = fac.get(d, 0) + 1
            x //= d
        d = 3 if d == 2 else d + 2
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    # generate divisors in increasing order
    divs = [1]
    for p, e in fac.items():
        divs = [d * (p ** k) for d in divs for k in range(e + 1)]
    for d in sorted(divs):
        if pow(a, d, m) == 1:
            return d
    raise RuntimeError("order not found")

def a003558_order(n: int) -> int:
    """A003558(n) = ord_{2n+1}(2)."""
    if n < 0:
        raise ValueError("n >= 0 required")
    m = 2*n + 1
    if m == 1:
        return 1
    return multiplicative_order(2, m)

def back_front_cycle_length(n: int) -> int:
    """
    Cycle length for back-front permutation on n items equals ord_{2n-1}(2).
    """
    if n <= 0:
        raise ValueError("n must be >=1")
    m = 2*n - 1
    if m == 1:
        return 1
    return multiplicative_order(2, m)

def prime_power_factors(n: int):
    """Return prime-power factorization list [(p,e),...]."""
    out = []
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out.append((p,e))
        p = 3 if p == 2 else p + 2
    if m > 1:
        out.append((m,1))
    return out
