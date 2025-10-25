Understanding Entropy, Split Entropy, and Information Gain

1. Entropy H(S)
What it is:  
A measure of how mixed or uncertain the labels are in the whole dataset.

Meaning:  
- High H(S) → labels are mixed (uncertain, unpredictable)  
- Low H(S) → labels are pure (certain, predictable)

Why it’s useful:  
Entropy tells how “confused” the dataset is before any split.

---

2. Split Entropy H(S|A)
What it is:  
The remaining uncertainty after splitting the dataset by an attribute A.

Meaning:  
- Low H(S|A) → the attribute helps separate labels (good split)  
- High H(S|A) → the attribute doesn’t help (labels stay mixed)

Why it’s useful:  
Split Entropy tells how effective an attribute is at making the data more uniform.

---

3. Information Gain IG(S, A)
What it is:  
The reduction in uncertainty caused by splitting on attribute A.

Formula:  
IG(S, A) = H(S) − H(S|A)

Meaning:  
- High IG → the split made subsets much purer (good attribute)  
- Low IG → the split didn’t change much (weak attribute)

Why it’s useful:  
Information Gain directly measures how much “new information” an attribute gives for predicting the label.

---

Intuitive Summary
- **Entropy** → how uncertain the dataset is.  
- **Split Entropy** → how much uncertainty remains after splitting.  
- **Information Gain** → how much uncertainty was removed.

Good attributes make uncertainty drop sharply → low H(S|A) and high IG(S, A).
