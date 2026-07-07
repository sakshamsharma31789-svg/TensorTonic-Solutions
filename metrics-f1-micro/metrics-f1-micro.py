import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    tp = np.sum(y_true==y_pred)
    total_elements = len(y_true)
    fp = total_elements-tp
    fn = total_elements-tp
    denominator = 2*tp + fp + fn
    if denominator ==0:
        return 0
    f1 = (2*tp)/denominator
    return float(f1)
    
    pass