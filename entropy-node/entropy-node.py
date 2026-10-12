import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    if not y:
        return 0.0
    _,counts = np.unique(y,return_counts=True)
    probabilities = counts/len(y)
    probabilities = probabilities[probabilities>0]
    entropy = -np.sum(probabilities*np.log2(probabilities))
    return float(entropy)
    pass