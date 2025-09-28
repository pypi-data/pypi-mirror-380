
import numpy as np
from a003558.octonions import octonion_mul, random_unit, norm

def test_alternativity_numeric():
    for _ in range(10):
        x = random_unit(seed=None)
        y = random_unit(seed=None)
        xx = octonion_mul(x,x)
        left = octonion_mul(xx, y)
        right = octonion_mul(x, octonion_mul(x, y))
        assert np.allclose(left, right, atol=1e-8)

def test_norm_multiplicative_numeric():
    for _ in range(10):
        x = random_unit(None); y = random_unit(None)
        xy = octonion_mul(x,y)
        assert np.isclose(norm(xy), norm(x)*norm(y), atol=1e-8)
