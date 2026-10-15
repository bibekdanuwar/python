import json

with open("animals.json", "r", encoding="utf8") as file:
    data = json.load(file)
for animal in data["animals"]:
        print(animal)
        print(animal["name"])