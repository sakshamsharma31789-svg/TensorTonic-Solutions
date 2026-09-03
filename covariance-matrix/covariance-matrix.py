import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.asarray(X, dtype=float)
    
    # 1. Center features along columns (axis=0)
    x_centered = X - np.mean(X, axis=0)
    
    # 2. Matrix multiplication (X_c^T @ X_c) divided by (N - 1)
    N = X.shape[0]
    return (x_centered.T @ x_centered) / (N - 1)