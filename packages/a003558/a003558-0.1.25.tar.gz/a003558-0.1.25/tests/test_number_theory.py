
import math
from a003558.number_theory import a003558_order, back_front_cycle_length, multiplicative_order, phi

def test_a003558_small():
    known = [1,2,4,3,6,10,12,4,8]
    for n, val in enumerate(known):
        assert a003558_order(n) == val

def test_back_front_relation():
    for n in range(1,200):
        m = 2*n - 1
        if m == 1:
            assert back_front_cycle_length(n) == 1
        else:
            assert back_front_cycle_length(n) == multiplicative_order(2, m)

def test_order_divides_phi():
    for m in [3,5,7,9,11,13,15,21,25,27,33,35,63,81]:
        if math.gcd(2,m)==1:
            k = multiplicative_order(2, m)
            assert phi(m) % k == 0
