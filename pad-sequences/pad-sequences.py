import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    if not seqs:
        return np.empty((0, 0), dtype=int)
    
    if max_len is None:
        L = max(len(seq) for seq in seqs) if seqs else 0
    else:
        L = max_len
        
    N = len(seqs)
    res = np.full((N, L), pad_value, dtype=int)
    
    for i, seq in enumerate(seqs):
        truncate_len = min(len(seq), L)
        res[i, :truncate_len] = seq[:truncate_len]
        
    return res