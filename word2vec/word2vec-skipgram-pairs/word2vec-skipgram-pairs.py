import torch

def skipgram_pairs(token_ids: torch.Tensor, window: int) -> torch.Tensor:
    """
    Returns int64 torch.Tensor of shape (num_pairs, 2).
    """
    pairs =[]
    n = len(token_ids)
    for i in range(n):
        for j in range(max(0,i-window),min(n,i+window+1)):
            if i == j :
              continue 
            pairs.append([token_ids[i].item(),token_ids[j].item()])
    if not pairs:
        return torch.zeros((0,2),dtype=torch.int64)
    return torch.tensor(pairs,dtype=torch.int64)
    pass
