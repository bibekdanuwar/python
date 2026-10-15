weather_info_per_days = {
    "total_day": 3,
    "temperature": {
        "2025-04-28": {"min": "10", "max": "20"},
        "2025-04-29": {"min": "12", "max": "24"},
        "2025-04-30": {"min": "15", "max": "23"}
    }
}

min_temperature_list = []
max_temperature_list = []

for day in weather_info_per_days["temperature"]:
    min_temperature_list.append(int(weather_info_per_days["temperature"][day]["min"]))
    max_temperature_list.append(int(weather_info_per_days["temperature"][day]["max"]))

print("最低気温:", min_temperature_list)
print("最高気温:", max_temperature_list)

print("平均最低気温:", sum(min_temperature_list) / len(min_temperature_list))
print("平均最高気温:", sum(max_temperature_list) / len(max_temperature_list))