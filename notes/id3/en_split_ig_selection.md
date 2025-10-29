Understanding Attribute Selection (ID3)

1. Entropy H(S)
What it is:
A measure of how mixed or uncertain the class labels are in the dataset.

Meaning:
- High → labels are mixed (uncertain)
- Low → labels are pure (certain)

Why it matters:
Entropy shows the dataset’s initial disorder before any split.

------------------------------------------------------------

2. Split Entropy H(S|A)
What it is:
The remaining uncertainty after splitting the dataset by an attribute A.

Meaning:
- Low → attribute separates labels well (good split)
- High → attribute doesn’t help (labels stay mixed)

Why it matters:
Shows how clean or uniform the subsets are after splitting.

------------------------------------------------------------

3. Information Gain IG(S, A)
What it is:
The reduction in uncertainty caused by splitting on attribute A.

Formula:
IG(S, A) = H(S) − H(S|A)

Meaning:
- High → strong attribute (big entropy drop)
- Low → weak attribute (little change)

Why it matters:
Measures how informative an attribute is about the class label.

------------------------------------------------------------

Essence for Attribute Selection
Choose the attribute with the highest Information Gain.
→ It best reduces label uncertainty and produces the purest subsets.