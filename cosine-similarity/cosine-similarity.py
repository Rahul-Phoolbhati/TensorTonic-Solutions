import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    divisor = math.sqrt(sum(e*e for e in a))*math.sqrt(sum(e*e for e in b))
    dividend = float(np.dot(a,b))
    
    if divisor == 0:
        return 0.0
    return dividend/divisor
    