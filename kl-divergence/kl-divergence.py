import numpy as np

def kl_divergence(p, q, eps=1e-12):
    p = np.array(p)
    q = np.array(q)
    return np.sum(p*(np.log(p/q)))
    pass