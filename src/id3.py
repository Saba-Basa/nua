#id3 logic

from selection import selection
from collections import Counter

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
    
    values = sorted({row[best_attr] for row in dataset})
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
#     attributes = [ "Outlook", "Humidity"]
#     # print(len(attributes))
    
    
#     print(data[0].keys())
#     print(list(data[0].keys())[2])
    
    
#     labels = []
#     for row in data:
#         labels.append(row[list(data[0].keys())[2]])

#     print(labels)
#     print(Counter(labels))
#     print(Counter(labels).most_common())
#     print(Counter(labels).most_common(1))
#     print(Counter(labels).most_common(2))
#     print(Counter(labels).most_common(1)[0])
#     print(Counter(labels).most_common(1)[0][0])
    attributes = [ "Outlook", "Humidity"]
    t= id3(data, attributes,"Play" )
    print(t)

    