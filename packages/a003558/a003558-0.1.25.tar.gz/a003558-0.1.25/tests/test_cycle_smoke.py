import math
import pathlib
from a003558.viz import plot_cycle

def test_plot_cycle_smoke(tmp_path: pathlib.Path):
    """Smoke-test: eenvoudige 6-hoek tekenen en opslaan."""
    n = 6
    points = [(math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i in range(n)]
    out = tmp_path / "cycle_smoke.png"
    fig = plot_cycle(points=points, save_path=str(out), show=False, title="Cycle Smoke")
    assert out.exists()
    assert fig is not None
