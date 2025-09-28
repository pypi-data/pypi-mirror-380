from typing import Optional, Iterable, Tuple
import numpy as np

def plot_basis(
    n: int = 12,
    save_path: Optional[str] = None,
    show: bool = True,
    title: Optional[str] = None,
):
    """
    Plot de eerste n termen van A003558 (voorbeeldvisualisatie).

    Parameters
    ----------
    n : int, default=12
        Aantal termen om te tonen (x-as: 0..n-1).
    save_path : str | None
        Pad om de figuur op te slaan; slaat niet op als None.
    show : bool, default=True
        Toon de figuur met plt.show().
    title : str | None
        Optionele titel.

    Returns
    -------
    matplotlib.figure.Figure
    """
    # Lazy import zodat core-import geen zware deps nodig heeft
    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        raise RuntimeError(
            "matplotlib is vereist voor visualisaties. "
            "Installeer met: pip install 'a003558[viz]'"
        ) from e

    # Importeer de term-functie uit jouw package
    try:
        from a003558.core import a003558_term
    except Exception:
        # Fallback: simpele identiteit zodat de plot werkt als core ontbreekt
        def a003558_term(i: int) -> int:
            return i

    x = np.arange(n, dtype=int)
    y = np.array([a003558_term(i) for i in x], dtype=float)

    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(x, y, "o-", lw=1.5, ms=4)
    ax.set_xlabel("n")
    ax.set_ylabel("a(n)")
    if title:
        ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.35)

    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


def plot_cycle(
    points: Iterable[Tuple[float, float]],
    save_path: Optional[str] = None,
    show: bool = True,
    title: Optional[str] = None,
):
    """
    Plot een gesloten cyclus (2D puntenlijst).

    Parameters
    ----------
    points : iterable of (x, y)
        Puntencoördinaten in volgorde; geef het startpunt ook als laatste punt
        mee om de cyclus te sluiten.
    save_path, show, title : zie plot_basis()

    Returns
    -------
    matplotlib.figure.Figure
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        raise RuntimeError(
            "matplotlib is vereist voor visualisaties. "
            "Installeer met: pip install 'a003558[viz]'"
        ) from e

    pts = np.array(list(points), dtype=float)
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(pts[:, 0], pts[:, 1], "o-", lw=1.5)
    ax.set_aspect("equal")
    if title:
        ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.35)

    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig
