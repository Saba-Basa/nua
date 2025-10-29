Q: Problem - Split Entropy
Given: A finite dataset consisting of samples, each described by attributes and a class label.
Find: A single number called the split entropy of the dataset with respect to a given attribute.
Such that: The number represents the expected uncertainty of the class labels after partitioning the dataset by the values of that attribute.
If all subsets are pure → split entropy = 0.
If subsets remain mixed → split entropy > 0.
If the attribute provides no information → split entropy = same as overall entropy.
Empty dataset → split entropy = 0

I: Input
A finite dataset S consisting of samples (records), each described by attributes and a class label.
Let:
    A       - the attribute by which the dataset is partitioned
    v       - a possible value of A
    S_v     - the subset of S for which A = v
    |S_v|   - the number of samples in subset S_v
    H(S_v)  - the entropy of class labels within subset S_v
    |S|     - the total number of samples in the dataset
    (|S_v| / |S|) - the relative weight (proportion) of subset S_v

O: Output
A single real number representing the conditional entropy H(S|A):
it measures how uncertain the class labels remain after the dataset has been partitioned by attribute A.

f: Transformation Rule
1. Partition the dataset S into subsets S_v according to the values v of attribute A.
2. For each subset S_v:
      - Extract the class labels.
      - Compute the entropy H(S_v).
      - Compute the weight |S_v| / |S|.
3. Multiply each subset's entropy by its weight.
4. Sum all weighted entropies to obtain the conditional entropy:
      H(S|A) = Σ_v (|S_v| / |S|) * H(S_v)

Interpretation
Split Entropy H(S|A) tells how much uncertainty remains after splitting the dataset by an attribute A.

If you want an attribute that provides a lot of information (i.e. makes the data more predictable), you want:
- High H(S): the dataset is initially uncertain.
- Low H(S|A): the split makes subsets pure.
→ High Information Gain (H(S) − H(S|A)).

If H(S|A) is high, that means too much uncertainty remains after the split, so the attribute contributes little predictive power.

In short:
Low H(S|A) → good split (pure subsets, high information gain).  
High H(S|A) → poor split (uncertainty remains, low information gain).