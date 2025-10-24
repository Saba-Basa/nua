"""
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
      -Extract the class labels.
      - Compute the entropy H(S_v).
      - Compute the weight |S_v| / |S|.
3. Multiply each subset's entropy by its weight.
4. Sum all weighted entropies to obtain the conditional entropy:
      H(S|A) = Σ_v (|S_v| / |S|) * H(S_v)
"""

from collections import defaultdict
from entropy import entropy



def split_entropy(dataset, attribute, label_key):
    """
    Compute the weighted average entropy after splitting the dataset by a given attribute.
    H(S|A) = Σ_v (|S_v| / |S|) * H(S_v)

    Steps:


    Returns:

    """
    if not dataset:
        return 0.0

    # automatically initializes missing keys with empty lists
    subsets = defaultdict(list)
    for sample in dataset:
        value = sample[attribute]
        label = sample[label_key]
        subsets[value].append(label)
        
    N = len(dataset)
    H_S_A = 0.0

    for value, labels in subsets.items():
        w = len(labels) / N
        H_S_v = entropy(labels)
        H_S_A += w * H_S_v

    
    return H_S_A




if __name__ == "__main__":
    # data = [
    #     {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
    #     {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
    #     {"Outlook": "Overcast", "Humidity": "High", "Play": "Yes"},
    #     {"Outlook": "Rain", "Humidity": "High", "Play": "Yes"},
    #     {"Outlook": "Rain", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Rain", "Humidity": "Normal", "Play": "No"},
    #     {"Outlook": "Overcast", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
    #     {"Outlook": "Sunny", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Rain", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Sunny", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Overcast", "Humidity": "High", "Play": "Yes"},
    #     {"Outlook": "Overcast", "Humidity": "Normal", "Play": "Yes"},
    #     {"Outlook": "Rain", "Humidity": "High", "Play": "No"}
    # ]   
    # # print(data)
    # # print(data[0])
    # print(data[0]["Outlook"])
    # subsets = defaultdict(list)

    # for r in data:
    #     value = r["Outlook"]
    #     label = r["Play"]
    #     subsets[value].append(label)
        

    # print("Subsets:", subsets)

    # #|S|
    # N = len(data)
    # print("|S| =", N)
    
    # #H(S_v)
    # # sunny_labels = subsets["Sunny"]
    # # H = entropy(sunny_labels)
    # # print(H)
    
    # H_S_A = 0.0
    
    # for value,labels  in subsets.items():
    # #(|S_v| / |S|)
    #     w = len(labels) / N
    #     H_S_v = entropy(labels)
    #     print(f"{value}: weight={w:f}, H(S_v)={H_S_v:f}")
    #     H_S_A += w * H_S_v
        
    # print("weights",w)
    # print(f"\n=> H(S|Outlook) = {H_S_A:f}")
    data = [
        {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
        {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
        {"Outlook": "Overcast", "Humidity": "High", "Play": "Yes"},
        {"Outlook": "Rain", "Humidity": "High", "Play": "Yes"},
        {"Outlook": "Rain", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Rain", "Humidity": "Normal", "Play": "No"},
        {"Outlook": "Overcast", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Sunny", "Humidity": "High", "Play": "No"},
        {"Outlook": "Sunny", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Rain", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Sunny", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Overcast", "Humidity": "High", "Play": "Yes"},
        {"Outlook": "Overcast", "Humidity": "Normal", "Play": "Yes"},
        {"Outlook": "Rain", "Humidity": "High", "Play": "No"}
    ]

    H_S_A = split_entropy(data, "Outlook", "Play")
    print(H_S_A)
    
