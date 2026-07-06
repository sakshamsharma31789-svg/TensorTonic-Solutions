import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    x = np.array(X)
    x_min = np.min(x,keepdims=True,axis=axis)
    x_max = np.max(x,keepdims=True,axis=axis)
    denominator = np.maximum(x_max-x_min,eps)
    return (x-x_min)/denominator
    pass