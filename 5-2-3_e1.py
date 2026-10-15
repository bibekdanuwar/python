import json

with open("animals.json", "r", encoding="utf8") as file:
    animals = json.load(file)
for animal in animals["animal"]:
        print(animal)
        print(animal["name"])