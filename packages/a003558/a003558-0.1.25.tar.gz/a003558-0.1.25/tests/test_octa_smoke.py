import pathlib
from a003558.viz_octa import plot_octahedron, plot_octahedron_and_cube

def test_plot_octahedron_smoke(tmp_path: pathlib.Path):
    """Smoke-test: losse octaëder moet renderen en opslaan."""
    out = tmp_path / "octa_smoke.png"
    fig = plot_octahedron(save_path=str(out), show=False, title="Octa Smoke")
    assert out.exists()
    assert fig is not None

def test_plot_octahedron_and_cube_smoke(tmp_path: pathlib.Path):
    """Smoke-test: octaëder + kubus moet renderen en opslaan."""
    out = tmp_path / "octa_cube_smoke.png"
    fig = plot_octahedron_and_cube(save_path=str(out), show=False, title="Octa+Cube Smoke")
    assert out.exists()
    assert fig is not None
