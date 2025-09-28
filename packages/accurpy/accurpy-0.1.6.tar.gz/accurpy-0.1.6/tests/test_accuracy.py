import numpy as np
import pytest
from accurpy import syncF
from accurpy._dd_fallback import syncF as syncF_py


def ulp_distance(a, b):
    av = a.view(np.uint64)
    bv = b.view(np.uint64)
    return np.abs(av.astype(np.int64) - bv.astype(np.int64)).astype(np.uint64)

@pytest.mark.slow
def test_wrapper_matches_fallback_dense():
    x = np.concatenate([
        np.geomspace(1e-18, 1e-6, 1000),
        np.geomspace(1e-6, 1.0,  1000),
        np.linspace(1.0, 300.0, 1000),
        np.geomspace(300.0, 1e6, 1000),
    ]).astype(np.float64)

    for skip in (False, True):
        y = syncF(x, skip_exp=skip)
        y_py = np.array([syncF_py(float(xi), skip_exp=skip) for xi in x])
        max_ulp = ulp_distance(y, y_py).max()
        assert max_ulp <= 1, f"C wrapper diverged by {max_ulp} ULPs"


def test_scalar_matches_fallback():
    samples = np.geomspace(1e-18, 1e3, 200)
    for skip in (False, True):
        for x in samples:
            y = syncF(float(x), skip_exp=skip)
            y_py = syncF_py(float(x), skip_exp=skip)
            assert np.allclose(y, y_py, rtol=0, atol=np.finfo(np.float64).eps)
