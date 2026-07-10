import numpy as np

def vgg_maxpool(x: np.ndarray) -> np.ndarray:
    """
    Implement VGG-style max pooling (2x2, stride 2).
    """
    N,H,W,C = x.shape
    reshaped = x.reshape(N,H // 2,2,W // 2,2,C)
    return reshaped.max(axis=2).max(axis=3)
    pass