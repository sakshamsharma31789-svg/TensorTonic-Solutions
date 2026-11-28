import numpy as np

def conv_block(x, W1, W2, Ws):
    """
    Returns the projection residual-block output as a nested list.
    """
    W1 = np.array(W1,dtype=np.float64)
    W2 = np.array(W2,dtype=np.float64)
    x = np.array(x,dtype=np.float64)
    Ws = np.array(Ws,dtype=np.float64)
    y1 = np.maximum(0,x@W1)
    return np.maximum(0,y1@W2 +x@Ws)
    pass