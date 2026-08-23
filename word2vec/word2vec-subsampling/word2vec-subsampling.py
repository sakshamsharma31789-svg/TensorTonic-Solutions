import torch

def subsample_keep_probs(counts: torch.Tensor, t: float = 1e-5) -> torch.Tensor:
    """
    Returns torch.Tensor of shape (vocab_size,) with the keep-probability for each word.
    """
    count_float = counts.to(torch.float32)
    total_counts = count_float.sum()
    f = count_float/total_counts
    p_keep = torch.sqrt(t/f)
    return torch.clamp(p_keep,max=1.0)
    pass
