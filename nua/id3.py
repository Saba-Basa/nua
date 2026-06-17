#id3 logic

from selection import selection
from collections import Counter
from base.classifier import Classifier

class ID3(Classifier):
    def __init__(self):
        self.tree_ = None
        self.is_fitted_ = False
        
    
    def fit(self, data, attributes, label_key):
        self.tree_ = id3(data, attributes, label_key)
        self.is_fitted_ = True
        return self

    def predict(self, X):
        if not self.is_fitted_:
            raise RuntimeError("Model is not trained. Call fit() first.")

        if isinstance(X, dict):
            node = self.tree_
            while isinstance(node, dict) and "attr" in node:
                attr = node["attr"]
                val = X.get(attr, None)
                node = node["children"].get(val, node["default"])
            return node

        out = []
        for sample in X:
            node = self.tree_
            while isinstance(node, dict) and "attr" in node:
                attr = node["attr"]
                val = sample.get(attr, None)
                node = node["children"].get(val, node["default"])
            out.append(node)
        return out


def id3(dataset, attributes, label_key):
    if not dataset:
        return None
    
    labels = []
    #extract labels
    for l in dataset:
        labels.append(l[label_key])
    
    if len(set(labels)) == 1:
        return labels[0]
    #stop condition
    if not attributes:
     return Counter(labels).most_common(1)[0][0]
    #select best attribute
    best_attr, _igs = selection(dataset, attributes, label_key)
    
    node = {
        "attr": best_attr,
        "children": {},
        "default": Counter(labels).most_common(1)[0][0],
    }
    
    values = sorted({row.get(best_attr, None) for row in dataset})
    remaining = [a for a in attributes if a != best_attr]

    for v in values:
        subset = [row for row in dataset if row[best_attr] == v]
        node["children"][v] = id3(subset, remaining, label_key) if subset else node["default"]

    return node


if __name__ == "__main__":
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
    t = ID3().fit(data, ["Outlook","Humidity"], "Play")
    print(t.predict({"Outlook":"Sunny","Humidity":"High"}))
    print(t.predict([
        {"Outlook":"Rain","Humidity":"Normal"},
        {"Outlook":"Overcast","Humidity":"High"},
    ]))

    