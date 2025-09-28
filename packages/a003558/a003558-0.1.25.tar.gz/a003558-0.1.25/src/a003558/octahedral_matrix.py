
from __future__ import annotations
import numpy as np

def octahedral_adjacency() -> np.ndarray:
    A = np.zeros((6,6), dtype=int)
    opp = {0:1, 1:0, 2:3, 3:2, 4:5, 5:4}
    for i in range(6):
        for j in range(6):
            if i != j and j != opp[i]:
                A[i,j] = 1
    return A

def embed_octonion_axes_to_octahedron() -> np.ndarray:
    dirs = np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1],
        [1,1,0],
        [1,0,1],
        [0,1,1],
        [1,1,1]
    ], dtype=float)
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    oct_dirs = np.array([
        [1,0,0],[-1,0,0],
        [0,1,0],[0,-1,0],
        [0,0,1],[0,0,-1]
    ], dtype=float)
    M = np.zeros((7,6))
    for i in range(7):
        cosines = dirs[i] @ oct_dirs.T
        M[i] = np.abs(cosines)
    return M
