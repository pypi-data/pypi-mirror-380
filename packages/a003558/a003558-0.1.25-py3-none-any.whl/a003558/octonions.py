from __future__ import annotations
import numpy as np

"""
Octonions via Cayley–Dickson from quaternions.

We represent an octonion x ∈ R^8 as a pair of quaternions (a, b),
with a = (x0, x1, x2, x3), b = (x4, x5, x6, x7).

Product (a,b) * (c,d) = ( a*c - conj(d)*b,  d*a + b*conj(c) )
Conjugate: conj(a,b) = (conj(a), -b)
Norm: ||(a,b)||^2 = ||a||^2 + ||b||^2

This guarantees:
- Alternativity: (xx)y = x(xy)
- Composition:   ||xy|| = ||x|| * ||y||
"""

# ---------- Quaternion helpers ----------

def _q_conj(q: np.ndarray) -> np.ndarray:
    q = np.asarray(q, dtype=float).reshape(4)
    out = q.copy()
    out[1:] *= -1.0
    return out

def _q_mul(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    """
    Hamilton quaternions (1, i, j, k) with i^2 = j^2 = k^2 = ijk = -1.
    """
    p = np.asarray(p, dtype=float).reshape(4)
    q = np.asarray(q, dtype=float).reshape(4)
    p0, p1, p2, p3 = p
    q0, q1, q2, q3 = q
    return np.array([
        p0*q0 - p1*q1 - p2*q2 - p3*q3,
        p0*q1 + p1*q0 + p2*q3 - p3*q2,
        p0*q2 - p1*q3 + p2*q0 + p3*q1,
        p0*q3 + p1*q2 - p2*q1 + p3*q0,
    ], dtype=float)

def _q_norm2(q: np.ndarray) -> float:
    q = np.asarray(q, dtype=float).reshape(4)
    return float(np.dot(q, q))

# ---------- Octonions via Cayley–Dickson ----------

def octonion_mul(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Cayley–Dickson product in R^8.
    x, y: arrays of length 8, basis (1, e1..e7) reals.

    Returns x*y as an array of length 8.
    """
    x = np.asarray(x, dtype=float).reshape(8)
    y = np.asarray(y, dtype=float).reshape(8)

    a = x[:4]  # quaternion
    b = x[4:]  # quaternion
    c = y[:4]
    d = y[4:]

    ac = _q_mul(a, c)
    d_conj = _q_conj(d)
    left = ac - _q_mul(d_conj, b)

    da = _q_mul(d, a)
    c_conj = _q_conj(c)
    right = da + _q_mul(b, c_conj)

    out = np.empty(8, dtype=float)
    out[:4] = left
    out[4:] = right
    return out

def conj(x: np.ndarray) -> np.ndarray:
    """
    Octonion conjugate: \bar{(a,b)} = (conj(a), -b)
    """
    x = np.asarray(x, dtype=float).reshape(8)
    a = x[:4]
    b = x[4:]
    out = np.empty(8, dtype=float)
    out[:4] = _q_conj(a)
    out[4:] = -b
    return out

def norm(x: np.ndarray) -> float:
    """
    Euclidean norm ||x||. For octonions built by Cayley–Dickson:
      ||xy|| = ||x|| * ||y||
    """
    x = np.asarray(x, dtype=float).reshape(8)
    # Euclidean norm coincides with the composition norm here
    return float(np.linalg.norm(x))

def random_unit(seed: int | None = None) -> np.ndarray:
    """
    Random unit octonion (uniform on the 7-sphere).
    """
    rng = np.random.default_rng(seed)
    v = rng.normal(size=8)
    v /= np.linalg.norm(v)
    return v

# ---------- Optional convenience ----------

def zero() -> np.ndarray:
    return np.zeros(8, dtype=float)

def one() -> np.ndarray:
    z = np.zeros(8, dtype=float)
    z[0] = 1.0
    return z

def from_scalar_vector(s: float, v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float).reshape(7)
    out = np.empty(8, dtype=float)
    out[0] = float(s)
    out[1:] = v
    return out

def to_scalar_vector(x: np.ndarray) -> tuple[float, np.ndarray]:
    x = np.asarray(x, dtype=float).reshape(8)
    return float(x[0]), x[1:].copy()
