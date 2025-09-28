
from a003558.coupling import coupled_step

def test_coupling_is_near_unit():
    for k1 in range(1,8):
        for k2 in range(1,8):
            err = coupled_step(k1, k2)
            assert err < 1e-8
