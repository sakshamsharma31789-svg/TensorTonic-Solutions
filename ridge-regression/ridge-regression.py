import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    X,y = (np.array(m,dtype=np.float64) for m in (X,y))
    rows,columns = X.shape
    I = np.eye(columns)
    y1 = X.T@X + lam*I
    y1 = np.linalg.inv(y1)
    return y1@(X.T@y)
    pass