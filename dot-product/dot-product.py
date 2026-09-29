import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    # print(type(np.dot(x,y)))
    # return float(np.dot(x,y))
    return float(x@y) # used for matrix multiplication 

    
    