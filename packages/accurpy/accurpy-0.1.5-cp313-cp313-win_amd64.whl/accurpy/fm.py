from __future__ import annotations
import numpy as np

try:
    from . import _fm as _cext
    _HAVE_CEXT = True
except Exception:
    _cext = None
    _HAVE_CEXT = False

# Python DD fallback (bit-for-bit STRICT)
from ._dd_fallback import syncF as _syncF_py

def syncF(x, skip_exp: bool = False, out=None):
    """
    Approximate FM_new(x).

    Parameters
    ----------
    x : float or array-like of float
    skip_exp : bool
        False  -> (P/Q)/s * x * exp(-x)
        True   -> (P/Q)/s * x
    out : optional numpy array to write into (must be float64 and match shape)

    Returns
    -------
    float or np.ndarray of float64
    """
    if np.isscalar(x):
        if _HAVE_CEXT:
            return _cext.fm_skipexp_opt(x) if skip_exp else _cext.fm_with_exp_opt(x)
        return _syncF_py(float(x), skip_exp=skip_exp)

    a = np.asarray(x, dtype=np.float64, order="C")
    if out is not None:
        if out.dtype != np.float64 or out.shape != a.shape:
            raise ValueError("out must be float64 and match input shape")

    if _HAVE_CEXT:
        # Use buffer API (zero-copy) and return frombuffer -> copy to 'out' or new array
        buf = memoryview(a).cast("B")  # raw bytes
        bb = _cext.fm_skipexp_opt_buf(buf) if skip_exp else _cext.fm_with_exp_opt_buf(buf)

        y = np.frombuffer(bb, dtype=np.float64).reshape(a.shape)
        if out is None:
            return y.copy()  # own the result
        out[...] = y
        return out

    # Fallback: Python DD loop (slower)
    if out is None:
        out = np.empty_like(a, dtype=np.float64)
    it = np.nditer([a, out], flags=["refs_ok", "multi_index"], op_flags=[["readonly"], ["writeonly"]])
    for xi, yi in it:
        yi[...] = _syncF_py(float(xi), skip_exp=skip_exp)
    return out
