import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x)
    q = np.exp(x) - np.exp(-x)
    p = np.exp(x) + np.exp(-x)
    return q/p
    pass