import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)
    s = np.dot(Z1,Z2.T)/temperature
    S_stable = s - np.max(s,axis =1 ,keepdims =True)
    exp_s = np.exp(S_stable)
    sum_exp_s = np.sum(exp_s,axis=1)
    diag_exp_s = np.diag(exp_s)
    loss = -np.log(diag_exp_s/sum_exp_s)
    return  float(np.mean(loss))
    pass