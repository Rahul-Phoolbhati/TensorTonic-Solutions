import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    nparr = np.array(x)
    nparr2 = np.array(y)
    fa = nparr*nparr2
    print(type((float)(fa.sum(dtype=float))))

    return (float)(fa.sum(dtype=float))