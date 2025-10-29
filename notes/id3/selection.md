Q: Problem – Attribute Selection (ID3)

Given:
A labeled dataset consisting of samples, each described by attribute–value pairs and a categorical class label, and a finite set of candidate attributes.

Find:
The attribute that, when used to split the dataset, produces the largest reduction in label uncertainty (the highest information gain).

Such that:
For each candidate attribute, compute how much it reduces the overall entropy of the dataset.
The attribute with the greatest reduction is selected as the best split.

In words:
→ Best attribute = the one that removes the most disorder in the labels.
→ If all attributes remove the same amount of uncertainty (or none), all have equal information gain.
→ If the dataset is already pure, every attribute has zero information gain.

Interpretation:
Information gain measures how much knowing the value of an attribute helps to predict the class label.
A high information gain means the attribute creates purer subsets, leading to a more informative split in the decision tree.

------------------------------------------------------------

I: Input
A finite labeled dataset S, where each record contains:
- A set of attributes with discrete values.
- A categorical class label.

Let:
- A        – the set of all candidate attributes
- a        – one specific attribute from A
- v        – a possible value of attribute a
- S_v      – the subset of S for which attribute a = v
- |S_v|    – the number of samples in subset S_v
- |S|      – the total number of samples in the dataset
- H(S)     – the entropy of class labels in S
- H(S_v)   – the entropy of class labels in subset S_v

------------------------------------------------------------

O: Output
- A* : the attribute that yields the greatest information gain (best split)
- Optionally: a mapping a → IG(S, a) for all a ∈ A

------------------------------------------------------------

f: Transformation Rule

1. Compute the overall label entropy H(S):
   Determine how mixed the class labels are in the dataset.
   (If all samples have the same label → entropy = 0.)

2. For each candidate attribute a ∈ A:
   a. Partition S into subsets {S_v}, one for each value v of a.
   b. For each subset S_v:
        - Compute H(S_v)
        - Compute weight = |S_v| / |S|
   c. Compute conditional entropy:
        H(S | a) = Σ_v [ (|S_v| / |S|) * H(S_v) ]
   d. Compute information gain:
        IG(S, a) = H(S) − H(S | a)

3. Select best attribute:
   A* = attribute with maximum IG(S, a)

4. Return:
   A* (and optionally all IG values)

------------------------------------------------------------

Interpretation:
- H(S) measures total disorder.
- H(S | a) measures remaining disorder after splitting by a.
- IG(S, a) measures how much uncertainty was removed.
- A high IG(S, a) → purer subsets → strong split.

This greedy step is repeated at each node of the decision tree
until all subsets are pure or no attributes remain.

------------------------------------------------------------

Example (PlayTennis):
Overall entropy H(S) = 0.94

| Attribute | H(S|a) | IG(S,a) |
|------------|---------|---------|
| Outlook    | 0.694   | 0.246   |
| Humidity   | 0.789   | 0.151   |
| Wind       | 0.892   | 0.048   |

Result:
A* = Outlook
