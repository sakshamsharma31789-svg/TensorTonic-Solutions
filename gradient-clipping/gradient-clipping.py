import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g)
    mod_g = np.linalg.norm(g)
    if mod_g<=max_norm:
        return g
    elif max_norm <= 0 or mod_g == 0:
        return g
    else:
        return g*(max_norm/mod_g)
    pass