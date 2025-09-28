# tests/test_viz_extra.py
import pathlib
import pytest

from a003558.viz import plot_basis, plot_cycle
from a003558.viz_octa import plot_octahedron

@pytest.mark.parametrize("title", ["Basis Plot", "Another Basis"])
def test_plot_basis_smoke(tmp_path: pathlib.Path, title: str):
    """Smoke-test: plot_basis moet figuur maken en opslaan."""
    out = tmp_path / "basis.png"
    fig = plot_basis(n=8, show=False, save_path=str(out), title=title)
    assert out.exists()
    assert fig is not None

def test_plot_octahedron_smoke(tmp_path: pathlib.Path):
    """Smoke-test: plot_octahedron moet figuur maken en opslaan."""
    out = tmp_path / "octa.png"
    fig = plot_octahedron(show=False, save_path=str(out))
    assert out.exists()
    assert fig is not None

def test_plot_cycle_smoke(tmp_path: pathlib.Path):
    """Smoke-test: plot_cycle moet figuur maken en opslaan."""
    out = tmp_path / "cycle.png"
    fig = plot_cycle([(0,0),(1,0),(1,1),(0,1),(0,0)], show=False, save_path=str(out), title="Cycle")
    assert out.exists()
    assert fig is not None
