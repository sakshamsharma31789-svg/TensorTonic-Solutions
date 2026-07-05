import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    if x.shape != p.shape:
        raise ValueError('Shapes of x and p must match')
    if not np.allclose(np.sum(p),1.0,atol=1e-6):
        raise ValueError('probability should be equal to 1')
    return float(np.sum(x*p))
    return np.sum(x*p)
    pass
