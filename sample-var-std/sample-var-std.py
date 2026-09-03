import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    arr = np.array(x, dtype=float)
    m = arr - np.mean(arr)
    
    # Cast the computed numpy scalar explicitly to a standard Python float
    variance = float(np.sum(m ** 2) / (len(arr) - 1))
    
    return {
        'variance': variance,
        'standard_deviation': float(np.sqrt(variance))
    }
    pass