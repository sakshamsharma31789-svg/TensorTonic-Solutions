def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    a = set(set_a)
    b = set(set_b)
    if not a and not b:
        return 0
    intersection_set = a & b
    union_set = a | b
    similarity = len(intersection_set)/len(union_set)
    return float(similarity)