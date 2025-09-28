"""
Export routines to generate simple OBJ geometry for Blender or other 3D tools.
"""

from __future__ import annotations

import math
import os
from typing import Iterable


def _write_obj(path: str, vertices: list[tuple[float, float, float]], faces: list[tuple[int, int, int]]) -> str:
    """Write a minimal Wavefront OBJ file."""
    with open(path, "w", encoding="utf-8") as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for face in faces:
            f.write("f " + " ".join(str(i) for i in face) + "\n")
    return path


def export_octa_cube_obj(out_dir: str, basename: str = "scene") -> dict[str, str]:
    """
    Exporteer zowel een octaëder als een kubus naar OBJ-bestanden.
    Retourneert een dict met paden.

    Parameters
    ----------
    out_dir : str
        Doelmap.
    basename : str
        Basisnaam van de bestanden (zonder extensie).
    """
    os.makedirs(out_dir, exist_ok=True)

    # Eenhedenkubus (vertices van -1 tot 1)
    cube_vertices = [
        (-1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (-1, 1, 1),
        (1, -1, -1),
        (1, -1, 1),
        (1, 1, -1),
        (1, 1, 1),
    ]
    cube_faces = [
        (1, 2, 4),
        (1, 4, 3),
        (5, 7, 8),
        (5, 8, 6),
        (1, 5, 6),
        (1, 6, 2),
        (2, 6, 8),
        (2, 8, 4),
        (3, 4, 8),
        (3, 8, 7),
        (1, 3, 7),
        (1, 7, 5),
    ]

    octa_vertices = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    octa_faces = [
        (1, 3, 5),
        (3, 2, 5),
        (2, 4, 5),
        (4, 1, 5),
        (3, 1, 6),
        (2, 3, 6),
        (4, 2, 6),
        (1, 4, 6),
    ]

    cube_path = os.path.join(out_dir, f"{basename}_cube.obj")
    octa_path = os.path.join(out_dir, f"{basename}_octa.obj")

    _write_obj(cube_path, cube_vertices, cube_faces)
    _write_obj(octa_path, octa_vertices, octa_faces)

    return {"cube": cube_path, "octa": octa_path}


def export_label_spheres_obj(
    out_dir: str | None = None,
    basename: str = "labels",
    labels: Iterable[str] | None = None,
    path: str | None = None,
) -> str:
    """
    Exporteer labels als kleine sferen (hier gesimuleerd als punten) naar OBJ-bestand.

    Parameters
    ----------
    out_dir : str, optional
        Doelmap waarin geschreven wordt (indien `path` niet is opgegeven).
    basename : str
        Basisnaam van het bestand.
    labels : Iterable[str], optional
        Namen van labels (momenteel niet gebruikt in geometrie).
    path : str, optional
        Volledig pad naar output-bestand. Heeft voorrang op `out_dir` + `basename`.

    Returns
    -------
    str
        Pad naar geschreven bestand.
    """
    if path is not None:
        out_path = str(path)
    else:
        if out_dir is None:
            raise ValueError("Either `path` or `out_dir` must be provided")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{basename}.obj")

    # Voorlopig: schrijf enkel vertices als punten
    verts: list[tuple[float, float, float]] = []
    if labels:
        r = 2.0
        for i, _ in enumerate(labels):
            angle = (2 * math.pi * i) / len(labels)
            verts.append((r * math.cos(angle), r * math.sin(angle), 0.0))
    else:
        verts = [(0.0, 0.0, 0.0)]

    with open(out_path, "w", encoding="utf-8") as f:
        for v in verts:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")

    return out_path
