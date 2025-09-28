import pathlib
import matplotlib
matplotlib.use("Agg")

from a003558.viz_octa import plot_octahedron_and_cube

def test_plot_octahedron_and_cube(tmp_path: pathlib.Path):
    out = tmp_path / "octa_cube.png"
    fig = plot_octahedron_and_cube(save_path=str(out), show=False, title="Octa-Cube")
    assert fig is not None
    assert out.exists() and out.stat().st_size > 0
