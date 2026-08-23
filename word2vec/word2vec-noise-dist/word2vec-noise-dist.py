import torch

def noise_distribution(counts: torch.Tensor, alpha: float = 0.75) -> torch.Tensor:
    """
    Returns torch.Tensor of shape (vocab_size,), a probability distribution that sums to 1.
    """
    count = torch.as_tensor(counts,dtype=torch.float64)
    powered_counts = count**alpha
    return powered_counts/powered_counts.sum()
    
    pass
