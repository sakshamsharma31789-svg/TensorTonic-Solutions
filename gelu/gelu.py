import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.array(x)
    q = np.vectorize(math.erf)
    return 1/2 *(x)*(1+q(x/np.sqrt(2)))
    pass
