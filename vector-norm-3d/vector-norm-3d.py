import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    res = np.linalg.norm(v,axis=-1)
    return float(res) if res.ndim ==0 else res
    pass