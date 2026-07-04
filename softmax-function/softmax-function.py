import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    q = np.max(x,axis=-1,keepdims=True)
    n = np.exp(x-q)
    d = np.sum(n,axis=-1,keepdims=True)
    return n/d
    
    
    
    pass