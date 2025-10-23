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


