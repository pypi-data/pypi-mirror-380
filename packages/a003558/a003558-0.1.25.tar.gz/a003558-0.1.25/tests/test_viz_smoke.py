# tests/test_viz_smoke.py
import pathlib
import pytest

from a003558.viz import plot_basis, plot_cycle
from a003558.viz_octa import plot_octahedron


@pytest.mark.parametrize("title", ["Smoke Basis", "Basis Extra"])
def test_plot_basis_smoke(tmp_path: pathlib.Path, title: str):
    """Smoke-test voor plot_basis: moet een figuur maken en opslaan."""
    out = tmp_path / "basis.png"
    fig = plot_basis(n=8, save_path=str(out), show=False, title=title)
    assert fig is not None
    assert out.exists()


@pytest.mark.parametrize("title", ["Cycle One", "Cycle Two"])
def test_plot_cycle_smoke(tmp_path: pathlib.Path, title: str):
    """Smoke-test voor plot_cycle: moet figuur maken en opslaan."""
    out = tmp_path / "cycle.png"
    # eenvoudige vierkant-cyclus (gesloten door startpunt opnieuw te plaatsen)
    points = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    fig = plot_cycle(points=points, save_path=str(out), show=False, title=title)
    assert fig is not None
    assert out.exists()



def test_plot_octahedron_smoke(tmp_path: pathlib.Path):
    """Smoke-test voor plot_octahedron: moet figuur maken en opslaan."""
    out = tmp_path / "octa.png"
    fig = plot_octahedron(save_path=str(out), show=False, title="Octa Smoke")
    assert fig is not None
    assert out.exists()
