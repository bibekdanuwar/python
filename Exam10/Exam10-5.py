cities_temperatures = [
    ["東京", [25.3, 27.8, 26.2]],
    ["大阪", [26.5, 25.0, 28.1]],
    ["福岡", [27.0, 26.8, 25.5]],
    ["札幌", [20.1, 21.5, 19.8]]
]

cities_avg_temperature = [] 

for cities in cities_temperatures:
    city_name = cities[0]    
    temperatures = cities[1] 
    
    total = 0
    for temperature in temperatures:
        total = total + temperature
        
    average = total / len(temperatures) 
    cities_avg_temperature.append([city_name, average])

top_city_avg_temperature = cities_avg_temperature[0]

for city in cities_avg_temperature:
    if city[1] > top_city_avg_temperature[1]:
        top_city_avg_temperature = city

print("各都市の名前と平均気温が格納された二次元リスト:", cities_avg_temperature)
print("3日間の平均気温が最も高い都市の名前と平均気温のリスト:", top_city_avg_temperature)