from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("a003558")
except PackageNotFoundError:
    __version__ = "0"

# Viz niet auto-importeren (vereist matplotlib):
# from a003558.viz import plot_basis  # gebruikers doen dit expliciet
