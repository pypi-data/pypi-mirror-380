# accurpy

Ultra-accurate and fast **double-double** (106-bit) approximation for the new FM function. The C extension ships a single FMA-enabled pipeline validated to stay within 1 ULP versus high-precision references, and a pure-Python double-double fallback is provided when the extension is unavailable.

## Install
```bash
pip install accurpy
```

## Usage
```python
import numpy as np
from accurpy import syncF

y = syncF(10.0, skip_exp=False)

x = np.geomspace(1e-12, 300.0, 1_000_000)
y_vec = syncF(x, skip_exp=True)
```

## Notes
- Scalar calls and NumPy arrays both dispatch to the fast C implementation when available.
- When the extension cannot be imported, the package falls back to the same algorithm implemented in pure Python double-double arithmetic (slower, but numerically identical).

## License
MIT
