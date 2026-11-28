import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns the bottleneck residual-block output as a nested list.
    """
    x,W1,W2,W3 = (np.array(m,dtype=np.float64) for m in (x,W1,W2,W3))
    Ws = x if Ws is None else x@np.array(Ws,dtype=np.float64)
    m1 = np.maximum(0,x@W1)
    m2 = np.maximum(0,m1@W2)
    m3 = np.maximum(0,m2@W3 + Ws)
    return np.maximum(0,m3).tolist()
    
    pass