import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v,dtype=float)
    norm = np.linalg.norm(v,axis=-1,keepdims=True)
    v_unit = np.where(norm>1e-10,v/norm,v)
    return v_unit
    pass