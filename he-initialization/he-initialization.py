def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    W = np.array(W)
    fan_in = np.array(fan_in)
    L = np.sqrt(6/fan_in)
    return W*2*L - L