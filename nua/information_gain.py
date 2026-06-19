from entropy import entropy
from split_entropy import split_entropy



def information_gain(dataset, attribute, label_key):
    labels=[]
    for s in dataset:
        labels.append(s[label_key])
    H_S = entropy(labels)
    H_S_a = split_entropy(dataset, attribute, label_key)
    return H_S - H_S_a



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


    IG_S_a = information_gain(data, "Outlook", "Play")
    print(IG_S_a)