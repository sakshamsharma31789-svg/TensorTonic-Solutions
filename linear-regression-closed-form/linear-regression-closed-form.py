import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    X,y = (np.array(m,dtype=np.float64) for m in (X,y))
    m1 = X.T@X
    y1 = np.linalg.inv(m1)
    m2 = X.T@y
    return y1@m2
    pass