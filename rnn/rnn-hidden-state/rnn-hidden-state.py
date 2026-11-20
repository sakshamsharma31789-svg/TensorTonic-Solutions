import numpy as np

def init_hidden(batch_size: int, hidden_dim: int) -> np.ndarray:
    """
    Returns a float64 zero hidden-state matrix.
    """
    matrix = np.zeros((batch_size,hidden_dim),dtype = np.float64)
    return matrix
    pass