import torch
import torch.nn.functional as F

def sgns_loss(center_vec: torch.Tensor, pos_vec: torch.Tensor, neg_vecs: torch.Tensor) -> torch.Tensor:
    """
    Returns a scalar torch.Tensor: the SGNS loss.
    """
    dot = torch.dot(center_vec,pos_vec)
    neg_dot = neg_vecs@center_vec
    loss = F.softplus(-dot) + F.softplus(neg_dot).sum()
    return loss
    pass
