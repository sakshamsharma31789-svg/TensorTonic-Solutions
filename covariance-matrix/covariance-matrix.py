import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)
    u = np.mean(X,axis=0)
    N = X.shape[0]
    X_centered = X - u
    if X.ndim != 2 or X.shape[0]<2:
        return None
    else:
        return (X_centered.T@X_centered)/(N-1)
    pass