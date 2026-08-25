import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    most = {word: index for index,word in enumerate(vocab)}
    vec = np.zeros(len(vocab),dtype=int)
    for token in tokens:
        if token in most:
            vec[most[token]] +=1
    return vec
    pass