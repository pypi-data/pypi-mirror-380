# src/a003558/viz_octa.py
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional

def _draw_edges(ax, edges, color="b", lw=1.5):
    for s, e in edges:
        s = np.array(s); e = np.array(e)
        ax.plot(*zip(s, e), color=color, lw=lw)

def plot_octahedron(save_path: Optional[str] = None, show: bool = True, title: Optional[str] = None):
    """Plot een octaëder in 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    r = [-1, 1]
    # Randen van de octaëder (verbindingen van de zes assenpunten)
    edges = [
        ((r[0], 0, 0), (0, r[0], 0)),
        ((r[0], 0, 0), (0, r[1], 0)),
        ((r[0], 0, 0), (0, 0, r[0])),
        ((r[0], 0, 0), (0, 0, r[1])),
        ((r[1], 0, 0), (0, r[0], 0)),
        ((r[1], 0, 0), (0, r[1], 0)),
        ((r[1], 0, 0), (0, 0, r[0])),
        ((r[1], 0, 0), (0, 0, r[1])),
        ((0, r[0], 0), (0, 0, r[0])),
        ((0, r[0], 0), (0, 0, r[1])),
        ((0, r[1], 0), (0, 0, r[0])),
        ((0, r[1], 0), (0, 0, r[1])),
    ]
    _draw_edges(ax, edges, color="b", lw=1.5)

    ax.set_box_aspect((1, 1, 1))
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    if title:
        ax.set_title(title)
    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig

def plot_octahedron_and_cube(save_path: Optional[str] = None, show: bool = True, title: Optional[str] = None):
    """
    Plot een octaëder én zijn omgeschreven kubus in 3D (smoke-test vriendelijk).
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Octaëder
    r = [-1, 1]
    oct_edges = [
        ((r[0], 0, 0), (0, r[0], 0)),
        ((r[0], 0, 0), (0, r[1], 0)),
        ((r[0], 0, 0), (0, 0, r[0])),
        ((r[0], 0, 0), (0, 0, r[1])),
        ((r[1], 0, 0), (0, r[0], 0)),
        ((r[1], 0, 0), (0, r[1], 0)),
        ((r[1], 0, 0), (0, 0, r[0])),
        ((r[1], 0, 0), (0, 0, r[1])),
        ((0, r[0], 0), (0, 0, r[0])),
        ((0, r[0], 0), (0, 0, r[1])),
        ((0, r[1], 0), (0, 0, r[0])),
        ((0, r[1], 0), (0, 0, r[1])),
    ]
    _draw_edges(ax, oct_edges, color="b", lw=1.5)

    # Kubus met hoekpunten (-1,±1,±1) etc.
    c = [-1, 1]
    cube_vertices = [(x, y, z) for x in c for y in c for z in c]
    # Lijst van alle paren die een ribbe vormen (1 coord verschilt)
    cube_edges = []
    for i, s in enumerate(cube_vertices):
        for j in range(i + 1, len(cube_vertices)):
            e = cube_vertices[j]
            if sum(si != ei for si, ei in zip(s, e)) == 1:  # precies één coord verschilt
                cube_edges.append((s, e))
    _draw_edges(ax, cube_edges, color="gray", lw=0.8)

    ax.set_box_aspect((1, 1, 1))
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    if title:
        ax.set_title(title or "Octahedron + Cube")
    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig
