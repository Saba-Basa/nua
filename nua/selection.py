from information_gain import information_gain


def selection(dataset,attributes, label_key):
    if not dataset or not attributes:
        return None, {}
    i_g = {}
    for a in attributes:
        i_g[a] = information_gain(dataset, a, label_key)
    best = max(i_g, key=i_g.get)
    return best, i_g


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
#     i_g ={}
#     attributes = [ "Outlook", "Humidity"]
#     print(type(i_g))
#     for a in attributes:
#         i_g[a] = information_gain(data, a, "Play")
#     print(i_g)   
#     l = i_g.get(attributes[0])
#     print(attributes[0])
#     print(attributes[1])
#     print(l) 
#     print("\n")
#     best = max(i_g, key=i_g.get)
#     print(best)
#     print(type(best))
    attributes = [ "Outlook", "Humidity"]
    result = selection(data, attributes,"Play")
    print(result)