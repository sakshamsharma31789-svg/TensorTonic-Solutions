def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k = set(recommended[:k])
    relevent_set = set(relevant)
    numerator = len(top_k.intersection(relevent_set))
    precision = numerator/k
    recall = numerator/len(relevant)
    return [precision,recall]
    pass