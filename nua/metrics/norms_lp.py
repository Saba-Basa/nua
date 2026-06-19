import math
import numpy as np


# Manhattan distance (L1 norm)
def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

# Euclidean distance (L2 norm)
def euclidean_distance(x,y):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y))) 

# Chebyshev distance (L-infinity norm)
def chebyshev_distance(x,y):
    return max(abs(a-b) for a,b in zip(x,y))

# Hamming distance
# D_H(x, y) = sum_{i=1}^k [x_i ≠ y_i]
def hamming_distance(x,y):
    return sum(a != b for a, b in zip(x, y))

# Cosine angle distance
# D_cos(x, y) = arccos( (x · y) / (||x|| * ||y||) )
#||x||, ||y||, norm of each vector
#x · y dot product
#Returns 0 if vectors point in the same direction
def cosine_angle_distance(x,y):
    ny = np.linalg.norm(y)
    nx = np.linalg.norm(x)
    if ny == 0 or nx == 0:
        return 0.0
    return np.arccos(np.dot(x,y)/(nx*ny))


# Discrete metric
# D_disc(x, y) = 0 if x == y, else 1
def discrete_metric(x, y):
    return 0 if x == y else 1

# General ℓp metric
# D_p(x, y) = (sum_i |x_i - y_i|^p)^{1/p}
def lp_metric(x, y, p):
    if p == float('inf'):
        return max(abs(a - b) for a, b in zip(x, y))
    return sum(abs(a - b) ** p for a, b in zip(x, y)) ** (1 / p)




if __name__ == "__main__":
    x = [1,2,3]
    y = [4,5,6]
    print(euclidean_distance(x,y))
    print(manhattan_distance(x,y))
    print(chebyshev_distance(x,y))
    print(hamming_distance(x,y))
    print(cosine_angle_distance(x,y))