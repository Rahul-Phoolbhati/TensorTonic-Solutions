import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    
    # divisor = math.sqrt(sum(e*e for e in a))*math.sqrt(sum(e*e for e in b))
    # dividend = float(np.dot(a,b))
    
    # if divisor == 0:
    #     return 0.0
    # return dividend/divisor

    npa = np.array(a)
    npb = np.array(b)

    # norm or magnitude or mode
    
    # norm_a = np.linalg.norm(npa)
    # norm_b = np.linalg.norm(npb)

    # for 1D vector faster
    norm_a = np.sqrt(npa.dot(npa))
    norm_b = np.sqrt(npb.dot(npb)) 

    mode_mul = norm_a*norm_b

    dividend = np.dot(a,b)
    if norm_a == 0 or norm_b == 0:
        return 0.0

    return float(dividend / mode_mul)
    
    