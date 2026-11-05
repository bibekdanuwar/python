fruits_stock = [
    ["りんご", 7],
    ["バナナ", 5],
    ["みかん", 3],
    ["ぶどう", 12],
    ["キウイ", 4]
]

low_fruits_stock = []

for name, stock in fruits_stock:
    if stock <= 5:
        low_fruits_stock.append([name, stock])

print("在庫が5個以下の果物の名前と在庫数の二次元リスト:", low_fruits_stock)