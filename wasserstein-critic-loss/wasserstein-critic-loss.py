import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    fake = np.mean(fake_scores)
    real = np.mean(real_scores)
    q = fake - real
    return float(q)
    pass