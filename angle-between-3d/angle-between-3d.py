import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.array(v)
    w = np.array(w)
    norm1 = np.linalg.norm(v)
    norm2 = np.linalg.norm(w)
    if norm1<1e-10 or norm2<1e-10:
        return np.nan
    dot_product = np.dot(v,w)
    cos_theta = dot_product/(norm1*norm2)
    cos_theta_clipped = np.clip(cos_theta,-1.0,1.0)
    theta = np.arccos(cos_theta_clipped)
    return float(theta)
    pass