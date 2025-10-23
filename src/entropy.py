"""
Q: Problem - Entropy labels
Given: A finit list of class labels
Find: A single number called entropy of this list.
Such that: The number represents how uncertain or mixed the labels are.
All same → entropy = 0 (pure).
Evenly split → entropy = maximum (fully mixed).
One label dominant → value between 0 and max.
Empty list → entropy = 0 (no information).
Terms with 0 probability contribute 0 (0·log2(0)=0).


I: Input
A finite list (or multiset) of categorical labels, e.g. ["Yes", "No", "Yes", "Yes"].
Let there be k unique label types.
For each class c:
    n_c = number of samples with label c
    N = total number of samples
    p_c = n_c / N  (relative frequency of class c)


O: Output
A single real number H(S) ∈ [0, log2(k)],
representing the entropy of the label distribution.

For binary classes, H(S) ∈ [0, 1].
Higher values → more mixed labels.
Lower values → more pure (less uncertainty).


f: Transformation Rule
1. Count occurrences of each unique label c in the input list.
2. Compute total N = sum of all counts.
3. For each label c:
     p_c = n_c / N
4. Compute entropy:
     H(S) = - Σ (p_c · log2(p_c))   for all c
     (Convention: if p_c = 0, then p_c·log2(p_c) = 0)
5. Return H(S)
"""
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