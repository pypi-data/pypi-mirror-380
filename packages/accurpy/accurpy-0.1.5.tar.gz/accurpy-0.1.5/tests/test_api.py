import numpy as np
from accurpy import syncF


def test_scalar_roundtrip():
    y = syncF(10.0, skip_exp=False)
    z = syncF(10.0, skip_exp=True)
    assert np.isfinite(y) and np.isfinite(z)


def test_vectorized_shape():
    x = np.linspace(1e-12, 100.0, 1000)
    y = syncF(x, skip_exp=True)
    assert isinstance(y, np.ndarray)
    assert y.shape == x.shape
    assert y.dtype == np.float64
