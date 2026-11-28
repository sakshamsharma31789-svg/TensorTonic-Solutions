import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    x = np.array(X,dtype = float)
    u = np.mean(x,axis=axis,keepdims=True)
    sigma = np.std(x,axis=axis,keepdims=True)
    safesigma= np.where(sigma>eps,sigma,1.0)
    z = (x-u)/safesigma
    z = np.where(sigma>eps,z,0.0)
    return z
    
    pass