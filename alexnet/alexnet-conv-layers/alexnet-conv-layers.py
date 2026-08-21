import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """
    AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation).
    """
    size = image.shape[0]
    H_in,W_in = image.shape[1],image.shape[2]
    k,s,p = 11,4,2
    H_out = (H_in + 2 *p - k)// s + 1
    W_out = (W_in + 2*p -k) // s + 1
    return np.zeros((size,H_out,W_out,96))
    pass