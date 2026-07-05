def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    fan_in = np.array(fan_in)
    fan_out = np.array(fan_out)
    W = np.array(W)
    L = np.sqrt(6/(fan_in+fan_out))
    return W*2*L - L