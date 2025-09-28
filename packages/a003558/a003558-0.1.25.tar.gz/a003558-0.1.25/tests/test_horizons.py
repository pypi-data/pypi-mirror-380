
import math
from a003558.number_theory import multiplicative_order
from a003558.horizons import horizon_bound, staircase_level

def test_horizon_bound_holds():
    for n in range(1,1024):
        m = 2*n - 1
        if m == 1: 
            L = 1
        else:
            L = multiplicative_order(2, m)
        assert horizon_bound(n, L)

def test_staircase_level():
    assert staircase_level(1)==1+0
    assert staircase_level(2)==2
    assert staircase_level(3)==2
    assert staircase_level(4)==3
