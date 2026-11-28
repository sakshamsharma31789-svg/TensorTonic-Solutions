import numpy as np

def identity_block(x, W1, W2):
    """
    Returns the identity residual-block output as a nested list.
    """
    x = np.array(x,dtype=np.float64)
    W1 = np.array(W1,dtype=np.float64)
    W2 = np.array(W2,dtype=np.float64)
    m1 = x@W1.T
    y1 = np.maximum(0,m1)
    y2 = y1@W2.T + x
    return np.maximum(0,y2).tolist()
    pass