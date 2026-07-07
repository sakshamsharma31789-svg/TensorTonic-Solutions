import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    v = np.array(V,dtype=float)
    td_error = r + gamma * v[s_next] - v[s]
    v[s] = v[s] + alpha*td_error
    return v
    pass