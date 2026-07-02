import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    error = np.abs(y_true-y_pred)
    quadratic_loss = 0.5*(error**2)
    linear_loss = delta*(error-0.5*delta)
    per_sample_loss = np.where(error<=delta,quadratic_loss,linear_loss)
    return float(np.mean(per_sample_loss))