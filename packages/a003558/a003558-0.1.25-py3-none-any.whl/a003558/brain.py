
from __future__ import annotations
import numpy as np

def quenneau_spin_to_dyadic_capacity(pattern: np.ndarray) -> int:
    """
    Toy: given a 'spin' pattern (0/1) length N, return dyadic capacity 2^k >= N
    as minimal cost abstraction target.
    """
    N = len(pattern)
    k = int(np.ceil(np.log2(max(1, N))))
    capacity = 2**k
    return capacity

def compression_loss(pattern: np.ndarray) -> float:
    """
    Simple proxy for loss when coarse-graining to nearest dyadic block.
    """
    N = len(pattern)
    capacity = quenneau_spin_to_dyadic_capacity(pattern)
    return (capacity - N) / capacity
