import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    dk = K.shape[-1]
    m1 = (Q@K.mT)/(dk**(1/2))
    softmax = torch.softmax(m1,dim=-1)
    return torch.matmul(softmax,V)
    pass