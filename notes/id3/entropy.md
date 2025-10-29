Q: Problem - Entropy labels
Given: A finite list of class labels.
Find: A single number called entropy of this list.
Such that: The number represents how uncertain or mixed the labels are.

- All same → entropy = 0 (pure)
- Evenly split → entropy = maximum (fully mixed)
- One label dominant → value between 0 and max
- Empty list → entropy = 0 (no information)
- Terms with 0 probability contribute 0 (0·log2(0)=0)

I: Input
A finite list (or multiset) of categorical labels, e.g. ["Yes", "No", "Yes", "Yes"].
Let there be k unique label types.
For each class c:
    n_c = number of samples with label c
    N   = total number of samples
    p_c = n_c / N   (relative frequency of class c)

O: Output
A single real number H(S) ∈ [0, log2(k)],
representing the entropy of the label distribution.

For binary classes, H(S) ∈ [0, 1].
Higher values → more mixed labels.
Lower values → more pure (less uncertainty).

Intuitive Interpretation
Entropy measures the uncertainty or disorder in a set of labels.

- H(S) = 0 → The dataset is pure: all samples have the same label.
- H(S) = 1 → The dataset is maximally mixed (for binary labels).
- 0 < H(S) < 1 → The dataset is partly uncertain.

Example:
Yes: 9, No: 5
p(Yes) = 9/14 = 0.643
p(No)  = 5/14 = 0.357
H(S) = -(0.643 * log2(0.643) + 0.357 * log2(0.357)) = 0.940

This means the label distribution is moderately mixed — not random, but not pure either.

Conceptual Meaning
Entropy quantifies the average information content or surprise in outcomes.

- Low entropy → few surprises (predictable)
- High entropy → many surprises (unpredictable)

It is measured in bits, meaning:
"How many binary questions are needed, on average, to know the label?"

Typical Ranges (for binary labels)

| H(S) | Label Distribution | Interpretation |
|-------|--------------------|----------------|
| 0.0 | 100% Yes | Completely certain |
| 0.3 | 85% Yes, 15% No | Mostly certain |
| 0.5 | 75% Yes, 25% No | Some uncertainty |
| 0.94 | 65% Yes, 35% No | Quite mixed |
| 1.0 | 50% Yes, 50% No | Fully uncertain (maximum entropy) |

Mathematical Definition

H(S) = - Σ (p_c * log2(p_c))

where:
- p_c: probability (frequency) of class c
- log2: base-2 logarithm (information measured in bits)
- H(S): expected information (uncertainty)

By convention, if p_c = 0, then p_c * log2(p_c) = 0.

Purpose in Decision Trees
Entropy is the core impurity measure in algorithms such as ID3 and C4.5.
It quantifies how mixed the class labels are in a dataset or node.
The goal of a decision tree is to reduce entropy at each split by selecting attributes that produce purer subsets.