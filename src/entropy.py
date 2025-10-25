from collections import Counter
from math import log2

def entropy(labels):
    """
    Compute the entropy of a categorical label list.

    Steps:
        counts         - absolute frequency of each label
        N              - total number of samples
        p              - relative class probabilities
        contributions  - individual entropy terms (-p*log2(p))
        H(S)           - total entropy (sum of contributions)

    Returns:
        float: entropy value in bits
    """
    
    counts = Counter(labels)
    
    ## H(S) = - Σ (p_c · log2(p_c))   for all c

    N = sum(counts.values())
    if N == 0:
        return 0.0
    p = {}
    for c, n in counts.items():
        p[c] = n / N
    contributions = {}
    for c, p_c in p.items():
        if p_c > 0:
            contributions[c] = -p_c * log2(p_c)
        else:
            contributions[c] = 0
    H = sum(contributions.values())

    return H
    

    


# if __name__ == "__main__":
#     test_data = ["Yes"] * 9 + ["No"] * 5
#     print(Counter(test_data))
#     print(Counter(test_data).values())
#     # l = list(Counter(test_data).values())
#     # for key, value in Counter(test_data).items():
#     #     print([key]*min(value,3))
#     print(Counter(test_data))
#     print(sum(Counter(test_data).values()))
#     p ={}
#     # print(Counter(test_data).items())
#     N = sum(Counter(test_data).values())
#     for c,n in Counter(test_data).items():
#         p[c] = n/N
#     print("o:",p)
        

# if __name__ == "__main__":
#     test_data = ["Yes"] * 9 + ["No"] * 5
#     print(entropy(test_data))