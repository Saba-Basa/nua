from id3 import id3

def predict(tree, sample, return_path=False):
    node = tree
    path = []

    while isinstance(node, dict):
        attr = node["attr"]
        val = sample.get(attr, None)
        path.append((attr, val))

        if val in node["children"]:
            node = node["children"][val]
        else:
            return (node["default"], path) if return_path else node["default"]

    return (node, path) if return_path else node


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
        {"Outlook": "Rain", "Humidity": "High", "Play": "No"},
    ]

    attributes = ["Outlook", "Humidity"]
    tree = id3(data, attributes, "Play")

    print("\nTree:\n")
    print(tree)

    test_samples = [
        {"Outlook": "Sunny", "Humidity": "High"},
        {"Outlook": "Rain", "Humidity": "Normal"},
        {"Outlook": "Overcast", "Humidity": "High"},
        {"Outlook": "Sunny", "Humidity": "Normal"},
        {"Outlook": "Storm", "Humidity": "Normal"},   # unknown
        {"Outlook": "Rain", "Humidity": "Extreme"},   # unknown
        {"Outlook": "Foggy", "Humidity": "Wet"},      # unknown
    ]

    print("\nPredictions:\n")
    for i, sample in enumerate(test_samples, 1):
        result, path = predict(tree, sample, return_path=True)
        print(f"{i}. Input: {sample}  →  Prediction: {result}  | Path: {path}")
