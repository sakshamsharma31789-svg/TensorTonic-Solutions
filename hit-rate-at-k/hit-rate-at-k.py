def hit_rate_at_k(recommendations: list, ground_truth: list, k: int) -> float:
    """
    Returns the fraction of users with a relevant item in their first k recommendations.
    """
    if not recommendations:
        return 0
    hits = 0
    for recs,gt in zip(recommendations,ground_truth):
        top_k = set(recs[:k])
        gt_set = set(gt)
        if top_k & gt_set:
            hits +=1
    return hits/len(recommendations)
    
    pass