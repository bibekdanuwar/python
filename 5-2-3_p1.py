import json
with open("cake.json", "r", encoding="utf8") as file:
    cakes = json.load(file)

    total_price = 0
    for cake in cakes:
        total = total_price + int(cake["Price"])
        print(cake["Name"] + " : " + cake["Price"])
        
    print(total)
