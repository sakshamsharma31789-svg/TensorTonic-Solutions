import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    arr = np.asarray(v,dtype=float)
    norms = np.sqrt(np.sum(arr**2,axis=-1))
    if norms.ndim ==0:
        return float(norms)
    return norms
    pass