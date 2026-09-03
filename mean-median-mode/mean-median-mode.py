from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    # 1. Compute mean and median
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    
    # 2. Count frequencies for mode
    counts = Counter(x)
    max_freq = max(counts.values())
    
    # 3. Find smallest key among those with maximum frequency
    mode_candidates = [val for val, freq in counts.items() if freq == max_freq]
    mode_val = float(min(mode_candidates))
    
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val
    }