# tests/test_viz_extra.py
import pathlib
from a003558.viz import plot_cycle
from a003558.viz_octa import plot_octahedron


def test_plot_cycle_smoke(tmp_path: pathlib.Path):
    """Smoke-test: plot_cycle moet zonder fouten renderen en een bestand opslaan."""
    out_png = tmp_path / "cycle.png"
    points = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    fig = plot_cycle(points, save_path=str(out_png), show=False, title="Cycle Test")
    assert out_png.exists()
    assert fig is not None


def test_plot_octahedron_smoke(tmp_path: pathlib.Path):
    """Smoke-test: plot_octahedron moet zonder fouten renderen en een bestand opslaan."""
    out_png = tmp_path / "octa.png"
    fig = plot_octahedron(save_path=str(out_png), show=False, title="Octa Test")
    assert out_png.exists()
    assert fig is not None
