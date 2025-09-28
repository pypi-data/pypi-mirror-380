
from __future__ import annotations
import numpy as np
from .octonions import octonion_mul, norm

def dyadic_clock_to_octonion(k: int, phase: float = 0.0) -> np.ndarray:
    theta = (np.pi / (2**k)) + phase
    v = np.zeros(8)
    v[0] = np.cos(theta)
    v[1] = np.sin(theta)
    return v

def coupled_step(k_brain: int, k_cosmos: int) -> float:
    a = dyadic_clock_to_octonion(k_brain, phase=0.0)
    b = dyadic_clock_to_octonion(k_cosmos, phase=np.pi/8)
    c = octonion_mul(a, b)
    return abs(norm(c) - norm(a)*norm(b))
